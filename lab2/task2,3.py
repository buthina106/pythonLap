# write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"
# 2)
def divisibleBy3_5(num):
    if isinstance(num,int):
        if num%3==0 and num%5==0:
            return "FizzBuzz"
        elif num%3==0:
            return "Fizz"
        elif num%5==0:
            return "Buzz"
        else:
            return "Not divisible on 3 or 5"
    else:
        return "not valid datatype"
    
try:
    num = int(input("Enter the Number: "))
    print(divisibleBy3_5(num))
except ValueError:
    print("Please enter a valid integer.")



# Write a function which has an input of a string from user then it
# will return the same string reversed.
# 3)
def reverse_string():
    inpt = input("Enter your string: ")
    reverse_str = inpt[::-1]
    return reverse_str

print(reverse_string())