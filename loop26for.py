#---------------------------
# loop => for
#---------------------------
# for items in iterable_object :
#     do something with item
#---------------------------
# item is a variable create and call whenever you want
# item refer to the current positio , can run to the end position
# iterable_object => sequence [lists , tupules , sets , dictionaries , set of characters ...]

numbers = [1,2,3,4,5,6,7,8,9]
# number = 1
# while number <= 9 : 
#     print(number)
#     number += 1
#     if number == 10 :
#         break


# for more shortage use for loop 
for number in numbers :
    print(number)
    # print(number*17)
    if number % 2 == 0 :
        print(f'the number {number} is even')
    else :
        print(f"the number {number} is odd")
else :
    print('the loop is end')

myname = 'ahmed sayed'
for letter in myname :
    print(f'[{letter.upper()}]')


# range(start,end)
#-------------------------
myrange = range(1,100)
for number in myrange :
    print(number)

# Dictionary 
#-------------------
myskills = {
    "html" : '90%',
    "css" : '60%',
    "php" : '70%',
    "js" : '80%',
    "python" : '95%'
}
print(myskills['css'])
print(myskills.get('python'))

for skill in myskills :
    # print(skill)
    print(f'my progress in {skill} is : {myskills[skill]}')
    print(f'my progress in {skill} is : {myskills.get(skill)}')
