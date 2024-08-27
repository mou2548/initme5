def sum_price():
    total = 0
    print("Menu\n1. Latte = 40\n2. Espresso = 45\n3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60")
    coffees = [40, 45, 50, 55, 60]
    for i in range(3):
        coffee = int(input("coffee : "))
        amount = int(input("amount : "))
        total += coffees[coffee-1] * amount

    print(f"total price : {total}")
    return total

def change(total, pay):
    change = pay-total
    print(f"customer's change : {change}")

    moneys = [1000, 500, 100, 50, 20, 10, 5]
    for money in moneys:
        if change // money > 0:
            print(f"change {money} : {change//money}")
            change %= money


total = sum_price()
pay = int(input("customer pay : "))
change(total, pay)