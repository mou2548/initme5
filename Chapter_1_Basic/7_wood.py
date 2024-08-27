chair = int(input("Amount of Chair: "))
table = int(input("Amount of Table: "))
storage = int(input("Amount of Storage: "))
stick = chair*4 + table*6 + storage*2
slab = chair*1 + table*3 + storage*2
log = chair*0 + table*1 + storage*4
print(f"Stick x{stick}")
print(f"Slab x{slab}")
print(f"Log x{log}")