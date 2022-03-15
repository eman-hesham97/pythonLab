myList = []
print("enter a number to display it's multiplication table: ")
num = int(input())
for i in range(1 , num+1):
    smallList = []
    for j in range(1 , i+1):
        smallList.append(i*j)
    myList.append(smallList)
print(myList)