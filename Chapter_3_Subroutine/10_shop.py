def sum_price():
    total = 0
    print("Menu\n1. T-shirt = 250\n2. Sneakers = 1200\n3. Jacket = 1500\n4. Hat = 300\n5. Gloves = 200")
    shirts = [250, 1200, 1500, 300, 200]
    for i in range(3):
        item = int(input("item number : "))
        amount = int(input("amount : "))
        discount_percent = int(input("discount : "))
        total += discount(shirts[item-1] * amount, discount_percent)
        
    print(f"total price : {total:.2f}")
    return total

def discount(price, discount_percent):
    return price * (100-discount_percent) / 100

def change(total, pay):
    change = int(pay-total)
    print(f"customer's change : {change}")

    moneys = [1000, 500, 100, 50, 20, 10, 5, 2]
    for money in moneys:
        if change // money > 0:
            print(f"change {money} : {change//money}")
            change %= money


total = sum_price()
pay = int(input("customer pay : "))
change(total, pay)