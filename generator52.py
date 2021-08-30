# .................................
# generator :
#.............
# [1] function with yield keyword instead of return
# [2] support iteration and return generator iterator by calling yield
# [3] can have one or more yield
# [4] by using next() it resume from where it called "yield"not from the beginning 
# [5] run when it called (gives you the control, no automatically run)
#....................................
def myGenerator1():
    return
print(myGenerator1)
print('*'*50)
def myGenerator() :
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
   
print(myGenerator) # <function myGenerator at 0x0000011A6C8C10D0>
mygen = myGenerator()
print(next(mygen))
# begin from the yield not from the begining
print("hello python , begin from yield not from the begining")
print(next(mygen))
print("hello python , begin from yield not from the begining")
print(next(mygen))
print("hello python , begin from yield not from the begining")
print(next(mygen))
print(next(mygen))
print('#'*50)
def hamdy():
    yield 5
    yield 15
    yield 25
    yield 35
hassan = hamdy()

for number in hassan : 
    print(number)
print('#'*50)
def begin_from_yield():
    yield 16
    yield 26
    yield 36
    yield 46
from_yield = begin_from_yield()
print(next(from_yield))
print(next(from_yield))
print(next(from_yield))
print('#'*50)
for num in from_yield:
    print(num)

