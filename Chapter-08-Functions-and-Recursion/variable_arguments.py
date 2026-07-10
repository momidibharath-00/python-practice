def add(*numbers):
    total = 0

    for num in numbers:
        total = total + num

    print("Sum =", total)

add(10, 20, 30, 40)
