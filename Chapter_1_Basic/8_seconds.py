total = int(input("second(s): "))
second = total%60
minute = total//60%60
hour = total//60//60
print(f"{total} => {hour} hour(s): {minute} minute(s): {second} second(s)")