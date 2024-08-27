isLeap = False
year = int(input("Year : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    isLeap = True
print(isLeap)