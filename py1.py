# file one 
print("print from file one")
# def hello():
#     print("print function from file one")

if 1 == 1 :
    print('True')
    
else :
    print('False')

if __name__== "__main__" : # function running directly(execute in this page only => page script not module script)
    print("file one is running directly")
    def hello():      # write here but call in another place in the page
        print("print function from file one")
else :
    print("you are Not running file one directly")

hello()
    