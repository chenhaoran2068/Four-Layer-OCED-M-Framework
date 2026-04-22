from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FILES = [
    "coordinate_registry.json",
    "ocedm_assignment.json",
    "mechanism_binding.json",
    "trace_event_allow.json",
    "trace_event_block.json",
]

ALLOWED_LAYERS = {"law", "object", "runtime", "audit"}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate_bundle(bundle_root: Path) -> list[str]:
    failures: list[str] = []
    for name in REQUIRED_FILES:
        ensure((bundle_root / name).is_file(), f"missing required file: {name}", failures)
    if failures:
        return failures

    coordinate = load_json(bundle_root / "coordinate_registry.json")
    ocedm = load_json(bundle_root / "ocedm_assignment.json")
    mechanism = load_json(bundle_root / "mechanism_binding.json")
    allow_event = load_json(bundle_root / "trace_event_allow.json")
    block_event = load_json(bundle_root / "trace_event_block.json")

    coordinate_id = coordinate.get("coordinate_id")
    ensure(bool(coordinate_id), "coordinate_registry.json must define coordinate_id", failures)
    ensure(coordinate.get("layer") in ALLOWED_LAYERS, "coordinate layer must be one of law/object/runtime/audit", failures)

    for file_name, payload in {
        "ocedm_assignment.json": ocedm,
        "mechanism_binding.json": mechanism,
        "trace_event_allow.json": allow_event,
        "trace_event_block.json": block_event,
    }.items():
        ensure(payload.get("coordinate_id") == coordinate_id, f"{file_name} coordinate_id must match coordinate_registry.json", failures)

    allowed_dispositions = set(coordinate.get("allowed_dispositions", []))
    ocedm_paths = set(ocedm.get("disposition", {}).get("allowed_paths", []))
    ensure(bool(allowed_dispositions), "coordinate_registry.json must declare allowed_dispositions", failures)
    ensure(allowed_dispositions == ocedm_paths, "coordinate_registry.json and ocedm_assignment.json must agree on allowed dispositions", failures)

    mechanism_map = mechanism.get("disposition_map", {})
    mechanism_values = set(mechanism_map.values())
    ensure(mechanism_values.issubset(allowed_dispositions), "mechanism disposition_map values must be declared in allowed_dispositions", failures)

    for file_name, payload in {
        "trace_event_allow.json": allow_event,
        "trace_event_block.json": block_event,
    }.items():
        outcome = payload.get("outcome")
        ensure(outcome in allowed_dispositions, f"{file_name} outcome must be declared in allowed_dispositions", failures)
        ensure(bool(payload.get("recorded_at")), f"{file_name} must define recorded_at", failures)
        ensure(isinstance(payload.get("evidence_refs"), list), f"{file_name} evidence_refs must be a list", failures)

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a public Four-Layer OCED-M worked-example bundle.")
    parser.add_argument("bundle_root", help="Example bundle directory.")
    args = parser.parse_args()

    bundle_root = Path(args.bundle_root).resolve()
    failures = validate_bundle(bundle_root)
    if failures:
        print("validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("validation passed")
    print(f"bundle: {bundle_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
