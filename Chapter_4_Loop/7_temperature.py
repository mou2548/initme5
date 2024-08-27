days = []
for i in range(7):
    temp = float(input(f"Enter temperature for day {i+1} : "))
    days.append(temp)
print(f"Highest temperature of this week is {max(days)}°C")
print(f"Lowest temperature of this week is {min(days)}°C")