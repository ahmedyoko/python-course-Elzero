#.............................................................
# regular_expression_python => re module search and findall
#.............................................................
# search(pattern,string)=> a string for match and return first match only
# findall(pattern,string)=> return a list of all matches and empty list if no matches
#..............................................................
# split(pattern,string,Maxsplit)=> Return a list of elements splited in each match
# sub(pattern,replace,string,replacecount)=> replace matches with what you want
#..............................................................
# group Training and flags
#..............................................................
# Email pattern => ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
#..............................................................


# module for seach is re (regular expression module)
import re
# print(dir(re))
# search method
print("search method")
my_search = re.search('[A-Z]','OsamaElzero') # (pattern,string)
print(my_search) # <re.Match object; span=(0, 1), match='O'>  span =>position of searched letter[0-1]
# print(dir(my_search))
print(my_search.span())
print(my_search.string)
print('*'*50)
my_search = re.search(r'[A-Z]{2}','OOsamaElzero')
print(my_search.group()) # group method => for the 2 successive matches
print('*'*50)
is_email = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$","os@osama.com")
if is_email :
    print("this is a valid email")
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())
else :
    print("This is not a Valid Email")
print('*'*50)
print('example for findall')
email_input = input("please write your Email : ")
# search = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$",email_input) # if grouping => output ['com']
search = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info$",email_input)# remove group to handle as one group
empty_list = []
if search != [] :
    empty_list.append(search)
    print('Email Added')
else :
    print('Invalid Email')
for email in empty_list :
    print(email)

print('*'*50)
# split(pattern,string,Maxsplit)=> Return a list of elements splited in each match
print('Split Method')
string_one = "I Love Python programming Language"
split_one = re.split(r"\s",string_one)
print(split_one)
split_one = re.split(r"\s",string_one,1)
print(split_one)
print('*'*50)
string_two = "How-To_writ_A_very-Good-Article"
split_two = re.split(r"-",string_two)
print(split_two)
split_two = re.split(r"-|_",string_two)
print(split_two)
print('*'*50)
# get word from URL
for word in split_two :
    print(word)
# to make a counter for it 
for word in enumerate(split_two,1) :
    print(word)
# to format the counter
for counter,word in enumerate(split_two,1) :
    print(f'The Word Number : {counter} => {word.lower()}')
# to neglect the article
for counter,word in enumerate(split_two,1) :
    if len(word) == 1 :
        continue
    print(f'The Word Number : {counter} => {word.lower()}')

print('*'*50)
print('sub Method')
# sub(pattern,replace,string,replacecount)=> replace matches with what you want
My_string = "I Love Python"
print(re.sub(r"\s","-", My_string))
print('*'*50)
print(re.sub(r"\s","-", My_string,1))
print('#'*50)
# group Training and flags
my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
search = re.search(r"(https?://)(www.)?(\w+)\.(\w+)(:\d+)?/?(\w+).+",my_web)
# print(dir(search)) # the content of search method
print(search.group()) # https://www.elzero.org:8080/category.php?article=105?name=how-to-do
print(search.group(1))
print('separator between group and groups')
print(search.groups()) #('https://', 'www.', 'elzero.org', ':8080', 'category')
for group in search.groups() : 
    print(group)

print('*'*50)
print('print group of website and its name')
print(f'Proctocol : {search.group(1)}')
print(f'Sub Domain : {search.group(2)}')
print(f'Domain : {search.group(3)}')
print(f'Top Level Domain : {search.group(4)}')
print(f'Port : {search.group(5)}')
print(f'Query : {search.group(6)}')
print('*'*50)
# in pythex website :
# between your regular expression and your regular string , there is :
# 1- Ignorecase => to ignore case of letter between expression and string_two
# 2- Dotall => to match any character as dot + \n
# 3- Verbose => to ignore comment in expression
# 4- MULTILINE => to match multline even if you determine begining and end(^line$)
print('where is the flag written?')
search = re.search(r"(https?://)(www.)?(\w+)\.(\w+)(:\d+)?/?(\w+).+",my_web,re.MULTILINE)
search = re.search(r"(https?://)(www.)?(\w+)\.(\w+)(:\d+)?/?(\w+).+",my_web,re.DOTALL)
search = re.search(r"(https?://)(www.)?(\w+)\.(\w+)(:\d+)?/?(\w+).+",my_web,re.IGNORECASE)
search = re.search(r"(https?://)(www.)?(\w+)\.(\w+)(:\d+)?/?(\w+).+",my_web,re.VERBOSE)

