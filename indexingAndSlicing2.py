# All Data in python is Object
# Object contains elements
# Every elements has its own index
#python use zero based indexing (Index start from zero) 
# use square Brackets to access elements
# Enable accessing parts of string , Tuples or lists
# ----------------------------------
# indexing (Access single Item)
myString = "I love python"
print(myString[0])
print(myString[9])
print(myString[-1])
# slicing (Access Multiple sequence Items)
# syntax : [start : end] or [start : end : steps] end not included
print(myString[3:5])
print(myString[:10])  #if start not mentioned , it mens start from zero
print(myString[10:])  #if end not mentioned , it mens go to the end
print(myString[:])  #if both start and end not mentioned , it mens print full data
# Steps
print(myString[::1]) # this the default
print(myString[::2])
