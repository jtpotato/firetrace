import gradio as gr
from firetrace.predict import ui_predict
from firetrace import interface_text

with gr.Blocks() as demo:
    gr.Markdown(
        """<img src="https://raw.githubusercontent.com/jtpotato/firetrace/main/assets/banner-transparent.svg" alt="Firetrace Logo" />"""
    )
    with gr.Row():
        with gr.Column():
            with gr.Row():
                with gr.Column():
                    maxtemp = gr.Number(label="Max temperature in Sydney")
                    maxtemp2 = gr.Number(label="Max temperature in Brisbane")
                    soi = gr.Number(label="Southern Oscillation Index")
                    year = gr.Number(label="Year", maximum=9999)
                    month = gr.Number(label="Month")
                    day = gr.Number(label="Day")
        with gr.Column():
            out = gr.Textbox(label="Fire Scan Area")
            additional_info = gr.Markdown(label="Additional Info")
    btn = gr.Button("Run")

    gr.Markdown(interface_text.q_and_a)

    btn.click(
        fn=ui_predict,
        inputs=[maxtemp, maxtemp2, year, month, day, soi],
        outputs=[out, additional_info],
    )

    with open("src/js/onload.js", "r") as f:
        scripts = f.read()
        print(scripts)

if __name__ == "__main__":
    demo.queue(concurrency_count=8, api_open=False)
    demo.launch()
