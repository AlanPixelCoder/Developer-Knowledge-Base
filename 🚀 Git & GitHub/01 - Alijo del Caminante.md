# 01. Alijo del Caminante

**Versión original en inglés:** [01 - Wayfarer Cache](./01%20-%20Wayfarer%20Cache.md)

**Curso:** Git & GitHub
**Tema:** Diario de expedición Wayfarer — control de versiones, configuración, inicialización del repositorio
**Etiquetas:** `#git` `#github` `#setup` `#wayfarer`

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

Dos caminantes, Finch y Mora, parten a cartografiar el Paso de Greyharbor. Al principio anotaban todo en pergaminos sueltos, cada uno en su propia mochila. Un mapa perdido aquí, una ruta revisada allá... nada coincidía. Para no volver a cometer el mismo error, necesitan un único alijo de notas de expedición que conserve el historial: cada cambio registrado, cada revisión rastreable. Ese alijo es un repositorio Git.

> [!NOTE]
> **El historial es la clave**
> Git es un sistema de control de versiones distribuido. No hace copias del directorio una y otra vez; registra instantáneas del proyecto en distintos momentos. GitHub aloja una copia compartida para que los dos caminantes puedan sincronizarse sin tener que enviarse pergaminos por correo.

## ¿Por qué un alijo y no montones de copias?

Antes de Git, Finch guardaba `ruta_v1.txt`, `ruta_v2_final.txt`, `ruta_v2_final_DEFINITIVA.txt`. Nadie podía saber cuál era la versión actual ni por qué había cambiado. Con Git, el «porqué» va en el mensaje del commit, y el historial muestra exactamente qué cambió entre instantáneas. Ese historial es el diario de expedición.

## Preparar la mochila

Lo primero es comprobar que Git está instalado en el terminal del camino.

```bash
git --version
```

La salida debería parecerse a esta:

```text
git version 2.39.3
```

> [!WARNING]
> Si el comando no se encuentra, hay que instalar Git antes de seguir. La versión exacta importa menos que tener `git` funcionando en la terminal.

## Guardar las notas en el alijo

Los caminantes empiezan con una nueva carpeta para los mapas del paso: `wayfarer-pass`. Para convertirla en un alijo (repositorio), inicializan Git en esa carpeta.

```bash
pwd
git init
```

Salida esperada (plausible):

```text
/Users/wayfarer/wayfarer-pass
Initialized empty Git repository in /Users/wayfarer/wayfarer-pass/.git/
```

`git init` crea un directorio oculto `.git`. Ahí se guarda todo el historial del alijo; sin ese directorio no hay repositorio Git.

## Enlazar con el campamento compartido

Para sincronizar con el campamento compartido (GitHub), el alijo necesita un remoto. Crean un repositorio vacío en GitHub llamado `wayfarer-pass` y lo enlazan como `origin`.

```bash
git remote add origin https://github.com/finch-mora/wayfarer-pass.git
git branch -M main
```

El segundo comando renombra la rama por defecto a `main`, el nombre que usarán a partir de ahora. Para comprobar que el enlace está bien configurado:

```bash
git branch
```

Salida esperada:

```text
* main
```

> [!TIP]
> `origin` es solo un nombre para la URL remota. Podrían llamarlo de otra forma, pero `origin` es la convención en todos los caminos. Conviene mantenerlo salvo que haya una razón muy fuerte para cambiarlo.

## Salida

Tras inicializar y enlazar, el alijo local conoce dónde guarda su historial (`.git`) y adónde debe enviar/recibir datos (`origin`). La rama es `main`. Aún no hay ningún commit: el alijo está vacío, esperando la primera marca del camino.

## Tarea 1: Sentar las bases del alijo

Crea la carpeta `wayfarer-pass`, ejecuta `git init` dentro, añade un remoto que apunte a `https://github.com/finch-mora/wayfarer-pass.git`, renombra la rama a `main` y compruébalo con `git branch`. Escribe los comandos en orden y las salidas plausibles que esperarías en cada paso.

**Por qué este orden:** el historial debe existir localmente antes de poder guardar ninguna instantánea en un commit. Enlazar el remoto antes del primer push solo sirve para tener la dirección lista cuando llegue el momento de compartir el alijo.

**Siguiente:** [[02 - Marcas del Sendero]]
