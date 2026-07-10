def is_palindrome(text):

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

text = input("Enter text: ")

is_palindrome(text)
