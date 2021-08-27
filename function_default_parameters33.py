#.................................
# function => Default parameters
#.................................
# default value either in all parameters or the two parameters from right or last parameters only 

def say_hello(name,age,country= "unknown") :
    print(f"hello {name} your age is {age} and your country is {country}")

say_hello("ahmed",45)
say_hello("morad",13 ,'moraco')

print('#'*60)
def say_hello(name,age ="unknown",country= "unknown") :
    print(f"hello {name} your age is {age} and your country is {country}")

say_hello("ahmed",45)
say_hello("morad",13 ,'moraco')
say_hello("ali")
print('#'*60)
def say_hello(name="unknown",age ="unknown",country= "unknown") :
    print(f"hello {name} your age is {age} and your country is {country}")

say_hello("ahmed",45)
say_hello("morad",13 ,'moraco')
say_hello("ali")
say_hello()


