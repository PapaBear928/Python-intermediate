projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for i,(pr,ld) in enumerate(zip(projects,leaders)):
	new = ('{} - {} - {} '.format(i+1, pr,ld, ))
	print(new)

for p,(dt,n) in enumerate(zip(dates,new)):
	print('{} - {} - {} '.format(i+1, pr,ld, ))