---
title: "Firetrace"
emoji: "🔥"
colorFrom: "yellow"
colorTo: "gray"
sdk: "gradio"
python_version: "3.11"
sdk_version: "3.40.1"
app_file: "app.py"
pinned: true
fullWidth: true
---
<img src="./assets/banner.svg" alt="Firetrace Logo" />

# About
Firetrace is an AI model and web interface that predicts the severity of bushfire events at a nationwide scale, by using projected weather data. It uses a deep neural network trained on data from BOM weather observatories around the country, NASA’s MODIS satellite and the Southern Oscillation Index as well as time information to represent seasonality and climate change trends.

Read the [Report](./Firetrace%20-%20Paper.pdf)

# Roadmap
- [x] Gradio UI
- [x] Web API
- [x] Take Southern Oscillation Index into consideration
- [ ] Take CO2 levels into consideration
- [ ] Take last year's rainfall into consideration (affects vegetation)