from tensorflow import keras
import pandas as pd
import numpy as np
from datetime import datetime

loaded_model = keras.models.load_model("model/model.h5")


def ui_predict(max_temp_syd, max_temp_bne, year, month, day):
    try: 
        predictions = fire_predict(max_temp_syd, max_temp_bne, year, month, day)
        additional = additional_context(predictions)
        return predictions, additional
    except Exception as e:
        return "Error", e


def fire_predict(max_temp_syd, max_temp_bne, year, month, day):
    date = datetime(int(year), int(month), int(day))
    day_of_year = int(date.strftime("%j"))

    time_sin = np.sin((day_of_year / 365) * 2 * np.pi)
    time_cos = np.cos((day_of_year / 365) * 2 * np.pi)

    data = {
        "max_t_syd": [max_temp_syd],
        "max_t_bne": [max_temp_bne],
        "year": [year - 2000],
        "time_sin": [time_sin],
        "time_cos": [time_cos],
    }
    data_df = pd.DataFrame(data=data)

    prediction = loaded_model.predict(data_df)
    predicted_fire_area = prediction.item(0)
    return predicted_fire_area


def additional_context(scan_area):
    LARGEST_EVENT = 5854.7

    percentage = round((scan_area / LARGEST_EVENT) * 100, 2)
    return f"""The scanned area of your fires was {round(scan_area, 2)} square kilometres. This is {percentage}% of the largest fire event in our database, at {round(LARGEST_EVENT, 2)} square kilometres, recorded on the 19th of September 2011."""
