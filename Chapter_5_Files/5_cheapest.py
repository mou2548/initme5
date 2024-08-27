file = input("Enter the filename : ")
product = input("Enter the product type you want to buy : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

cheapest = 999999
brand = ''
for row in rows:
    if row[0] == product and int(row[2]) < cheapest:
        cheapest = int(row[2])
        brand = row[1]
        
print(f"{brand} is the cheapest and costs {cheapest} baht.")