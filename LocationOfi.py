strInp = input("Enter a string:")
myChar = 'i'
myList = []
for pos,char in enumerate(strInp):
    if(char == myChar):
        myList.append(pos)
print("Places where 'i' was written: ", myList)