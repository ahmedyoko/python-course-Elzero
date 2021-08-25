#------------------------
#lists : 
#.........
#1- items enclosed in square brackets []
#2- ordered item and accessed by index
#3- mutable => Add , delete , Edit
#4- list items : are not unique
#5-list can have different data type
#------------------------

MyAwesomelist = ['one','two','one',1,2.5,True]
print(MyAwesomelist)
# index : output in the form of string or the type of element
print(MyAwesomelist[1])
print(MyAwesomelist[-1])
print(MyAwesomelist[-3])
print(type(MyAwesomelist[-3]))

#for slice : output in the form of list
print(MyAwesomelist[1:4]) #['two', 'one', 1]
print(MyAwesomelist[:4])#['one', 'two', 'one', 1]
print(MyAwesomelist[1:]) #['two', 'one', 1, 2.5, True]

#using steps of slice: [start: end: step]
print(MyAwesomelist[::1]) #the whole list
print(MyAwesomelist[::2])

# out of range error: when you write index does not exist
# print(MyAwesomelist[130])

#modify of elements in the list
#............................
#1-modify one element in the list
print(MyAwesomelist) #['one', 'two', 'one', 1, 2.5, True]
MyAwesomelist[1] = 2
print(MyAwesomelist[1]) #2
print(MyAwesomelist) # ['one', 2, 'one', 1, 2.5, True]

#2-modify more than one element in the list
MyAwesomelist = ['one','two','one',1,2.5,True]
MyAwesomelist[0:2] = [] # remove this elements => ['one', 1, 2.5, True]
print(MyAwesomelist)
MyAwesomelist = ['one','two','one',1,2.5,True]
MyAwesomelist[0:3] = ['A','B','C']
print(MyAwesomelist)
MyAwesomelist[0:3] = ['A'] #replace 3 elements by one element
print(MyAwesomelist)  # ['A', 1, 2.5, True]


