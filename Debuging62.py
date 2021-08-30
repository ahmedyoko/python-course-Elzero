#.....................................
# Debuging code
#.....................................
mylist = [1,2,3,4,5,6]
mydict = {'name':'osama','age':39,'country':'egypt'}
for num in mylist :
    print(num)
for key,value in mydict.items() :
    print(f'{key} => {value}')

def function_one_one():
    print('hello from function one')

function_one_one()