import random


def believeable_values():
  soi = random.randint(-10, 10)

  average_temp = random.randint(5, 30)
  max_t_bne = average_temp + random.randint(-5, 5)
  max_t_mel = average_temp + random.randint(-5, 5)
  max_t_cns = average_temp + random.randint(-5, 5)
  max_t_pth = average_temp + random.randint(-5, 5)
  max_t_syd = average_temp + random.randint(-5, 5)

  day = random.randint(1, 28)
  month = random.randint(1, 12)
  year = random.randint(2001, 2030)

  return soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, day, month, year