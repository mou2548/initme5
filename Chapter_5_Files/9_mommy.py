file = input("Enter the filename : ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:]]

products = []
for row in rows:
    if int(row[1]) > 800:
        products.append(row[0])

txt = ", ".join(products)
print(f"Products priced over 800 baht : {txt}")