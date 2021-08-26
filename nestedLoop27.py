#-----------------
# loop => for 
# nested loop
#-----------------
peoples = ['osama','ahmed','sayed','ali']
skills = ['html','css','js']
for name in peoples : # outer loop
    print(name)
    for skill in skills : # inner loop
        print(skill)


peoples = {
    "osama" : {
        "html" : " 70%",
        "css" : "80%",
        "js" : "70%",
        } ,
    "ahmed" : {
        "html" : " 90%",
        "css" : "80%",
        "js" : "90%",
        } ,
    "sayed" : {
        "html" : "50 %",
        "css" : "60%",
        "js" : "60%",
        } 

        }

print(peoples['osama'])
print(peoples['osama']['css'])
for name in peoples :
    print(name)
    print(f'skill and progress for {name} is : {peoples[name]}') # give a whole column
    for skill in peoples[name] :
        # print(skill)
        print(f'{skill.upper()} => {peoples[name][skill]}') # give each row in column