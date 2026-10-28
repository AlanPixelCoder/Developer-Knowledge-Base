# 03. Bifurcaciones del Camino

**Versión original en inglés:** [03 - Forks in the Trail](./03%20-%20Forks%20in%20the%20Trail.md)

**Curso:** Git & GitHub
**Tema:** Colaboración Wayfarer — clonar, fork, ramas, switch, pull
**Etiquetas:** `#git` `#branching` `#collaboration` `#wayfarer`

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

El camino se bifurca. Finch quiere explorar un posible atajo por los acantilados de pizarra; Mora debe seguir cartografiando el paso principal. Ninguno quiere borrar el trabajo del otro. En el camino se dividirían el grupo por un tiempo: en Git, se crean ramas. Para trabajar juntos a distancia, clonan, hacen fork y traen actualizaciones para mantener sus alijos sincronizados.

> [!NOTE]
> **Las ramas son senderos secundarios**
> Una rama es una línea de historia paralela. Los cambios en `shortcut-scout` no afectan a `main` hasta que se fusionan deliberadamente. Se puede explorar, marcar el camino y dar media vuelta sin reescribir la ruta principal.

## Unirse a la expedición desde otra mochila

Mora está lejos del terminal de Finch. Para tener una copia completa del alijo de la expedición, lo clona.

```bash
git clone https://github.com/finch-mora/wayfarer-pass.git
cd wayfarer-pass
```

Clonar descarga todo el repositorio —historial, ramas y archivos— en una nueva carpeta. Tras clonar, `origin` ya apunta a ese remoto.

## Forks cuando no hay permisos

A veces un caminante quiere contribuir al alijo de otro pero no tiene permisos de escritura. En ese caso hace un **fork** en GitHub: crea una copia personal del repositorio bajo su propia cuenta. Clona su fork, hace los cambios en una rama y luego propone fusionarlos mediante un Pull Request (lo veremos después).

Para un equipo de dos con permisos de escritura, no hace falta hacer fork: basta con clonar y crear ramas. Conocer ambos formas parte del camino.

## Permisos en el campamento

Los niveles de acceso de GitHub determinan qué se puede hacer:

- **Read** — puede ver y clonar, pero no hacer push.
- **Write** — puede hacer push de ramas y commits (nivel habitual para caminantes de confianza).
- **Admin** — puede gestionar configuración, colaboradores y reglas de protección.

> [!TIP]
> Si `git push` es rechazado por un error de permisos, comprueba si clonaste el repositorio original o tu fork, y si tu cuenta tiene permisos de escritura.

## Abrir un sendero secundario

Para explorar el atajo con seguridad, Finch crea y cambia a una nueva rama.

```bash
git branch shortcut-scout
git switch shortcut-scout
```

O en un solo comando:

```bash
git checkout -b shortcut-scout
```

Mientras esté en `shortcut-scout`, cualquier commit solo afectará a esa rama. `main` quedará exactamente como estaba. Para ver todas las ramas:

```bash
git branch -a
```

Salida plausible:

```text
* shortcut-scout
  main
  remotes/origin/main
```

## Sincronizar con las novedades del campamento

Mora acaba de hacer push de una actualización de `supply-manifest.md` a `main`. Finch quiere traer esos cambios a su trabajo actual para saber qué suministros hay disponibles. Desde su rama (o desde `main`), hace pull.

```bash
git pull
```

`git pull` descarga los cambios del remoto y los fusiona en la rama local actual. Si está en `main`, actualiza `main`. Si está en una rama de trabajo y tiene upstream configurado, la actualiza — pero lo más seguro suele ser traer `main` primero y luego fusionarlo en el sendero secundario, o hacer rebase según las reglas del grupo.

Lo importante por ahora: hacer pull mantiene el alijo al día con lo que otros han dejado en la hoguera del campamento.

> [!WARNING]
> Hay que hacer pull con frecuencia, sobre todo antes de empezar a trabajar o antes de hacer push. Un alijo desactualizado es la forma más fácil de crear conflictos evitables en el camino.

## Salida

Las ramas permiten dividir el grupo y explorar sin pisarse. Clonar trae todo el historial a una nueva mochila. Hacer fork crea una copia personal cuando no hay permisos de escritura. `git pull` mantiene los alijos sincronizados con el campamento compartido. La ruta principal se mantiene intacta hasta que el sendero secundario esté listo para revisión y fusión.

## Tarea 3: Dividir el grupo

En el alijo compartido, crea una rama llamada `cliff-scout`, cámbiate a ella, añade `cliff-notes.md`, haz commit con el mensaje `"trail: add cliff scout observations"`, y sube la rama a origin con `-u origin cliff-scout`. También escribe los comandos para clonar el repositorio en una carpeta nueva y para traer los últimos cambios estando en `main`. Indica salidas plausibles donde corresponda.

**Por qué este orden:** aislar la exploración arriesgada en una rama. Sube la rama para que otros la vean, pero no toques `main`. Mantén `main` actualizado con `git pull` al sincronizarte.

**Siguiente:** [[04 - Revisiones en la Hoguera]]
