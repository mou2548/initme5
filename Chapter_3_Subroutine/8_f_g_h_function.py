def f(x):
    if 5 <= x <= 25:
        return 3*x - 5
    return 5

def g(x, y):
    if x > 0:
        return x + y
    elif x < 0:
        return 5 * x * y
    return 1

def h(x, y):
    if x * y > 0:
        return f(g(x, y))
    return g(f(x), y)

x = int(input("x: "))
y = int(input("y: "))
print(h(f(x), g(x,y)))