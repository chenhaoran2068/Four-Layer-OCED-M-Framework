# Four-Layer OCED-M Framework

This repository packages a public-facing framework for governable agentic
workflow systems.

It focuses on a specific workflow-governance problem:

- systems that keep moving while silently drifting
- systems that produce results but cannot later reconstruct why they were allowed
- systems that continue through implicit convenience rather than explicit bounds

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

## What Problem Does This Solve?

Many AI workflow systems do not fail by crashing.
They fail by quietly becoming something else while still appearing successful.

This repository is for teams that need workflow systems to remain:

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

- no full public workflow-system implementation repository has been released yet
- this repository therefore uses distilled public examples rather than a full
  runtime mirror
- the current clinical research example is a public-safe instantiation profile,
  not a raw export of an active local orchestration system
- the public materials in this repository provide the conceptual and structural
  foundation for future public implementations

In other words:

- this repository explains the framework
- this repository includes minimal public examples of how the framework can be
  instantiated
- a later public runtime repository may expose a fuller system implementation

## Repository Layout

- `docs/`
  - problem framing, framework summaries, workflow-instantiation guidance,
    scope, and implementation relationship
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
3. Read `docs/workflow_instantiation_order.md`.
4. Inspect `examples/build_readiness_coordinate/`.
5. Inspect `examples/research_orchestration_instantiation/`.
6. Run:

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
