file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
for row in data:
    print(row, end="")