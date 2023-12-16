import random
import pandas as pd
import plotly.express as px

heatmap_df = pd.read_csv("data/gen_2/processed/fire_coordinate_weights.csv", dtype={"month": str})


def generate_map(fire_size, month: str):
    new_df = heatmap_df.copy(deep=True)
    # print("Month: ", month)

    month_df = new_df[new_df["month"] == month]

    # print(month_df)

    samples = min(int(fire_size * 5), len(month_df))
    # print(samples)

    month_df = month_df.sample(samples)
    month_df = month_df.sort_values(by=["count"], ascending=False)
    month_df = month_df.head(int(fire_size))
    month_df["visible"] = 1

    fig = px.density_mapbox(
        month_df,
        lat="latitude",
        lon="longitude",
        z="visible",
        radius=8,
        center=dict(lat=-24, lon=133),
        zoom=2,
        mapbox_style="open-street-map",
    )

    return fig
