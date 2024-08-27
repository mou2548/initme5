a = int(input())
b = int(input())

# f(x) function
def f(x):
    return b - x

# g(x) function
def g(x):
    return a - x

# whoIsDead(a, b) function
def whoIsDead(a, b):
    if a <= 0 and b != 0:
        print('Win dead')
    elif a != 0 and b == 0:
        print('Fah dead')
    elif a != 0 and b != 0:
        print('No one dead')
    elif a == 0 and b == 0:
        print('Both dead')

x = int(input())
b = f(x)
x = int(input())
a = g(x)
x = int(input())
b = f(x)
x = int(input())
a = g(x)

whoIsDead(a,b)