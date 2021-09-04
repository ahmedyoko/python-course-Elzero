#.................................................
# Advanced lesson => Add logging to your code  سجل الأشياء التي حدثت
#.................................................
# print out to console of file
# print logs of what happens
#.................................................
# Debug 
# Info  
# Warning  
# Error
# Critical 
#.................................................
# name => logging module give it to the default logger
#.................................................
# Basic config : 
#  level => level of severity
#  file name => file name and extension ملف تسجيل الاخطاء
#  mode of the file a => append
#  format => format for the log message 
#.................................................
# get logger => return a logger with the specified name 

import logging

# print(dir(logging))
# logging.basicConfig(filename="my_app.log",filemode="a", format="%(name)s") # name => root
# logging.critical(" this is critical message")


# logging.basicConfig(filename="my_app.log",filemode="a",
#                     format="%(asctime)s logger_Name= %(name)s %(levelname)s %(message)s")
# logging.critical(" this is critical message")
# # make more format
# logging.basicConfig(filename="my_app.log",filemode="a",format="(%(asctime)s)=> | logger_Name= %(name)s | %(levelname)s => %(message)s")
# logging.critical(" this is critical message")
# logging.basicConfig(filename="my_app.log",filemode="a",
#                     format="(%(asctime)s) | logger_Name= %(name)s | %(levelname)s => %(message)s")
# logging.error(" this is error message")
# logging.basicConfig(filename="my_app.log",filemode="a",
#                     format="(%(asctime)s) | logger_Name= %(name)s | %(levelname)s => %(message)s")
# logging.warning(" this is warning message")
# # datefmt =>date format 

logging.basicConfig(filename="my_app.log",filemode="a",
                            format="(%(asctime)s)=> | %(name)s | %(levelname)s => ' %(message)s'",
                            datefmt="%d - %B - %Y,%H:%M:%S")
my_logger = logging.getLogger("ahmed")
my_logger.warning(" this is warning message")# make the previous variable object to the warning
