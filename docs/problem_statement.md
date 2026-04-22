# Problem Statement

Current AI workflow systems are becoming increasingly capable at execution.
They can plan, route, call tools, and sustain long multi-step runs.
But execution capability alone does not guarantee governability.

This framework focuses on three structural failure modes.

## 1. Silent Workflow-Governance Drift

The primary failure term in this repository is **silent
workflow-governance drift** (hereafter, **silent drift**).
It is the condition in which the effective law, object, runtime, or audit
bindings of a workflow system change without explicit approval, formal change
registration, or an auditable transition, such that the system continues to
operate while no longer matching the system that was declared, constrained, and
reconstructable.

The danger is that the system can still appear successful at the surface level.
This is not the same as output-level hallucination.
Hallucination is about unsupported content being produced.
Silent drift is about the effective governing workflow changing while still
appearing normal.

## 2. Irreconstructible Execution

The system produces an output, but later cannot strongly reconstruct:

- the decision path
- the evidence basis
- the authorization chain
- the reason the result was allowed or blocked

Execution happened, but governance cannot later inspect it in an attributable
sense.

## 3. Unbounded Movement

Unbounded movement is the condition in which progression continues through
implicit convenience rather than explicit movement constraints.
The system keeps moving, but what counts as lawful movement, current object
identity, or lawful return is no longer stably represented.

## Why The Gap Persists

Many systems are still organized around capability orchestration rather than
around explicit governance structure.
They may expose agents, tools, memory, or routing logic, while leaving legality,
evidence burden, authority boundary, and disposition control diffuse across the
system.

## Framework-Level Answer

The framework treats the workflow problem as structural.
It answers with:

- a four-layer architecture
- an authored but admissible registry
- coordinate-level assurance via OCED-M
- machine-carried mechanism formation

Within the framework claim, the target properties are drift externalization,
reconstructability, and bounded execution.
The third of these is a target property: it is the answer to unbounded
movement rather than a second name for the same failure.
 
