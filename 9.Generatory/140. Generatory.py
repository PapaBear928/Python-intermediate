import datetime as dt

def MD( year,month,day, maxdays):
	date = dt.datetime(year,month,day)

	for i in range(maxdays):
		yield(date + dt.timedelta(days= i))



for d in MD(2000,1,1,2500000):
	print(d)