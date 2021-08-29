#.................................
# Date_and_Time_Format
#.................................
# https://strftime.org
#.................................

import datetime
birthday = datetime.datetime(1976,7,15)
print(birthday)
print(birthday.strftime('%a')) # abbreviation of day name
print(birthday.strftime('%A')) # name of day name
print(birthday.strftime('%b')) # abbreviation of month
print(birthday.strftime('%B')) # name of month

print(birthday.strftime('%d %B %Y')) # %d day , %B month , %Y year full name
print(birthday.strftime('%d , %B , %Y'))
print(birthday.strftime('%d / %B / %Y'))
print(birthday.strftime('%d - %B - %Y'))

# print(dir(datetime.datetime)) # strftime function