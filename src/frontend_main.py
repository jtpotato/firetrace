import gradio as gr

from frontend.get_ui_prediction import get_ui_prediction
from frontend.generate_believeable import believeable_values
from frontend.ui_text import q_and_a

with gr.Blocks() as demo:
  gr.Markdown("![Firetrace Logo](https://raw.githubusercontent.com/jtpotato/firetrace/main/assets/banner-transparent.svg)")
  with gr.Row():
    with gr.Column():
      generate_believeable_button = gr.Button(value="Generate Random Values")
      soi = gr.Number(label="Southern Oscillation Index")
      max_t_bne = gr.Number(label="Max Temperature Brisbane")
      max_t_mel = gr.Number(label="Max Temperature Melbourne")
      max_t_cns = gr.Number(label="Max Temperature Cairns")
      max_t_pth = gr.Number(label="Max Temperature Perth")
      max_t_syd = gr.Number(label="Max Temperature Sydney")
      year = gr.Number(label="Year")
      month = gr.Number(minimum=1, maximum=12, step=1, label="Month")
      day = gr.Number(minimum=1, maximum=31, step=1, label="Day")
    
    with gr.Column():
      prediction = gr.Markdown(value="Waiting...")
      map = gr.Plot()
      disclaimer = gr.Markdown(value="This map isn't *real*. It shows where fires are *likely* to be but we cannot guarantee that there will actually be fires in these locations. It's more than likely that fires will appear in completely different regions compared to what is illustrated on the map.")

      predict_button = gr.Button(value="Predict")

  gr.Markdown(value=q_and_a)

  # --------Behaviours--------
  generate_believeable_button.click(believeable_values, inputs=[], outputs=[soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year])

  predict_button.click(get_ui_prediction, inputs=[soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year], outputs=[prediction, map])

# print(get_prediction(10.9,28.2,24.4,31.9,22.9,26.0,-0.8660254037844386,0.5000000000000001,2005.0))
  
demo.launch()