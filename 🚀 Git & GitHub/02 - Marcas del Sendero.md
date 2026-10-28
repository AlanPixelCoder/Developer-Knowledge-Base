# 02. Marcas del Sendero

**Versión original en inglés:** [02 - Trail Markers](./02%20-%20Trail%20Markers.md)

**Curso:** Git & GitHub
**Tema:** Flujo de trabajo Wayfarer — directorio de trabajo, área de preparación, commits, estado, push
**Etiquetas:** `#git` `#workflow` `#commits` `#wayfarer`

<p align="left">
  <img src="https://img.shields.io/badge/HERRAMIENTA-GIT-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge">
  <img src="https://img.shields.io/badge/PLATAFORMA-GITHUB-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge">
  <img src="https://img.shields.io/badge/Leyenda-Wayfarer-8D7358?style=for-the-badge" alt="Wayfarer">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7A3EE8?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=8D7358&height=70&section=header" width="100%" alt="Ola Wayfarer" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #8D7358, #C9B7A3, #8D7358, transparent); margin: 24px 0;" />

Con el alijo listo, Finch deja la primera marca del camino: un mapa del Paso de Greyharbor. En lugar de tallarlo en piedra, escribe `pass-map.md`. Mora añade `supply-manifest.md`. Cada vez que quieren guardar un cambio significativo en la historia de la expedición, dejan una marca en forma de commit. La clave está en saber dónde se encuentran las notas antes de convertirse en marcas.

> [!NOTE]
> **Tres lugares para las notas**
> Git sigue los cambios en tres zonas: el **directorio de trabajo** (archivos que se editan), el **área de preparación** (archivos marcados para el siguiente snapshot) y el **repositorio local** (instantáneas guardadas en `.git`).

## Marcar el mapa

Finch crea `pass-map.md` con el primer boceto del paso. En ese momento es solo un archivo en disco: Git lo ve como no rastreado. Para elegir qué va en la siguiente instantánea, lo pasa al área de preparación.

```bash
git add pass-map.md
```

Para preparar todo lo modificado en la carpeta actual:

```bash
git add .
```

Para preparar solo archivos de un tipo concreto:

```bash
git add *.md
```

Preparar es intencionalmente selectivo. Si Finch corrige una errata en un archivo pero sigue editando otro, puede preparar solo el cambio ya terminado.

## Dejar una marca en el camino

Cuando los cambios preparados forman una marca coherente —«primer boceto del mapa»—, hace un commit con un mensaje que explique por qué.

```bash
git commit -m "trail: add first sketch of Greyharbor Pass"
```

Un commit es una instantánea con un ID, autor, fecha/hora y mensaje. Forma parte de la historia de la expedición. Los buenos mensajes dicen *qué* y *por qué* en pocas palabras; mensajes vagos como «actualizar» son difíciles de seguir a tres curvas del camino.

> [!TIP]
> El área de preparación es como preparar las alforjas para esta etapa del viaje. No es necesario meter todo lo que se tocó hoy: solo lo que forme una marca coherente con esta etapa.

## Comprobar el camino

Antes de hacer commit o push, conviene comprobar el estado de la carga. `git status` muestra archivos no rastreados, cambios preparados y cambios sin preparar.

```bash
git status
```

Salida plausible en ese momento:

```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to remove from index)
	new file:   pass-map.md
```

O tras editar archivos:

```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
	modified:   supply-manifest.md

no changes added to commit (use "git add" and/or "git commit")
```

## Enviar marcas al campamento compartido

Las marcas existen localmente en `.git`. Para compartirlas con el campamento en GitHub, hay que hacer push. La primera vez en una rama nueva se establece el seguimiento.

```bash
git push -u origin main
```

Después, enviar nuevas marcas es más sencillo:

```bash
git push
```

Salida plausible (resumida):

```text
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 245 bytes | 245.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/finch-mora/wayfarer-pass.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main' by default.
```

> [!WARNING]
> Solo se envían lo que se ha guardado con commit. `git add` pasa al área de preparación; `git commit` crea la instantánea; `git push` envía las instantáneas al remoto. Si te olvidaste de hacer commit, no se enviará nada nuevo al campamento.

## Salida

El flujo se convierte en un ciclo: editar en el directorio de trabajo → `git add` para preparar → `git commit` para dejar una marca → `git push` para compartirla con el campamento. `git status` es la brújula para saber qué paso sigue. Cada marca debe ser pequeña y explicar su propósito.

## Tarea 2: Dejar dos marcas

Crea `pass-map.md` y `supply-manifest.md` en `wayfarer-pass`. Prepáralos con `git add .`, haz commit con el mensaje `"trail: add pass map and initial supply manifest"`, y envíalos a `origin/main` con `-u` en el primer push. Muestra la secuencia plausible de comandos y las salidas plausibles de `git status` antes de preparar y después del commit.

**Por qué este orden:** prepara lo que va junto, haz commit con un mensaje claro y compártelo. Marcas pequeñas y con propósito son más fáciles de leer en el historial que commits gigantes con cambios de todo tipo.

**Siguiente:** [[03 - Bifurcaciones del Camino]]
