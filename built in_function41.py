#...............................
# built in_function :
#...............................
# all()
# any()
# bin()
# id()
# sum()
# round()
# range()
# print()
# abs()
# pow()
# min()
# max()
# slice()
#
#................................

# x = [1,2,3,4]
from typing import Iterable


x = [1,2,3,4,[]]
if all(x):
    print('all elements are true')
else :
    print('there is at least one element false')
print('#'*50)
# x = [1,2,3,4]
# x = [1,2,3,4,[]]
x = [0,0,[]]
if any(x):
    print('there is at least one element is true')
else :
    print('there is no true element')
print('#'*50)
# binary convertion
print(bin(100))
print('#'*50)
# id or address of the variable in the memory
print('id function')
a = 1
b = 2
print(id(a))
print(id(b))
print('*'*50)

print('sum function')
# sum(Iterable,start) iterable is obligatory
a = [1,10,19,40]
print(sum(a))
print(sum(a,50))
print('*'*50)

print('Round function')
# round(number,number of digit) number parameter is obligatory
print(round(190.5484554)) # 191
print(round(190.42484554)) # 190
print(round(190.5484554 , 2)) # 190.55
print('*'*50)

print('Range function')
# range(start , end ,step) end parameter is obligatory , start default =0 , step default =1
print(list(range(0))) # []
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,20,2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print('*'*50)
print('print function')
# 1- separator between words and change it by sep=
print('Hello Osama How Are You?')
print('Hello','Osama','How','Are','You?') # default separator is space(replace comma)
print('Hello','Osama','How','Are','You?',sep="|")
print('Hello','Osama','How','Are','You?',sep="@")
print('Hello','Osama','How','Are','You?',sep=" ")

# change end : by default is end="\n"
print('first line') #by default it is=> print('first line',end='\n')
print('second line',end=' ') #change end to space so the third line become after it in same line
print('third line')
print('fourth line')

print('*'*50)
print('absolute function => convert to positive number') 
print(abs(-100))
print(abs(100.99))
print(abs(100))
print(abs(-100.66))

print('*'*50)
print('pow => power of the number')
# pow(base,exponent,modulous) modulous is optional
print(pow(2,5))
print(pow(2,5,10)) # => (2*2*2*2*2)%10 => (32)%10 => 2

print('*'*50)
print('minimum function')
# min(item ,item , item ...etc or iterator) item => all number or all string , iterator(list,tuple,dict..etc)
print(min(1,10,-20,50,30)) # all number
print(min('A','Z','x','Ahmed')) # all string
mytuple = (1,-100,20 ,50)
print(min(mytuple))
print('*'*50)
print('maximum function')
# max(item ,item , item ...etc or iterator) item => all number or all string , iterator(list,tuple,dict..etc)
print(max(1,10,-20,50,30)) # all number
print(max('A','Z','X','Ahmed')) # all string
mytuple = (1,-100,20 ,50)
print(max(mytuple))
print('*'*50)

print('slice function')
# slice(start,end,step) end is obligatory
a = ['a','b','c','d','e','f']
print(a[:5])
print(a[slice(5)])
print(a[slice(2,5)])
print(a[slice(1,6,2)])


