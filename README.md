# Four-Layer OCED-M Framework

This repository packages a public-facing framework for governable agentic
workflow systems.

It focuses on a specific workflow-governance problem family:

- systems that undergo **silent workflow-governance drift**
- systems that fall into **irreconstructible execution**
- systems that continue through **unbounded movement**

The framework answers that problem with two named structural commitments:

- **Four-Layer**: a structural organization over law, object, runtime, and audit
- **OCED-M**: a coordinate-level assurance model over obligation, control,
  evidence, disposition, and mechanism formation
- authored registry coordinates rather than purely runtime-inferred governance
- local mechanism formation that turns governance into machine-carried
  boundaries

These are complementary views, not sequential stages.
**Four-Layer** describes where workflow-governance structure lives.
**OCED-M** describes how a real registry coordinate is assured.
A coordinate typically sits in one dominant structural layer while also
carrying an OCED-M assignment.
This does not require one separately deployed executable unit per coordinate.
Multiple coordinates may be carried through shared compiled mechanisms so long
as coordinate-level governance and audit boundaries remain explicit.

Throughout this repository, the primary failure term is **silent
workflow-governance drift** (hereafter, **silent drift**): a change in the
effective law, object, runtime, or audit bindings of a workflow system without
explicit approval, formal change registration, or an auditable transition, such
that the system continues to operate while no longer matching the system that
was declared, constrained, and reconstructable.

This is not the same as hallucination.
Hallucination is an output-level failure in which unsupported content is
produced.
Silent drift is a workflow-governance failure in which the effective governing
system changes while still appearing to operate normally.

The other two paper-facing failure names are **irreconstructible execution**
and **unbounded movement**.
Their corresponding target properties are **reconstructability** and
**bounded execution**.

## What Problem Does This Solve?

Many AI workflow systems do not fail by crashing.
They fail by quietly becoming something else while still appearing successful.

Teams using this framework typically need workflow systems to remain:

- governable instead of merely executable
- attributable instead of only outcome-producing
- reconstructable instead of opaque after completion
- bounded instead of open-ended under pressure

## What This Repository Contains

- framework-level documentation
- theoretical framing and formal model documents
- public-facing concepts and terminology
- minimal schemas for registry, assurance, and trace objects
- minimal templates for worked examples
- a small build-readiness worked example
- a distilled research-workflow instantiation example
- GitHub-safe helper scripts for validating the example bundle

## What This Repository Does Not Contain

- private project workspaces
- local production data
- workstation-specific path bindings
- internal memory stores
- full local production assets from active workflow systems
- active paper workspace build artifacts

## Public Implementation Status

This repository is a framework and specification repository.
It is not intended to duplicate every implementation surface or to claim that a
full public runtime repository already exists.

Current public implementation status:

- a public workflow-facing companion repository is now available:
  `https://github.com/chenhaoran2068/Research_Workflow`
- that companion repository presents a cleaned public workflow example and
  bounded public validation surface
- that companion repository is not a full public runtime mirror
- this framework repository still uses distilled public examples rather than a
  full runtime mirror
- the current clinical research example is a public-safe instantiation profile,
  not a raw export of an active local orchestration system
- the public materials in this repository provide the conceptual and structural
  foundation for future public implementations

In other words:

- this repository explains the framework
- this repository includes minimal public examples of how the framework can be
  instantiated
- `Research_Workflow` is the main public workflow-facing companion repository
  for the current research workflow pack
- a later fuller public runtime repository may still expose a broader system
  implementation

## Repository Layout

- `docs/`
  - problem framing, framework summaries, workflow-instantiation guidance,
    terminology, scope, and implementation relationship
- `schemas/`
  - minimal JSON schemas for registry, assurance, mechanism, and trace artifacts
- `templates/`
  - starter JSON templates for the public worked-example format
- `examples/`
  - a minimal build-readiness coordinate example
  - a distilled research-orchestration instantiation example
- `scripts/`
  - GitHub-safe helper scripts
- `figures/`
  - diagram placeholders and figure notes

## Quick Start

1. Read `docs/problem_statement.md`.
2. Read `docs/four_layer_model.md` and `docs/ocedm_model.md`.
3. Read `docs/terminology.md`.
4. Read `docs/workflow_instantiation_order.md`.
5. Inspect `examples/build_readiness_coordinate/`.
6. Inspect `examples/research_orchestration_instantiation/`.
7. Inspect the workflow-facing companion repository:
   `https://github.com/chenhaoran2068/Research_Workflow`
8. Run:

```powershell
python scripts/validate_example_bundle.py examples/build_readiness_coordinate
python scripts/validate_example_bundle.py examples/research_orchestration_instantiation
```

## Current Scope

This repository is intentionally narrow.
It is a public framework repository for Four-Layer OCED-M, not a mirror of a
larger local workspace.

For scope boundaries and release-readiness guidance, review:

- `docs/repository_scope.md`
- `docs/release_readiness.md`

## License And Citation

- license: Apache-2.0
- citation metadata: `CITATION.cff`

License and citation metadata are included in this repository and can be
updated in future releases as needed.
