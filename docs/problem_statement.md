# Problem Statement

Current AI workflow systems are becoming increasingly capable at execution.
They can plan, route, call tools, and sustain long multi-step runs.
But execution capability alone does not guarantee governability.

This framework focuses on three structural failure modes.

## 1. Silent Drift

The system changes its goal, identity, evidence basis, or lawful path without
surfacing that change as a block, reroute, re-authorization, invalidation, or
auditable transition.

The danger is that the system can still appear successful at the surface level.

## 2. Irreconstructible Execution

The system produces an output, but later cannot strongly reconstruct:

- the decision path
- the evidence basis
- the authorization chain
- the reason the result was allowed or blocked

Execution happened, but governance cannot later inspect it in an attributable
sense.

## 3. Unbounded Execution

The system continues through implicit convenience rather than explicit movement
constraints.
It keeps moving, but what counts as lawful movement, current object identity,
or lawful return is no longer stably represented.

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
- coordinate-level assurance via OCED
- machine-carried mechanism formation

