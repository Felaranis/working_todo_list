from datetime import datetime, timedelta, date

date_time = "05/10/2022"
format_date = "%d/%m/%Y"
object_datetime = datetime.strptime(date_time, format_date)
format_otherdate = "%b %d, %y"



today = date.today()
time_delta = today + timedelta(days=7)
print(time_delta)
