#....................
#strings Formating:
#1- using placeholder:if one placeholder after quotation mention value in quotation or just variable without quotation
# if 2 placeholders : after quotation mention 2 values or variables in parantheses
# to make output in numerical not in string form , use %d for integer and %f for float
#.........................
Name = 'osama'
Age = 30
Rank = 1
print('my name is :' + Name)
# print('my name is :' + Name + ' My Age is'+ Age) # TypeError : concatenate str to str only

# to avoid type error , use place holder to determine the type of variable
#1- using placeholder: if one placeholder after quotation mention value in quotation or just variable without quotation
print('my name is : %s' % 'osama')
print('my name is : %s' % Name)
# if 2 placeholders : after quotation mention 2 values or variables in paranthesis
print('My name is : %s and My Age is : %s' %(Name,Age))
print('My name is : %s and My Age is : %s' %('osama','30'))

# to make output in numerical not in string form , use %d for integer and %f for float
print('My name is : %s and My Age is : %d and My Rank is : %f' %(Name,Age,Rank))

n = 'osame'
l = 'python'
y = 10
print("I'm %s and my programming language is %s and I spent in it %d years Experience" % (n,l,y))

#to control floating point => put the number of decimal number you want before f as %.2f = 2 decimal numbers
# the default float is ten numbers
myNumber = 10
print('My Number is : %d' % myNumber)
print('My Number is : %f' % myNumber)
print('My Number is : %.2f' % myNumber)
print('My Number is : %.1f' % myNumber)

#Truncate string : like slicing 
MyLongString = 'Hello people of elzero school , I love you all'
print('message is : %s' % MyLongString)
print('message is : %.5s' % MyLongString) #print 5 characters only