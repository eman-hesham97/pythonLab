def myNum():
    count = 0
    mysum = 0.0
    print("enter your numbers and after you finish enter 'done'")
    while True:
        myNumber = input("Enter a number: ")
        if myNumber == 'done':
            break
        num1 = int(myNumber)
        if myNumber.isnumeric():
            count = count + 1
            mysum = mysum + num1
        else:
            print("invalid input, enter a number or enter 'done'")

    print ('sum is: ', mysum)
    print ('\naverage is: ', mysum/count)

myNum()