from datetime import datetime, timedelta
print (datetime.now())
one_day = timedelta(days=1)
datestr = "Tue, 13 May 2014 21:43:00 GMT"

print(datetime.strptime(datestr, "%a, %d %b %Y %H:%M:%S %Z"))