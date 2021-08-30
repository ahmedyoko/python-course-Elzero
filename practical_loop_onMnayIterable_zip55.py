#.......................................................
# ..practical_loop_onMnayIterators with_zip
#.......................................................
# zip() return a zip object contain all object
# zip() the length is the length of the lowest object
#.......................................................
from typing import Tuple


list1 = [1,2,3,4,5]
list2 = ['A','B']
ultimatelist = zip(list1,list2)
print(ultimatelist) # <zip object at 0x000002102C2D6B00>
for item in ultimatelist :
    print(item)
print('*'*50)
list1 = [1,2,3,4,5]
list2 = ['A','B','C']
ultimatelist = zip(list1,list2)
print(ultimatelist) # <zip object at 0x000002102C2D6B00>
for item in ultimatelist :
    print(item)
print('*'*50)
list1 = [1,2,3,4,5]
list2 = ['A','B','C']

for item1,item2 in zip(list1,list2) :
    print('list one item =>',item1)
    print('list two item =>',item2)
print('*'*50)
list1 = [1,2,3,4,5]
list2 = ['A','B','C']
Tuple = ('man','woman','girl','boy')
dict = {'name':'ahmed','age':45,'country':'egypt'}
for item1,item2,item3,item4 in zip(list1,list2,Tuple,dict) :
    print('list one item =>',item1)
    print('list two item =>',item2)
    print('tuple one item =>',item3)
    print('dict one key =>',item4 ,'value =>',dict[item4])