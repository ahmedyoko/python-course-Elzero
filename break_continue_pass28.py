# ------------------------
# break , continue , pass
#-------------------------
numbers = [1,3,5,7,10,13,14,15,19]

#continue :
#.........
for number in numbers : # number member in numbers
    if number == 10 :
        continue # don't see it
    
    print(number)
print('#'*50)
# break = stop when you see it
numbers = [10,30,50,70,100,130,140,150,190]
for number in numbers : # number member in numbers
    if number == 100 :
        # break # stop when you see => see number before print and stop print
        print(number)
        break

print('#'*50)
# pass
for number in numbers : # number member in numbers
    if number == 100 :
       pass # to make pseudo body to ignore the condition in that moment
    print(number)
       

         
    