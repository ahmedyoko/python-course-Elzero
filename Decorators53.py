#..............................
# Decorators التزيين
# [1] sometimes called metaprogramming
# [2] everything in python is object even function
# [3] take a function and add some functionality and return it
# [4] wrap other function and enhance thier behavior
# [5] is higher ordered function (accept other function as a parameter)
#................................
# Decorate function without parameters

def myDecorators(func): # decorator
    def nestedfunc(): # any name it is just for decoration
        print('message before Decoration') # message from decorator
        func()                             # execute function
        print('message after Decoration') # message from decorator
    return nestedfunc                      # return all data
def say_hello():
    print('Hello from say hello function')

say_hello()
after_decoration = myDecorators(say_hello)
after_decoration()
print('*'*50)
@myDecorators  # to make decoration directly to the function
def say_hello():
    print('Hello from say hello function')
say_hello()
print('*'*50)
@myDecorators
def say_howAreYou():
    print('how are you')
say_howAreYou()
print('#'*50)
# Decorate function with parameters
print(" Decorate function with parameters")
def myDecorators(func): # decorator
    def nestedfunc(num1,num2): # any name it is just for decoration + parameters
        print('message before Decoration') # message from decorator
        func(num1,num2)                             # execute function + parameters
        print('message after Decoration') # message from decorator
    return nestedfunc
@myDecorators
def calculate(n1,n2) :
    print(n1+n2)
calculate(10,90)
print('#'*50)
# how we used decorator
def myDecorators(func): 
    def nestedfunc(num1,num2): 
        
        if num1 < 0 or num2 < 0 :                            
         print('beware one number at least less than zero')
        func(num1,num2)
    return nestedfunc
@myDecorators
def calculate(n1,n2) :
    print(n1+n2)
calculate(10,90)
calculate(-5,90)
print('#'*50)
# can make more than one decorator in the same function
def myDecorators(func): 
    def nestedfunc(num1,num2): 
        
        if num1 < 0 or num2 < 0 :                            
         print('beware one number at least less than zero')
        func(num1,num2)
    return nestedfunc
def myDecoratorTwo(func): 
    def nestedfunc(num1,num2): 
        print('coming from decorator Two')
        func(num1,num2)
    return nestedfunc
@myDecorators
@myDecoratorTwo
def calculate(n1,n2) :
    print(n1+n2)
calculate(10,90)
calculate(-5,90)
print('#'*50)

