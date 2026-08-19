# Safe public examples

The technical source checkout contains report artifacts, not a standalone detector or tracker implementation. This folder therefore documents the shape of a publishable example without copying proprietary code or real rows.

## Abstract observation contract

An approved synthetic example could show fields such as:

```text
frame_index
timestamp_seconds
observation_type       # person or object
track_id                # synthetic or explicitly estimated ID
zone_id                 # scenario-specific polygon label
confidence              # model confidence, if approved
position_xy             # image-space coordinate, not metric-world position
```

This is a portfolio abstraction, not a claim about the exact production schema.

## Example requirements

- Use synthetic coordinates and IDs.
- Avoid real faces, footage, customer names and row-level data.
- Label whether a value is measured, inferred or illustrative.
- Include the scenario, frame cadence and known limitations.
- Do not publish model weights, private code or credentials.


<!-- VISUAL SLOT: Add a tiny synthetic JSON/CSV sample only after the public data contract is approved. -->