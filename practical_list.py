list = [1,2,3,4,'a','s','d','f']
print(list[0])
print(list[3])
print(list[-1])
print(list[-3])

print(list[:])
print(list[:-1])
print(list[:len(list)-2])
print(list[1:5])
print(list[len(list)-6:])

print(len(list))

list[7]='q'
print(list)

list.append(8)
list.append(['z','x'])
list.append(['n','m'])
print(list)

list.extend(['z','x','n','m'])
print(list)

list.remove(list[2])
print(list)
list.remove(list[3])
print(list)
list = ['a','s','d','f']
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.clear()
print(list)
list = ['a','s','d','f']
list.insert(1,4)
print(list)
list.insert(-1,-1)
print(list)

print(list.count('a'))
list.pop(2)
print(list.pop(2))
list = ['a','s','d','f']
print(list.index('d'))

string = ' '.join(list)
print(string)
list = string.split()
print(list)