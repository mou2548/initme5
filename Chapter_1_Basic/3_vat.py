price = float(input("summary price : "))
print(f"food : {price/107*100:.3f}")
print(f"vat : {price-(price/107*100):.3f}")