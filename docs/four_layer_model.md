# Four-Layer Model

The framework organizes workflow governance across four structural layers:

- Law
- Object
- Runtime
- Audit

These are structural layers, not chronological workflow stages.

## Law

The law layer defines typed lawful movement classes.

It answers questions such as:

- what kinds of movement are admissible
- what kinds of transition are allowed
- what counts as a lawful return, reroute, or block

## Object

The object layer preserves currentness, stale invalidation discipline, and local
object identity.

It answers questions such as:

- what object is current
- what authority tuple is attached to that object
- what event makes the current object stale

## Runtime

The runtime layer preserves mediated corridor passage, scoped reentry, and
fail-closed execution boundaries.

It answers questions such as:

- how governance-relevant actions are lowered into explicit mediated acts
- how runtime continuation, wait, route, or spawn behavior remains bounded
- where fail-closed checks are attached

## Audit

The audit layer preserves authoritative replay lineage, quarantine surfacing,
and reconstructability.

It answers questions such as:

- what trace records are emitted
- how blocked or allowed progression can later be reconstructed
- how later inspection distinguishes attributable execution from informal description

## Structural Reading

These layers are not decorative labels.
Each layer removes a distinct governability-bearing structure when isolated or
collapsed.
