# OCED-M Model

OCED-M is the local assurance model used at a real registry coordinate.

It consists of:

- Obligation
- Control
- Evidence
- Disposition

and

- Mechanism Formation

## Obligation

Obligation defines what must already hold at the coordinate for lawful
continuation to be possible.

Examples:

- a route lock exists
- dependencies are resolved
- the current object binding is present

## Control

Control defines what the mechanism checks and where it must fail closed.

Examples:

- missing lock binding
- unresolved dependency
- stale object state
- failed integrity condition

## Evidence

Evidence defines what explicit record or justification must be attached to the
coordinate.

Examples:

- build package identifier
- integrity judgment
- audit trace identifier

## Disposition

Disposition defines the typed next-state meaning of the coordinate.

Examples:

- continue
- return to repair
- block continuation

## Mechanism Formation

Mechanism formation is the step that makes the assurance tuple machine-carried
rather than prose-only.

The point is not just to describe the governance rule.
The point is to compile it into a local mechanism that enforces the rule.
