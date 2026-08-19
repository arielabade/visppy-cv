# Visppy — Computer Vision & Spatial Intelligence

> Technical portfolio case study for a computer-vision product that turns video of physical spaces into operational and spatial signals.

![Visppy executive dashboard](assets/screenshots/dashboard-executive.png)

<!-- VISUAL SLOT: Replace or complement the hero screenshot with an approved product capture that contains no customer-identifying data. -->

## The short version

Visppy is presented here as a system for understanding how people and objects occupy, move through, and interact with physical spaces. The technical evidence available in the source repository is concentrated in three interactive HTML reports: a branded-event stand, a store-and-surroundings analysis, and a lecture-room analysis.

The portfolio focuses on the engineering story behind those reports:

```text
Video / camera context
        ↓
Computer-vision observations
        ↓
Tracking, relinking and spatial zones
        ↓
Occupancy, heatmaps, flows and temporal signals
        ↓
Operational recommendations and dashboards
```

The upstream detector and tracker implementation is not present in the inspected checkout. Therefore, this repository distinguishes what is directly evidenced by code or report artifacts from what is an architectural inference.

## What the portfolio demonstrates

| Capability | Portfolio treatment | Evidence status |
| --- | --- | --- |
| Object detection and YOLO-derived measures | Confidence, object classes and detection caveats | Confirmed by report artifacts |
| Object tracking and relinking | Stable-ID trajectories, fragmentation and dwell time | Confirmed by report artifacts |
| Spatial analytics | Polygons, heatmaps, occupancy by zone and transitions | Confirmed by report artifacts |
| Video analytics | Sampling, temporal windows, hotspots and forecasting | Confirmed by report artifacts |
| Dashboard delivery | React/Vite shell, embedded HTML reports and Plotly | Confirmed by source code |
| Firebase hosting | Static hosting and SPA rewrite | Confirmed by configuration |
| GPU, edge and real-time inference | Design considerations and open questions | Not confirmed in this checkout |

## Case studies at a glance

### Mandala — commercial intelligence in a physical stand

The report frames the right side as a circulation-heavy area, the center as a transition toward the screen, and the left side as a more consultative area. It explicitly separates measured signals from inference and unavailable signals.

Selected report values: 40,362 processed frames, 23 simultaneous visible people at peak, 10.9 visible people per frame on average, 7.50 analyzed frames per second, and 1,828 estimated stable IDs from 6,123 raw IDs. These are trajectory estimates, not unique visitors.

### Loja — spatial analytics across eight effective zones

The store report adapts the narrative to the actual dataset instead of forcing a three-zone model. It distinguishes external flow, gateways, retention areas and physical structures across eight effective zones and documents the limits of the measurement.

Selected report values: 76,242 frames, approximately 150 minutes of coverage, 20,547 event-triggered segmentation masks across 897 frames, and a zone table covering occupancy, peaks, trajectories, dwell time and heuristic staff presence.

### Palestra — occupancy and circulation in a lecture room

The lecture report treats a mostly stationary audience as expected behavior rather than noise. It uses spatial distribution, camera framing, circulation and a limited next-minute occupancy forecast, while stating that participation, attention and conversion require explicit signals such as QR or check-in.

Selected report values: 2h03m21s analyzed, 12.7 visible people per frame on average, 23 at peak, 40.4% of observed occupancy on the left, and a one-test forecast comparison with mean error 1.04 versus 1.41 for a simple baseline.

## Explore the engineering story

1. [Architecture](docs/architecture.md) — evidence-based system map and scope boundaries.
2. [Computer-vision pipeline](docs/computer-vision-pipeline.md) — detection, tracking and what the reports can safely claim.
3. [Spatial analytics](docs/spatial-analytics.md) — zones, heatmaps, occupancy, transitions and dwell time.
4. [Video analytics](docs/video-analytics.md) — sampling, temporal windows, hotspots and forecasting.
5. [Data pipeline](docs/data-pipeline.md) — Parquet-oriented evidence model and derived analytical layers.
6. [Infrastructure](docs/infrastructure.md) — the verified React/Vite/Firebase delivery layer.
7. [Edge AI](docs/edge-ai.md) — what would need to be validated for edge or real-time deployment.
8. [Product case study](docs/product-case-study.md) — problem, product, decisions and impact.
9. [Technical decisions](docs/technical-decisions.md) — trade-offs and explicit limitations.
10. [Privacy and publication rules](docs/privacy.md) — what is intentionally excluded from this derivative.
11. [Evidence ledger](docs/evidence.md) — provenance and confidence labels.

## Visual system and asset plan

The portfolio preserves the evidence-backed Visppy visual language: warm ivory surfaces, mineral indigo, signal orange, deep amber, mineral green, DM Sans for body text and Space Grotesk for labels and UI accents. See [the visual system notes](docs/technical-decisions.md#visual-system).

Real material currently included:

- [Executive dashboard screenshot](assets/screenshots/dashboard-executive.png)
- [Visppy logo](assets/brand/visppy-logo.png)
- [Pipeline diagram](assets/architecture/visppy-pipeline.mmd)

Intentional missing-material slots are documented in the [visual-slot index](assets/placeholders/README.md). Each slot states the technical concept, preferred format, suggested dimensions and privacy review required before publication.

The [safe public example](examples/safe-public-examples/observation-contract.json) is synthetic. It demonstrates the shape of an observation record without exposing source rows, footage, model weights or proprietary code.

## Scope and disclosure

This is a curated portfolio derivative, not a mirror of the technical source repository and not a runnable copy of the private application. It does not include credentials, Firebase configuration, customer footage, source Parquet files, full HTML reports, embedded Plotly bundles, private endpoints or proprietary upstream inference code.

Claims are labeled as:

- **Confirmed by source code** — visible in the React/Vite or hosting files.
- **Confirmed by report artifact** — stated or rendered by the supplied reports.
- **Confirmed by visual asset** — visible in the supplied screenshot or logo.
- **Inferred** — a reasonable architecture interpretation, not a proven implementation detail.
- **Portfolio recommendation** — a proposed next step, not a shipped capability.

The source application contains client-side Firebase configuration and a client-side password hash. Neither is reproduced here.

## Status


Portfolio case study enriched from the current source evidence. The visual case study remains intentionally incomplete until approved Computer Vision frames, tracking examples, infrastructure visuals and deployment material are available.
