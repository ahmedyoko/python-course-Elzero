#.............................................
# Advanced lesson => Timming your code by Timeit
#.............................................
# Timeit => get execution time of code by running 1M time and give you minmal time
#          It used for performance by testing all functionality
# Timeit(stmt,setup,timer,number)
# Timeit(pass , pass , default , 1.000.000)Default values
#.............................................
# stmt => code you want to measure the execution time
# setup => setup done before the code execution 
# timer => the timer value  
# number => How many execution that will run
#.............................................

import timeit
# import random

# print(dir(timeit))

# how much time that operation take?
# print(timeit.timeit('"Elzero"* 1000'))# between quotes as it value of stmt
# name = "Elzero"
# print(name * 1000)
# print(timeit.timeit("name = 'Elzero'; name * 1000")) # between quotes as it value of stmt

# print(dir(random))
# print(random.randint(0,50))


# print(timeit.timeit(stmt="random.randint(0,50)", setup ="import random"))
print(timeit.repeat(stmt="random.randint(0,50)", setup ="import random", repeat=4))