#........................
# Global scope 
#........................

x = 1 # global scope
def one():
    print(f"print the variable from the function scope : {x}")
print(f"print the variable from the global scope : {x}")
one()
print('#'*50)
x = 1 # global scope
def one():
    x = 2 # what happens in vagas stay in vagas => the effect of local variabe in function scope only
    print(f"print the variable from the function scope : {x}")
print(f"print the variable from the global scope : {x}")
one()
print('#'*50)
# change local variable to global variabe => all function use after call that function use it as global
x = 1 # global scope
def one():
    global x # convert local variable as global(override global of the system)
    x = 2 
    print(f"print the variable from the function scope : {x}")
print(f"print the variable from the global scope : {x}") 
one()
print(f"print the variable from the global scope after calling function: {x}") 
