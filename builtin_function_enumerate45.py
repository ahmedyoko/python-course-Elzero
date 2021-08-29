#........................................ 
# builtin_function :
#........................................ 
# enumerate()=> add a counter
# help()
# reversed()
#........................................ 

# enumerate(iterable , start=0) iterable is obligatory
skills = ['html','css','js','python']
# skillsWithCounter = enumerate(skills)
skillsWithCounter = enumerate(skills,20)
print(type(skillsWithCounter))
for skill in skillsWithCounter :
    print(skill)
print('.'*50)
print('counter')
skills = ['html','css','js','python']
skillsWithCounter = enumerate(skills,30)
for counter,skill in skillsWithCounter :
    print(f'{counter} - {skill}')

print('.'*50)
print('help function') #=> print(help(function))
# print(help(print))

print('.'*50)
print('reversed function => reverses the iterable')
mmystring = 'elzero'
print(reversed(mmystring)) # => make it as object to loop <reversed object at 0x000002859ADA8CD0>
for letter in reversed(mmystring) :
    print(letter)