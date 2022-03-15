myList = []
print("please enter 5 strings and press enter after each one: ")
for i in range(5):
    ele = (input())
    if ele.isnumeric():
        print("please enter a string")
    else:
        myList.append(ele)
myList.sort()
print("Your list sorted ascendingly: " ,myList)
myList.sort(reverse=True)
print("Your list sorted descendingly: ", myList)