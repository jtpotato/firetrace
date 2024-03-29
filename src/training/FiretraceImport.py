import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib


def FiretraceImport(dataPath = None, modelPath = None):
    if dataPath == None:
        dataPath = "data"
    if modelPath == None:
        modelPath = "models"

    df = pd.read_csv(dataPath + "/gen_2/processed/with_fire_area_soi_weather_time.csv")

    df_y = df["fire_area"]
    df_x = df.drop(["fire_area"], axis=1)

    x_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()
    df_x_scaled = x_scaler.fit_transform(df_x)
    df_y_scaled = y_scaler.fit_transform(df_y.values.reshape(-1, 1))

    # save scalers
    joblib.dump(x_scaler, modelPath + "/x_scaler.save")
    joblib.dump(y_scaler, modelPath + "/y_scaler.save")

    X_train, X_test, y_train, y_test = train_test_split(
        df_x_scaled, df_y_scaled, train_size=0.8, shuffle=True, random_state=12424
    )

    return X_train, X_test, y_train, y_test
