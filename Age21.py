#------------------------------------------
# practical for Age full details
#################################
#------------------------------------------


# Input Age
age = int(input('what\'s your age?').strip())
print(age)
print(type(age))

# Get age in all time unit : 
months = age * 12
weeks = months * 4
days = age * 356
hours = days * 24
minutes = hours * 60
seconds = minutes *60
print('You are lived for :')
print(f' {months} Months')
print(f' {weeks:,} weeks')
print(f' {days:,} days')
print(f' {hours:,} hours')
print(f' {minutes:,} Minutes')
print(f' {seconds:,} Seconds')