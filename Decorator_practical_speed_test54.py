# .........................................
# Decorator_practical_speed_test
# .........................................
def myDecorators(func): 
    def nestedfunc(*numbers):
        for number in numbers : 
        
         if number < 0  :                            
          print('beware one number at least less than zero')
        func(*numbers)
    return nestedfunc
@myDecorators
def calculate(n1,n2,n3,n4) :
    print(n1+n2+n3+n4)
calculate(50,60,80,90)

print('#'*50)
from time import time
print('speed test') # to estimate the time of running a function
def speedTest(func) :
    def wrapper() :
        start = time()
        func()
        end = time()
        print(f'function running time is {end - start}')
    return wrapper
@speedTest
def bigloop() :
    for number in range(1,2000) :
        print(number)

bigloop()