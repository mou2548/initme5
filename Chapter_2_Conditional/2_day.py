isLeap = False
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = int(input("m: "))
y = int(input("y: ")) - 543
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    isLeap = True
if m == 2 and isLeap:
    print(months[m-1] + 1)
else:
    print(months[m-1])