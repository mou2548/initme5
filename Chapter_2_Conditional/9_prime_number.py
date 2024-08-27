n = int(input("N : "))
for i in range(2, round(n**0.5)+1):
    if n % i == 0:
        print(f"{n} is not a Prime Number")
        break
else:
    print(f"{n} is a Prime Number")