i = 1
largest = 0
round = 1
while True:
    nums = [int(num) for num in input(f"Round #{i}: ").split()]
    if nums == []:
        break
    total = sum(nums)
    print(f"- sum: {total}")
    print(f"- avg: {total/len(nums):.2f}")
    print(f"- max: {max(nums)}")
    print(f"- min: {min(nums)}")
    if total > largest:
        largest = total
        round = i
    i += 1

print(f"Largest Amount is {largest} at round #{round}")