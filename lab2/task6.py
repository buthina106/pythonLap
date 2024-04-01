sum = 0
count = 0

while True:
    inpt = input("Enter a number or (done) to exit: ")
    if inpt.lower() == "done":
        break
    try:
        number = float(inpt)
        sum += number
        count += 1
    except ValueError:
        print("Invalid input! Please enter a valid number or 'done' to exit.")

if count > 0:
    average = sum / count
    print(f"Total: {sum}")
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("No numbers")
