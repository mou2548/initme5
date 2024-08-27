file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

items = {}
for row in rows:
    if row[0] in items:
        items[row[0]] += 1
    else:
        items[row[0]] = 1
for key, value in items.items():
    print(f"{key} has {value} item(s).")