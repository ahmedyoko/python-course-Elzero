# string method 
#######################
# method is the function of object or dotted function to do something
#1-len => length or the number of the characters
#2-strip method : to remove space from the right and left , rstrip : for right only, lstrip : for left only
#3-Title method : convert first letter to capital case and convert any letter after number to capital case
#4-capitalize method
#5-zfill method : needs number of characters , it is short for zero fill
#6-upper and lower method
#7-split method : separate object into its elements in the form of list, by default it separate by space
#8-center method: make the name at the center of a set of wanted characters => center(total character or width,fill chch)
#9-count method : to count the argument  occurs between parathesis , it has mandatory argument : counted text
#10-swapcase method : change the state of letters
#11-startswith method : means is , It takes argument as count
#12-endswith method : the same as previous
#.............................
# 1-len => length or the number of the characters
a = " I love python"
b = "    I love python    "
print(len(a))
print(len(b))
# method is the function of object or dotted function to do something
# strip method : to remove space from the right and left , rstrip : for right only, lstrip : for left only 
b = "    I love python    "
print(b.strip())
print(b.rstrip())
print(b.lstrip())
print(len(b.lstrip()))

# don't forget to put the character between 2 quotes , otherwise it will give you syntaxError
b = "###I love python####"
print(b.strip("#"))
print(b.rstrip("#"))
print(b.lstrip("#"))
print(len(b.lstrip("#")))

b = "@#@#@#I love python@#@#@#@#"
print(b.strip("@#"))
print(b.rstrip("@#"))
print(b.lstrip("@#"))
print(len(b.lstrip("@#")))

#Title method : convert first letter to capital case and convert any letter after number to capital case
a = " I love 3d Graphics and 2g Technology and python"
print(a.title())
#capitalize method
a = " I love 3d Graphics and 2g Technology and python"
print(a.capitalize())

#zfill method :  to make the same pattern of number or make all number has the same character by using zero 
#zfill method : needs number of characters , it is short for zero fill
a, b , c = "1" , '11' , '111'
print(a)
print(b)
print(c)
print(a.zfill(3))

#upper and lower method
a = "osama"
b = "ahmed"
print(a.upper())
print(b.lower())

#split method : separate object into its elements in the form of list, by default it separate by space
a = 'I love pthon and PHP'
print(a.split())
a = 'I-love-pthon-and-PHP'
print(a.split())
#split accept 2 values : separator as dash , max split : make split to number maximum and make all other in one element
a = 'I-love-pthon-and-PHP'
print(a.split('-'))
a = 'I-love-pthon-and-PHP'
print(a.split('-',2))
#rsplit the same but the direction rlt
a = 'I-love-pthon-and-PHP'
print(a.rsplit('-',2))
#center method: make the name at the center of a set of wanted characters => center(total character or width,fill chch)
a = 'osama'
print(a.center(9)) # by default make osama at the center of spaces
print(a.center(9,'#')) # make osama at the center of hashes
print(a.center(9,'@')) # make osama at the center of @
# count method : to count the argument  occurs between parathesis , it has mandatory argument : counted text
f = ' I love python and php because php is easy'
print(f.count('php'))
# count has optional argument : start and end
print(f.count('php', 0 , 25))

# swapcase method : change the state of letters
a = ' I Love Python'
b = ' i loVE pythoN'
print(a.swapcase())
print(b.swapcase())

# startswith method : means is , It takes argument as count
a = 'I Love Python'
print(a.startswith('I'))
print(a.startswith('P',7,12))
#endswith method : the same as previous
a = 'I Love Python'
print(a.endswith('n'))
print(a.endswith('e',2,6)) # begin with zero index and end not included



