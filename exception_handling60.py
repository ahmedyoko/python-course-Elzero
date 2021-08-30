#....................................................
#..............Exception handling....................
#           try | except | else | finally
#....................................................
# try => test the code
# Except => handle the error
#....................................................
# else => if no errors
# finally => run the code 
#....................................................

# number = int(input('write your age'))
# print(number)

try :   # test code means if number ==int
    number = int(input('write your age : '))
    print('this is integer => from try ')
except :  # handle the error if found
    print('this is not integer')
else :
    print('this is integer => from else ')
finally :
    print('print finally whatever happens')

print('*'*50)
try :         # is that devision acceptable 
    # print(10/0)
    # print(x)
    print(int('hello'))
except ZeroDivisionError:  # identify the type of error
    print('can not divide')
except NameError :        # if you found the output variable not previously identified
    print('Identifier not found')
except ValueError :
    print('value error elzero')
except :
    print('error happens')
