file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

info = {}
for row in rows:
    if row[0] in info:
        info[row[0]] += int(row[2])
    else:
        info[row[0]] = int(row[2])

for key, value in info.items():
    if value == max(info.values()):
        print(f"Highest material usage on {key} uses {value} units.")