#.............................
# builtin_function_map
#.............................
# 1-Map take a function and iterator
# 2- called map as it maps function in all elements
# 3- can be predifined function or lambda function
#..............................

# 1- use map with predifined function=> map(function,iterable)
print('use map with predifined function=> map(function,iterable)')
def formatText(text):
    return f'- {text.strip().capitalize()} -'
mytext = ['ahmed','sayed','ahmed']
# store in variable
myformatedText = map(formatText , mytext) # make function to all iterator(list)
# print(myformatedText)# <map object at 0x00000235C345B1F0> => address in computer memory
for name in myformatedText : # for extraction of formated iterator
    print(name)
# use map direct in loop without storing in variable
formatedData = ['osama','ahmed','sayed']
for name in map(formatText , formatedData ) : # for extraction of formated iterator
    print(name)

for name in list(map(formatText , formatedData )) : # for extraction of formated iterator in list
    print(name)
print(type(name))

print('*'*50)
#  2- use map with lambda function
print('use map with lambda function')

# def formatText(text):
#     return f'- {text.strip().capitalize()} -'
mytext = ['ahmed','sayed','ahmed']
for name in map(lambda text: f'- {text.strip().capitalize()} -', mytext ) :
    print(name)
for name in list(map(lambda text: f'- {text.strip().capitalize()} -', mytext )) :
    print(name)

