#............................
# function_packing_unpacking
#............................
# print(1,2,3,4,5)
# mylist = [1,2,3,4,5]
# print(*[1,2,3,4,5])
# print(mylist)
# print(*mylist)

def say_hello(n1,n2,n3,n4):
    peoples = [n1,n2,n3,n4]
    for name in peoples :
        print(f'Hello {name.capitalize()}')
say_hello("ahmed",'sayed','ahmed','osama') # if the argument increase than the limit it will give an error
# to met the need of increasing the argument use astriske
def say_hello(*peoples): # astrisk = met the need of any number of argument
    for name in peoples :
        print(f'Hello {name.capitalize()}')
say_hello("ahmed",'sayed','ahmed','osama','ali','salah') 

print('#'*50)

def show_details(name,*skills):
    
        print(f'hello{name.capitalize()},your skill is')
        for skill in skills:
            print(f' {skill}')
show_details("ahmed",'html','css','python')

    