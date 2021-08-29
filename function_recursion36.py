#...............................
# function_recursion
# what is the mean of recursion
#...............................

# test word
# x = "wwwwoooorrrrlllldddd"
# print(x[1:])

def cleanword(word) :
    if len(word) == 1 :
        return word
    if word[0] == word[1] :         # wwwwoooorrrrlllldddd
        return cleanword(word[1:]) # remove first letter and begin with second and try function again as loop of function
    return word  # return indentation as if as all thing under if recursive
print(cleanword('wwwwoooorrrrlllldddd'))

print('#'*50)
def cleanword(word) :
    print(f'print start function {word}') # 'wwwwoooorrrrlllldddd' 
    if len(word) == 1 :
        return word                       # 'wwwwoooorrrrlllldddd'
    if word[0] == word[1] :
        print(f'print before condition {word}')  # 'wwwwoooorrrrlllldddd'       
        return cleanword(word[1:]) # remove repeated letter=> word[0] and repeat till finish the repeatation
    print(f'print before return {word}')
    return word[0] + cleanword(word[1:]) # return an repeated letter and make a condition in repeated one
    #stash [world] put first letter of the repeated letters in stash and clean the rest 
print(cleanword('wwwwoooorrrrlllldddd'))

print('#'*50)