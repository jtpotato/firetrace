import gradio as gr
import keras
import pandas as pd
import numpy as np
from datetime import datetime

loaded_model = keras.models.load_model('/Users/jillxu/Downloads/model.keras')


def your_function(max_temp_syd, max_temp_bne, year, month, day):
    date = datetime(int(year), int(month), int(day))
    day_of_year = int(date.strftime('%j'))

    time_sin = np.sin((day_of_year / 365) * 2 * np.pi)
    time_cos = np.cos((day_of_year / 365) * 2 * np.pi)

    data = {
        "max_t_syd": [max_temp_syd],
        "max_t_bne": [max_temp_bne],
        "year": [year - 2000],
        "time_sin": [time_sin],
        "time_cos": [time_cos]
    }
    data_df = pd.DataFrame(data=data)

    prediction = loaded_model.predict(data_df)
    predicted_fire_area = prediction.item(0)
    return predicted_fire_area

demo = gr.Interface(
    fn = your_function,
    inputs = ["number", "number", "number", "number", "number"],
    outputs = "number"
)

demo.launch()