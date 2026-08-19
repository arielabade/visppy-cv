# Privacy, security and publication rules

## Materials intentionally excluded

This derivative does not copy:

- Firebase configuration, API keys or authentication details;
- environment files, secrets, private endpoints or network addresses;
- camera credentials or RTSP URLs;
- source Parquet files or row-level observations;
- customer video, identifiable people or private footage;
- full HTML reports with embedded data and Plotly bundles;
- model weights, proprietary inference code or private commercial rules.

The source checkout also contains client-side Firebase configuration and a client-side password hash. Even when a web configuration value is technically visible to browsers, it is not needed for this case study and is excluded from the public derivative. The portfolio does not reproduce the password flow or any credential-like value.

## Safe visual policy

The current portfolio includes one existing dashboard screenshot and the brand logo because they contain no visible faces, camera credentials or private endpoint information in the inspected files. Any future screenshot should be reviewed for:

1. faces, names, badges, license plates or other identifiers;
2. customer, event or venue names;
3. URLs, tokens, project IDs or internal filenames;
4. row-level metrics that were not approved for publication;
5. camera placement details that create a security concern.

## Analytics claims

The reports themselves model uncertainty. The portfolio therefore avoids presenting the following as proven capabilities:

- unique visitor counting;
- identity or re-identification of real people;
- gaze, emotion, age or gender estimation;
- confirmed screen or product interaction;
- entry/exit counting from an internal line;
- conversion, sales or ROI attribution without explicit business signals;
- metric-world speed without homography;
- real-time or edge processing without deployment evidence.

## Public repository hygiene


The `.gitignore` blocks environment files, keys, certificates, logs, build outputs and private directories. New assets should be added only after a human privacy and intellectual-property review.
