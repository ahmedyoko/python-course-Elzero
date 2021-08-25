#....................
#string methods:
################
#1-index(substring,start,end)
#2-find(substring,start,end)
#3-rjust,ljust
# 4-splitlines => return all lines in one list
#5-expandtabs : control the space of tabs 
# 6- istitle method :  to check boolean value
#7- isspace method : to checkout the space
#8-islower method : to checkout the lowercase
# 9- isidentifier method : to checkout if it is identifier as variable or not
# 10- isalpha method : to checkout if it is alphabetical characters or not
# 11- isalnum method : is short for alpha numerical
# 12- replace method => (old value , new value , count) count : number of times you want to replace
# 13- join method => (Iterable) join elements of lists or tuple in one string
#..........................



#1-index(substring,start,end) substring is mandatory



a = 'I love python'
print(a.index('p'))
print(a.index('p',2,10))
# print(a.index('p',2,5)) #through Error=> valueError: substring not found

#1-find(substring,start,end) substring is mandatory
a = 'I love python'
print(a.find('p'))
print(a.find('p',2,10))
print(a.find('p',2,5)) #-1


# 3-rjust,ljust(total character or width , fill character or type the default type is space)
c = 'osama'
print(c.rjust(9))
print(c.rjust(9,'#'))
c = 'osama'
print(c.ljust(9))
print(c.ljust(9,'#'))

#4-splitlines => return all lines in one list
e = '''first line
second line
third line
'''
print(e.splitlines())
print(type(e.splitlines()))

f = 'first line\nsecond line\nthird line'
print(f.splitlines())
print(type(f.splitlines()))

#5-expandtabs : control the space of tabs 
z = 'I\tlove\tpython'
print(z.expandtabs(2))

# 6- istitle method :  to check boolean value
a = ' I Love Python 3G'
b = ' I Love Python 3g'
print(a.istitle())
print(b.istitle())

#7- isspace method : to checkout the space
c = ' '
d = ''
print(c.isspace())
print(d.isspace())

#8-islower method : to checkout the lowercase
a = ' i love python'
v = 'I Love Python'
print(a.islower())
print(v.islower())
print('='*40)
# 9- isidentifier method : to checkout if it is identifier as variable or not 
a = 'osama_elzero'
b = 'osama_elzero100'
c = 'osama--elzero'
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())

# 10- isalpha method : to checkout if it is alphabetical characters or not
a = 'aAaaabBbbbbb'
x = 'aAaaabBbbbbb22121'
print(a.isalpha())
print(x.isalpha())

#11- isalnum method : is short for alpha numerical
a = 'aAaaabBbbbbb'
x = 'aAaaabBbbbbb22121'
print(a.isalnum())
print(x.isalnum())

# 12- replace method => (old value , new value , count) count : number of times you want to replace
a = ' Hello one two three one one'
print(a.replace('one','1'))
print(a.replace('one','1',1))

# 13- join method => (Iterable) join elements of lists or tuple in one string
#(separator.join(list or tuple))
mylist = ['osama','Mohammed','Elsayed']
print('-'.join(mylist))
print(' '.join(mylist))
print(' , '.join(mylist))
print(type(' , '.join(mylist)))