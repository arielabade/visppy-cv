# Evidence ledger

This ledger keeps portfolio claims traceable to the inspected source. File references point to the original technical repository; no original files are copied into this derivative unless explicitly listed under the portfolio assets.

| Claim | Source evidence | Classification |
| --- | --- | --- |
| The product has three dashboard views — Mandala, Loja and Palestra | `src/App.jsx` dashboard registry and raw HTML imports | Confirmed by source code |
| Reports are isolated in iframes | `src/App.jsx` `srcDoc` iframe | Confirmed by source code |
| The shell keeps session state in the browser | `src/App.jsx` `sessionStorage` flow | Confirmed by source code |
| Static delivery targets Firebase Hosting | `firebase.json` hosting block | Confirmed by configuration |
| The app uses React/Vite and Firebase web SDK packages | `package.json`, `src/main.jsx` | Confirmed by source code |
| Reports use Plotly interactive charts | Inline Plotly 3.3.1 bundle and chart calls in the HTML artifacts | Confirmed by report artifact |
| Mandala has 40,362 frames, 23 peak and 10.9 average visible people | Mandala report executive metrics | Confirmed by report artifact |
| Mandala reports 7.50 FPS and 0.133 s interval | Mandala technical audit section | Confirmed by report artifact |
| Mandala stable IDs are trajectory estimates, not unique visitors | Mandala executive and quality sections | Confirmed by report artifact |
| Loja has eight effective zones and ~150 minutes | Loja real-file adaptation section | Confirmed by report artifact |
| Loja segmentation is event-triggered | Loja scope section: 20,547 masks in 897 frames | Confirmed by report artifact |
| Loja contains 76,242 frames and 1,647,746 observations | Loja zone comparison table | Confirmed by report artifact |
| Palestra has 2h03m21s, 12.7 average and 23 peak | Palestra hero and executive metrics | Confirmed by report artifact |
| Palestra forecast error is 1.04 vs 1.41 baseline | Palestra prediction section | Confirmed by report artifact |
| The upstream detector/tracker implementation is present | No source files for it were found in the checkout | Not confirmed |
| GPU, edge, API or real-time topology | No corresponding infrastructure files were found | Not confirmed |

## Source inventory reviewed


The read-only review covered the repository root, React/Vite files, Firebase config, brand kit, screenshots, logo and all three report HTML artifacts under `src/assets` plus the two published root copies. I also visually inspected the source screenshots and the selected portfolio screenshot. Large embedded Plotly bundles and binary payloads were treated as generated/rendered material rather than duplicated into the portfolio.

## Publication classification

Each portfolio statement should use one of these labels internally:

- **Confirmed by source code** — visible in React/Vite or application files.
- **Confirmed by configuration** — visible in hosting or build configuration.
- **Confirmed by report artifact** — stated or rendered by a supplied report.
- **Confirmed by visual asset** — visible in an inspected image.
- **Inferred** — a reasonable architecture interpretation, not a proven implementation detail.
- **Portfolio recommendation** — a proposed next step, not a shipped capability.
- **Not confirmed** — no supporting evidence was found in the inspected checkout.

The source application contains a hard-coded Firebase web configuration and a client-side password hash. Neither is reproduced here. The portfolio records only the existence of those implementation patterns and the resulting security limitation.
