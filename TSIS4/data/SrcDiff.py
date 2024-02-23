import datetime

firstDate = datetime.datetime(2022, 5, 13, 0, 0, 0)
secondDate = datetime.datetime(2025, 9, 9, 0, 0, 0)
diff = secondDate - firstDate
diffInSec = diff.total_seconds()
print("The difference between the two dates is", diffInSec, "seconds.")