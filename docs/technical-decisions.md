# Technical decisions

## 1. Curated derivative instead of source mirror

The original repository remains the technical source of truth. This repository publishes the case study, selected safe visuals and architecture explanations without copying full reports, dependencies, Firebase configuration, credentials or upstream proprietary code.

## 2. Report artifacts as evidence, not implementation proof

The dashboards contain rich analytical language and rendered metrics. They are reliable evidence for what the product communicates, but not sufficient evidence for the internal detector, tracker, queue, API or deployment implementation. The documentation keeps that distinction visible.

## 3. Scenario-specific zones

Mandala, Loja and Palestra use different spatial models. The portfolio preserves that difference because forcing one universal schema would make the story less accurate and less useful.

## 4. Measurement labels are part of the product

The source reports use explicit states equivalent to “Measured”, “Inferred”, “Not measured” and “Unavailable”. The portfolio keeps the same discipline. A recommendation can be valuable while still being a hypothesis.

## 5. Static report delivery with iframe isolation

The verified app shell imports reports as raw HTML and renders them in an iframe. This is a pragmatic boundary for self-contained Plotly documents, but it increases bundle size and duplicates report assets. It should be treated as a presentation choice, not a long-term analytics platform architecture.

## Visual system

The brand kit and application source establish the following tokens:

| Role | Token | Use |
| --- | --- | --- |
| Mineral indigo | `#1A1838` | Navigation, hero surfaces, primary text on warm backgrounds |
| Signal orange | `#FF7A1A` | CTA, active state, emphasis and measured attention |
| Deep amber | `#D95F00` | Secondary accent and labels |
| Warm ivory | `#F7F1E8` | Page background |
| Warm graphite | `#181615` | Body text |
| Mineral green | `#4E8F7A` | Supporting / positive state |
| Dust gray | `#9C9890` | Muted text and secondary metadata |

Typography uses DM Sans for the wordmark/body and Space Grotesk for labels, section markers and UI accents. The portfolio uses the same warm, technical, restrained direction and keeps visual density under control so diagrams and evidence remain primary.

Accessibility and future UI work should preserve visible focus states, non-color labels for measured/inferred states, keyboard access to interactive charts and reduced-motion behavior.

## 6. No invented screenshots


Where the correct asset is missing, the portfolio uses a written slot rather than stock imagery or an AI-generated approximation. A real detection/tracking frame is more valuable than decorative computer-vision art.
