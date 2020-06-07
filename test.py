import datetime
from datetime import timedelta  

now = datetime.datetime.now()


print("Current date and time using str method of datetime object:")
print(str(now))
d = str(now + timedelta(minutes=2))

print(d[:-3])
print(type(d))


"""
print("Current date and time using instance attributes:")
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Current 88888microsecond: %d" % (now.microsecond/1000))
"""

print("Current date and time using strftime:")
time = now.strftime("%Y-%m-%d %H:%M:%S:%f")
print(time[:-3])
print(type(time))

"""
print("Current date and time using isoformat:")
print(now.isoformat())
"""