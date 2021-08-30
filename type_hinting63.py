#......................................
# type_hinting ->
#......................................

def say_hello(name)->str :  # -> type , it is a hint and will appear when you call the function
    print(f'hello {name}')

say_hello('Ahmed')
say_hello('10')

print('*'*50)

def calculate(n1,n2)->int :
    print(n1+n2)
calculate(15,41)