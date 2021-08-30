#...............................................
# .. docstring_and_commenting_vs_documenting
#................................................
# [1] Documentation string for class ,module and function
# [2] can be accessed from help and doc attributes
# [3] to understand the functionality of complex code
# [4] one line or multiple line doc strings
# []
#................................................

def elzero_function(name) :
    '''that is function to say hello from elzero => an example of single doc string'''
    print(f'Hello {name} from elzero')

elzero_function('ahmed')
# print(dir(elzero_function)) # has function called __doc__
print(elzero_function.__doc__) # print doc string as you write
print('*'*50)
help(elzero_function)
print('*'*50)

def elzero1_function(name) :
    ''' elzero1_function
    It say hello from elzero
    parameter:
    name => person that the function uses to greeting
    return => hello or greeting message to the person
     => an example of multiple doc string'''
    print(f'Hello {name} from elzero')

print(elzero1_function.__doc__) # print doc string as you write
print('*'*50)
help(elzero1_function)
