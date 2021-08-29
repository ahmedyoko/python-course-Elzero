#......................................
# function_lambda / anonymous function :
#......................................
# 1- has no name
# 2- you can call it inline without defining it
# 3- you can use it in return data from another function
# 4- used for simple functions and def handle the large Tasks
# 5- one single expression not block of code
# 6- lambda type is function
#......................................

def say_hello(name) : return f'hello {name}'

hello = lambda name : f'hello {name}'
print(say_hello('ahmed'))
print(hello('morad'))

print(say_hello.__name__) # to know the name of the function
print(hello.__name__)

x = lambda n1,n2 : n1+n2 
print(x(9,5))

def say_hello(name,age) : return f'hello {name} your age is {age} years'

hello = lambda name,age : f'hello {name} your age is {age} years'
print(say_hello('ahmed',45))
print(hello('morad',100))

print(type(hello)) # <class 'function'>
