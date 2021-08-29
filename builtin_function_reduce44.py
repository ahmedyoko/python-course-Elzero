#.....................................
# builtin_function_reduce
# ....................................
# [1] take function and iterator
# [2] run a function on first and second elements and give the result
# [3] then run function on result and third element
# [4] then run function on result and fourth element and so on
# [5] function can be predefined function or lambda function
#.....................................
from functools import reduce
def sumAll(num1,num2) :
    return num1 + num2
numbers = [1,2,8,9,100]
result = reduce(sumAll,numbers)
print(result)
# ((((1+2)+8)+9)+100)=> one element (reduce multiple elements into one element)
print('*'*50)
print('making reduce function by using lambda function')
result = reduce(lambda num1,num2 :num1 + num2,numbers)
print(result)