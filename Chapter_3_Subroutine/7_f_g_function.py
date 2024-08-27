def f(x):
    if 5 <= x <= 25:
        return 3*x - 5
    return 5

def g(x, y):
    if x > 0:
        return x + y
    elif x < 0:
        return 5 * x *y
    return 1

x = int(input("x: "))
y = int(input("y: "))
print(f(y) * g(y, x))