import gradio as gr

from frontend.get_ui_prediction import get_ui_prediction
from frontend.generate_believeable import believeable_values
from frontend.ui_text import q_and_a
from frontend.theme import theme

with open("src/frontend/js/onload.js", "r") as f:
    onload_script = f.read()


with gr.Blocks(theme=theme, title="Firetrace Demo", js=onload_script) as demo:
    gr.Markdown(
        '<center><img src="https://raw.githubusercontent.com/jtpotato/firetrace/main/assets/banner-transparent.svg" width="300"></img></center>'
    )
    generate_believeable_button = gr.Button(value="Generate Random Values")

    soi = gr.Number(label="Southern Oscillation Index")
    with gr.Row():
        year = gr.Number(label="Year")
        month = gr.Number(minimum=1, maximum=12, step=1, label="Month")
        day = gr.Number(minimum=1, maximum=31, step=1, label="Day")
    with gr.Row():
        max_t_bne = gr.Number(label="Max Temperature in Brisbane")
        max_t_mel = gr.Number(label="Max Temperature in Melbourne")
        max_t_cns = gr.Number(label="Max Temperature in Cairns")
        max_t_pth = gr.Number(label="Max Temperature in Perth")
        max_t_syd = gr.Number(label="Max Temperature in Sydney")

    predict_button = gr.Button(value="Predict")

    with gr.Row():
        map = gr.Plot()
        prediction = gr.Markdown(value="Waiting...")

    disclaimer = gr.Markdown(
        value="Sorry to break it to you, but the map isn't *real* 😧. It shows where fires are *likely* to be, based on historical data for that time of year, but we cannot guarantee that there will actually be fires in these locations. It's possible that fires will appear in completely different regions compared to what is illustrated on the map. 🔥"
    )
    gr.Markdown(value=q_and_a)

    # --------Behaviours--------
    demo.load(
        fn=believeable_values,
        inputs=[],
        outputs=[
            soi,
            max_t_bne,
            max_t_mel,
            max_t_cns,
            max_t_pth,
            max_t_syd,
            day,
            month,
            year,
        ],
    )

    generate_believeable_button.click(
        believeable_values,
        inputs=[],
        outputs=[
            soi,
            max_t_bne,
            max_t_mel,
            max_t_cns,
            max_t_pth,
            max_t_syd,
            day,
            month,
            year,
        ],
    )

    predict_button.click(
        get_ui_prediction,
        inputs=[
            soi,
            max_t_bne,
            max_t_mel,
            max_t_cns,
            max_t_pth,
            max_t_syd,
            day,
            month,
            year,
        ],
        outputs=[prediction, map],
    )

if __name__ == "__main__":
    demo.launch(quiet=True)