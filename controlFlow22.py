#-------------------------------
#--------Control Flow----------
#--------if,Elif,Else----------
#-------Make Decision------------
#-------------------------------
# 1-brief control follow by logical operator :
# 2- Nested if :
# 3- Ternary conditional operator : 
#-------------------------------

from stringFormat9 import Age


uName = 'osama'
cName = 'python'
cprice = 100
cdiscount = 30
print(f'Hello {uName} the course \"{cName}\" price is ${cprice - cdiscount } ')
print('='*50)
uName = 'osama'
ucountry = 'Egypt'
cName = 'python'
cprice = 100

if ucountry == 'Egypt':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 80 }') 
print('='*50)
uName = 'osama'
ucountry = 'KSA'
cName = 'python'
cprice = 100

if ucountry == 'Egypt':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 80 }') 
elif ucountry == 'KSA':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 60 }') 
else:
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 30 }')
    print('='*40)
# 1-brief control follow by logical operator :
#.........................................
print('brief')
if ucountry == 'Egypt' or ucountry == 'KSA' or ucountry == 'Qatar':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 80 }') 
elif ucountry == 'Kuwait' or ucountry == 'Bahrain':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 60 }') 
else:
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 30 }')
    print('='*40)
    
print('='*40)
#===================
#2- Nested if :
#------------------
print('Nested if')
uName = 'osama'
isStudent = 'yes'
cName = 'python'
cprice = 100
cdiscount = 30
if ucountry == 'Egypt' or ucountry == 'KSA' or ucountry == 'Qatar':
     
     if isStudent == 'yes':
        print(f'Hello {uName} because you are from {ucountry} and student')
        print(f'the course \"{cName}\" price is : ${cprice - 90 }')
     else:
        print(f'Hello {uName} because you are from {ucountry}')
        print(f'the course \"{cName}\" price is : ${cprice - 80 }') 
elif ucountry == 'Kuwait' or ucountry == 'Bahrain':
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 60 }') 
else:
    print(f'Hello {uName} because you are from {ucountry}')
    print(f'the course \"{cName}\" price is : ${cprice - 30 }')
print('='*40)

# 3- Ternary conditional operator : 
#......................................
print('Ternary conditional operator')
Country = "Egypt"
if Country == "Egypt":
        print(f'The weather in this {Country} is 15')
elif Country == "KSA":
        print(f'The weather in this {Country} is 30')
else:
        print('your country doesn\'in the list')


MovieRate = 18
Age = 16
if Age < 18 :
    print('the movie is not Good for you') # condition if true 
else :
    print('the Movie is for your age') # condition if false

# syntax :
# condition if true | If condition | else | condition if false
print('the movie is not Good for you' if Age < MovieRate else 'the Movie is for your age')
