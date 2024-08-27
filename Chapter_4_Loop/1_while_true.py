total = 0
while True:
    num = int(input("Enter a number (0 to stop) : "))
    total += num
    if num == 0:
        break
print(f"Total is {total}")