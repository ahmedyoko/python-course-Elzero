a = "the light of the moon"
print(type(a))
print(len(a))
print(a*3)
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")
print(txt.strip(",.grt"))
print(x)


good = ",the moon is high ..xl"
a = good.strip(",.xl")
print(a)
z = a.title()
print(z)
x = a.upper()
print(x)
c = a.lower()
print(c)

n = " this is wonderful computer t90"
v = n.capitalize()
print(v)
c = n.title()
print(c)

a = "sound"
x = a.center(9,"#")
print(x)
z = a.rjust(9,"@")
print(z)
a = " the moon lighe is good"
list = a.split()
print(list)
b = '''every day 
I want to end some lesson
and I could
'''
c = b.splitlines()
print(c)
a = " the moon light is good"
print(a.count("the"))
print(a.count("the",5,16))

a = " the moon light is good"
print(a.swapcase())
print(a.index('the'))
print(a.find('new'))

z = a.replace("the", "that",1)
print(z)

a = "the\t moon\t light\t is\t good"
ex = a.expandtabs(5)
print(ex)

list = ['the','nice','boy']
string = " ".join(list)
print(string)
print('every day I notice %s' %(string))
print('every day I notice {:s}'.format(string))
print(f"every day I notice {string}")

a = 'the good news'
print(a.startswith('the'))
print(a.endswith('news'))
print(a.istitle())
print(a.isspace())
print(a.isidentifier())
print(a.isalpha())
print(a.isalnum())

