#.................................................................
# OOP_Class_Attributes
#.................................................................
#.Class_Attributes => Attribute defines outside the constructor
#.................................................................


class member :  # if your in member => IT gives all instances to go to it directly
    not_Allowed_Names = ['Hell','Shit','Baloot'] # if begin with capital letter make error(class attribute => outside constructor)
    users_num = 0
    def __init__(self,first_name,middle_name,last_name,gender) :  # parameter to put argument in object method
        self.fname = first_name   
        self.mname = middle_name   
        self.lname = last_name
        self.gender = gender
        member.users_num += 1
    def full_name(self) :
        if self.fname in member.not_Allowed_Names :
            raise ValueError('Name not Allowed')
        else :
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
    def delete_users(self) :
        member.users_num -= 1
        return f"user {self.fname} Deleted"
print(member.users_num)

Member_one = member("Ahmed","Sayed","Ahmed","Male") # object or instance = class name method
Member_two = member("Maged","Abbas","Eltaweel","Male")
Member_three = member("Morad","AbdElhamid","ElNafrawy","Male")
# Member_four = member("Hell","Hassan","Habib","Male")
Member_four = member("Atef","Hassan","Habib","Male")
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
print(member.users_num)
print(Member_four.delete_users())
print(member.users_num)
print('*'*50)
# method of instance :
# print(dir(member))