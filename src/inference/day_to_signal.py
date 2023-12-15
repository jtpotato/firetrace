from datetime import datetime
import math

def day_to_signal(day, month):
  # just put an arbitrary year in here it should be fine.
  day_of_year = datetime(2020, int(month), int(day)).timetuple().tm_yday
  sin_signal = math.sin(day_of_year * 2 * math.pi / 365)
  cos_signal = math.cos(day_of_year * 2 * math.pi / 365)

  return sin_signal, cos_signal