from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime

# Disable GPU
tf.config.set_visible_devices([], "GPU")

loaded_model = keras.models.load_model("model/model.h5")


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

    prediction = loaded_model.predict(data_df)
    predicted_fire_area = prediction.item(0)
    print(prediction, predicted_fire_area)
    return predicted_fire_area


def additional_context(scan_area):
    LARGEST_EVENT = 5854.7
    AUSTRALIA_AREA = 7.688 * 10**6

    percentage_largest = round((scan_area / LARGEST_EVENT) * 100, 2)
    percentage_australia = round((scan_area / AUSTRALIA_AREA) * 100, 2)

    return f"""The predicted area of your fires 🤓 was `{round(scan_area, 2)}` square kilometres. 🤯 This is `{percentage_largest}%` of the largest fire event 🔥 in our database, at {round(LARGEST_EVENT, 2)} square kilometres, recorded on the 19th of September 2011. This is also `{percentage_australia}%` of Australia's land size. 😧"""
