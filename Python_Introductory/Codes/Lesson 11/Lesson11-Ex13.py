import datetime
now = datetime.datetime.now() 
yesterday = datetime.datetime(2016, 5, 14, 11, 0, 0)
delta = now - yesterday
print(now)
print(yesterday)
print(delta)
