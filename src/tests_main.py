from frontend.get_ui_prediction import get_ui_prediction
from frontend.generate_believeable import believeable_values

print("TEST: MODEL PROPERLY INTERPRETS RANDOM DATA")
def model_properly_interprets_random_data():
  soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year = believeable_values()
  prediction = get_ui_prediction(soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year)
  print("Result: ", prediction)

model_properly_interprets_random_data()