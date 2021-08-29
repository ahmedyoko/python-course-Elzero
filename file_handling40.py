#...................................
# file_handling => truncate
#...................................
# file = open('osama.txt','a')
# file.truncate(5)
# print(file.tell()) # the position of the cursor 'every enter = 2 character) don't forget to save in word text
file = open('osama.txt','r') # change the position of the begining of the read
file.seek(6)
print(file.read())

# to remove file :
import os
os.remove('ahmed.txt')# 