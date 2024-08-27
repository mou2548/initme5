def findSlope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def isParallel(m1, m2):
    if m1 == m2:
        return "Parallel"
    return "Not Parallel"

x1 = int(input("Input x1: "))
y1 = int(input("Input y1: "))
x2 = int(input("Input x2: "))
y2 = int(input("Input y2: "))
m = int(input("Input m: "))
print(isParallel(m, findSlope(x1, y1, x2, y2)))