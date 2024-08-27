layer = int(input("Enter a number of cake layer(s) : "))
strawberry = 1
for i in range(1, layer+1):
    strawberry *= i
print(f"Cake {layer} layer(s) use {strawberry} strawberry(s) to decorate.")