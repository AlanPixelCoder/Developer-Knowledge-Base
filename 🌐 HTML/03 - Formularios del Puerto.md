# 03. Formularios del Puerto

**Versión original en inglés:** [03 - Harbor Intake Forms](./03%20-%20Harbor%20Intake%20Forms.md)

**Curso:** HTML
**Tema:** Formularios de admisión del puerto, tipos de input, validación, radios, casillas, etiquetas
**Etiquetas:** `#html` `#web-development` `#forms` `#inputs` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/M%C3%B3dulo-HTML-7C5CFF?style=for-the-badge" alt="Módulo HTML">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Ola Tideglass" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

La oficina de mareas de Greyharbor no adivina quién solicita usar el dique seco restringido. Cada solicitud de amarre, entrega de suministros o pase de acceso por tormenta pasa por el formulario de admisión del puerto. Un `<form>` convierte el tablón de anuncios en una puerta: recoge información y el navegador puede aplicar reglas básicas antes de que nada salga del muelle.

> [!NOTE]
> **Recoger, no suponer**
> Los formularios HTML son sobres. Todo lo que hay dentro va junto al enviarse. `action` indica adónde va, `method` cómo — por ahora pueden quedar vacíos mientras se prueba la estructura. El objetivo es recoger los datos correctos en el formato correcto.

## El formulario de admisión

Un formulario empieza con `<form>`. Los campos van dentro. Los más básicos son texto y un botón de envío.

```html
<form action="" method="">
  <p>Buscar en el registro de boyas de Tideglass</p>
  <input type="text">
  <br><br>
  <input type="submit" value="Buscar en el registro">
</form>
```

`<input>` se cierra a sí mismo. El `type` controla su función; el `value` en un botón de envío cambia su etiqueta. Sin backend, enviar el formulario simplemente recarga la página: eso es lo esperado, no un error.

## Registro de tripulación

Distintos datos requieren distintos tipos de entrada. `type="email"` comprueba que haya una arroba. `type="password"` oculta los caracteres. Todos los campos de una misma solicitud deben ir dentro de un solo formulario, como los elementos de un manifiesto.

```html
<form>
  <h2>Registro de tripulación</h2>
  <p>Nombre de guardia:<br><input type="text"></p>
  <p>Correo electrónico:<br><input type="email"></p>
  <p>Clave de acceso:<br><input type="password"></p>
  <input type="submit" value="Registrarse para el turno">
</form>
```

> [!IMPORTANT]
> Trata `<form>` como el sobre. Si un campo queda fuera, no se incluirá al «sellar» el sobre al enviar. Mantén los campos relacionados juntos.

## Reglas para el manifiesto

No todos los campos son opcionales. El observatorio necesita un nombre de guardia para cada registro. `required` impide el envío si está vacío. `minlength` y `maxlength` imponen la longitud, y el navegador mostrará un error si no se cumplen.

```html
<form>
  <p>Nombre de guardia: <input type="text" minlength="3" maxlength="20" required></p>
  <p>Correo electrónico: <input type="email" required></p>
  <p>Clave de acceso: <input type="password" minlength="8" maxlength="64" required></p>
  <input type="submit" value="Enviar manifiesto">
</form>
```

> [!WARNING]
> `maxlength` detiene las pulsaciones; `minlength` es el que impide el envío si es demasiado corto. Usarlos juntos es útil cuando hay un límite práctico y un mínimo por seguridad o legibilidad.

## Números para el dique seco

Algunos campos necesitan números. `type="number"` muestra flechas para aumentar o disminuir. `min`, `max` y `step` restringen el valor.

```html
<p>Número de amarres solicitados: <input type="number" min="1" max="4" step="1"></p>
```

Las flechas respetan `min` y `max`, pero escribir directamente no está impedido: el navegador marcará el valor fuera de rango al enviar. Eso es correcto para validación en cliente: orienta, pero no sustituye la validación en el servidor.

## Elegir un rol de guardia

Cuando solo se permite una opción, se usa `type="radio"`. Todos los radios de un grupo comparten el mismo `name`. Cada uno necesita un `id` único y una `<label>` con `for` que coincida. Al hacer clic en la etiqueta se selecciona el radio: esto es fundamental para la usabilidad.

```html
<p>Rol de guardia:</p>
<input type="radio" id="role-tide" name="watch-role" value="tidewatcher">
<label for="role-tide">Vigilante de mareas</label><br>
<input type="radio" id="role-radio" name="watch-role" value="radio">
<label for="role-radio">Operador de radio</label><br>
<input type="radio" id="role-logistics" name="watch-role" value="logistics">
<label for="role-logistics">Logística</label>
```

> [!IMPORTANT]
> Los radios sin etiquetas son casi imposibles de pulsar con fiabilidad. Si el usuario tiene que apuntar con precisión a un círculo diminuto, el formulario es hostil. Las etiquetas no son decoración: son el área clicable.

## Preparar el equipo para una salida por tormenta

Cuando se pueden seleccionar varias opciones, se usa `type="checkbox"`. Las casillas de un grupo pueden compartir el mismo `name`, pero son independientes: cualquier combinación es válida.

```html
<p>Equipo de tormenta:</p>
<input type="checkbox" id="kit-lantern" name="kit" value="lantern">
<label for="kit-lantern">Linterna</label><br>
<input type="checkbox" id="kit-rope" name="kit" value="rope">
<label for="kit-rope">Cabo de amarre</label><br>
<input type="checkbox" id="kit-chart" name="kit" value="chart">
<label for="kit-chart">Carta de mareas</label><br>
<input type="checkbox" id="kit-signal" name="kit" value="signal">
<label for="kit-signal">Bengalas de señal</label>
```

> [!TIP]
> Regla práctica: si al seleccionar una opción se deben desmarcar las demás, usa radio. Si las selecciones se acumulan, usa casillas. «¿Qué rol vas a tomar?» es radio. «¿Qué llevas en el equipo?» es casillas.

## Salida

Un formulario de admisión completo se renderiza con campos etiquetados, agrupaciones para radios y casillas y un botón de envío. El navegador aplica restricciones básicas a `email`, `required`, `minlength`, `maxlength`, `min`, `max`. La estructura es el manifiesto: aunque aún no se envíe nada, deja claro qué necesita la oficina del puerto.

## Tarea 3: Presentar la solicitud al dique seco por tormenta

Crea `slipway-request.html` con un formulario que contenga: un encabezado «Solicitud de dique seco por tormenta», un campo de texto obligatorio para el nombre de la embarcación con `minlength` 3 y `maxlength` 16, un campo de correo obligatorio, un campo numérico para el número de amarres solicitados (`min` 1, `max` 3), un grupo de radios llamado `urgency` con al menos tres opciones debidamente etiquetadas, un grupo de casillas llamado `equipment` con al menos cuatro opciones debidamente etiquetadas, y un botón de envío con la etiqueta «Enviar solicitud». Todos los campos deben estar dentro de un solo `<form>`.

**Por qué este orden:** recopilar datos estructurados es una habilidad distinta a escribir texto estático: las etiquetas, los nombres y las restricciones forman parte de la especificación, no son un añadido posterior.

**Siguiente:** [[04 - Semántica del Astillero]]
