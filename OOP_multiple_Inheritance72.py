#..................................................
# OOP => multiple_Inheritance
#..................................................
# [1] Method override : by making method by the same name in second class
# [2] MRO => Method resolution order
# [3] Multiple inheritance
#..................................................

# [1] Method override : by making method by the same name in second class
class food :  # Base Class
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(f'{self.name} is created from the Base class')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple(food) : # Derived Class => inherite from base class by making it as parameter to its instance

    def __init__(self,name,price) : # constructor override the constructor of the previous class
        #    food.__init__(self,name,price) # use the name of the first constructor
        super().__init__(name,price)
        print(f'{self.name} is created from the Derived class And price is {self.price} $')
    def eat(self) :
        print('Eat Method from the Derived class class') # Method override 
    

# food_one = food("pizza")
food_two = Apple("kishta",150)
food_two.eat()

print("*"*50)
# [2] Multiple inheritance

class BaseOne :
    pass
class BaseTwo :
    pass
class Derived(BaseOne,BaseTwo) :
    pass
print("*"*50)
# [2] Multiple inheritance

class BaseOne :
    def __init__(self):
        print('BaseOne')
    def func_one(self) :
        print('one')
class BaseTwo :
    def __init__(self):
        print('BaseTwo')
    def func_two(self) :
        print('two')
class Derived(BaseOne,BaseTwo) :
    pass

my_var = Derived()
print(Derived.mro()) # method resolution ordered
print(my_var.func_one)
print(my_var.func_two)
my_var.func_one()
my_var.func_two()

print("*"*50)

class Base :
    pass
class Derived_one(Base) :
    pass
class Derived_two(Derived_one) : # this is the multiple inheritance
    pass

