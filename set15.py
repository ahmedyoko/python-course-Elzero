#...................................
#Set :
#########
# 1- set Item enclosed in curly braces
# 2- not ordered item so not indexed
# 3- indexing and slicing can not be done
# 4- its items may be immutable data types(numbers,string,tuple)not list and dictionary=> as it mutable
# 5- Item is unique
#.............
# Set method
##############
# 1- clear method : for removal all elements
# 2- union method : to unify more than one sets
# 3- add method : to add one  element
# 4- copy method : shallow copy not deep copy mean separate copies 
# 5- remove method : remove one element from the set
# 6- discard method : remove one element from the set
# 7- pop method : pop out random elements
# 8- update method : as union
# 9 - difference method : the output is the items distinguish the first set
# 10 - difference_update method : the output is the items distinguish the first set
# 11- intersection method : the output is the item present in two sets only and no update or change to original set
# 12- intersection_update method : the output is the item present in two sets only and update or change to original set
# 13- symmetric_difference : the difference between 2 sets
# 14- symmetric_difference_update : the difference between 2 sets
# 3- isdisjoint method : no same elements or items between 2 sets
#.................................................
#Boolean method :
###############
# 1- issuperset method : is the second set included(subset)in the original set?
# 2- issbset method : is the original set part of second set?
#...................................

# 2- not ordered item so not indexed
MyAwesomeSet = {'Osama','Ahmed',100}
print(MyAwesomeSet)
print(MyAwesomeSet)
# print(MyAwesomeSet[1]) #TypeError: 'set' object is not subscriptable 


# 4- has immutable data types
# MySet = {'Osama',1.5,100,True,[1,2,3]}
# print(MySet) #TypeError: unhashable type: 'list'
MySet = {'Osama',1.5,100,True,(1,2,3)}
print(MySet)
print('#'*50)

# 5- Item is unique
a = {1,1,'osama','osama',2}  
print(a)

# Set method
##############
# 1- clear method : for removal all elements
a = {2,4,5,7,4}
print(a.clear()) # None
print(a) #set()
print('#'*50)
# 2- union method : to unify more than one sets
a = {1,2,3,5}
b = {'A','V','B'}
c = {'a','v','b'}
print(a | b | c)
print(a.union(b,c))

# 3- add method : to add one  element
a = {1,2,3,4}
a.add(5)
a.add(6)
print(a)
# print(a.add(5,6)) #TypeError: set.add() takes exactly one argument (2 given)
print('#'*50)
# 4- copy method : shallow copy not deep copy mean separate copies 
a = {1,2,3,5,'a'}
f = a.copy()
print(f)

a.add('b')
print(a)
print(f)
print('#'*50)
# 5- remove method : remove one element from the set
a = {1,2,3,5,'a',6}
a.remove('a')
# a.remove(10) #KeyError: 10
print(a)


# 6- discard method : remove one element from the set
a = {1,2,3,5,'a',6 ,'b'}
a.discard(10) 
print(a)
print('#'*50)
# 7- pop method : pop out random elements
i = {'a','b',True,1,2,3,4,5}
print(i.pop())
print('#'*50)
# 8- update method : as union(I can enter list items as a several items)
a = {1,2,3,4,'z'}
v = {'a','b','z',1,5,6}
a.update(['html','css'])
a.update(v)
print(a)
print('#'*50)
# 9 - difference method : the output is the items distinguish the first set
x = {1,2,3,4}
y = {1,2,'A','B'}
print(x)
print(x.difference(y))
print(x-y)

print('='*40) #separator

# 10 - difference_update method : the output is the items distinguish the first set
x = {1,2,3,4}
y = {1,2,'A','B'}
print(x)
x.difference_update(y)
print(x) # remove the repeated elements from the original set
print('='*40) #separator
# 11- intersection method : the output is the item present in two sets only and no update or change to original set
e = {1,2,3,4,'x','osama'}
f = {'osama','x',2}
print(e)
print(e.intersection(f)) # e&f
print(e&f)
print(e)
print('='*40) #separator
# 12- intersection_update method : the output is the item present in two sets only and update or change to original set
e = {1,2,3,4,'x','osama'}
f = {'osama','x',2}
print(e)
e.intersection_update(f) 
print(e)
print('#'*40)

# 13- symmetric_difference : the difference between 2 sets
i = {1,2,3,4,'A','B'}
j = {'osama','x',1,2,4}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i^j)
print(i)
print('#'*40)

# 14- symmetric_difference_update : the difference between 2 sets
i = {1,2,3,4,'A','B'}
j = {'osama','x',1,2,4}
print(i)
i.symmetric_difference_update(j)
print(i)
print('#'*50)

# 1- issuperset method : is the second set included(subset)in the original set?
a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}
print(a.issuperset(b)) #True
print(a.issuperset(c)) #False
print('#'*50)

# 2- issubset method : is the original set part of second set?
d = {1,2,3,4}
e = {1,2,3}
f = {1,2,3,4,5}
print(d.issubset(e))#False
print(d.issubset(f)) # True
print('#'*50)

# 3- isdisjoint method : no same elements or items between 2 sets
g = {1,2,3,4}
h = {1,2,3}
j = {10,11,12}
print(g.isdisjoint(h)) # False
print(g.isdisjoint(j)) # True

