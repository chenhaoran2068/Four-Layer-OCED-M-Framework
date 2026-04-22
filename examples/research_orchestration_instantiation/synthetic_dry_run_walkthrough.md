# Synthetic Dry Run Walkthrough

This walkthrough is synthetic.
It is not copied from a live local project.

## Scenario

- research question: Does a baseline clinical risk score remain associated with
  a binary outcome after predefined adjustment?
- available support: one approved dataset family, one seed evidence packet, and
  one reporting-guideline stack
- current focus: show the protocol-lock boundary rather than the whole runtime

## Walkthrough

1. Intake creates a governed project shell and records a study-question draft.
2. Inventory review confirms that the required dataset family and literature
   subset exist.
3. The manager assembles a pre-protocol evidence packet.
4. The protocol worker proposes:
   - the main question
   - the main endpoint family
   - the primary model family
   - explicit exploratory branches
5. A gate check evaluates whether the protocol boundary is complete.
6. If the package is coherent, the project advances to knowledge build.
7. If a late change tries to replace the main endpoint family, the workflow
   does not silently continue.
8. Instead, it emits a decision request and routes the change to explicit user
   approval.

## Public Example Artifacts

- `synthetic_run/project_registry_snapshot.json`
- `synthetic_run/handoff_envelope.json`
- `synthetic_run/gate_check_report.json`

These artifacts are intentionally minimal and only demonstrate the control
shape.
