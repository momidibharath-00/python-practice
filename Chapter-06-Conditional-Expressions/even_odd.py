number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")

    if number % 4 == 0:
        print("It is divisible by 4.")
    else:
        print("It is not divisible by 4.")
else:
    print("Odd Number")
