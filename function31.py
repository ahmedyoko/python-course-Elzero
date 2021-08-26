#.................................
# function parameter and argument
# ................................
# before function
# a,b,c = "ahmed",'osama','sayed'
# print(f'hello {a}')
# print(f'hello {b}')
# print(f'hello {c}')

# by using function
# def                   => function key word [define]
# say_hello             => function name
# name                  => parameter  
# print(f'hello {name}')   => Task
# ahmed , osama,sayed   => argument
def say_hello(name): # you can use any symbol like n as a parameter
    print(f'hello {name}')

say_hello('osama') # you can use variable instead of its value => say_hello(a)
say_hello("ahmed")
say_hello('sayed')

# def addition(num1,num2):
#     print(num1 + num2)

# addition(8,101)
def addition(num1,num2):
    if type(num1) != int or type(num2) != int :
        print("only integer is allowed")
    else :
        print(num1 + num2)

addition(500,101)
# addition('500',101)

def full_name(first,middle ,last):
    print(f'hello {first.strip().capitalize()},{middle.strip().capitalize():.1s},{last.strip().capitalize()}')

full_name(  'osama'  ,  'ahmed'  ,  'hassan'  )