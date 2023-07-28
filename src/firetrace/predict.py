from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime

from src.firetrace.interface_text import additional_context

# Disable GPU
tf.config.set_visible_devices([], "GPU")

loaded_model = tf.saved_model.load("./model")


def ui_predict(max_temp_syd, max_temp_bne, year, month, day, soi):
    try:
        predictions = fire_predict(max_temp_syd, max_temp_bne, year, month, day, soi)
        additional = additional_context(predictions)
        return predictions, additional
    except Exception as e:
        return "Error", e


def fire_predict(max_temp_syd, max_temp_bne, year, month, day, soi):
    date = datetime(int(year), int(month), int(day))
    day_of_year = int(date.strftime("%j"))
    print(day_of_year)

    time_sin = np.sin((day_of_year / 365) * 2 * np.pi)
    time_cos = np.cos((day_of_year / 365) * 2 * np.pi)

    # it is IMPERATIVE THAT THESE ARE IN THE SAME ORDER AS THEY ARE WHEN TRAINING.
    data = {
        "max_t_syd": [max_temp_syd],
        "max_t_bne": [max_temp_bne],
        "time_sin": [time_sin],
        "time_cos": [time_cos],
        "soi": [soi],
        "year": [int(year)],
    }
    data_df = pd.DataFrame(data=data)

    print(data_df)

    prediction = loaded_model.serve(data_df)
    predicted_fire_area = prediction.numpy()[0][0]
    print(prediction, predicted_fire_area)
    return predicted_fire_area
