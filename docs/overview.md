# Overview

The Four-Layer OCED-M Framework is a workflow-governance framework for agentic
systems that operate over long-horizon, multi-step, and production-facing work.

Its core claim is that workflow governability is not only a prompt-quality
question or a local model-quality question.
It is also a structural systems question.

The framework therefore centers:

- explicit law
- explicit objects
- explicit runtime mediation
- explicit audit surfaces
- explicit registry coordinates
- explicit assurance assignment
- explicit compiled mechanism formation

## How Four-Layer And OCED-M Relate

The framework uses two different but complementary views.

- **Four-Layer** is the structural view.
  It describes where workflow-governance structure lives: law, object,
  runtime, and audit.
- **OCED-M** is the coordinate-assurance view.
  It describes how a real registry coordinate is constrained and carried:
  obligation, control, evidence, disposition, and mechanism formation.

These are not chronological workflow stages.
They are not two competing taxonomies either.

A coordinate typically belongs to one dominant structural layer while also
carrying an OCED-M assignment.
In that sense, Four-Layer gives the structural map, while OCED-M gives the
local assurance grammar used at a real coordinate.

In this repository, the term **silent workflow-governance drift** (hereafter,
**silent drift**) names a change in the effective law, object, runtime, or
audit bindings of a workflow system without explicit approval, formal change
registration, or an auditable transition, such that the system keeps operating
while no longer matching the system that was declared, constrained, and
reconstructable.

This is intentionally narrower than generic uses of `drift`.
It is not the same as classical data or concept drift, and it is not the same
as output-level hallucination.
Hallucination concerns unsupported content in an output.
Silent drift concerns governance-relevant change in the effective operating
workflow.

The practical aim is not to make every workflow identical.
The practical aim is to give workflow builders a structure for externalizing
silent drift, preserving reconstructability, and keeping execution inside
explicit movement bounds.
