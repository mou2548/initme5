def f(x):
    if 5 <= x <= 25:
        return 3*x - 5
    else:
        return 5

x = int(input("x : "))
print(f(x) + f(2*x))