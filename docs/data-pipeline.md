# Data pipeline

## Evidence model

The report artifacts refer to a Parquet-oriented analytical dataset. The source checkout contains no Parquet files or extraction jobs, so this page documents the evidence model without publishing data or claiming an exact schema.

```mermaid
flowchart LR
    RAW[Source observations<br/>frames, people, objects]
    CONTEXT[Frame and environment context]
    TRACK[Tracking and relinking events]
    ZONES[Zone transitions and spatial metrics]
    DERIVED[Behavioral aggregates<br/>dwell, friction, funnel proxies]
    REPORT[Report-ready tables and charts]

    RAW --> TRACK
    CONTEXT --> ZONES
    TRACK --> ZONES
    ZONES --> DERIVED
    DERIVED --> REPORT
```

The report inventory names files such as `person_observations.parquet`, `object_detections.parquet`, `raw_yolo_detections.parquet`, `zone_transitions.parquet`, `line_crossings.parquet`, `interactions.parquet`, `environment_context.parquet` and `frame_context.parquet`. These names are evidence of the report’s analytical vocabulary, not files included in this public portfolio.

## Derived layers

| Layer | Example output | Safe portfolio statement |
| --- | --- | --- |
| Observation | person or object detection per frame | Model observations can be aggregated by time and location |
| Context | frame cadence, environment and event metadata | Metrics need recording context to be interpreted correctly |
| Tracking | raw IDs, stable IDs, relink events | Trajectories require continuity and uncertainty labels |
| Spatial | zone assignment, occupancy, transitions | Polygons turn image coordinates into operational regions |
| Behavioral proxy | dwell, friction, staff/fixed heuristic, funnel stages | Proxies prioritize experiments; they do not prove intent or conversion |
| Product output | chart, table, recommendation and caveat | The dashboard combines evidence with a decision narrative |

## Data quality and missing inputs

The reports explicitly note missing summary, timeline, persistence-diagnostic and consolidated-inventory files in at least one scenario. They recalculate available indicators from the supplied Parquet material and document the limitation. That is a useful engineering behavior: a report can remain useful while making the missing evidence visible.

## Public example policy


No real row-level data is copied here. A safe example should use synthetic values and preserve only the conceptual fields needed to explain the pipeline. See [safe-public-examples](../examples/safe-public-examples/README.md).