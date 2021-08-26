#..........................
# Advanced dictionary loop
#..........................
myskills = {
    "html" : '90%',
    "css" : '60%',
    "php" : '70%',
    "js" : '80%',
    "python" : '95%'
}
print(myskills.items())
print('#'*50)
for skill in myskills :
    print(f'this is skill :{skill} and this is its progress {myskills[skill]}')
print('#'*50)
for key,value in myskills.items() :
    print(f'{key} => {value}')
print('#'*50)
myUltimateSkills = {  # key is html and css
    'html' : {        # value are consisting of child_key and child_value
        'main' : '80%',
        'pagjs' : '80%'
    },
    'css' : {
        'main' : '70%',
        'sass' : '70%'

    }
}
for key,value in myUltimateSkills.items():
    # print(f'{key} =>{value}')
    print(f'{key} => progress is')
    for child_key,child_value in value.items():
        print(f'-{child_key} ==> {child_value}')