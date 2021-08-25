#.........................
#Tuple :
########
#1- are Items enclosed in parantheses
#2- you can remove the paranthese if you want
#3- ordered item , you can use index to access the item
#4- Immutable
#5- can be different data types
#6- Items not unique
#7-operator used in string and list used in tuple
# 8- tuple with one element with or without parantheses , the item must followed by commma
# 9-Tuple concatenation
# 10 - Tuple , list , string repeat (*)
# 11- count method : to count an item in tuple
# 12 - Index method to know the position of the Item
#13- Tuple destruct or unpack : distribute tuple items to equal number of variable
#.........................

#Tuple syntax and type test:
MyAwesomeTupleOne = ('osama','ahmed')
MyAwesomeTupleTwo = 'osama','ahmed'

print(MyAwesomeTupleOne)
print(MyAwesomeTupleTwo)
print(type(MyAwesomeTupleOne))
print(type(MyAwesomeTupleTwo))

#Tuple Indexing : 
MyAwesomeTupleThree = (1,2,3,4,5)
print(MyAwesomeTupleThree[0])
print(MyAwesomeTupleThree[-1])
print(MyAwesomeTupleThree[3])

# #Tuple assign value : 
# MyAwesomeTupleThree[1] = 90
# print(MyAwesomeTupleThree) #TypeError: 'tuple' object does not support item assignment

# not unique and different data types : 
a = ('osama','osama',1,2,3,4,100.5,True)
print(a)

# Tuple with one element : 
a = ('osama')
b = 'osama'
print(type(a)) #<class 'str'>
print(type(b)) #<class 'str'>
# to differentiate between tuple and string but comma after the item
a = ('osama',)
b = 'osama',
print(type(a)) #<class 'tuple'>
print(type(b)) #<class 'tuple'>
print(len(a)) #<class 'tuple'>
print(len(b)) #<class 'tuple'>

# 9-Tuple concatenation
a = (1,2,3,4)
b = (5,6)
c = a + b
print(a + b)
print(c)
# print()

# 10 - Tuple , list , string repeat (*)
MyString = ('osama')
Mylist = [1,2]
MyTuple = ('A','B')

print(MyString*6) 
print(Mylist*6) 
print(MyTuple*6) 

# 11- count method : to count an item in tuple
a = (1,3,5,8 , 7 , 3 ,8,9)
print(a.count(8))

# 12 - Index method to know the position of the Item
a = (1,3,5,8 , 7 , 3 ,8,9)
print('the position of indexing of 8 is : {}'.format(a.index(3)))                               
print('the position of indexing of 8 is : {:d}'.format(a.index(3)))                               
print(f'the position of indexing of 8 is : {a.index(3)}')   

# 13- Tuple destruct or unpack : distribute tuple items to equal number of variable
a = ('A','B','C')
x,y,z = a
print(x)
print(y)
print(z)

# if there more item in tuple and I want certain item use under score in adjacent variable to ignore
a = ('A','B',3,'C')
x,y,_,z = a
print(x)
print(y)
print(z)                         