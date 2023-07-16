import gradio as gr
import keras
import pandas as pd
import numpy as np
from datetime import datetime

loaded_model = keras.models.load_model('model/model.keras')


def fire_predict(max_temp_syd, max_temp_bne, year, month, day):
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

    percentage = round((predicted_fire_area / 1043.8) * 100, 2)
    return (f"""
            The scanned area of your fires was {predicted_fire_area} square kilometres. 
            This is {percentage}% of the Black Saturday week.""")

with gr.Blocks() as demo:
    gr.Image(src='https://raw.githubusercontent.com/jtpotato/firetrace/fe00ca92f3ca2280118bc8b4784396055dd53513/assets/banner.svg', alt="Firetrace Logo")
    gr.Markdown(
        """
        Q: What's the deal with Firetrace? 🔍\n
        A: Picture this—it's like having your very own bushfire fortune teller! 
        🔮 Firetrace is an AI-powered web interface that predicts the severity of bushfire events all across Australia. 
        🌍 It's armed with projected weather data, BOM weather observatories and NASA's MODIS satellite intel. 
        It even considers time information to get climate change trends. 🦸‍♂️🔥
        \n

        Q: What is the inspiration behind Firetrace? 🤔 \n
        A: Those bushfires, mate! They cause habitat loss, put many animal species at risk, and drastically impact the economy 😢📉 
        The series of bushfires that took place in Australia is a clear demonstration of this. 
        ☝️ So, we put our heads together to conjure up Firetrace—a cutting-edge tool that helps us predict the severity of these fiery events.
        This will be helpful in making smarter decisions and being prepared to take on the bushfire challenges head-on! 💪🌳
        \n

        Q: How do I use Firetrace? 🎉 \n
        A: It's easy-peasy! 🔥 
        Simply enter in values for the input boxes below, and you'll unlock access to the hottest predictions, 
        and uncover the secrets of bushfire severity. 
        The prediction you receive will be in the form of a percentage - the area covered your bushfire as a percentage of the area covered by the most severe week of the 2011-2012 bushfire season 
        (Keep in mind that it's not completely right - but it does have reasonable accuracy)
        \n

        Let's work together to face these fiery challenges to create a safer future! 🚀🌿
        
        """
    )
    with gr.Row():
        with gr.Column():
            maxtemp = gr.Number(label="Max temperature in Sydney")
            maxtemp2 = gr.Number(label="Max temperature in Brisbane")
            year = gr.Number(label="Year")
            month = gr.Number(label="Month")
            day = gr.Number(label="Day")
        with gr.Column():
            out = gr.Textbox(label="Predicted Result")
    btn = gr.Button("Run")
    gr.Markdown(
        "The scanned area of fires for the week of Black Saturday was 1043.8 square kilometres. 🔥")
    btn.click(fn=fire_predict, inputs=[
              maxtemp, maxtemp2, year, month, day], outputs=out)

demo.launch()
