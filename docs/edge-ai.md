# Edge AI and real-time processing

## Current evidence boundary

The source checkout contains dashboard artifacts that were generated from video analysis, but it does not contain enough implementation evidence to claim edge inference, GPU scheduling or real-time processing. The reports are post-event analytical products; their existence does not reveal the runtime topology.

That distinction matters in a computer-vision portfolio. Edge AI is not a visual adjective; it is a measurable deployment property involving camera ingress, compute placement, buffering, latency, resilience and privacy.

## What a validated edge story would include

```text
Camera / RTSP
    → frame sampling and back-pressure
    → detector + tracker runtime
    → local event buffer
    → secure upload or API
    → spatial aggregation
    → dashboard and alerting
```

Evidence to add before presenting this as shipped:

- device model, accelerator and memory envelope;
- supported input protocol and camera constraints;
- end-to-end latency and throughput at the target frame rate;
- behavior during network loss and process restarts;
- model update and rollback path;
- local retention and deletion policy;
- anonymization or access-control boundary;
- benchmark methodology and representative scenes.

## Portfolio slot

<!-- VISUAL SLOT: Edge AI deployment. Show an approved device/camera diagram or photo, with no private network details. -->

<!-- VISUAL SLOT: Real-time benchmark. Show latency, FPS, device utilization and accuracy trade-offs for a documented test scene. -->

## Safe wording for now


Use “video analytics reports derived from computer-vision observations” in the current portfolio. Reserve “real-time edge AI platform” for a later revision backed by deployment and benchmark evidence.