import math
X = 0.230104 * 10**(-2.90743)
m = float(input("m(g)  = "))
T = float(input("T(°C) = "))
E = (m*(T + math.e))/(2*math.pi*X)
print(f"The Saitron energy is {E:.5f} J")