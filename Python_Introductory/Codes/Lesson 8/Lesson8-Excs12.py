month = input("Input the month (e.g. January, February etc.): ")
month = month.upper()
day = int(input("Input the day: "))

if month in ('JANUARY', 'FEBRUARY', 'MARCH'):
	season = 'winter'
elif month in ('APRIL', 'MAY', 'JUNE'):
	season = 'spring'
elif month in ('JULY', 'AUGUST', 'SEPTEMBER'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'MARCH') and (day > 19):
	season = 'spring'
elif (month == 'JUNE') and (day > 20):
	season = 'summer'
elif (month == 'SEPTEMBER') and (day > 21):
	season = 'autumn'
elif (month == 'DECEMER') and (day > 20):
	season = 'winter'

print("Season is: ",season)
