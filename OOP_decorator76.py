#.........................................
# OOP => decorators
#.........................................

class member :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hello(self):
        return f"hello{self.name}"
    def age_in_days(self) :
        return self.age*356
    
one = member("ahmed",45)
print(one.name) # acess the constructor parameter=> property
print(one.age)
print(one.say_hello()) # acess the methods
print(one.age_in_days)#  it is properities =><bound method member.age_in_days of <__main__.member object at 0x0000023D24B2FFD0>>
print(one.age_in_days())
# to run method as property => use decorator => @property before the method
print('*'*60)
class member :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hello(self):
        return f"hello{self.name}"
    @property
    def age_in_days(self) :
        return self.age*356
    
one = member("ahmed",45)
print(one.name) # acess the constructor parameter=> property
print(one.age)
print(one.say_hello()) # acess the methods
# print(one.age_in_days)#  it is properities =><bound method member.age_in_days of <__main__.member object at 0x0000023D24B2FFD0>>
# print(one.age_in_days())
# to run method as property => use decorator => @property before the method
print(one.age_in_days)





  