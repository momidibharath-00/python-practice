number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

elif number < 0:
    print("Negative Number")

else:
    print("Zero")
