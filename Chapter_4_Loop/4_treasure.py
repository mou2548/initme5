last = int(input("Enter number of last floor : "))
total = 0
for i in range(1, last+1, 2):
    total += i
print(f"Total score from all level {last} : {total}")