
# ● Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu

def longestSubstring(inpt):
    inpt = inpt.lower()
    longest = ""
    current = inpt[0]
    for char in inpt[1:]:
        if ord(char) >= ord(current[-1]):
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = char

    return longest

input_str = input("Enter a string: ")
longest_substring = longestSubstring(input_str)
print("Longest substring in alphabetical order is:", longest_substring)
