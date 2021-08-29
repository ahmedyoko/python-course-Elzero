#...............................
# builtin_function_filter
#...............................
# 1- filter take a function and iterator
# 2- called filter as it run function in all elements
# 3- can be predifined function or lambda function
# 4- function return boolean value
# 5- if true element => filter out it
# ................................
def checknumber(num):
    if num > 10 :
        return num
mynumbers =[1,19,10,20,100,5]
myResult = filter(checknumber, mynumbers)
for number in myResult :
    print(number)
print('*'*50)
print('true value only')
# filter deal with true value 
def checknumber(num):
    return num > 10 # filter will return all value true (ask question is => if true,filter it)
mynumbers =[1,19,10,20,100,5]
myResult = filter(checknumber, mynumbers)
for number in myResult :
    print(number)
print('*'*50)
print('zero as false value')
# filter not return false value as zero otherwise it become true
def checknumber(num):
    if num == 0 :
        return num
mynumbers =[0,0,1,19,10,20,100,5,0,0]
myResult = filter(checknumber, mynumbers)
for number in myResult :
    print(number)
# to make filter change zero to true condition
def checknumber(num):
    if num == 0 :
        return True
mynumbers =[0,0,1,19,10,20,100,5,0,0]
myResult = filter(checknumber, mynumbers)
for number in myResult :
    print(number)
print('#'*50)
print('for strings')
def checkname(name):
    return name.startswith('o')
mytext = ['omar','osama','omier','ahmed','sayed','othman']
mydata = filter(checkname,mytext)
for person in mydata :
    print(person)
print('.'*50)
print('by using lambda function')
# def checkname(name):
#     return name.startswith('o')
mytext = ['omar','osama','omier','ahmed','sayed','othman','amer']
mydata = filter(lambda name :name.startswith('a'),mytext)
for person in mydata :
    print(person)
print('.'*50)
print('filter directly without variable')
for person in filter(lambda name :name.startswith('a'),mytext) :
    print(person)


