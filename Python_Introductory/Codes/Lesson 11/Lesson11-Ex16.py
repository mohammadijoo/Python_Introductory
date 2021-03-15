import time 
import datetime
tm=[]
for i in range(5):
	tm.append(datetime.datetime.now())
	time.sleep(1)
for i in tm:
	print(i)
