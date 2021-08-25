#---------------------------------------
# Type conversion : 
####################
#
#
#
#
#
#
#
#
#
#
#
#---------------------------------------

# by builtin function before primitive data type and string
a = 10 
b = 1.5 
c = 0
print(type(str(a)))
print(type(str(b)))
print(type(float(a)))
print(type(int(b)))
print(type(bool(a)))
print(type(bool(b)))
print(type(bool(c)))

print('='*50)
# for compound data type : 
# Tuple function :
a = 'osama' # string
b = [1,2.3,2,4] #list
c = {'A','B','C'} # set 
d = {'A' : 1 , 'B' : 2} #dict => make tuple of key only 

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))

print('='*50)
# list function : 
a = 'osama' # string
b = (1,2.3,2,4) #tuple
c = {'A','B','C'} # set 
d = {'A' : 1 , 'B' : 2} #dict => make tuple of key only 

print(list(a))
print(list(b))
print(list(c))
print(list(d))
print('='*50)
# set function :
print('Set') 
a = 'osama' # string
b = (1,2.3,2,4) #tuple
c = ['A','B','C'] # list
d = {'A' : 1 , 'B' : 2} #dict => make tuple of key only 

print(set(a))
print(set(b))
print(set(c))
print(set(d))
print('='*50)
# dict function : 
print('Dict from only nested list and tupule') 
# a = 'osama' # string can not form dict
# b = (1,2.3,2,4) #tuple => must be nested tuple(each item is subtuple) which contain key and values
b = (('A' , 1),('B' , 2))
c = [['one',1],['two',2]] # list as tuple
# d ={{'A',1}  , {'B',2 }}  #set => TypeError: unhashable type: 'set'

# print(dict(a))
print(dict(b))
print(dict(c))
# print(dict(d))
