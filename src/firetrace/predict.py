from tensorflow import keras
import pandas as pd
import numpy as np
from datetime import datetime

loaded_model = keras.models.load_model("model/model.h5")


def ui_predict(independent_var, max_temp_syd, max_temp_bne, year, month, day, soi):
    try: 
        predictions = fire_predict(max_temp_syd, max_temp_bne, year, month, day, soi)
        additional = additional_context(predictions)
        graph = generate_graph(independent_var, max_temp_syd, max_temp_bne, year, month, day, soi)
        return predictions, additional, graph
    except Exception as e:
        return "Error", e


def fire_predict(max_temp_syd, max_temp_bne, year, month, day, soi):
    date = datetime(int(year), int(month), int(day))
    day_of_year = int(date.strftime("%j"))

    time_sin = np.sin((day_of_year / 365) * 2 * np.pi)
    time_cos = np.cos((day_of_year / 365) * 2 * np.pi)

    data = {
        "max_t_syd": [max_temp_syd],
        "max_t_bne": [max_temp_bne],
        "year": [year],
        "time_sin": [time_sin],
        "time_cos": [time_cos],
        "soi": [soi],
    }
    data_df = pd.DataFrame(data=data)

    prediction = loaded_model.predict(data_df)
    predicted_fire_area = prediction.item(0)
    return predicted_fire_area


def additional_context(scan_area):
    LARGEST_EVENT = 5854.7

    percentage = round((scan_area / LARGEST_EVENT) * 100, 2)
    return f"""The scanned area of your fires was {round(scan_area, 2)} square kilometres. This is {percentage}% of the largest fire event in our database, at {round(LARGEST_EVENT, 2)} square kilometres, recorded on the 19th of September 2011."""

def generate_graph(independent_var, max_temp_syd, max_temp_bne, year, month, day, soi):
    data = {}

    if independent_var == "Max temperature in Sydney":
        temps = np.linspace(max_temp_syd - 30, max_temp_syd + 30, 20)
        predictions = []
        for temp in temps:
            prediction = fire_predict(temp, max_temp_bne, year, month, day, soi)
            predictions.append(prediction)

        data = {
            "Max temperature in Sydney": temps,
            "Fire scan area": predictions
        }

    elif independent_var == "Max temperature in Brisbane":
        temps = np.linspace(max_temp_bne - 30, max_temp_bne + 30, 20)
        predictions = []
        for temp in temps:
            prediction = fire_predict(max_temp_syd, temp, year, month, day, soi)
            predictions.append(prediction)

        data = {
            "Max temperature in Brisbane": temps,
            "Fire scan area": predictions
        }

    elif independent_var == "Southern Oscillation Index":
        oscilation_index = np.linspace(-30, 30, 20)
        predictions = []
        for entry in oscilation_index:
            prediction = fire_predict(max_temp_syd, max_temp_bne, year, month, day, entry)
            predictions.append(prediction)

        data = {
            "Southern Oscillation Index": oscilation_index,
            "Fire scan area": predictions
        }

    elif independent_var == "Date":
        dates = pd.date_range(start=f"1/1/{int(year)}", end=f"1/1/{int(year + 20)}", freq="Y")
        predictions = []
        for date in dates:
            prediction = fire_predict(max_temp_syd, max_temp_bne, date.year, date.month, date.day, soi)
            predictions.append(prediction)

        data = {
            "Date": dates,
            "Fire scan area": predictions
        }

    df = pd.DataFrame(data=data)
    return df.plot(x=independent_var, y="Fire scan area", kind="line").get_figure()