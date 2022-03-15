strInp = input("Enter a string:")
vowel = set("aeiouAEIOU")
vowelCount = 0
for i in strInp:
      if i in vowel:
            vowelCount = vowelCount + 1
print("Number of vowels in string = ", vowelCount)