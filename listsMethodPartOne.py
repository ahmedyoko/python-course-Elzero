#.............................................
#lists method:
#.................
#1-Append() : add an element at the end of the list
#2-extend method : make a new list from 2 lists as concatenate
#3-remove() : remove first element matched to its paramter from the list
#4- Sort() : to order the elements,sort has parameter reverse , it is by default False , and I can make it True
# 5- reverse() : to reverse the position of elments of list
# 6- clear() : remove all item from the list
# 7- copy() : return a shallow copy of the list
# 8- count() : count how many times the element repeat in the list
# 9-index() : position of element in the list
# 10-insert(index,object) : insert the object before the index 
# 11- pop(index)
#........................

#1-Append() : add an element at the end of the list , whatever element type accepted , and even accept list as an element
MyFriends = ['osama','mohamed','alaa']
OldFriends = ['haitham','sameh','ali']
MyFriends.append('ahmed')
MyFriends.append(1)
MyFriends.append(1.5)
MyFriends.append(True)
MyFriends.append(OldFriends) #['osama', 'mohamed', 'alaa', 'ahmed', 1, 1.5, True, ['haitham', 'sameh', 'ali']]
print(MyFriends)
print(MyFriends[3])
print(MyFriends[6])
print(MyFriends[7])
print(MyFriends[7][2])
print('#'*50)
#2-extend method : make a new list from 2 lists as concatenate
a = [1,2,3]
b= ['A','B','C']
a.extend(b)
print(a)
c = ['one','two']
a.extend(c)
print(a)
print('#'*50)
#3-remove() : remove first element matched to its paramter from the list
x = [1,2,3,4,5 , 'osama', True,'osama','osama']
x.remove('osama')
print(x)
print('#'*50)
#4- Sort() : to order the elements,sort has parameter reverse , it is by default False , and I can make it True
#it require only one type of element either number or string
a = [50,1,30,-10,23]
# a.sort()
a.sort(reverse=False)
print(a)
a.sort(reverse=True)
print(a)
print('#'*50)
# 5- reverse() : to reverse the position of elments of list
x = [1,5,2,4,8,3,'ali',5]
x.reverse()
print(x)
print('#'*50)
# 6- clear() : remove all item from the list
a = [1,2,3,4]
a.clear()
print(a)
print('#'*50)
# 7- copy() : return a shallow copy of the list
b = [1,2,3,4]
c = b.copy()
print(b) #Main list
print(c) #copied list
b.append(5)
print(b) #Main list
print(c) #copied list
print('#'*50)
# 8- count() : count how many times the element repeat in the list
x = [1,2,3,1,4,5,1,2,1,3,14,1]
print(x.count(1))
print('#'*50)
# 9-index() : position of element in the list
a = ['osama','ahmed','mona','ramy','mohamed']
print(a.index('ramy'))
print('#'*50)
# 10-insert(index,object) : insert the object before the index 
a = [1,2,3,4,5,'A','B']
a.insert(0,'one')
print(a)
a.insert(-1,'one')
print(a)
print('#'*50)
# 11- pop(index)
x = [1,2,3,4,5,'A','B']
print(x.pop(-1)) #B     