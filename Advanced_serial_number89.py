#...............................................
# Advanced Lesson :
# Generate random serial number
#...............................................

import string
import random

# print(dir(string))
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def make_serial(count) :
    all_char = string.ascii_letters + string.digits
    print(all_char)
    char_count = len(all_char)
    print(char_count)
    serial_list = []
    while count > 0 :
        random_number = random.randint(0,char_count - 1) # number of presented characters 62-1 as it begin with zero
        random_character = all_char[random_number]
        serial_list.append(random_character)
        count -= 1
    # print(serial_list)
    print(" ".join(serial_list))

make_serial(10)