import random
import pandas as pd
import plotly.express as px

heatmap_df = pd.read_csv("data/gen_2/processed/fire_coordinate_weights.csv")


def generate_map(fire_size):
    new_df = heatmap_df.copy(deep=True)

    samples = min(int(fire_size * 5), len(new_df))
    print(samples)

    new_df = new_df.sample(samples)
    new_df = new_df.sort_values(by=["count"], ascending=False)
    new_df = new_df.head(int(fire_size))
    new_df["visible"] = 1

    fig = px.density_mapbox(
        new_df,
        lat="latitude",
        lon="longitude",
        z="visible",
        radius=8,
        center=dict(lat=-24, lon=133),
        zoom=2,
        mapbox_style="open-street-map",
    )

    return fig
