#..............................................
# Object Oriented Programming(OOP):
#..............................................
# [1] python support oop
# [2] oop is paradigm or coding style (paradigm نموذج)
# [3] paradigm => structuring programmming (attribute and method bundled or collected in object)
# [4] method => function use the information of the object
# [5] python is multiparadigm programming language [procedural,OOP,Functional]
# [6] Procedural => structure APP like receipe => sets of steps to make the task
# [7] Functional => built on the concept of mathematical function
# benefit of OOP => organize code and make it readable and reusable
#..............................................
# [1] Attributes => all information(adj) => name , age , address , phone number 
# [2] Methods (behaviour-actions)=> Eating,Walking,Singing,Playing 
#..............................................
# car as an object => example of attribute and method
# attribute => Model,Color,Price
# Method => Walking,Stopping

#......................................................................
#           Class مخطط انشاء الكائنات
# [01] is the template for creating an object (object constructor)(blueprint مخطط)
# [02] can create many object
# [03] class instantiate means => create instance of class انشاء مثيل
# [04] instance => object created from class and has its methods and attributes
# [05] class defined with keyword => class
# [06] class name written with pascalCase(UpperCamelCase)style
# [07] class may contain methods and attributes
# [08] when creating an object python is looking for built in __init__ method
# [09] __init__ method called every time you create object from the class
# [10] __init__ method initialize the data for the object
# [11] any Method with 2 underscores in the start and end is called dunder or magic method
# [12] self refer to => current instance created from class and must be first parameter
# [13] self can be named anything
# [14] in python => no need to call new() keyword to crate an object
#.......................................................................
# syntax : 
# class name :
#   constructor => Do instantiation [create instance from a class]
#   each instance is separate object
#   def __init__(self,other_data):
#           body of function 
# 

class member :
    def __init__(self) :
        print('A New Member has been Added')
member()
member()
member()
member()
# print(dir(member)) # to know its content and available method in it
member_one = member()
member_two = member()
member_three = member()
print(member_one.__class__) #to determine that object belong to which class <class '__main__.member'>

print('*'*50)
my_dictionary = {
    "name":"osama",
    "age":36 ,
    "monthly_salary":5000,
    "yearly_salary":'' # something
}