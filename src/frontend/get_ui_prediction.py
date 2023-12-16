# Process predictions from the UI

from inference.day_to_signal import day_to_signal
from inference.get_prediction import get_prediction
from frontend.additional_context import additional_context
from frontend.generate_map import generate_map


def get_ui_prediction(soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year):
    """
    Process predictions from the UI, using the variables from the UI.
    """
    sin_signal, cos_signal = day_to_signal(day, month)

    fire_size = get_prediction(soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, sin_signal, cos_signal, year)

    context_string = additional_context(fire_size)
    figure = generate_map(fire_size, str(int(month)).zfill(2))
    return f"{context_string}", figure