# Research Orchestration Instantiation

This directory contains a distilled public-safe instantiation example derived
from a governed clinical research workflow family.

It is intentionally smaller than a live orchestration system root.
Its purpose is to show how Four-Layer OCED-M can govern a research workflow
without copying a private local console into the public repository.

This example includes:

- a minimal coordinate bundle for `r_protocol_lock`
- a condensed stage map
- a condensed gate map
- two sample agent-control specifications
- a synthetic handoff, gate-check, registry snapshot, and walkthrough

Files and subdirectories:

- `coordinate_registry.json`
- `ocedm_assignment.json`
- `mechanism_binding.json`
- `trace_event_allow.json`
- `trace_event_block.json`
- `stage_map.md`
- `gate_map.md`
- `synthetic_dry_run_walkthrough.md`
- `agent_specs/`
- `synthetic_run/`

This example does not contain:

- workstation-specific absolute paths
- real project memory or approvals
- raw local dry-run exports
- runnable copies of the full private orchestration system
