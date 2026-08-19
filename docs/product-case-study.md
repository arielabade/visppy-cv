# Product case study

## Problem

Teams operating a stand, store, lecture room or other physical space can observe movement, congestion and dwell qualitatively, but they struggle to compare those signals across zones and event phases. A heatmap alone cannot tell whether a hotspot is a corridor, a fixed structure, a staff cluster or a meaningful interaction.

## Product response

Visppy packages computer-vision observations into a spatial decision layer:

1. detect visible people and objects;
2. maintain estimated trajectories with explicit continuity caveats;
3. assign observations to scenario-specific polygons;
4. aggregate occupancy, dwell, heat, transitions and temporal peaks;
5. present measured, inferred and unavailable signals side by side;
6. turn the evidence into operational experiments.

The last three steps are strongly represented in the supplied reports and dashboard screenshot. The first two are represented by report metrics rather than source implementation in this checkout.

## Three decision stories

### 1. Convert circulation into qualified dwell

The Mandala report observes high pressure on the right and treats the transition toward the central screen as the commercial opportunity. The recommended action is to test a CTA and attendant at the right–center boundary without blocking the corridor.

### 2. Separate external flow from in-store retention

The Loja report refuses to collapse eight effective zones into a generic left/center/right narrative. It distinguishes external flow, gateways, retention areas and fixed structures, then prioritizes entry measurement and qualified permanence before claiming commercial conversion.

### 3. Measure the room before interpreting the audience

The Palestra report treats a stationary audience as expected. It recommends camera and polygon changes, real participation signals and a separate lecture mode before using behavioral labels designed for stores or stands.

## Impact language

The current evidence supports operational impact claims such as:

- identifying pressure windows;
- locating likely circulation bottlenecks;
- comparing zone occupancy and dwell proxies;
- prioritizing camera, layout and staffing experiments;
- creating a measurement roadmap toward leads, sales or participation.

It does not support claims of unique visitors, gaze, emotion, demographics, proven attention, conversion, revenue attribution or ROI from video alone.

## Product metrics to mature next

| Product question | Current proxy | Next instrument |
| --- | --- | --- |
| Did someone enter? | Zone transitions and visible occupancy | Valid entrance line or check-in |
| Did someone engage? | Dwell and heuristic approach | Human validation, QR, interaction event |
| Did the activation convert? | None in current reports | CRM, POS, lead or order timestamp |
| Did the model improve? | Confidence, quality and fragmentation | Labeled benchmark set and recurring evaluation |
