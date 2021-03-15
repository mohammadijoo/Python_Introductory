def minsec_to_hours(seconds , minutes):
      hours = minutes / 60 + seconds / 3600
      print(hours)

# Class of NoneType!!!
print(type(minsec_to_hours(300,200)))
