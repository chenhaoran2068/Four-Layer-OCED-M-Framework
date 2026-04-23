# Relationship To Implementations

This repository is a public framework repository.

Its purpose is to expose:

- the formal problem
- the four-layer structure
- the OCED-M assurance model
- minimal schemas and examples

It is not intended to duplicate every concrete implementation repository.

## Current Public Status

- this repository stays at the framework/specification layer
- a public workflow-facing companion repository is now available:
  `https://github.com/chenhaoran2068/Research_Workflow`
- that companion repository is the main public workflow instantiation
  repository for the current research workflow pack
- that companion repository is a cleaned public workflow pack, not a full
  runtime mirror
- the public examples in this repository are intentionally distilled and
  synthetic enough to remain upload-safe

## Current Public Example Surfaces

- `https://github.com/chenhaoran2068/Research_Workflow`
  - the public workflow-facing companion repository
  - presents a cleaned public workflow example with explicit reading,
    validation, agent-entry, and frozen-evidence surfaces
  - not a full public runtime mirror
- `examples/build_readiness_coordinate/`
  - a coordinate-level micro example for route binding, fail-closed checks, and
    traceable continuation versus blocking
- `examples/research_orchestration_instantiation/`
  - a public-safe instantiation profile derived from a governed clinical
    research workflow family
  - includes a minimal coordinate bundle, condensed stage and gate maps, agent
    contract samples, and synthetic handoff/gate/trace artifacts

## Important Boundary

- these examples are not a full runtime mirror
- they do not expose an entire local control console
- they do not expose local private paths, historical approval logs, or private
  project surfaces

## Future Public Direction

A later public workflow-system repository may expose:

- governed project state
- route locking
- gate logic
- audit-native progression
- mediated execution lowerings

Until that fuller public runtime repository exists, this framework repository
should remain honest about scope and should not pretend to include a complete
public runtime implementation.
