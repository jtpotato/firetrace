import random
import pandas as pd
import plotly.graph_objects as go

heatmap_df = pd.read_csv(
    "data/gen_2/processed/fire_coordinate_weights.csv", dtype={"month": str}
)


def generate_map(fire_size, month: str):
    new_df = heatmap_df.copy(deep=True)
    # print("Month: ", month)

    month_df = new_df[new_df["month"] == month]

    # print(month_df)

    samples = min(int(fire_size * 3), len(month_df))
    # print(samples)

    month_df = month_df.sample(samples)
    month_df = month_df.sort_values(by=["count"], ascending=False)
    month_df = month_df.head(int(fire_size / 2))
    month_df["visible"] = 1

    fig = go.Figure(
        go.Densitymapbox(
            lat=month_df.latitude,
            lon=month_df.longitude,
            z=month_df.visible,
            radius=2,
            showscale=False,
        )
    )

    fig.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox_center_lon=133,
        mapbox_center_lat=-25,
        mapbox_zoom=2.5,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig
