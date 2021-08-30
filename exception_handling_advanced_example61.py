#...........................................
#        exception_handling_advanced_examples
#           try | except | else | finally
#....................................................
the_file = None
the_tries = 5
while the_tries > 0 :
    print(f'{the_tries} tries left')
    the_tries -= 1
else :
    print('All tries are done')
print('*'*50)
the_file = None
the_tries = 5
while the_tries > 0 :
    try : # try to open the file
        print('enter the file name with the absolute path to open')
        print(f'you have {the_tries} tries left')
        print('Example => D:\python\file\yourfile.extension')
        file_name_and_path = input('file name => : ').strip().lower()
        the_file = open(file_name_and_path,'r')
        print(the_file.read())
        break
    except FileNotFoundError:
        print('the file not found please be sure the name is valid')
        the_tries -= 1
    except :
        print('error happens')
    finally :
        if the_file is not None :
            the_file.close()
            print('the file is closed')
else :
    print('All tries are done')