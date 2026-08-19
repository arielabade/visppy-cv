# Visual-slot index

These are intentional publication slots, not fabricated evidence. Replace a slot only with an approved Visppy asset and keep the caption explicit about whether the image is measured, inferred, illustrative or unavailable.

| Slot | Technical concept | Preferred asset | Suggested size | Narrative location | Required review |
| --- | --- | --- | --- | --- | --- |
| Product hero | Product context and dashboard outcome | PNG or SVG screenshot | 16:9, 1600×900 or larger | README opening | Remove names, URLs, identifiers and unapproved metrics |
| YOLO detection example | Person/object observations and confidence | PNG or short GIF | 16:9, 1280×720 | Computer-vision pipeline | No faces, plates or private footage; label confidence as observation |
| Object-tracking sequence | Association across frames | 3–5 PNG frames or MP4 | 16:9 | Computer-vision pipeline | Use synthetic or approved track IDs; show occlusion caveats |
| Persistent track IDs | Relinking and continuity | Annotated frame sequence | 16:9 | Computer-vision pipeline | Never imply identity or unique visitors |
| Trajectory visualization | Image-space paths and re-entry | PNG or SVG | 4:3 or 16:9 | Spatial analytics | State that paths are estimated and not metric-world routes |
| Spatial zones | Polygon assignment | PNG or SVG overlay | 4:3 or 16:9 | Spatial analytics | Remove venue labels and private camera geometry |
| Heatmap | Concentration versus operational context | PNG or SVG | 4:3 or 16:9 | Spatial analytics | Explain that a hotspot is not automatically interest or conversion |
| Occupancy chart | Simultaneous visible occupancy | PNG or SVG chart | 16:9 | Video analytics | Include camera coverage and time window |
| Flow analytics | Transitions and gateways | PNG or SVG matrix/flow chart | 16:9 | Spatial or video analytics | Do not call internal lines entrances or exits without evidence |
| Dashboard walkthrough | Question → evidence → decision | MP4, GIF or paired PNGs | 16:9 | README and case study | Review every visible label and metric |
| Architecture diagram | Product data and delivery path | Mermaid or SVG | Wide landscape | Architecture | Mark inferred or unavailable implementation layers |
| Edge/GPU infrastructure | Compute placement and runtime | SVG, PNG or Mermaid | 16:9 | Edge AI and infrastructure | Publish device, latency and throughput only when measured and approved |
| Deployment environment | Camera/edge installation context | PNG or JPEG | 4:3 or 16:9 | Edge AI and infrastructure | Remove IPs, credentials, venue and customer context |
| Benchmark chart | Accuracy/latency/compute trade-off | PNG/SVG plus data table | 16:9 | Edge AI | Include scene, sample size, device and methodology |
| Real-world event setup | Physical operating context | Approved photo or diagram | 4:3 or 16:9 | Product case study | Clear people, signage, venue and commercial details |

Existing placeholder briefs:

- [Computer Vision demo](computer-vision-demo.md)
- [Object tracking](object-tracking.md)
- [Spatial analytics](spatial-analytics.md)
- [Dashboard walkthrough](dashboard.md)
- [Architecture](architecture.md)
- [Edge/GPU infrastructure](edge-infrastructure.md)
- [Deployment](deployment.md)
- [Benchmark](benchmark.md)
