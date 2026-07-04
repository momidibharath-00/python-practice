marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")

    if marks >= 75:
        print("Distinction")
    else:
        print("First Class")
else:
    print("Fail")
