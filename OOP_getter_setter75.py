#....................................................
# OOP => getter_setter
#....................................................
# to set and get parameter of private properities => can acess and modify
#....................................................

print("private encapsulation")
class member :
    def __init__(self,name):
        self.__name = name
    def say_hello(self):
        print(f"hello{self.__name}")
    def get_name(self) :  # getter to access from outside the class 
        return self.__name
    def set_name(self,new_name) : # setter to modify the private prop
        self.__name = new_name
one = member("Ahmed")
# print(one.__name) has no direct acess to private properities
print(one.get_name())
one.set_name("Ismail")
print(one.get_name())
