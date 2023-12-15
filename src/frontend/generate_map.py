import random
import pandas as pd
import plotly.express as px

heatmap_df = pd.read_csv("../data/gen_2/processed/fire_coordinate_weights.csv")


def generate_map(fire_size):
    new_df = heatmap_df.sample(fire_size * 5)
    new_df = new_df.sort_values(by=["count"], ascending=False)
    new_df["visible"] = 1

    fig = px.density_mapbox(
        heatmap_df,
        lat="latitude",
        lon="longitude",
        z="visible",
        radius=8,
        center=dict(lat=-20, lon=140),
        zoom=4,
        mapbox_style="open-street-map",
    )

    return fig
