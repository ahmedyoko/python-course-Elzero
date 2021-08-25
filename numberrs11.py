#.....................
#numbers:
#1-integer
#2-float
#3- complex numbers : consist of 2 parts : 1- real part 2-imaginary part
#===============
#convert number types to each other:
#...........
#convert int to float and vice versa
#can convert from float and int to complex
#can not convert from complex to any type 
#.....................
#1-intever
print(type(-1))
print(type(0))
print(type(100))
print(type(-200))

#2-float
print(type(-1.2))
print(type(-200.00))
print(type(0.00))
print(type(0.123))
print(type(1.1))
print(type(9.2564654))

#3- complex numbers : consist of 2 parts : 1- real part 2-imaginary part
MyComplexNumber = 5+6j
print(type(5+6j))
print(type(MyComplexNumber))
print('My real part is : {}'.format(MyComplexNumber))
print('My real part is : {}'.format(MyComplexNumber.real))
print('Imaginary part is : {}'.format(MyComplexNumber.imag))


#convert int to float and vice versa
print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

#can not convert from complex to any type
print(10+9j)
print(int(10+9j))
