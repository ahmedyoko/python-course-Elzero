#--------------------------
# User Input :
##############
#--------------------------


fname = input("what\'s your first name?")
mname = input("what\'s your middle name?")
lname = input("what\'s your last name?")
fname = fname.strip().capitalize()  # chain function           
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()
print(f'Hello {fname} {mname:.1s} {lname} Happy to see you') # to avoid spaces use strip method
# print(f'Hello {fname} {mname.strip().capitalize():.1s} {lname} Happy to see you') # to avoid spaces use strip method
# print(f'Hello {fname.strip()} {mname.strip()} {lname.strip()} Happy to see you') # to avoid spaces use strip method
print('hello {:s} {:.1s} {:s} Happy new year'.format(fname,mname,lname))