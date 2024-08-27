salad = int(input("Input starting salad (X): "))
W = int(input("Input Win's eating rate (W): "))
N = int(input("Input Nobi's eating rate (N): "))
print(f"Win eats {salad//W} time(s)")
salad %= W
print(f"Nobi eats {salad//N} time(s)")
salad %= N
print(f"Remaining {salad} for Atom")