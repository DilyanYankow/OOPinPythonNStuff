import time


# print(time.ctime(0))  # prints a time expressed in seconds converted to string since epoch
                        # epoch = time that your computer thinks time began

# print(time.time())      # return current seconds since epoch

print(time.ctime(time.time()))     #amount of seconds since epoch, as string / current time

time_obj = time.localtime()
print(time_obj)
# time.strftime(format, time_obj)
# https://docs.python.org/3/library/time.html
# time_obj = time.strftime("%B %d %Y %H:%M:%S", time_obj)
# print(time_obj)
# time_obj2 = time.gmtime()   # UTC time universal time
#
# time_string = "20 April, 2020"
# time_time = time.strptime(time_string, "%d %B, %Y")     #strptime not strftime
# print(time_time)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)      #asctime = tuple to string
time_string = time.mktime(time_tuple)         # seconds till epich of custom time
print(time_string)