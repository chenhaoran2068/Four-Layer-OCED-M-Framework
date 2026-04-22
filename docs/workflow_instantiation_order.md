# Workflow Instantiation Order

This document defines a recommended build order for instantiating a real
workflow family with the Four-Layer OCED-M Framework.

It answers a practical question that the theory documents do not answer by
themselves:

- in what order should a builder turn a workflow idea into a governed workflow
  surface

## Why This Document Exists

Four-Layer and OCED-M are complementary views, not chronological workflow
stages.

- Four-Layer describes where workflow-governance structure lives
- OCED-M describes how a real registry coordinate is assured

That theoretical split is important, but builders still need a practical
construction order.

Without an explicit order, teams often do one of the following:

- start by writing many agent roles before the workflow boundary is clear
- start by writing scripts before artifact contracts exist
- start by registering too many coordinates before the major gates are known
- start by exposing implementation detail before the governance model is stable

This document recommends a more conservative sequence.

## Recommended Order

The recommended order is:

1. scope the workflow family
2. define the stage skeleton
3. define the gate skeleton
4. select a small set of governance-bearing coordinates
5. assign each coordinate to a dominant Four-Layer location
6. assign OCED-M to each coordinate
7. bind the coordinate into executable mechanism logic
8. define artifact contracts for state, handoff, gate, trace, and registry
9. define control roles such as manager and worker agents
10. build bootstrap and deterministic execution helpers
11. validate in a bounded environment before real use
12. capture retrospective learning and promote only when needed

The sections below expand each step.

## Step 1. Scope The Workflow Family

Complete:

- define the workflow family's purpose
- define what it owns
- define what it does not own
- define the first realistic use case

Outputs:

- short scope note
- ownership boundary
- non-goal list

Watch for:

- trying to absorb the whole workspace into one workflow root
- confusing a workflow family with one project instance
- confusing shared assets with local workflow ownership

Why first:

- if scope is wrong, every later stage, gate, and coordinate will drift

## Step 2. Define The Stage Skeleton

Complete:

- list the major stages from intake to completion
- define the main route through the workflow
- define where rollback or rework may return

Outputs:

- stage map
- short route narrative

Watch for:

- making stages too fine-grained too early
- confusing structural layers with workflow stages
- defining worker roles before the stage windows are clear

Why here:

- a workflow must know its major progression shape before it can know where
  governance boundaries matter

## Step 3. Define The Gate Skeleton

Complete:

- identify which stage boundaries require explicit review
- define what a pass, hold, reroute, or failure means at each gate
- define where human approval may be required

Outputs:

- gate map
- gate names
- one-line gate intent for each boundary

Watch for:

- making every transition a gate
- treating gates as mere status labels instead of evidence-bearing boundaries
- hiding a missing default or failure path

Why here:

- gate logic should be visible before coordinate registration expands

## Step 4. Select A Small Set Of Governance-Bearing Coordinates

Complete:

- shortlist the coordinates that truly matter for lawful progression
- begin with a few high-value coordinates rather than a full ontology

Outputs:

- initial coordinate shortlist
- short reason for each coordinate

Watch for:

- registering everything that exists instead of everything that governs
- choosing coordinates that are too vague to emit evidence
- building a large registry before any gate is stable

Why here:

- the workflow now has enough structure to identify meaningful control points

## Step 5. Assign Each Coordinate To A Dominant Structural Layer

Complete:

- decide whether each coordinate is mainly law, object, runtime, or audit
- record the dominant layer explicitly

Outputs:

- coordinate registry draft with layer assignment

Watch for:

- treating the layer as a chronological stage
- forcing a coordinate into multiple layers instead of picking a dominant one
- forgetting that cross-layer consequences can still exist

Why here:

- Four-Layer gives the structural location before OCED-M describes local
  assurance

## Step 6. Assign OCED-M To Each Coordinate

Complete:

- define obligation
- define control
- define evidence
- define disposition
- define mechanism-formation intent

Outputs:

- one OCED-M assignment per coordinate

Watch for:

- writing only prose aspiration with no typed disposition
- omitting user-approval requirements where they materially matter
- letting evidence remain implicit

Why here:

- once the coordinate and dominant layer are known, its local assurance model
  can be made explicit

## Step 7. Bind The Coordinate Into Mechanism Logic

Complete:

- turn OCED-M into preconditions
- define fail-closed checks
- define emitted records
- define a disposition map

Outputs:

- mechanism binding
- explicit emitted-record list

Watch for:

- leaving OCED-M as prose only
- mixing approval-sensitive reroutes with ordinary repairable failures
- failing open when a required input is missing

Why here:

- mechanism binding is what stops the model from remaining theoretical only

## Step 8. Define Artifact Contracts

Complete:

- define state records
- define handoff envelopes
- define gate-check reports
- define trace events
- define registry and inventory artifacts

Outputs:

- schemas
- templates
- canonical file locations

Watch for:

- scripts writing into unstable paths
- overwriting audit history instead of appending
- having only machine-readable or only human-readable outputs instead of both

Why here:

- artifacts give the workflow a durable control surface and make later
  automation auditable

## Step 9. Define Control Roles

Complete:

- define the manager role
- define worker stage windows
- define escalation rules
- define user-approval boundaries
- define what skills are reusable capabilities versus role ownership

Outputs:

- agent specifications
- skill boundary notes

Watch for:

- writing a large agent zoo before the gates are known
- putting content warehouses into `agents/` or `skills/`
- allowing workers to silently change protected boundaries

Why here:

- roles should inherit the workflow's boundary model rather than invent it

## Step 10. Build Bootstrap And Deterministic Helpers

Complete:

- create project bootstrap scaffolds
- create inventory and registry builders
- create gate-check runners
- create deterministic build and export helpers where needed

Outputs:

- bootstrap scripts
- inventory or registry builders
- gate-check scripts

Watch for:

- letting scripts fabricate approvals or canonicality
- coupling state advancement to gate checking
- making the script layer the first place where the workflow becomes explicit

Why here:

- the scripts should implement an existing contract, not define the contract by
  accident

## Step 11. Validate In A Bounded Environment Before Real Use

Complete:

- perform at least one bounded validation pass before broader use
- choose a validation form that matches the workflow's maturity and risk
- verify that stage, gate, coordinate, and artifact logic behave coherently
- check that obvious failure paths fail conservatively rather than silently

Outputs:

- bounded validation evidence
- validation notes

Watch for:

- jumping directly into live projects
- treating any one validation form as sufficient by itself
- treating a neat demonstration as proof that the live system is stable

Why here:

- bounded validation is the first serious proof that the workflow is coherent
  before it is trusted in broader use

Possible forms include:

- synthetic examples
- local dry runs
- simulated gate transitions
- bounded pilot runs
- partial artifact-generation checks

## Step 12. Capture Retrospective Learning And Promote Only When Needed

Complete:

- run retrospective review after bounded real use or dry-run completion
- decide whether the workflow should remain local, become reusable internally,
  or be promoted more broadly
- promote only the durable lessons when promotion is actually part of the goal

Outputs:

- retrospective summary
- optional promotion decision
- updated docs, gates, templates, or agent contracts when justified

Watch for:

- leaving critical lessons trapped in chat history
- fixing generated outputs without also fixing their generator or template
- assuming that every workflow must be promoted or shared
- promoting too early because the workflow looks conceptually elegant

Why last:

- even when a workflow is not meant for public sharing, retrospective learning
  still improves the next build
- promotion should be conditional, not assumed

## What The Research Workflow Taught

The current research workflow suggests several practical lessons:

1. stage and gate clarity came before durable automation
2. registry builders were most useful after the intake and gate contracts were
   already known
3. manager authority and approval routing mattered early
4. dry runs became meaningful only after artifact locations and gate outputs
   stabilized

This is why the recommended order is not:

- agents first
- scripts first
- full registry first

It is closer to:

- workflow skeleton first
- boundaries second
- coordinates third
- assurance and mechanism fourth
- automation fifth
- rehearsal and promotion last

## Why This Order Is Recommended

The order above is not taken from one source alone.
It is synthesized from three inputs.

### 1. Framework Logic

From this repository's own theory:

- `docs/overview.md`
- `docs/four_layer_model.md`
- `docs/ocedm_model.md`

The framework implies that builders should distinguish:

- workflow skeleton
- governance-bearing boundaries
- registry coordinates
- coordinate assurance
- mechanism binding
- trace and audit surfaces

### 2. External Reference Patterns

The recommended order is also informed by several external official patterns.

- AWS Step Functions: the first step in developing a workflow is defining the
  workflow steps in Amazon States Language, and state machines are defined as a
  structured set of states and transitions before execution
  - `https://docs.aws.amazon.com/step-functions/latest/dg/developing-workflows.html`
  - `https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html`
- Open Policy Agent: policy decision-making should be decoupled from policy
  enforcement rather than being hidden inside arbitrary execution code
  - `https://www.openpolicyagent.org/docs`
- Camunda BPMN guidance: decisions and defaults should be modeled explicitly at
  gateways, and process documentation should live with the process definition
  rather than outside it
  - `https://docs.camunda.io/docs/components/modeler/bpmn/exclusive-gateways/`
  - `https://docs.camunda.io/docs/next/components/modeler/web-modeler/modeling/advanced-modeling/process-documentation-with-readme-files/`

These references do not define Four-Layer OCED-M.
They do support three broad lessons:

1. define the process skeleton before running it
2. separate policy or boundary logic from arbitrary execution detail
3. keep decision points and process documentation explicit

### 3. Local Build History

The current `Research_Orchestration_Workflow` grew in a way that also points to
an effective order.

Its own README identifies these as early core documents:

- `docs/workflow_outline.md`
- `docs/memory_model.md`
- `docs/professional_review_panel.md`
- `docs/qa_rounds.md`
- `schemas/research_project_layout.md`
- `gates/gate_map.md`
- `docs/gate_check_framework.md`

Only after that design surface existed did the system add explicit bootstrap and
registry builders such as:

- `docs/bootstrap_registry_builders.md`
- `scripts/bootstrap_research_project.py`
- `scripts/build_source_inventory.py`
- `scripts/build_research_registry.py`

That local history matters.
It suggests that a governed workflow becomes stable faster when builders define
its structure, gate logic, and artifact contracts before scaling out
automation.

## Appendix: Minimum Public-Safe Instantiation Pack

If a workflow family is not ready to publish a full implementation repository,
the smallest useful public-safe pack is:

- one stage map
- one gate map
- one coordinate registry entry
- one OCED-M assignment
- one mechanism binding
- one allow trace
- one block or reroute trace
- one or two control-role samples
- one synthetic walkthrough

This repository's two current examples follow that philosophy:

- `examples/build_readiness_coordinate/`
- `examples/research_orchestration_instantiation/`

## Short Version

Do not start by writing many agents or scripts.

Start by making the workflow legible:

1. stages
2. gates
3. coordinates
4. layer assignment
5. OCED-M
6. mechanism
7. artifacts
8. roles
9. scripts
10. bounded validation
11. retrospective learning
12. optional promotion
