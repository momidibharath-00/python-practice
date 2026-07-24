file = open("sample.txt", "r")

lines = file.readlines()

print("Lines:", len(lines))

file.close()
