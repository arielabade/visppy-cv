# Architecture

## Executive view

The portfolio architecture has two distinct layers:

1. An analytical layer represented by the report artifacts: observations, tracks, spatial polygons, temporal aggregations and recommendations.
2. A verified delivery layer implemented in the checkout: a React/Vite shell that loads raw HTML reports into an iframe and is configured for Firebase Hosting.

```mermaid
flowchart LR
    CAM[Camera / recorded video]
    CV[Computer-vision observations]
    TRACK[Tracking + relinking]
    SPACE[Zones + heatmaps]
    VIDEO[Temporal analytics]
    REPORT[Plotly HTML reports]
    APP[React/Vite shell]
    HOST[Firebase Hosting]

    CAM --> CV --> TRACK
    TRACK --> SPACE --> REPORT
    TRACK --> VIDEO --> REPORT
    REPORT --> APP --> HOST
```

The editable Mermaid source is available at [`assets/architecture/visppy-pipeline.mmd`](../assets/architecture/visppy-pipeline.mmd).
The reliability-oriented source is available at [`assets/architecture/reliability-flow.mmd`](../assets/architecture/reliability-flow.mmd).

## Public analytical flow

The following flow translates the supplied portfolio proposal into a safe, implementation-agnostic architecture. It is deliberately specific about data boundaries and deliberately non-specific about proprietary model configuration.

```mermaid
flowchart TD
    VIDEO[Video input] --> PROCESS[Video processing<br/>frame extraction and preprocessing]
    PROCESS --> DETECT[Object detection<br/>people and objects]
    DETECT --> TRACK[Object tracking<br/>temporary IDs, trajectories, movement history]
    TRACK --> SPACE[Spatial mapping<br/>zones, ROIs, entry and exit areas]
    SPACE --> EVENTS[Event generation<br/>zone enter, zone exit, dwell, crossing, occupancy]
    EVENTS --> SCHEMA[Analytics event contract<br/>timestamp, camera, track, coordinates, zone, event type]
    SCHEMA --> STORAGE[Data pipeline<br/>Python / Polars, Parquet, SQL / DuckDB]
    STORAGE --> DERIVED[Derived analytics<br/>flows, heatmaps, occupancy, density, dwell]
    DERIVED --> REPORT[Dashboard and operational KPIs]
```

This is a portfolio-level reconstruction of the analytical story. The current checkout verifies the report and delivery layers, but it does not contain the upstream jobs, weights, stream consumers, APIs, or orchestration that would implement every arrow.

## Reliability-oriented flows

Reliability is treated as a chain of explicit checks rather than as a property of the detector alone.

```mermaid
flowchart LR
    INPUT[Input and camera context] --> CONTRACT[Schema and metadata validation]
    CONTRACT --> DETECTION[Detection observations]
    DETECTION --> TRACKING[Tracking and relinking]
    TRACKING --> SPATIAL[Zone assignment and geometry checks]
    SPATIAL --> EVENTS[Event contract validation]
    EVENTS --> STORAGE[Partitioned analytical storage]
    STORAGE --> QC[Quality checks<br/>coverage, confidence, continuity, missingness]
    QC --> PUBLISH[Publish aggregate metrics]
    QC --> REVIEW[Flag for review or quarantine]
    REVIEW -.-> PUBLISH
```

Recommended reliability controls include:

- validate camera, timestamp, frame-rate, and coordinate metadata before aggregation;
- keep raw observations separate from derived events and executive metrics;
- carry confidence, continuity, and missingness fields into downstream aggregates;
- quarantine impossible coordinates, duplicate events, broken timestamps, and invalid zone assignments;
- compare flow, dwell, and occupancy metrics only when the camera and sampling context are comparable;
- attach provenance and caveats to every published chart or KPI.

The controls above are portfolio recommendations unless explicitly marked as confirmed elsewhere in the evidence ledger.

## Evidence map

| Layer | What is directly visible | Confidence |
| --- | --- | --- |
| Delivery shell | React components, dashboard registry, login/session state, iframe rendering | Confirmed by source code |
| Build and hosting | Vite build, Firebase Hosting target `dist`, SPA rewrite to `index.html` | Confirmed by source/configuration |
| Report rendering | Plotly 3.3.1 embedded inside the HTML reports | Confirmed by report artifacts |
| Detection layer | YOLO confidence, object classes, people observations and frame-level language | Confirmed by report artifacts |
| Tracking layer | Raw/stable ID counts, relinking, dwell and trajectory language | Confirmed by report artifacts |
| Spatial layer | Heatmaps, effective polygons, zone occupancy and transition matrices | Confirmed by report artifacts |
| Upstream compute | Exact model runtime, GPU, edge device, queue, API or orchestration | Not present in checkout |

## Delivery shell

The React app keeps the reports as raw HTML imports and selects among three dashboards: Mandala, Loja and Palestra. Each report runs inside an iframe, which isolates its CSS and native script behavior from the shell. The build is a static Vite output and the Firebase configuration supplies a catch-all rewrite for client-side delivery.

This is a presentation architecture. It should not be read as proof that inference occurs in the browser or on Firebase Hosting.

## Upstream analytical inference boundary

The reports refer to Parquet-derived metrics, YOLO detections, tracking/relinking, segmentation triggers and forecasting. The source checkout does not contain the Python jobs, model weights, stream consumers, APIs or infrastructure definitions that produced those artifacts. The arrows from video to observations and from observations to tracking in the diagram are therefore a portfolio-level reconstruction of the analytical story, not a claim about the exact production implementation.

## Security boundary


The source app contains a client-side login flow and a Firebase web configuration. Those details are intentionally not copied into this public derivative. A client-side password hash is not a substitute for production authentication; the portfolio describes the UI shell without publishing credentials or reproducing the access mechanism.
