def FizzBuzz(num):
    if int(num)%3 == 0 and int(num)%5 == 0:
        print("FizzBuzz")
    elif int(num)%5 == 0:
        print("Buzz")
    elif int(num)%3 == 0:
        print("Fizz")
    else:
        print("try another number")

num = input("please enter a number: ")
FizzBuzz(num)