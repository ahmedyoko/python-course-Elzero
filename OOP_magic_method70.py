#..................................................
# OOP_magic_method :
#..................................................
# Everything in python is an object
# __init__ called automatically when instantiated class
# self.__class__ the class to which class instance belong
# __str__ gives a human readable output of the object
# __len__ gives the length of the container
#         called when builtin len function used in the object
#..................................................

class Skill :
    def __init__(self) :
        self.skills = ['Html','Css','Js']
    def __str__(self) -> str:
        return f"This is my Skills : {self.skills}"
    def __len__(self) :
        return len(self.skills)

profile = Skill()
print(profile) # <__main__.Skill object at 0x0000020AAD29CB50>
print(len(profile))
profile.skills.append("PHP")
profile.skills.append("MySQL")
print(len(profile))
print(profile.__class__) # to which class belong to(name of class)

print('*'*50)
string = 'osama'
print(type(string)) # <class 'str'>
# print(string.__class__) # <class 'str'>
# print(dir(str))
