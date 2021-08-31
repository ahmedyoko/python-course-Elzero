#........................................
# regular_expression :
#........................................
# [1] sequence of character => define the search pattern
# [2] it is general concept in all language
# [3] used in [ credit card validation , Ip address validation , email validation]
# [4] test regex (https://pythex.org)
# [5] characters sheet (https://www.debuggex.com/cheatsheet/regex/python)=> name of website :Python Regex Cheatsheet 
# [6] https:regex101.com
#........................................
# Regular Expression => Quantifiers
#........................................
#   *           0 or more
#   +           1 or more
#   ?           0 or 1
#   {2}         exactly 2
#   {2,5}       between 2 and 5
#   {2,}        2 or more
#   {,5}        up to 5
#........................................
# Assertion:
# [1]          ^  start of string
# [2]          $  end of string
#........................................
# Match an Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# [A-z0-9\.]+@[A-z0-9]+\.{com}
# ^[A-z0-9\.]+@[A-z0-9]+\.{com|net|org|info}$
#...........................................
# logical : or and escaping :
# [1]         | or
# [2]         \ escape special character
# [3]         () separate groups
# example :
# 1- HTML
# 2- CSS
# 3- PHP

# 1) HTML
# 2) CSS
# 3) PHP

# 1> HTML
# 2> CSS
# 3> PHP
# (\d-|\d\)|\d>) (\w+)

# example 
# 012 3456 954
# 011 5423 (123)

# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))

# example of websites pattern :
# http://www.elzero.net
# http://elzero.org
# https://elzerocourses.com

# ^(https?://)(www\.)?(\w+\.)(net|org|com)$