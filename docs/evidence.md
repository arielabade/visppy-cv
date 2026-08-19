# Evidence ledger

This ledger keeps portfolio claims traceable to the inspected source. File references point to the original technical repository; no original files are copied into this derivative unless explicitly listed under the portfolio assets.

| Claim | Source evidence | Classification |
| --- | --- | --- |
| The product has three dashboard views | `src/App.jsx` dashboard registry and raw HTML imports | Confirmed by source code |
| Reports are isolated in iframes | `src/App.jsx` `srcDoc` iframe | Confirmed by source code |
| Static delivery targets Firebase Hosting | `firebase.json` hosting block | Confirmed by configuration |
| Reports use Plotly interactive charts | Inline Plotly 3.3.1 bundle and chart calls in the HTML artifacts | Confirmed by report artifact |
| Mandala has 40,362 frames, 23 peak and 10.9 average visible people | Mandala report executive metrics | Confirmed by report artifact |
| Mandala reports 7.50 FPS and 0.133 s interval | Mandala technical audit section | Confirmed by report artifact |
| Mandala stable IDs are trajectory estimates, not unique visitors | Mandala executive and quality sections | Confirmed by report artifact |
| Loja has eight effective zones and ~150 minutes | Loja “Adaptação ao arquivo real” section | Confirmed by report artifact |
| Loja segmentation is event-triggered | Loja scope section: 20,547 masks in 897 frames | Confirmed by report artifact |
| Palestra has 2h03m21s, 12.7 average and 23 peak | Palestra hero and executive metrics | Confirmed by report artifact |
| Palestra forecast error is 1.04 vs 1.41 baseline | Palestra prediction section | Confirmed by report artifact |
| The upstream detector/tracker implementation is present | No source files for it were found in the checkout | Not confirmed |
| GPU, edge, API or real-time topology | No corresponding infrastructure files were found | Not confirmed |

## Source inventory reviewed


The read-only review covered the repository root, React/Vite files, Firebase config, brand kit, screenshots, logo and all three report HTML artifacts under `src/assets` plus the two published root copies. Large embedded Plotly bundles and binary payloads were treated as generated/rendered material rather than duplicated into the portfolio.