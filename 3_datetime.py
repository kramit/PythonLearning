# Import the datetime and the classes from datetime


from datetime import datetime, timedelta
current_date = datetime.now()
print('today is: ' + str(current_date))
print('todays day is: ' + str(current_date.day))
print('todays month is: ' + str(current_date.month))

one_day = timedelta(days=1)
yesterday = current_date - one_day
print('yesterday was: ' + str(yesterday))
