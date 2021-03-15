def minsec_to_hours(seconds , minutes = 70):
    hours = minutes / 60 + seconds / 3600
    return hours
print(minsec_to_hours(300))
print(minsec_to_hours(300 , 200))
