import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(2001, 6, 8)
print(birthday)

# Find days and birth
days_sins_birth = today - birthday
print(days_sins_birth)

# Add 10 days ad current day
delta = datetime.timedelta(days=10)
print(today + delta)
print(today - delta)

print(today.month)
print(today.day)
print(today.weekday())

# Monday = 0 , Sunday = 6

print(datetime.time(7, 2, 20, 15))

# datetime.date(Y , M , D)
# datetime.time(h ,m ,s ,ms)
# datetime(y ,m ,d ,h ,m ,s, ms)

# Add 10 hour at current day
hour_delta = datetime.timedelta(hours=11)
print(datetime.datetime.now() + hour_delta)

print(datetime.datetime.now(tz=pytz.UTC))

date_time_today = datetime.datetime.now(tz=pytz.UTC)
date_and_time_pacific = date_time_today.astimezone(pytz.timezone('US/Pacific'))
print(date_and_time_pacific)

for tz in pytz.all_timezones:
    print(tz)


# String formatting with dates
# 2022-06-17 -> june 16, 2022

print(date_and_time_pacific.strftime('%B %d, %Y'))

# March 09 , 2022 -> date time (20222,6,17)
# strptime = (p = parsing)
datetime_thing = datetime.datetime.strptime('June 17, 2022' , '%B %d, %Y')
print(datetime_thing)