#...................................................
# error_And_exception raising :
#...................................................
# [1] Exception is runing time error reporting mechanism
# [2] give you message to understand the problem
# [3] traceback => look for the code error in this line
# [4] have types (syntax error,Indexerror,Keyerror,..etc)
# [5] Exception list (https://docs.python.org/3/library/exceptions.html)
# [6] raise keyword used to raise your own exceptions
#...................................................

# determine the error in my app => number less than zero
# x = -10
# if x < 0 :
#     # this is error in your app and must handling so use raise exception to raise my own exception
#     raise Exception(f'the number {x} is less than zero')
#     # exception => make break , so anything after it not printed
#     print('not printed as the error stop printing')
# else :
#     print(f'{x} is good number')

y = 'osama'
if type(y) != int :
    raise ValueError('only number allowed')
