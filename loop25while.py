#-------------------
# loop => while
#-------------------
# while condition_is_true :
#      code will run until condition become false
a = 0
while a < 10 :
    print(a)
    a += 1
else :
    print("loop is Done") # true become false
print("#"*50)

myf = ['os','ah','aj','so','no','ju','on','ha','em','ya']

print(len(myf)) # list length : number of its elements
a = 0
while a < len(myf) :
    # print(myf[a])
    print(f"#{str(a+1).zfill(3)} {myf[a]}")
    a += 1
else : 
    print('All friends printed to the screen')

print('#'*30)
print(myf[0])
print(myf[1])
print(myf[2])
print(myf[3])
print(myf[4])
print(myf[5])
print(myf[6])
print(myf[7])
print(myf[8])
print(myf[9])

#---------------------------
# simple bookmark manage
#---------------------------
 
# empty list to fill later
MyFavouriteWebs = []

# maximum allowed websites
maximumWebs = 5
while maximumWebs > 0 :
    # every time input web and added to the list and decrease the index by one to finite loop
    # input the new website
    web = input('website name without https://')

    # add the new website to the list
    MyFavouriteWebs.append(f"https:// {web.strip().lower()}")

    # decrease the index by one
    maximumWebs -= 1

    # print the added message
    print(f"website added , {maximumWebs} places left")

    # print the list 
    print(MyFavouriteWebs)
else :
    print('Book mark is full , you can not add more')

if len(MyFavouriteWebs) > 0 :
    # sort the list 
    MyFavouriteWebs.sort()
    index = 0
    while index < len(MyFavouriteWebs) :
        print(MyFavouriteWebs[index])
        index += 1

#-------------------------
# simple password guess
#-------------------------
tries = 4
mainpassword = 'osama@123'
inputpassword = input('write your password : ').lower()
while inputpassword != mainpassword :
    tries -= 1
    print(f'wrong password , {"last" if tries == 0 else tries} chance left')
    inputpassword = input('write your password : ').lower()
    if tries == 0 :
        print('All tries is finished')
        break
else :
    # the condition of while become false
    print('correct password')
print('the end of loop')



