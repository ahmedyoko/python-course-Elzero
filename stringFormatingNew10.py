#.........................
#string formating in new ways:
#1- using format method : replace first placeholder by {} and second by .format
#.........................



Name = 'osama'
Age = 30
Rank = 1
#1- using format method : replace first placeholder by {} and second by .format
print('my name is : {}'.format('osama') )
print('my name is : {}'.format(Name))
# if 2 formats : after quotation mention 2 values or variables in paranthesis
print('My name is : {} and My Age is :{}'.format(Name,Age))
print('My name is : {} and My Age is :{}'.format('osama','30'))
# to make output in numerical not in string form , use %d for integer and %f for float
print('My name is :{:s} and My Age is : {:d} and My Rank is : {:f}'.format(Name,Age,Rank))
# exercise:
n = 'osame'
l = 'python'
y = 10
print("I'm {:s} and my programming language is {:s} and I spent in it {:d} years Experience".format(n,l,y))
# to control floating point => put the number of decimal number you want before f as %.2f = 2 decimal numbers
# the default float is ten numbers
myNumber = 10
print('My Number is : {:d}'.format(myNumber))
print('My Number is :{:f}'.format(myNumber))
print('My Number is : {:.2f}'.format(myNumber))
print('My Number is : {:.1f}'.format(myNumber))
print('='*50)
#Truncate string : like slicing 
MyLongString = 'Hello people of elzero school , I love you all'
print('message is :{:s}'.format(MyLongString) )
print('message is : {:.5s}'.format(MyLongString)) #print 5 characters only

#Format Money : 
MyMoney = 124578963214
print('My Money is {:d}'.format(MyMoney ))
print('My Money is {:_d}'.format(MyMoney )) # separate each 3 digits by this characters
print('My Money is {:,d}'.format(MyMoney ))
# print('My Money is {:.d}'.format(MyMoney )) it will make error as it reserved to floating point only
print('='*50)
# Rearrange items
a , b , c = 'one' , 'two','three'
print('Hello {} {} {}'.format(a , b , c))
#rearrange by putting indexing in between curly bracis {indexing}
print('Hello {1} {2} {0}'.format(a , b , c))
print('Hello {2} {1} {0}'.format(a , b , c))
#exercise :
#{indexing : control}
a,b,c = 10,20 ,30
print('Hello {1:d} {0:d} {2:d}'.format(a , b , c))
#rearrange by putting indexing in between curly bracis
print('Hello {1:d} {2:.2f} {0:.4f}'.format(a , b , c))
print('Hello {2:f} {1:f} {0:f}'.format(a , b , c))

#format for version 3.6+ and after
MyName = 'ahmed'
MyAge = 45
print('My name is : {MyName} and my age is : {MyAge} ')
# add f before quotation as formating
print(f'My name is : {MyName} and my age is : {MyAge} ')