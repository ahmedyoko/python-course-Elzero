#.............................
# Module_creation
#.............................
#.............................

# import sys
# sys.path.append(r"D:\Games") # add python file to the sys.path
# print(sys.path) # all path of python file in the system

import ahmed
print(dir(ahmed)) # to show the function in this module
# to use function in it => module.function 
ahmed.say_hello('osama')
ahmed.say_HowAreYou('osama')

# to make alias to the imported function or module use => import as
print('*'*50)
print('use alias for imported module and function') 
import ahmed as aa  # alias of this module
aa.say_hello('mostafa')
aa.say_HowAreYou('mostafa')
aa.say_HowAreYou('aadel')

print('*'*50)
print('alias for imported function')
from ahmed import say_hello 
say_hello('hassan')
from ahmed import say_hello as ss
say_hello('hassan')
ss('omar')
