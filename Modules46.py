#......................................
# Modules => builtin modules
#......................................
# [1] module is a file contain set of function
# [2] you can import the module in your app to help you
# [3] you can import multiple modules
# [4] you can create your own module
# [5] modules save your time
#......................................

# import module 
import random
# print(random) # path in your computer
print(f'print random float number {random.random()}')
print('.'*50)
# show all function inside the module 
print(dir(random)) # dir command => all data about the directory(object)
print('.'*50)

# import one or more than one function from the module => from module import function
from random import randint 
print(f'print random integer {randint(100,900)}')
print('.'*50)

# import more than one function from the module => from module import function
from random import randint , random 
print(f'print random float number {random()}')
print(f'print random integer {randint(100,900)}')

# from random import randint , random , third function
# from random import * => all functions in the module

