import random

words =["apple","bannana","orange","mango","ٍStrawberry","melon"]
randomIdx = random.randint(0, len(words) - 1)
theWord = words[randomIdx].lower()  
guessingWord = "_" * len(theWord)
numOfTries = 7
guessedChars = []

print(f"please guss the word: {guessingWord}")

while numOfTries > 0 and guessingWord != theWord:
    print(f"\n==== You have {numOfTries} tries left ====")
    inpt = input("Guess a character: ").lower()  

    if len(inpt) != 1 or not inpt.isalpha():
        print("invalid input please enter one char.")
        continue

    if inpt in guessedChars:
        print("aready guess please enter another char")
        continue

    guessedChars.append(inpt)

    positions = [i for i, letter in enumerate(theWord) if letter == inpt]

    if len(positions) == 0:
        print("Wrong guess")
        numOfTries -= 1
    else:
        for pos in positions:
            guessingWord = guessingWord[:pos] + inpt + guessingWord[pos + 1:]

    print(f"Guessed so far: {guessingWord}")

if guessingWord == theWord:
    print("Congrats! You guessed the word correctly")
else:
    print(f"Sorry, you have used all your tries. The word was '{theWord}'.")
