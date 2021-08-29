#.....................................
# Date_and_Time
#.....................................
#.....................................
import datetime
print(dir(datetime))
print('*'*60)
print(dir(datetime.datetime))
print('*'*60)
print('the current date and time')
print(datetime.datetime.now()) # you will find year:month:day
print('*'*60)
print('*'*60)
print('the current year')
print(datetime.datetime.now().year)
print('*'*60)
print('*'*60)
print('the current month')
print(datetime.datetime.now().month)
print('*'*60)
print('*'*60)
print('the current day')
print(datetime.datetime.now().day)
print('*'*60)
print('*'*60)
print('start and end of the date')
print(datetime.datetime.min)
print(datetime.datetime.max)
print('*'*60)
print(dir(datetime.datetime.now())) # => you will find time function => you can print the time
# the current time :
print(datetime.datetime.now().time()) # time in hour : minute : second : part of second
# the current time in hour :
print(datetime.datetime.now().time().hour)
# the current time in minute :
print(datetime.datetime.now().time().minute)
# the current time in second :
print(datetime.datetime.now().time().second)
print('*'*50)
print('start and end of time')
print(datetime.time.min)
print(datetime.time.max)
print('*'*50)

# print specific date => datetime.datetime(year,month,day)
print(datetime.datetime(1976,7,15))
# optional you can print hour,minute,second,microsecond
print(datetime.datetime(1976,7,15,10,40,55,12564))
print('*'*50)
# to know how many years , month , date you live till now :
birthday = datetime.datetime(1976,7,15)
dateNow = datetime.datetime.now()
print(f'my birthday is {birthday} And',end=" ")
print(f'date now is {dateNow}')
print(f'I lived for {dateNow - birthday}')
print(f'I lived for {(dateNow - birthday).days} Days')