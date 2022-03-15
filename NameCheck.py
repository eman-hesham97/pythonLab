import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checkInfo(UsrName, UsrMail):
    print(f"username: {UsrName} \n mail: {UsrMail}")

UsrName = input("please enter your name: ")
if not UsrName:
    UsrName = input("Empty Name, please enter your name: ")
UsrMail = input("please enter your mail: ")
if (re.fullmatch(regex, UsrMail)):
    checkInfo(UsrName, UsrMail)
else:
    print("Invalid Email")

