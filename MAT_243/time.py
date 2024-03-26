# Getting current date and time using now().

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)

# Python3 code to demonstrate
# attributes of now()

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing attributes of now().
print("The attributes of now() are :")

print("Year :", current_time.year)

print("Month : ", current_time.month)

print("Day : ", current_time.day)

print("Hour : ", current_time.hour)

print("Minute : ", current_time.minute)

print("Second :", current_time.second)

print("Microsecond :", current_time.microsecond)

# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

# printing current time in india
print("The current time in india is :", current_time)



import time

curr_time = time.strftime("%H:%M:%S", time.localtime())

print("Current Time is :", curr_time)

millisec = int(round(time.time() * 1000))

print("Time in Milli seconds: ", millisec)

curr_time = time.strftime("%H:%M:%S", time.localtime())

print("Current Time is :", curr_time)

nano_seconds = time.time_ns()

print("Current time in Nano seconds is : ", nano_seconds)

# current GMT Time
gmt_time = time.gmtime(time.time())

print('Current GMT Time:\n', gmt_time)


print("Epoch Time is : ", int(time.time()))


