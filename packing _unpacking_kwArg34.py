#............................................
# packing _unpacking_kwArg(key word argument)
#............................................



def show_skills(*skills):
    print(type(skills))
    for skill in skills :
        print(f'{skill}')
show_skills('html','css','js')
print('#'*50)
myskills = {'html' : '70%','css' :'70%','js' :'80%'}
def show_skills(**skills): # key word dictionary by this second astrisk
    print(type(skills))
    for skill,value in skills.items() :
        print(f'{skill} => {value}')
show_skills(html = '70%',css ='70%',js ='80%')
show_skills(**myskills)
print('#'*50)
myskills = {'html' : '70%','css' :'70%','js' :'80%','Mysql' :'85%'}
mytuple = ('html','css','perl')
def show_skills(name ,*skills , **skillswithprogress): # key word dictionary by this second astrisk
    print(f'- hello {name} \nskills without progress is :')
    for skill in skills :
        print(f'{skill}')
    print('skills with progress is :')
    for skill_key,skill_value in skillswithprogress.items() :
        print(f'{skill_key} => {skill_value}')
show_skills('osama','python',html = '70%',css ='70%',js ='80%')
show_skills('hassan', *mytuple)
show_skills('ahmed', *mytuple,**myskills)
