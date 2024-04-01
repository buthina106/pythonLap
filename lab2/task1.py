# Write a function that accepts two arguments (length, start) to generate an array of a specific 
# length filled with integer numbers increased by one from start.

def generateArray(length:int,start:int):
    if isinstance(length,int) and isinstance(start,int):
        arr=[]
        for i in range(start,start+length):
            arr.append(i)
        return arr
    else:
        return "invalid data type" 

try:
    length = int(input("Please input a value for length "))
    start = int ( input ("Enter the start point ") )
    print(generateArray(length, start))
except ValueError:
    print("Please enter valid integers")


