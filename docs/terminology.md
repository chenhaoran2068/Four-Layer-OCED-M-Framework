# Terminology Baseline

This document fixes the core terminology used throughout the Four-Layer
OCED-M Framework repository.

It is intentionally narrow.
Its role is not to define every framework object.
Its role is to stabilize five closely related governance terms that are easy
to blur together:

- silent workflow-governance drift
- hallucination
- drift externalization
- reconstructability
- bounded execution

## House Style

- use **silent workflow-governance drift** as the formal name of the primary
  workflow-governance failure
- after first definition, **silent drift** is the acceptable short form
- do not use bare `drift` as the repository's primary failure name
- preserve established outside terms such as `configuration drift`,
  `process drift`, and `data/concept drift` when referring to prior work
- keep `hallucination` as the term for unsupported output content rather than
  using `drift` for that failure class

## 1. Silent Workflow-Governance Drift

Silent workflow-governance drift is the condition in which the effective law,
object, runtime, or audit bindings of a workflow system change without explicit
approval, formal change registration, or an auditable transition, such that the
system continues to operate while no longer matching the system that was
declared, constrained, and reconstructable.

Operational reading:

- the danger is not only that an output changes
- the deeper danger is that the effective governing workflow changes while the
  system still appears normal
- product change may be one consequence, but it is not the full definition

## 2. Hallucination

Hallucination is an output-level failure in which the system produces
unsupported content as though it were grounded, evidenced, or otherwise
licensed.

Typical examples include:

- fabricated claims
- fabricated citations
- unsupported field values
- unsupported summaries

Operational reading:

- hallucination concerns what is said or emitted
- silent workflow-governance drift concerns what governing system is actually
  operating

## 3. Drift Externalization

Drift externalization is the workflow property under which silent
workflow-governance drift cannot remain a silent normal operating mode and must
instead surface as an explicit block, reroute, re-authorization, invalidation,
or auditable transition.

Operational reading:

- drift externalization is not drift prevention
- it is not a claim that all deviation is impossible
- it is the claim that governance-relevant change must not remain hidden inside
  apparently ordinary successful execution

## 4. Reconstructability

Reconstructability is the workflow property under which later inspection can
recover what happened, why it happened, what evidence the system relied upon,
and what authority or mechanism licensed the next movement.

Operational reading:

- reconstructability is stronger than flat logging
- it requires explicit coordinate, evidence, control, and attribution surfaces
- the point is not perfect token replay but governance-relevant recovery of the
  executed path

## 5. Bounded Execution

Bounded execution is the workflow property under which execution remains inside
explicit movement boundaries concerning what is allowed, which object is
current, which path is lawful, and when progression must stop, return, or
reroute.

Operational reading:

- bounded execution is governance-boundedness, not a theorem of universal
  termination
- the point is that movement does not proceed through implicit convenience
- lawful path, current object identity, mediated runtime action, and audit
  trace remain structurally coupled

## Relationship Map

These five terms are related but not interchangeable.

1. Hallucination and silent workflow-governance drift are different failure
   classes.
   Hallucination is output-level unsupported content.
   Silent workflow-governance drift is workflow-level ungoverned change in the
   effective operating system.
2. A system may hallucinate without having undergone silent
   workflow-governance drift.
   One local answer may fabricate content even if the workflow contract itself
   remains stable.
3. A system may undergo silent workflow-governance drift without obvious
   hallucination.
   The outputs may still look plausible while the effective governing system
   has already changed.
4. Drift externalization is the property that opposes silent
   workflow-governance drift.
   It forces governance-relevant change to surface explicitly.
5. Reconstructability is the property that allows later recovery of the
   governing path after execution.
   It answers what happened and why.
6. Bounded execution is the property that keeps runtime progression inside
   explicit movement constraints while execution is still occurring.
7. Together, drift externalization, reconstructability, and bounded execution
   form a coordinated governance posture:
   - drift externalization prevents hidden governance-relevant change from
     remaining silent
   - reconstructability preserves later attributable recovery of the governing
     path
   - bounded execution constrains progression before open-ended convenience
     takes over

## Relationship To Four-Layer And OCED-M

Four-Layer and OCED-M are not synonyms for the five terms above.
They are the framework structures used to support them.

- Four-Layer distributes workflow-governance structure across law, object,
  runtime, and audit
- OCED-M supplies coordinate-level assurance through obligation, control,
  evidence, disposition, and mechanism formation

Within the current framework claim:

- silent workflow-governance drift is the primary workflow-governance failure
- drift externalization, reconstructability, and bounded execution are the
  primary target properties
- Four-Layer and OCED-M are the structural means used to support those
  properties
