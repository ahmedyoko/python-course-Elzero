#..................................................
# Numpy => Compare Data Location and Type
#..................................................

import numpy as np

my_list = [1,2,3,4,5]
my_array = np.array([1,2,3,4,5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print('*'*50)
# Memory location by identifier => id
print("list elements position")
print(id(my_list[0])) # not after each other
print(id(my_list[1]))
print("array elements position")
print(id(my_array[0])) # after each other
print(id(my_array[1]))

print('*'*50)
my_list_of_data = [1,2,'A','B',True,10,50]
my_array_of_data = np.array([1,2,'A','B',True,10,50])

print(my_list_of_data) # heterogenous data type => [1,2,'A','B',True,10,50]
print(my_array_of_data) # homogenous data type => strings ['1' '2' 'A' 'B' 'True' '10' '50']

print(type(my_list_of_data[0])) # <class 'int'>
print(type(my_array_of_data[0])) # <class 'numpy.str_'>