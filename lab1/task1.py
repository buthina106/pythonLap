
# Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string.
# 1)

vowels = 'aeiou'
count = 0
input_str = input("Please enter a string:")
while not input_str.replace(" ", "").isalpha():
    input_str = input("Please enter a valid string:")

for letter in input_str.lower():
    if letter in vowels:
        count += 1
print(f"Number of vowels in \"{input_str}\" = {count}")


# Fill an array of 5 elements from the user, Sort it in descending
# and ascending orders then display the output.
# 2)

arr = []

for i in range(5):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

arr_asc = sorted(arr)
print("Sorted Ascending:", arr_asc)

arr_desc = sorted(arr, reverse=True)
print("Sorted Descending:", arr_desc)


# Write a program that prints the number of times the string 'iti'occurs in anystring
# 3)

input_str=input("Enter your string ")

while not input_str.replace(" ", "").isalpha():
    input_str = input("Please enter a valid string:")

print("Number of of iti = "+str(input_str.count('iti')))


# Write a program that remove all vowels from the input word and
# generate a brief version of it.
# 4)

vowels = 'aeiouAEIOU'
result = ''
numOfVowels = 0

input_word = input("Enter your word: ")

while not input_word.strip() or not input_word.isalpha():
    input_word = input("Please enter a valid string:")

for ch in input_word:
    if ch in vowels:
        numOfVowels += 1
    else:
        result += ch

print(f"Number of vowels removed: {numOfVowels}")
print(f"Word without vowels: {result}")


# Write a program that prints the locations of "i" character in any
# string you added.
# 5)

string = input("Enter your string: ")
while not string.strip() or not string.isalpha():
    string = input("Please enter a valid string:")

char_to_find = input("Enter the character to find: ")
while len(char_to_find) != 1 or not char_to_find.isalpha():
    char_to_find = input("Please enter one char :")

positions = []
for i in range(len(string)):
        if string[i] == char_to_find:
            positions.append(i)

print(f"Positions of '{char_to_find}' in '{string}': {positions}")


# Write a program that generate a multiplication table from 1 to the
# number passed.
# 6)
  
inpt=""
while(not inpt.isdigit()):
    inpt=input("Enter a number ")
num=int(inpt)
multiTable=[]
for i in range(1,num+1) :
    entity=[]
    for j in range(1,i+1):
        entity.append(i*j)
    multiTable.append(entity)
print(multiTable)

#Write a program that build a Mario pyramid like below:
# 7)

inpt = ""
while not inpt.isdigit():
    inpt = input("Enter a number: ") 
num = int(inpt)

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)
