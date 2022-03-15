import random
UsrName = input("enter your name: ")
wordsList = ['cat', 'dog', 'horse', 'ant']
chosenWord = random.choice(wordsList)
CharGuesses = ''
UsrTurns = 7
while UsrTurns > 0:
    failed = 0
    for char in chosenWord:
        if char in CharGuesses:
            print(char, end=" ")
        else:
            failed += 1
    if failed == 0:
        print(f"\nyou won {UsrName}")
        print("the word is: ", chosenWord)
        break
    guess = input(f"\n{UsrName}, guess a letter from the word: ")
    CharGuesses += guess
    if guess not in chosenWord:
        UsrTurns -= 1
        print(f"wrong guess {UsrName}, try again")
        if UsrTurns == 0:
            print(f"you lost {UsrName}")