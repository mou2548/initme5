target = int(input("Target number of coins : "))
total = 0
day = 0
while total < target:
    day += 1
    today = int(input("Enter the number of coins collected today : "))
    total += today
print(f"Win uses {day} days to collect {target} coins.")