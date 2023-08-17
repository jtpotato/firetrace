"""
This file contains all of the UI elements in the Gradio interface.

The UI allows people to interact with the AI :)
"""

import gradio as gr
from firetrace.predict import ui_predict
from firetrace import interface_text

from firetrace.theme import theme

with gr.Blocks(theme=theme) as demo:
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
            with gr.Group():
                out = gr.Textbox(label="Fire Scan Area")
                with gr.Box():
                    additional_info = gr.Markdown(label="Additional Info", value="Waiting for input...")
            btn = gr.Button("Run", variant="primary")

    gr.Markdown(interface_text.q_and_a)

    btn.click(
        fn=ui_predict,
        inputs=[maxtemp, maxtemp2, year, month, day, soi],
        outputs=[out, additional_info],
    )

    with open("firetrace/js/onload.js", "r") as f:
        scripts = f.read()
        print(scripts)
        demo.load(_js=scripts) # load can only be called within a Blocks context

demo.queue(concurrency_count=8)

if __name__ == "__main__":
    demo.launch()
