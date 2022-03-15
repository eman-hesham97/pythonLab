strInput = input("please enter a string: ")
def longestStr(strInput):
    strOutput = ""
    strCompare = ""
    for char in strInput:
        if strCompare == "":
            strCompare = char
        elif strCompare[-1]<= char:
            strCompare = strCompare + char
        elif strCompare[-1]>char:
            if len(strOutput) < len(strCompare):
                strOutput = strCompare
                strCompare = char
            else:
                strCompare=char
    if (len(strCompare) > len(strOutput)):
        strOutput = strCompare
    print(f"the longest substring is: {strOutput}")

longestStr(strInput)