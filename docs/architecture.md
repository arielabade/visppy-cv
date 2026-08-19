# High-level product architecture

Visppy follows a simple client-facing journey: observe a physical space, organize what happened by region and time, and turn the pattern into an operational decision.

```mermaid
flowchart LR
    SPACE[Physical space] --> OBS[Observed movement]
    OBS --> MAP[Zones and journeys]
    MAP --> SIGNALS[Occupancy, dwell, flow, and timing]
    SIGNALS --> DECISIONS[Recommendations and experiments]
```

## Reliability by design

The product is most useful when every insight carries its context and limits.

```mermaid
flowchart LR
    INPUT[Camera and space context] --> CHECK[Context and quality check]
    CHECK --> MEASURE[Movement measurements]
    MEASURE --> REVIEW[Interpretation and review]
    REVIEW --> OUTPUT[Client decision]
    CHECK -. incomplete context .-> LIMIT[Explain the limitation]
    LIMIT --> OUTPUT
```

The public portfolio does not disclose private implementation rules, calibration, thresholds, credentials, customer-specific logic, or infrastructure details. It shows what the client can understand and act on.
