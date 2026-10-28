# 04. Revisiones en la Hoguera

**Versión original en inglés:** [04 - Campfire Reviews](./04%20-%20Campfire%20Reviews.md)

**Curso:** Git & GitHub
**Tema:** Integración Wayfarer — merge, conflictos, Pull Requests, flujo open source
**Etiquetas:** `#git` `#pull-requests` `#merging` `#wayfarer`

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

Finch regresa de los acantilados de pizarra con buenas noticias: el atajo es transitable. Antes de grabarlo en el mapa oficial del camino, el grupo se reúne alrededor de la hoguera para revisarlo. Tienen que fusionar `cliff-scout` en `main`, resolver cualquier desacuerdo en las notas y proponer los cambios formalmente mediante un Pull Request. Es junto a la hoguera donde las notas borradores se convierten en parte oficial del diario de expedición.

> [!NOTE]
> **Fusionar une los caminos**
> `git merge` toma los commits de una rama y los integra en otra. Si los cambios no se solapan, suele ser limpio. Si ambos lados editaron las mismas líneas, Git marca un conflicto que debe resolverse manualmente.

## Traer el atajo a casa

La forma más limpia es actualizar `main` primero, cambiar a ella, asegurarse de que está al día y luego fusionar el sendero secundario. O bien fusionar desde la rama de trabajo, pero mantener `main` actualizado es un buen hábito.

```bash
git checkout main
git pull
git checkout cliff-scout
git merge main
```

O directamente desde `main`:

```bash
git checkout main
git pull
git merge cliff-scout
```

Si no hay conflictos, Git crea un commit de fusión (o hace fast-forward) y las notas del atajo pasan a formar parte de `main`. Luego se envían:

```bash
git push
```

## Cuando las notas chocan

A veces Finch y Mora editan `pass-map.md` al mismo tiempo: uno añade una marca de puente, el otro una marca de vado, en la misma sección. Git no puede decidir y marca el conflicto así:

```text
<<<<<<< HEAD
Marca de vado añadida por Mora en main
=======
Marca de puente añadida por Finch en cliff-scout
>>>>>>> cliff-scout
```

Los caminantes deben editar el archivo para elegir uno, combinar ambos o escribir una nueva versión. Hay que eliminar los marcadores `<<<<<<<`, `=======`, `>>>>>>>`. Tras resolverlo, se prepara y se hace commit:

```bash
git add pass-map.md
git commit -m "trail: resolve pass-map merge conflict"
git push origin cliff-scout
```

> [!WARNING]
> Nunca se deben dejar marcadores de conflicto en archivos commiteados. Si hay dudas, hay que revisar ambos lados con cuidado y asegurarse de que el texto final tiene sentido. Una mala fusión crea un lío mucho más difícil de arreglar que una pequeña demora.

## Pull Requests junto a la hoguera

Un **Pull Request (PR)** es una propuesta para fusionar una rama en otra. En GitHub abre un espacio para discusión, revisión y comprobaciones antes de integrar los cambios. Incluso para un equipo de dos merece la pena usarlo: el PR queda como registro del «porqué» de añadir el atajo, con comentarios y diferencias.

Flujo habitual:

1. Hacer push de la rama a origin.
2. Abrir un Pull Request en GitHub desde `cliff-scout` a `main`.
3. Revisar el diff, discutir y pedir cambios si es necesario.
4. Una vez aprobado, fusionar el PR (GitHub puede hacer merge commit, squash o rebase).
5. Traer el `main` actualizado localmente con `git pull`.

> [!TIP]
> Una buena descripción del PR explica qué cambia el camino, por qué es necesario y cualquier nota para quien revise (por ejemplo: «probado con marea baja, seguro cruzarlo»).

## El mapa para expediciones mayores

Para contribuir al alijo de otro sin permisos de escritura, el flujo es ligeramente distinto:

1. **Hacer fork** del repositorio original en GitHub, en tu propia cuenta.
2. **Clonar** tu fork localmente: `git clone <url-de-tu-fork>`.
3. **Crear una rama** para el cambio: `git switch -c trail-fix`.
4. **Hacer commit y push** a tu fork: `git add . && git commit -m "..." && git push -u origin trail-fix`.
5. **Abrir un Pull Request** desde la rama de tu fork a la rama `main` del repositorio original.

## Salida

Fusionar integra los senderos secundarios en la ruta principal. Los conflictos son esperables cuando el trabajo se solapa: basta con resolverlos con cuidado. Los Pull Requests formalizan la revisión junto a la hoguera y crean un registro de las decisiones. El flujo de código abierto escala este mismo patrón a grupos mucho mayores de caminantes.

## Tarea 4: Celebrar la revisión junto a la hoguera

Simula la fusión de `cliff-scout` en `main`: indica los comandos para actualizar `main`, fusionar la rama y hacer push. Muestra un conflicto plausible en `pass-map.md` con `<<<<<<<`, `=======`, `>>>>>>>`, y luego los pasos para resolverlo (`git add`, `git commit`, `git push`). Por último, enumera los cinco pasos para contribuir a un repositorio externo mediante fork y PR, con comandos plausibles cuando proceda.

**Por qué este orden:** integrar requiere cuidado. Revisar antes de fusionar, resolver conflictos deliberadamente y documentar la propuesta en un PR. Estos hábitos evitan perder notas y mantienen la ruta oficial fiable.

**Fin del camino Wayfarer.**
