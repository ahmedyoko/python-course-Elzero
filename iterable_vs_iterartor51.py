#.....................................
# iterable_vs_iterartor
#.....................................
# Iterable : 
# [1] object contain data , that can be iterated upon
# [2] example ( list , tuple , set , dictionary)
#.....................................
# iterator : يعيد العنصر
# [1] object used to iterate over iterable using next method and return one element at a time
# [2] generate iterator from iterable by using iter()method
# [3] for loop called Iter()method behind the scene
# [4] give stopIteration if there is no next element
#.....................................

# iterable
string = "osama"
list = [1,2,3,4]
for letter in string :
    # print(letter)
    print(letter , end=" ")

print("*"*50)
for num in list :
    print(num ,end=" ")
print("*"*50)

myIterator = iter(string)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# for loop consist of : iter and next method and break after last element
for num in iter(list) : 
    print(num ,end=" ")