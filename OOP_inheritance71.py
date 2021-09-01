#............................................
# OOP => inheritance
#............................................

class food :  # Base Class
    def __init__(self) -> None:
        print('Food is created from the Base class')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple : # Derived Class
    def __init__(self) -> None:
        print('Food is created from the Derived class')

food_one = food()
food_two = Apple()

print('*'*50)
# inheritance of method :
#............................
print('inheritance of method :')
class food :  
    def __init__(self) -> None:
        print('Food is created from the Base class')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple(food) : # Derived Class => inherite from base class by making it as parameter to its instance
    def __init__(self) -> None:
        print('Food is created from the Derived class')

# food_one = food()
food_two = Apple()
food_two.eat()
print('*'*50)
# # inheritance of constructor :
# print('inheritance of constructor :')
class food :  # Base Class
    def __init__(self,name):
        self.name = name
        print(f'{self.name} is created from the Base class')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple(food) : # Derived Class => inherite from base class by making it as parameter to its instance
       def __init__(self,name) :
           self.name = name 
           print(f'{self.name} is created from the Derived class')
    

food_one = food("pizza")
food_two = Apple("jampo")
# # food_two.eat()
print('*'*50)
# # inheritance of constructor :
#...................................
print('inheritance of constructor :')
class food :  # Base Class
    def __init__(self,name):
        self.name = name
        print(f'{self.name} is created from the Base class')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple(food) : # Derived Class => inherite from base class by making it as parameter to its instance
       def __init__(self,name) : # constructor override the constructor of the previous class
        #    food.__init__(self,name) # use the name of the first constructor
           super().__init__(name)
           print(f'{self.name} is created from the Derived class')
    

# food_one = food("pizza")
food_two = Apple("kishta")
food_two.eat()
print('*'*50)
# # inheritance of constructor :
#...................................
print('inheritance of constructor :')
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
    

# food_one = food("pizza")
food_two = Apple("kishta",150)
food_two.eat()

print("#"*50)
class food :  # Base Class
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(f'{self.name} is created from the Base class and price {self.price}')
    def eat(self) :
        print('Eat Method from the Base class')

class Apple(food) : # Derived Class => inherite from base class by making it as parameter to its instance

    def __init__(self,name,price,amount) : # amount is paramater of this constructor only

        self.name = name 
        self.price = price +30 # override the constructor of the previous method
        self.amount = amount
        print(f'{self.name} is created from the Derived class and price {self.price} and the amount is {self.amount} kg')
    def get_from_tree(self) :
        print('Get From Tree From Derived Class')

    

food_one = food("pizza",20)
food_two = Apple("jampo",20,50)
food_two.eat()
food_two.get_from_tree()
