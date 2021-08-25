#------------------------
# Membership operator :
#--------------------------
# in 
# not in
#--------------------
# String 
name = "osama"
print('s' in name)
print('a' in name)
print('A' in name)

print('#'*50)

#list
print('list')
friends = ['Ahmed','Sayed','Mahmoud']
print('Osama' in friends )
print('Ahmed' in friends )
print('Ahmed' not in friends )

# using in and not in with condition
print('condition')
CountriesOne = ['Egypt','KSA','Kwait','Bahrain']
CountriesOneDiscount = 80

CountriesTwo = ['USA','Italy']
CountriesTwoDiscount = 50

mycountry = 'Italy'

# if mycountry == 'Egypt' or mycountry == 'KSA' or mycountry == 'Kwait' or mycountry == 'Bahrain' :
#     print(f"hello you have a discount of ${CountriesOneDiscount}")
# else :
#     print('you have no discount')

# use membership instead of the list of countries 
if mycountry in CountriesOne :
    print(f"hello you have a discount of ${CountriesOneDiscount}")
elif mycountry in CountriesTwo :
    print('you have no discount')

print('#'*50)

# practical Membership Control :
#---------------------------------------

# list contain admins:
admins = ["Ahmed","Osama","Sameh","Manal","Manal","Rahma", "Mahmoud","Enas"]

# login
name = input('please Type your name :').strip().capitalize()

if name in admins :
    # print('you are admin')
    print(f"hello {name} welcome back")
    option = input('Delete or update your name :').strip().capitalize()
    print(option)
    if option == 'Update' or option == 'U' :
        theNewName = input('your new name : ')
        print(theNewName)
        admins[admins.index(name)] = theNewName
        print('the name updated')
        print(admins)
    elif option == 'Delete' or option == 'D' :
        # print(option)
        admins.remove(name)
        print(admins)
    else :
        print('wrong option')
else :
    # print('you are not admin')
    status = input('not admin , Add you , y or n ? ').strip().capitalize()
    if status == 'Yes' or status == 'Y' :
        admins.append(name)
        print(admins)
    else  :
        print('you are not added')
