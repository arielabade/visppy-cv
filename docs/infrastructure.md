# Infrastructure and delivery

## What is verified

The inspected checkout verifies a small static delivery layer:

- React 19 and React DOM provide the application shell.
- Vite builds the client bundle.
- The shell imports three raw HTML reports and renders the selected one in an iframe.
- Plotly is embedded inside the report artifacts for interactive charts.
- Firebase Hosting targets `dist` and rewrites routes to `index.html`.
- The UI exposes a client-side session state and dashboard selector.

This is enough to explain how a report is presented to a reviewer. It is not enough to explain where inference runs.

## What is not verified

No Dockerfile, Kubernetes manifest, cloud worker, message queue, GPU provisioning, model registry, API server, RTSP credential flow, edge device specification or monitoring stack is present in the inspected repository. The portfolio does not convert the product brief into a false infrastructure claim.

| Question | Current status | Required evidence before publishing a claim |
| --- | --- | --- |
| Where does YOLO inference run? | Unknown from checkout | Runtime diagram, deployment manifest or approved architecture record |
| Is processing real-time? | Not proven; reports are post-event artifacts | End-to-end latency and stream-processing evidence |
| Is there edge hardware? | Not proven | Device model, topology and deployment photo/diagram |
| Is there GPU acceleration? | Not proven | Runtime configuration, benchmark or infrastructure record |
| How do APIs deliver metrics? | Not present | API contract, endpoint diagram and auth model |
| How are datasets stored? | Reports reference Parquet | Approved storage and retention architecture |

## Portfolio architecture slot

The current diagram intentionally ends at the verified static reporting layer and labels upstream compute as an inference boundary. That keeps the portfolio technically credible while reserving space for approved infrastructure evidence.

<!-- VISUAL SLOT: Edge/GPU architecture. Show camera → edge or GPU worker → storage/API → dashboard, with device names and latency only if approved. -->


<!-- VISUAL SLOT: Deployment environment. Add a photo or diagram of an approved edge device, camera placement or GPU host. Do not add IPs, credentials or customer identifiers. -->