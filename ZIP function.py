# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, ect.)
#                  creates a zip object with paired elements stored in tuples for each element
usernames = ["Dude", "username", "usrname"]
password = ["pass", "pass123", "pass132"]
login_dates = ["14.9.21", "15.9.21", "16.9.21"]
# usernames= dict(zip(usernames, password))
# for key,value in usernames.items():
#     print(key + " " + value)
# print(type(usernames))
#
# usernames= zip(usernames, password)
#
# for i in usernames:
#     print(i)
#     print(type(usernames))
usernames= zip(usernames, password, login_dates)
for i in usernames:
    print(i)