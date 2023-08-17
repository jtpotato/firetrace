"""
This file contains the theme for the Gradio interface.
"""

import gradio as gr

theme = gr.themes.Default(
    neutral_hue="zinc",
    font=[gr.themes.GoogleFont('Poppins'), 'ui-sans-serif', 'system-ui', 'sans-serif'],
    font_mono=[gr.themes.GoogleFont('JetBrains Mono'), 'ui-monospace', 'Consolas', 'monospace'],
)