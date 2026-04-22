# Build Readiness Worked Example

This directory contains a minimal public worked example for a build-readiness
coordinate, `r_build`.

The example follows a high-level framework sketch in which:

- a route lock must remain bound
- dependencies must remain resolved
- build state must remain current
- downstream continuation must fail closed when these conditions are violated

Files:

- `coordinate_registry.json`
- `ocedm_assignment.json`
- `mechanism_binding.json`
- `trace_event_allow.json`
- `trace_event_block.json`
