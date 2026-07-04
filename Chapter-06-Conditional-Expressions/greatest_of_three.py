A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A > B and A > C:
    print("Greatest number is:", A)
elif B > A and B > C:
    print("Greatest number is:", B)
else:
    print("Greatest number is:", C)
