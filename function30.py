#........................
# Function :
# def : reusable block of code to do a task
# run only when you call it
# accept elements to deal with called parameters
# can do task without returning data 
# can do task with returning data
# main purpose of creating function is to prevent DRY(don't repeat yourself)
# after calling function => accept elements called Arguments
# Builtin function and user defined function
# a function is for all teams and all Apps
#......................................

# make a function
def function_name():
    print('hello python from inside function')
# call a function
function_name()
# make a function return data and take you to use it as you want
def function1_name():
    return 'hello el-maghreb and breakfast after fasting' # return not printed if you call function
# call a function itself make nothing as it return data , but I can store or make another function on it
function1_name()
print(function1_name())
dataFrom_function1_name = function1_name()
print(dataFrom_function1_name + ' great work')