#..................................................
# OOP => ABCs => abstract base classes
#..................................................
# [1] class called abstract => if it has one or more abstract method
# [2] abc module in python provides => infrastructure for defining base classes
# [3] by adding @abstractmethod decorators on the methods
# [4] ABCMeta class is a metaclass defining the abstract base class
#..................................................

class programming() : 
    def has_oop(self) :
        return "yes"
class python(programming) :
    def has_oop(self) :
        return "yes"
class pascal(programming) :
    def has_oop(self) :
        return "no"

one = programming()
print(one.has_oop())
print('*'*50)
from abc import ABCMeta,abstractmethod
class programming(metaclass = ABCMeta) : # interface without functionality = abstract , make functionality method below
    @abstractmethod
    def has_oop(self) :
        pass
class python(programming) :
    def has_oop(self) :
        return "yes"
class pascal(programming) :
    def has_oop(self) :
        return "no"

# one = programming() TypeError: Can't instantiate abstract class programming with abstract method has_oop
one = python()
print(one.has_oop())
one = pascal()
print(one.has_oop())
print('*'*50)
from abc import ABCMeta,abstractmethod
class programming(metaclass = ABCMeta) : # interface without functionality = abstract , make functionality method below
    @abstractmethod
    def has_oop(self) :
        pass
    def has_name(self):
        pass
class python(programming) :
    def has_oop(self) :
        return "yes"
class pascal(programming) :
    def has_oop(self) :
        return "no"

# one = programming() TypeError: Can't instantiate abstract class programming with abstract method has_oop
one = python()
print(one.has_oop())
one = pascal()
print(one.has_oop())
print('*'*50)
from abc import ABCMeta,abstractmethod
class programming(metaclass = ABCMeta) : # interface without functionality = abstract , make functionality method below
    @abstractmethod
    def has_oop(self) :
        pass
    # @abstractmethod
    # def has_name(self): #TypeError: Can't instantiate abstract class python with abstract method has_name
    #     pass
class python(programming) :
    def has_oop(self) :
        return "yes"
class pascal(programming) :
    def has_oop(self) :
        return "no"

# one = programming() 
one = python()
print(one.has_oop())
one = pascal()
print(one.has_oop())
print('*'*50)
from abc import ABCMeta,abstractmethod
class programming(metaclass = ABCMeta) : # interface without functionality = abstract , make functionality method below
    @abstractmethod
    def has_oop(self) :
        pass
    @abstractmethod
    def has_name(self): #TypeError: Can't instantiate abstract class python with abstract method has_name
        pass

class python(programming) :
    def has_oop(self) :
        return "yes"
class pascal(programming) :
    def has_oop(self) :
        return "no"
    def has_name(self):
        return "pascal"

# one = programming() TypeError: Can't instantiate abstract class programming with abstract method has_oop
one = pascal()
print(one.has_oop())
one = pascal()
print(one.has_name())
   
