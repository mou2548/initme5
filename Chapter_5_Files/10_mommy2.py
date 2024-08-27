file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

products = []
for row in rows:
    if int(row[2]) < 10:
        products.append(row[0])

txt = ", ".join(products)
print(f"Products with stock less than 10 items : {txt}")