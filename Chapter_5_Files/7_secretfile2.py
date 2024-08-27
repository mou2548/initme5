file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()

i = 0
for line in data:
    if i % 2 == 0:
        print(line.upper(), end="")
    else:
        print(line.lower(), end="")
    i += 1
print()