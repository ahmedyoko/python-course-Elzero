# ----------------------------------
# ------CALCULATE AGE ADVANCED VERSION AND TRAINING
# ----------------------------------

# write a very beautiful note :
print('#' * 80)
print(' You can write the full unit or its first letter of the time unit '.center(80,'#'))
print('#' * 80)
# collect age data :
age = input('please write your age ').strip()

# collect time unit data :
unit = input(
    'please choose time unit : months , weeks , days  ').strip().lower()
# get time unit :
months = int(age) * 12
weeks = months * 4
days = int(age) * 356
if unit == 'months' or unit == 'm':
    print('you choosed the unit months')
    print(f'you lived for {months:,} Months')
elif unit == 'weeks' or unit == 'w':
    print('you choosed the unit weeks')
    print(f'you lived for {weeks:,} Weeks')
elif unit == 'days' or unit == 'd':
    print('you choosed the unit days')
    print(f'you lived for {days:,} days')
