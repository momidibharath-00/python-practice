file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Words:", len(words))

file.close()
