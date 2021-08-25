# ...................................
# --Variable
# -----------------
# syntax => [variable name] [ assignment operator][value] 
#special characters : can not be start or within the variable
# .....................................
#python is dynamic language => you can change data type during runtime
# c is static language=>you can not do that
# ......................
x = 10
x = "hello"
print(x)
# to know the preserved words make this function
help("keywords")
# how to assign
a,b, c = 1, 2, 3
print(a)
print(b)
print(c)
# ...................
# Escape sequence characters:
# -----------------
# \b => backspace => remove one letter before it
# \ => escape to newline => print the words in the same line
# to print back slashe between double quotes add another back slash
# to escape single quote
# to escape double quote
# \n => go to second line[named line feed character]
# \r => Carriage Return =>replace start character to the character after it
# \t => horizontal tab 
# \xhh=> character hex value
# ............................
# backspace
print("hello\bworld")
# escape to newline
print("hello\
    world")
# to print back slashe between double quotes add another back slash
print("I love back slashe \\")
# to escape single quote
print('I love single Quotes \'Test\'')
# to escape double quote
print("I love double Quotes \"Test\" ")
# \n => go to second line[named line feed character]
print("hello\nworld")
# \r => Carriage Return =>replace  the character after it to start character
print('123456\rabcd') 
# \t => horizontal tab 
print("hello\tworld")
# \xhh=> character hex value
print('\x4F\x73')
