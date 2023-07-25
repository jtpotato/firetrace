---
title: "Firetrace"
emoji: "🔥"
colorFrom: "yellow"
colorTo: "gray"
sdk: "gradio"
python_version: "3.11"
sdk_version: "3.36.1"
app_file: src/main.py
pinned: true
fullWidth: true
---
<img src="./assets/banner.svg" alt="Firetrace Logo" />

# About
Firetrace is an AI model and web interface that predicts the severity of bushfire events at a nationwide scale, by using projected weather data. It uses a deep neural network trained on data from BOM weather observatories around the country, NASA’s MODIS satellite and the Southern Oscillation Index as well as time information to represent seasonality and climate change trends.

Launching: 3/08/2023

![A diagram of the shape of the model.](./assets/Schematic.jpg)
A diagram of the shape of the model.
- 8 input nodes
- 7 hidden layers, 32 nodes each
- 1 output node

# Roadmap
- [x] Gradio UI
- [x] Web API
- [x] Take Southern Oscillation Index into consideration
- [ ] Take CO2 levels into consideration
- [ ] Take last year's rainfall into consideration (affects vegetation)

# Development
We recommend running the following commands to get started:
```bash
pip install tensorflow # pip3 install tensorflow
pip install gradio # pip3 install gradio

# mac users
pip3 install tensorflow-metal
```