#------------------------------
# Dictionary :
##############
# 1- Items enclosed in curly braces
# 2- Items consist of keys and values
# 3- dictionary key is immutable (number,string,tuple)so that list not allowed 
# 4- dictionary value can be any data type
# 5- dictionary key must be unique
# 6- dictionary as set not ordered , you can access Items only by its key
# 7- to access dict items in one dimension dict : dict[keys] or dict.get(key)
# 8- to print all keys : dict.keys()
# 9- to print all values : dict.values()
# 10- to access dict items in 2 dimensions dict : dict[key of 1st dict][key of the 2nd dict]
###########################
# method : 
#################
# 1- len method : len(dict) or len(dict[key])
# 2- clear method : to remove all elements
# 3- update method : to add new items to your dict or more than one items=> dict.update({key:value})
# 4- copy method : shallow copy not affected by the change in the parent or original one
# 5-keys and values methods :
# 6-setdefault method : is a search
# 7- popitems : show last item added to the dict (before version 3.7 show random item)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#...................................

# Dictionary :
user = {
    'name' : 'ahmed',
    'age' : 45 ,
    'nationality' : 'egyptian',
    'skills' : ['HtMl','css'],
    'rating' : 10.5,
    ('a','b') : 'sections',
    1 : "door"


}
print(user)
print(user['nationality'])
print(user.get('nationality')) # use get method : dictionayName.get(key)

# to print all keys : dictionayName.keys()
print(user.keys())
# to print all : dictionayName.values()
print(user.values())
print('#'*50)

# Two Dimensional dictionary : 
language = {
    'one' : {
        'name' : 'HTML',
        "progress" : '80%'
    },
    'two' : {
        'name' : 'css',
        "progress" : '70%'
    },
    'three' : {
        'name' : 'js',
        "progress" : '70%'
    }
}

# dictionary length
print(language)
print(language['one'])
print(language['three']['progress'])
print(len(language))
print(len(language['two']))

# to make multiple dictionary in one dictionary , make them as a value for keys
frameworkone = {
     'name' : 'js-vue',
        "progress" : '80%'
}
frameworktwo = {
     'name' : 'react-js',
        "progress" : '80%'
}
frameworkthree = {
     'name' : 'angular',
        "progress" : '80%'
}
allframework = {
    'one' : frameworkone ,
    'two' : frameworktwo,
    'three' : frameworkthree
}
print(allframework )

# 2- clear method : to remove all elements
user = {
    'name' : 'ahmed'
}
print(user)
user.clear()
print(user)
print('#'*40)


# 3- update method : to add new items to your dict or more than one items=> dict.update({key:value})
# simple way to add by assignment
user = {
    'name' : 'ahmed'
}
user['age'] = 45
print(user)
user.update({'country':'egypt'})
print(user)
user.update({'skills':'vet','experience':10 , 11 : 11})
print(user)
print('#'*40)

# 4- copy method : shallow copy not affected by the change in the parent or original one
main = {
    'name': 'osama'
    }
b = main.copy()
print(b)
main.update({'skils':'fighting'})
print(main)
print(b)
print('#'*40)


# 5-keys and values methods :
main = {
    'name': 'osama'
    }
print(main.keys())
print(main.values())
print('#'*40)

# 6-setdefault method : is a search
main = {
    'name': 'osama'
    }
print(main.setdefault('name'))
print(main.setdefault('name','osama'))
print(main.setdefault('name','ahmed'))
print(main.setdefault('age',36))
print(main.setdefault('skil'))
print('#'*40)

# 7- popitems : show last item added to the dict (before version 3.7 show random item)
member = { 
    'name' : 'osama',
    'skill' : 'ps4'
}
print(member)
print(member.popitem())
member.update({'age':36})
print(member.popitem())
print('#'*40)

# 8- Items method : to return whole item in the list and each item in tuple form
view = { 
    'name' : 'osama',
    'skill' : 'xbox'
}
allItems = view.items()
print(view)
view.update({'age':36})
view['country'] = 'Egypt'
print(allItems)
print('#'*40)

# 9- Fromkeys method : make dict from more than one keys and one value
a = ('keyone','keytwo','keythree')
b = 'x'
print(dict.fromkeys(a,b)) # dict.fromkeys(iterable,b) 
