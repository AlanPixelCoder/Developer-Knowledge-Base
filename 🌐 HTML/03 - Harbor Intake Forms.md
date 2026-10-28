# 03. Harbor Intake Forms

**Spanish version:** [03 - Formularios del Puerto](./03%20-%20Formularios%20del%20Puerto.md)

**Course:** HTML
**Topic:** Harbor intake forms, input types, validation, radios, checkboxes, labels
**Tags:** `#html` `#web-development` `#forms` `#inputs` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Module-HTML-7C5CFF?style=for-the-badge" alt="HTML Module">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Tideglass wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

The Greyharbor tide office does not guess who is asking to use the restricted slipway. Every berth request, supply drop, or storm access pass goes through the harbor intake form. A `<form>` turns a page from a notice board into a gate — it collects information, and the browser can enforce basic rules before anything ever leaves the pier.

> [!NOTE]
> **Collect, don't assume**
> HTML forms are envelopes. Everything inside goes together when submitted. `action` says where it goes, `method` says how — for learning purposes those can stay empty while the structure is tested. The point now is collecting the right pieces of data in the right form.

## The Intake Form

A form starts with `<form>`. Inputs live inside it. The most basic are text and a submit button.

```html
<form action="" method="">
  <p>Search the Tideglass buoy registry</p>
  <input type="text">
  <br><br>
  <input type="submit" value="Search Registry">
</form>
```

`<input>` is self-closing. The `type` controls what it does; the `value` on a submit button changes its label. Without a backend, submitting just reloads the page — that is expected, not broken.

## Crew Registration

Different data needs different input types. `type="email"` checks for an @ sign. `type="password"` hides characters. All inputs for one request should stay inside a single form, like items in one manifest.

```html
<form>
  <h2>Crew Registration</h2>
  <p>Watch Name:<br><input type="text"></p>
  <p>Email:<br><input type="email"></p>
  <p>Passcode:<br><input type="password"></p>
  <input type="submit" value="Register for Watch">
</form>
```

> [!IMPORTANT]
> Treat `<form>` as the envelope. If an input is outside the form, it will not be included when the envelope is "sealed" on submit. Keep related fields together.

## Rules for the Manifest

Not every field is optional. The observatory needs a watch name for every registration. `required` blocks submission if empty. `minlength` and `maxlength` enforce length, and the browser shows an error when violated.

```html
<form>
  <p>Watch Name: <input type="text" minlength="3" maxlength="20" required></p>
  <p>Email: <input type="email" required></p>
  <p>Passcode: <input type="password" minlength="8" maxlength="64" required></p>
  <input type="submit" value="Submit Manifest">
</form>
```

> [!WARNING]
> `maxlength` stops keystrokes; `minlength` is what blocks submission when too short. Both are useful together when there is both a practical cap and a minimum for security or readability.

## Slipway Numbers

Some fields need numbers. `type="number"` brings up spinner arrows. `min`, `max`, and `step` constrain the value.

```html
<p>Berth count requested: <input type="number" min="1" max="4" step="1"></p>
```

The arrows respect `min` and `max`, but typing is not prevented — the browser flags an out-of-range value when submitting. That is correct behavior for client-side checks: it guides, it does not replace server validation.

## Choosing a Watch Role

When exactly one choice is allowed, use `type="radio"`. All radios in a group share the same `name`. Each needs a unique `id`, and each needs a `<label>` with `for` matching that `id`. Clicking the label toggles the radio — this is essential for usability.

```html
<p>Watch Role:</p>
<input type="radio" id="role-tide" name="watch-role" value="tidewatcher">
<label for="role-tide">Tidewatcher</label><br>
<input type="radio" id="role-radio" name="watch-role" value="radio">
<label for="role-radio">Radio Operator</label><br>
<input type="radio" id="role-logistics" name="watch-role" value="logistics">
<label for="role-logistics">Logistics</label>
```

> [!IMPORTANT]
> Radios without labels are nearly impossible to click reliably. If a mouse user has to aim for a tiny circle, the form is hostile. Labels are not decoration — they are the hit target.

## Packing for a Storm Run

When multiple items can be selected, use `type="checkbox"`. Checkboxes in a group can share the same `name`, but each is independent — any combination is valid.

```html
<p>Storm Kit:</p>
<input type="checkbox" id="kit-lantern" name="kit" value="lantern">
<label for="kit-lantern">Lantern</label><br>
<input type="checkbox" id="kit-rope" name="kit" value="rope">
<label for="kit-rope">Mooring Rope</label><br>
<input type="checkbox" id="kit-chart" name="kit" value="chart">
<label for="kit-chart">Tide Chart</label><br>
<input type="checkbox" id="kit-signal" name="kit" value="signal">
<label for="kit-signal">Signal Flares</label>
```

> [!TIP]
> Rule of thumb: if selecting one should deselect others, use radio. If selections accumulate, use checkbox. "Which role are you taking?" is radio. "What are you packing?" is checkbox.

## Output

A complete intake form renders as labeled fields, groupings for radios and checkboxes, and a submit button. The browser enforces basic constraints on `email`, `required`, `minlength`, `maxlength`, `min`, `max`. The structure is the manifest — even if nothing is sent yet, it is unambiguous about what the harbor office needs.

## Task 3: File the Storm Slipway Request

Create `slipway-request.html` with a form containing: a heading "Storm Slipway Request", a required text input for Vessel Name with minlength 3 and maxlength 16, a required email input for the contact, a number input for berths requested (min 1, max 3), a radio group named `urgency` with at least three options each labeled properly, a checkbox group named `equipment` with at least four options each labeled properly, and a submit button labeled "Submit Request". Put all inputs inside a single `<form>`.

**Why this order:** collecting structured data is a different skill from writing static text — the labels, names, and constraints are part of the specification, not afterthoughts.

**Next:** [[04 - Slipway Semantics]]
