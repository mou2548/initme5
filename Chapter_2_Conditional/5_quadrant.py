x = float(input("x: "))
y = float(input("y: "))
if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x > 0 and y < 0:
    print("Quadrant 4")
elif x == 0 and y > 0:
    print("Positive Y-Axis")
elif x == 0 and y < 0:
    print("Negative Y-Axis")
elif x < 0 and y == 0:
    print("Negative X-Axis")
elif x > 0 and y == 0:
    print("Positive X-Axis")
elif x == 0 and y == 0:
    print("Origin")