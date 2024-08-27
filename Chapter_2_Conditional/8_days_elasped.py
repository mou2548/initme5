months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input("D: "))
m = int(input("M: "))
y = int(input("Y: ")) - 543
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    months[1] = 29
day = sum(months[:m-1]) + d
print(day)