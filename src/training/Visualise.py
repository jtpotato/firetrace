import pandas as pd
import joblib
import torch
import matplotlib.pyplot as plt


df = pd.read_csv("data/gen_2/processed/with_fire_area_soi_weather_time.csv")

# Pick last x rows
df = df.tail(1000)

y = df["fire_area"]
y = y.reset_index()["fire_area"]
X = df.drop("fire_area", axis=1)

# Scale stuff
x_scaler = joblib.load("models/x_scaler.save")
y_scaler = joblib.load("models/y_scaler.save")

x_scaled = x_scaler.transform(X)

def generate_visualisation(compiled_model, epoch):
  test_output = compiled_model(torch.tensor(x_scaled, dtype=torch.float32))
  y_unscaled = y_scaler.inverse_transform(test_output.detach().numpy())

  # Make a plot
  plt.plot(y, label="Actual")
  plt.plot(y_unscaled, label="Predicted")
  plt.legend()
  plt.title("Actual vs Predicted Fire Area")
  plt.xlabel("Day")
  plt.ylabel("Fire Area (sqkm)")

  plt.savefig(f"training_visualisations/{epoch}_vis.jpg")

  plt.clf()

def graph_loss(history):
  plt.plot(history[0], label="Train Loss")
  plt.plot(history[1], label="Val Loss")
  plt.legend()
  plt.title("Train vs Val Loss")
  plt.xlabel("Epoch Unit")
  plt.ylabel("Loss")

  if len(history[2]) > 0:
    for epoch in history[2]:
      plt.axvline(epoch, color="r", linestyle="--", lw=0.5)

  plt.savefig(f"training_visualisations/loss.jpg")

  plt.clf()