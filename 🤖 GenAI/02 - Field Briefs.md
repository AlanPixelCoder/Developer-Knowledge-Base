
# 02. Field Briefs

**Spanish version:** [02 - Instrucciones de Campo](./02%20-%20Instrucciones%20de%20Campo.md)

**Course:** GenAI
**Chapter:** 2 — Verdant Relay
**Topic:** Prompts, roles, constraints, few-shot, failure
**Tags:** `#genai` `#prompts` `#few-shot` `#llm` `#python`

At Verdant Relay, a vague dispatch to a field crew produces vague repairs. A precise **field brief** states role, context, constraints, and the exact output shape before anyone leaves the pole yard. The same holds for a language model: a prompt is an instruction set, not a question tossed into the void. This lesson treats prompt crafting as specification writing — testable, constrained, and easy to break with ambiguity. No "chatbot persona" fluff: just briefs that produce usable relay notes.

## From guess to specification

Compare two briefs for the same job: summarize a short relay burst for a night log. The first is a question; the second is a brief.

```text
Brief A (vague): "What happened at Pole-3?"
Brief B (precise): "You are a Verdant Relay night-logger. Summarize in exactly one line,
using: <pole> | <issue> | <action>. Only use facts present in the burst. 
Burst: 'Pole-3 reports fog at gate, crew placed sandbags.'"
```

> [!NOTE]
> Specificity isn't wordiness. Brief B fixes role, format, allowed scope (only given facts), and output shape. Those constraints are easier to check than "be helpful".

## Building constraints

Good briefs narrow the space of possible answers. For relay work, useful constraints are: output format, length, tone (terse), what to include/exclude, and refusal conditions. Write constraints as rules, not requests.

```python
burst = "Pole-7 reports loose guy-wire near mast. Crew tightened turnbuckle."
brief = (
  "Role: Verdant Relay night-logger.\n"
  "Task: Write one terse log line in format '<POLE> | <ISSUE> | <ACTION>'.\n"
  "Rules: only use facts from burst; no speculation; no extra commentary.\n"
  f"Burst: {burst}"
)
print(brief)
```

## Output

```text
Role: Verdant Relay night-logger.
Task: Write one terse log line in format '<POLE> | <ISSUE> | <ACTION>'.
Rules: only use facts from burst; no speculation; no extra commentary.
Burst: Pole-7 reports loose guy-wire near mast. Crew tightened turnbuckle.
```

A correct answer for this brief would be `Pole-7 | loose guy-wire near mast | tightened turnbuckle`. The shape is testable by eye.

## Few-shot: showing, not telling

Sometimes a rule is clearer as an example. **Few-shot prompting** gives the model a couple of input/output pairs that follow the exact shape, then gives the new burst. This is especially effective for tight formats like log lines or field codes.

```python
few_shot = [
    ("Pole-3 reports fog at gate, crew placed sandbags.", "Pole-3 | fog at gate | placed sandbags"),
    ("Pole-1 reports corroded clamp near base, crew replaced clamp.", "Pole-1 | corroded clamp near base | replaced clamp"),
]
burst = "Pole-9 reports blocked drain at footing, crew cleared debris."
# brief would include pairs + burst
print("examples:", len(few_shot))
```

> [!TIP]
> Keep examples minimal and identical in structure to the target. If examples drift in format, the model will drift too. Consistency beats quantity.

## The cost of ambiguity

Ambiguous briefs create failure modes. "Summarize nicely" invites extra words. "Write a report" invites paragraphs. "Be thorough" invites speculation. For Verdant Relay, speculation is dangerous — a night log must not invent a fix that wasn't done. The fix is to replace adjectives of degree with checkable rules.

```python
# bad: "Summarize this nicely and be thorough."
# good: "Return exactly one line. Include only facts present. Do not add causes/recommendations."
print("replace 'nice' with 'exactly one line'")
```

> [!WARNING]
> A prompt that says "think step by step" is not wrong in general, but for a rigid format like a log line it's usually unnecessary and can bloat output. Match the level of reasoning required by the task: terse tasks need terse briefs.

## Testing a brief by hand

Treat the prompt as code: change one constraint, test mentally against the burst, see what breaks. For example, remove "only use facts" and the model might add "likely caused by moisture" — plausible, but unverified. Add "exactly one line" and paragraphs disappear. This is debugging by specification, not by begging the model to "try again".

```python
def check_line(s):
    # rough sanity for the format
    parts = s.split(' | ')
    return len(parts) == 3

print(check_line("Pole-7 | loose guy-wire near mast | tightened turnbuckle"))
print(check_line("Summary: there was an issue at Pole-7."))  # wrong format
```

## Output

```text
True
False
```

## Field discipline

Verdant Relay doesn't need a chatty briefing — it needs a brief that can be checked against a field code. Role, task, format, rules, and examples (if needed) are the ingredients. Keep it short, make it testable, and never ask for "more" when you mean "follow this shape exactly". That discipline carries over to the next lesson: once you know how to ask precisely, you can focus on *what* to ask over — finding relevant telem
