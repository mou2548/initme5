file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

total = 0
for row in rows:
    total += float(row[1])
total /= len(rows)
print(f"Average score of all students is {total:.2f}")