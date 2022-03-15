def LengthFun(ArrLength, ArrStart):
    mylist = []
    mylist.append(int(ArrStart))
    for i in range(1, int(ArrLength)):
        mylist.append(int(ArrStart) + int(i))
    print(mylist)

ArrLength = input("please enter length: ")
ArrStart = input("please enter start number: ")
LengthFun(ArrLength, ArrStart)