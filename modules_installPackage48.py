#.....................................
# modules_install External Package
#.....................................
# [1] module vs package
# [2] External package download from the internet
# [3] install packag by package manager => in python called pip
# [4] pip install package and its dependencies
# [5] modules list "https://docs.python.org/3/modindex.html"
# [6] package and module directory "https://pypi.org"
# [7] pip manual "https://pip.pypa.io/en/stable/reference/pip_install/"
#
#.....................................

# odule vs package
# module a file contain set of function to perform an idea 
# package => has set of module (it may contain million package for language so it place external)
# dependencies => package depend on another package

 
print('command in typed in terminal')
print('to know the version of package manager => pip --version')
print(' to know the package installed by package manager => pip list')
print('to install the package or module => pip install package or module name')
print('you can install more than module => pip install module1 module2 module3')
print('you can determine the release => pip install module==1.0.4')
print('to upgrade any library => pip install name_of_library --upgrade')
print('if any problem with upgrade => pip install --user name_of_library --upgrade')

print('*'*50)
print('import the module you have installed')
# to fix the module can not be seen by the visual studio code => ctrl + p =>  >reload => choose window reload

import termcolor
import pyfiglet

# print(dir(pyfiglet)) # to know the function in this module
print(pyfiglet.figlet_format('Elzero'))
print(termcolor.colored('Elzero', color='yellow'))

print('*'*50)
print(termcolor.colored(pyfiglet.figlet_format('Elzero'), color='yellow'))

