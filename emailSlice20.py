#------------------------------------------
# Email Slice : practical for Email Slice
##############
#
#
#------------------------------------------


TheName = input('what\'s your name?').strip().capitalize()
TheEmail = input('what\'s your email?').strip()
print('Hello {} your email is {} '.format(TheName,TheEmail))
print(f'Hello {TheName} your email is {TheEmail} ')
theUserName = TheEmail[:TheEmail.index('@')]
# thewebsite =  TheEmail[TheEmail.index('@'):]  # website is the domain
thewebsite =  TheEmail[TheEmail.index('@') +1:]  # to not print @ we add one to the index
print(f'your user name is {theUserName} \nyour website is {thewebsite}')
print('your user name is {}  \nyour Domain is {} '.format(theUserName,thewebsite))

# email = 'osama@el_zero.org'
# print(email[:5])
# print(email[0])
# print(email.index('@'))
# print(email[:email.index('@')])