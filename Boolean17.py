#-----------------------------------
# Boolean :
# ##########
# to know if your code is true or false
# 2 constant values => True and False
# True values
# False values
#.................................................
# Boolean operator(logical operators) :
#######################################
# comparison operator
# logical operator (and or not)
# Assignment operator( = += -= *= /= //= %= **=) to assign a value to a variable
# comparison operator (==  !=  >  <  >=   <= )
#
#
#
#-----------------------------------

name = ''
print(name.isspace())
name = ' '
print(name.isspace())
print('='*50)

print(100>200)
print(100>90)
print('='*50)

# bool : builtin function , its output either True or False
#True values
print(bool('string'))
print(bool(100))
print(bool(100.5))
print(bool([1,2,3,4]))
print(bool(True))

print('='*50)
# False values
print(bool(0)) #zero
print(bool("")) #empty data
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(False))

print('='*50)

# logical operator : and or not
age = 30
country = 'Egypt'
rank = 10
print(age > 16 and country =='Egypt' and rank > 0)
print(age > 16 and country =='ksa' and rank > 0)
print('='*50)
print(age > 16 or country =='ksa')
print(age > 40 or country =='ksa' or rank > 20)
print('='*50)

print(age > 16)
print( not age > 16)
print('='*50)

#boolean operator : add value to variable
x = 10 # var one 
y = 20 # var two
# z = x + y
# var one = self [operator +]var two
# x = x + y
# var one [operator +]=  var two
x += y 
print(x)
x -= y
print(x)
print('='*50)

# comparison operator (==  !=  >  <  >=   <= )
# equal 
print(100 == 100)
print(100 == 200)
print(100 == 100.00)
print('='*50)
# not equal 
print(100 != 100)
print(100 != 200)
print(100 != 100.00)
print('='*50)
# greater than 
print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40.00)
print('='*50)
# less than 
print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print('='*50)
# greater than or equal
print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 > 40.00)
print('='*50)
# less than or equal
print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)






