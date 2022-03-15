strInp = input("Enter a string:")
vowel = set("aeiouAEIOU")
newStr = strInp
for i in strInp:
      if i in vowel:
            newStr = newStr.replace(i,"")
print("Your string without vowels = ", newStr)