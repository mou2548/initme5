import math

def saitron_energy(m, T):
    X = 0.230104 * 10**(-2.90743)
    E = (m*(T + math.e))/(2*math.pi*X)
    return E

def is_saitron_collide(x1, y1, x2, y2, e1, e2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if distance <= (e1+e2)/1000:
        return 'Collided!'
    else:
        return 'Not Collided!'

m1 = float(input("m1(g)  = "))
T1 = float(input("T1(°C) = "))
m2 = float(input("m2(g)  = "))
T2 = float(input("T2(°C) = "))
e1 = saitron_energy(m1, T1)
e2 = saitron_energy(m2, T2)
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print(is_saitron_collide(x1, y1, x2, y2, e1, e2))