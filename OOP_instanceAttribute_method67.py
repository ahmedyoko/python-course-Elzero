#......................................................
# OOP => Instance attribute and method:
#......................................................
#   self => point to Instance Created From Class 
#   Instance Attribute => defined inside constructor
#......................................................
# Instance Method :
# [1] Take self Parameter Which Point To Instance Created From Class
# [2] Can Have More Than One Parameter Like Any Function
# [3] Can Freely Access Attributes and Methods In The Same Object
# [4] Can Access The Class Itself
#......................................................

class member : # name of class which create instance or object
    def __init__(self) :  # self => means (the adjective of the constructor or Method) created from class itself=> method craeator 
        self.name = 'osama'  # attribute

Member_one = member() # object or instance = class name method
Member_two = member()
Member_three = member()
Member_four = member()

# print(dir(Member_one)) # you will find name attribute which you created
# to Access the Attribute => print(instance.attribute)
print(Member_one.name)
print('*'*50)
class member :
    def __init__(self,first_name) :  # parameter to put argument in object method
        self.name = first_name   

Member_one = member("Ahmed") # object or instance = class name method
Member_two = member("Maged")
Member_three = member("Morad")
Member_four = member("Ali")


print(Member_one.name)
print(Member_two.name)
print(Member_three.name)
print(Member_four.name)
print('*'*50)
class member :
    def __init__(self,first_name,middle_name,last_name) :  # parameter to put argument in object method
        self.fname = first_name   
        self.mname = middle_name   
        self.lname = last_name   

Member_one = member("Ahmed","Sayed","Ahmed") # object or instance = class name method
Member_two = member("Maged","Abbas","Eltaweel")
Member_three = member("Morad","AbdElhamid","ElNafrawy")
Member_four = member("Ali","Hassan","Habib")
print('*'*50)
class member :
    def __init__(self,first_name,middle_name,last_name) :  # parameter to put argument in object method
        self.fname = first_name   
        self.mname = middle_name   
        self.lname = last_name
    def full_name(self) :
        return f"Hello Mr : {self.fname} {self.mname} {self.lname} "

Member_one = member("Ahmed","Sayed","Ahmed") # object or instance = class name method
Member_two = member("Maged","Abbas","Eltaweel")
Member_three = member("Morad","AbdElhamid","ElNafrawy")
Member_four = member("Ali","Hassan","Habib")


# print(Member_one.fname,Member_one.mname,Member_one.lname)
# print(Member_two.fname,Member_two.mname,Member_two.lname)
# print(Member_three.fname,Member_three.mname,Member_three.lname)
# print(Member_four.fname,Member_four.mname,Member_four.lname)

print(Member_one.full_name()) # instance or object . method
print('*'*50)
class member :
    def __init__(self,first_name,middle_name,last_name,gender) :  # parameter to put argument in object method
        self.fname = first_name   
        self.mname = middle_name   
        self.lname = last_name
        self.gender = gender
    def full_name(self) :
        return f"{self.fname} {self.mname} {self.lname} "
    def name_with_title(self) :
        if self.gender == "Male" :
            return f"Hello Mr : {self.fname}  "
        elif self.gender == "Female" :
            return f"Hello Miss : {self.fname}  "
        else :
            return f"Hello : {self.fname}"

Member_one = member("Ahmed","Sayed","Ahmed","Male") # object or instance = class name method
Member_two = member("Maged","Abbas","Eltaweel","Male")
Member_three = member("Morad","AbdElhamid","ElNafrawy","Male")
Member_four = member("Ali","Hassan","Habib","Male")
Member_five = member("Mona","Hassan","Habib","Female")


# print(Member_one.fname,Member_one.mname,Member_one.lname)
# print(Member_two.fname,Member_two.mname,Member_two.lname)
# print(Member_three.fname,Member_three.mname,Member_three.lname)
# print(Member_four.fname,Member_four.mname,Member_four.lname)

print(Member_one.full_name()) # instance or object . method
print(Member_two.full_name())
print(Member_three.full_name())
print(Member_four.full_name())
print(Member_five.name_with_title())

print('*'*50)
class member :
    def __init__(self,first_name,middle_name,last_name,gender) :  # parameter to put argument in object method
        self.fname = first_name   
        self.mname = middle_name   
        self.lname = last_name
        self.gender = gender
    def full_name(self) :
        return f"{self.fname} {self.mname} {self.lname} "
    def name_with_title(self) :
        if self.gender == "Male" :
            return f"Hello Mr : {self.fname}  "
        elif self.gender == "Female" :
            return f"Hello Miss : {self.fname}  "
        else :
            return f"Hello : {self.fname}"
    def get_all_info(self) :
        return f"{self.name_with_title()},your full name is : {self.full_name()} "

Member_one = member("Ahmed","Sayed","Ahmed","Male") # object or instance = class name method
Member_two = member("Maged","Abbas","Eltaweel","Male")
Member_three = member("Morad","AbdElhamid","ElNafrawy","Male")
Member_four = member("Ali","Hassan","Habib","Male")
Member_five = member("Mona","Hassan","Habib","Female")


# print(Member_one.fname,Member_one.mname,Member_one.lname)
# print(Member_two.fname,Member_two.mname,Member_two.lname)
# print(Member_three.fname,Member_three.mname,Member_three.lname)
# print(Member_four.fname,Member_four.mname,Member_four.lname)

print(Member_one.get_all_info()) # instance or object . method
print(Member_two.get_all_info())
print(Member_three.get_all_info())
print(Member_four.get_all_info())
print(Member_five.get_all_info())
print('*'*50)
# method of instance :
# print(dir(member))
