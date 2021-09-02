#..........................................
# OOP => Polymorphism
#..........................................
# method change thier action according to type of data
#..........................................


n1 = 10
n2 = 20
print(n1+n2)

s1 = "Hello"
s2 = "Python"
print(s1 + " " + s2)

print(len([1,2,3,4,5,6]))
print(len("osama Elzero"))
print(len({"key_one":1,"key_two":2}))

# print("*"*50)
# class A :
#     def do_something(self) :
#         print("From Class A")
#         raise NotImplementedError("Derived class must implement this method")
# class B(A) :
#     pass

# class C(A) :
#     pass
# my_instance = B()
# my_instance.do_something()
print("*"*50)
class A :
    def do_something(self) :
        print("From Class A")
        raise NotImplementedError("Derived class must implement this method")
class B(A) :
    def do_something(self) :
        print("From Class B")

class C(A) :
    def do_something(self) :
        print("From Class C")
my_instance = B()
my_instance.do_something()