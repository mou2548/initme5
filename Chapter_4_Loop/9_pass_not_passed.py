n = int(input("Number of scores : "))
passed = 0
failed = 0
for i in range(n):
    score = float(input(f"score {i+1} : "))
    if score < 50:
        failed += 1
    else:
        passed += 1
print(f"Pass : {passed}")
print(f"Fail : {failed}")