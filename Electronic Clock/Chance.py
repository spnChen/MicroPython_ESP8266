
def Week_English(Week):
  if Week == 1:
    Week = "Mon."
  elif Week == 2:
    Week = "Tues."
  elif Week == 3:
    Week = "Wed."
  elif Week == 4:
    Week = "Thurs."
  elif Week == 5:
    Week = "Fri."
  elif Week == 6:
    Week = "Sat."
  elif Week == 7:
    Week = "Sun."
  return Week

def Weather_English(Weather):
  if Weather == "阴":
    Weather = "Overcast"
  elif Weather == "多云":
    Weather = "Cloudy"
  elif Weather == "晴":
    Weather = "Sunny"
  elif Weather == "雨":
    Weather = "Rainy"
  elif Weather == "小雨":
    Weather = "Light Rain"
  elif Weather =="阵雨":
    Weather = "Shower"
  elif Weather == "雷雨":
    Weather = "Thunder Storm"
  elif Weather == "雷阵雨":
    Weather = "Thunder Shower"
  elif Weather == "中雨":
    Weather = "Moderate Rain"
  elif Weather == "大雨":
    Weather = "Heavy Rain"
  elif Weather == "雪":
    Weather = "Snowy"
  elif Weather == "小雪":
    Weather = "Light Snow"
  elif Weather =="阵雪":
    Weather = "Snow Shower"
  elif Weather == "中雪":
    Weather = "Moderate Snow"
  elif Weather == "大雪":
    Weather = "Heavy Snow"  
  else:
    Weather = "Other"
  return Weather


