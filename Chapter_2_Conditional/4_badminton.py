minute = int(input("Total minute(s): "))
hour = minute//60
if minute % 60 > 20:
    hour += 1
price = hour*900
if hour >= 2 and hour < 4:
    price *= 0.9
elif hour == 4:
    price *= 0.8
elif hour >= 5:
    price *= 0.7
print(f"Total price is {price:.2f} baht.")