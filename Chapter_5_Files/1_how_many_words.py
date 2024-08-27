file = input("Enter the filename : ")
with open(file) as f:
    data = f.read()
    words = data.split()
print(f"Total number of words in {file} is {len(words)} words.")