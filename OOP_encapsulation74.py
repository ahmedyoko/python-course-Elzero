#...............................................................
# OOP => encapsulation
#...............................................................
# Encapsulation :
# restrict access to the data stored in attributes and methods
# Public :
# every attributes and methods that we used so far be public
# attributes and methods can be run from everywhere
# Inside our outside the class
# protected :
# attributes and methods can be accessed from the class and subclasses(derived or inherted class)
# attributes and methods are prefixed with one underscore _
# private : 
# attributes and methods can be accessed from within the class and object only
# attributes can not be modified from outside the class
# attributes and method prefixed with 2 underscores __
#...............................................................
#  Attributes = variable = properties
#...............................................................

class member :
    def __init__(self,name):
        self.name = name

one = member("Ahmed")
print(one.name)
one.name = "Ismail"   # modify it 
print(one.name)

print('*'*50)
# protected 
print("proctected encapsulation")
class member :
    def __init__(self,name):
        self._name = name

one = member("Ahmed")
print(one._name)
one._name = "Ismail"
print(one._name)

print('*'*50)
# private encapsulation
print("private encapsulation")
class member :
    def __init__(self,name):
        self.__name = name
    def say_hello(self):
        print(f"hello{self.__name}")
one = member("Ahmed")
# print(one.__name) has no direct acess to private properities
# one._name = "Ismail"
# print(one._name)
print(one.say_hello())
print(one._member__name)

print('*'*50)