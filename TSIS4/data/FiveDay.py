import datetime

today = datetime.date.today()
new_date = today - datetime.timedelta(days = 5)
print("Today is:", today)
print("5 days ago was:", new_date)