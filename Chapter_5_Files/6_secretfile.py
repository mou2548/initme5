file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip("\n").split() for i in data]

count = 0
for row in rows:
    for word in row:
        if word == 'Python':
            count += 1
print(f"The word 'Python' appears in the file {count} time(s).")