#..................................
# file_handling :
#..................................
# the mode is one of the following :
# a -> append value in the file if exist , and make file if not exist
# r => read => it is the default of open for the file, if the file not exist =>gives error
# w => write value for the first time or overriding the exist one , andnmake the file if not exist
# x => create file , make error if file not exists
#....................................

# file = open('fileNameInItsPath','mode')
# file = open('ahmed.txt') # relative path by current or working directory
# file = open("D:\\python\\ahmed.txt")
# file = open(r"D:\python\ahmed.txt") # raw string to not consider \ as skip sequence
# file = open("D:/python/ahmed.txt")

print('#'*50)
# to know current working directory
import os   # operating system module or units
print(os.getcwd()) # parent current working directory of the system(if you open the file not open the folder)
print(os.path.dirname(os.path.abspath(__file__))) # current opened directory of specific file
# change current directory based on specific file path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
# print(os.path.abspath(__file__)) # current working directory + opened file name
print('*'*70)
# file read : (1- read metadata in form of data object)(2-read file content)
#............
# 1- read metadata in form of data object:
print('file_read')
myfile = open('sample3.txt') # read is the default => ('ahmed.txt'.'r')
# print(myfile) # print metadata of file in form of object not the content of the file
# print(myfile.name)
# print(myfile.mode)
# print(myfile.encoding)
# 2-read file content :
# default value is -1 => read all file 
# print(myfile.read())
# print(myfile.read(5)) # read 5 characters only
# print(myfile.readline(5)) # read 1st line , you can specify number of chch in that line .readline(6)
# print(myfile.readline()) # the rest of 1st line
# print(myfile.readline()) # read 2nd line
# print(myfile.readlines()) # all lines inform of list
print(myfile.readlines(50)) # limit the character inform of list

print('*'*50)
# for line in myfile :
#     print(line)
#     if line.startwith(7):
#         break
# close the file
myfile.close

print('*'*50)
# write a file :
myfile = open('hassan.txt','w')
myfile.write('hello from pyton file with love\nsecond line')
print('*'*50)
myfile = open(r'D:\python\fun.txt','w')
myfile.write('elzero_web_school\n'*1000)
print('*'*50)
# write a list by object.writelines()
mylist =['osama\n','ahmed\n','sayed\n'] # if I want them in next lines
# mylist =['osama','ahmed','sayed']
myfile = open('osama.txt','w')
myfile.writelines(mylist)
# myfile.writelines(','.join(mylist)) # if I want them in the same line with delimeter
myfile.write('hello\n')
myfile.write('osama')
#............................................................
print('how to make append? as write mode but make the mode a')
myfile = open('osama.txt','a')
myfile.write('  excellent')
