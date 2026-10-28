#!/usr/bin/env python3
"""
selftest.py — prueba que los verificadores siguen detecting fallos.

Un verificador que nadie ha visto fallar no es un verificador: puede estar
comprobando la condición equivocada, o haber dejado de comprobar algo, y en
ambos casos se limita a decir `RESULTADO: OK` mientras el vault se pudre. Aquí
se introduce cada fallo a propósito en una copia temporal del vault y se exige
que el verificador correspondiente lo detecte y salga con código 1.

Los fallos de `check_transcripts.py` no se inyectan: alterar la salida esperada
de una nota rompe la auditoría entera de ese bloque, así que basta comprobar
que el script corre y termina en verde sobre el vault real.

Uso:  python3 tools/selftest.py [--sin-transcripciones]

`--sin-transcripciones` omite el runner de zsh, que necesita macOS, para que
el job rapido de CI pueda ejecutarlo igual en Linux.
Salida: 0 si los verificadores detectan todo lo que deben; 1 si alguno no.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# (nombre del verificador, fichero a tocar, transformación o marcador, texto
#  que debe aparecer en la salida al detectar el fallo)
def first_note(folder):
    """Primera nota real del modulo, siempre la inglesa: los nombres de archivo
    cambian con cada reescritura, la marca `**Spanish version:**` no."""
    d = os.path.join(ROOT, folder)
    for name in sorted(os.listdir(d)):
        if not name.endswith('.md') or name.startswith('README'):
            continue
        text = open(os.path.join(d, name), encoding='utf-8').read()
        if '**Spanish version:**' in text:
            return f'{folder}/{name}'
    raise SystemExit(f'modulo sin notas en ingles: {folder}')


PAIR = '<add a note with no Spanish mirror>'
ORPHAN = '<add a note no README links to>'
FAULTS = [
    ('check_notes.py', first_note('🖥️ Command Line'),
     lambda t: t + '\n```\n', 'sin cerrar'),
    ('check_notes.py', first_note('🐍 Python'),
     lambda t: t + '\n```pythonx\nx = 1\n```\n', 'etiqueta de fence'),
    ('check_notes.py', 'README.md',
     lambda t: t + '\n| A | B | C |\n| :--- | :--- | :--- |\n| 1 | 2 |\n',
     'la cabecera tiene'),
    ('check_notes.py', 'README.md',
     lambda t: t + '\nWikilink: [[Nota Que No Existe]]\n',
     'wikilink roto'),
    ('check_notes.py', 'README.md',
     lambda t: t + '\n> [!DANGER]\n> algo\n', 'no la reconoce GitHub'),
    ('check_notes.py', 'README.md',
     lambda t: t + '\n> [!NOTE] texto en la misma linea\n', 'solo en su linea'),
    ('check_parity.py', '🐍 Python', PAIR, 'sin traduccion al espanol'),
    ('.check_readme_index.py', '98 - Nota Huerfana.md', ORPHAN,
     'Huerfana'),
]


def find(script):
    """Los verificadores viven en tools/, salvo el indice, que esta en la raiz."""
    for d in (HERE, ROOT):
        path = os.path.join(d, script)
        if os.path.isfile(path):
            return path
    raise SystemExit(f'verificador no encontrado: {script}')


def label(mutate, target):
    return {PAIR: 'nota sin traducir', ORPHAN: 'nota huerfana'}.get(
        mutate, target)


def run(script, root):
    p = subprocess.run([sys.executable, find(script), root],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def orphan_fault(root):
    """A note on disk that no README links to: invisible in Obsidian's graph
    only as a file you never stumble on, which is exactly what this catches."""
    open(os.path.join(root, '🐍 Python', '98 - Nota Huerfana.md'), 'w',
         encoding='utf-8').write('# Huerfana\n\nSin enlace entrante.\n')


def pair_fault(root):
    """Add a numbered note with no Spanish mirror."""
    src = os.path.join(root, first_note('🐍 Python'))
    dst = os.path.join(root, '🐍 Python', '99 - Nota Sin Traducir.md')
    shutil.copyfile(src, dst)


def main():
    base = tempfile.mkdtemp(prefix='vault-')
    root = os.path.join(base, 'vault')
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
        '.git', 'node_modules', '__pycache__'))

    failures = []
    for script, target, mutate, expected in FAULTS:
        # A fresh copy per fault, so one fault cannot mask the next.
        sandbox = os.path.join(base, 'run')
        shutil.rmtree(sandbox, ignore_errors=True)
        shutil.copytree(root, sandbox)

        if mutate is PAIR:
            pair_fault(sandbox)
        elif mutate is ORPHAN:
            orphan_fault(sandbox)
        else:
            path = os.path.join(sandbox, target)
            open(path, 'w', encoding='utf-8').write(
                mutate(open(path, encoding='utf-8').read()))

        code, out = run(script, sandbox)
        ok = code == 1 and expected in out
        print(f'{"OK  " if ok else "FALLA"}  {script:<24}{label(mutate, target)}')
        if not ok:
            failures.append((script, target, code, expected, out[-600:]))

    # The expensive runner: not fault-injected, but it must run and pass.
    # `--sin-transcripciones` exists because it needs macOS, so the cheap CI
    # job on Linux can still prove the other four verifiers.
    if '--sin-transcripciones' in sys.argv:
        print('SKIP  check_transcripts.py     (--sin-transcripciones)')
    else:
        code, out = run('check_transcripts.py', root)
        ok = code == 0 and 'RESULTADO: OK' in out
        print(f'{"OK  " if ok else "FALLA"}  check_transcripts.py     '
              f'(sin inyectar fallo)')
        if not ok:
            failures.append(('check_transcripts.py', 'vault real', code,
                             'RESULTADO: OK', out[-600:]))

    shutil.rmtree(base, ignore_errors=True)
    if failures:
        print(f'\n=== VERIFICADORES QUE NO DETECTAN ({len(failures)}) ===')
        for script, target, code, expected, out in failures:
            print(f'\n--- {script} sobre {label(mutate, target)}: salió con '
                  f'{code}, '
                  f'se esperaba 1 y {expected!r}')
            print(out)
        return 1
    print('\nRESULTADO: OK  (todos los verificadores detectan sus fallos)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
