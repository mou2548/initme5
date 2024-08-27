sentence = input("Enter the sentence : ").split()
maximum = int(input("Maximum word length : "))
longer = []
for word in sentence:
    if len(word) > maximum:
        longer.append(word)
txt = ", ".join(longer)
if txt == "":
    print(f"No word is longer than {maximum} words in the sentence.")
else:
    print(f"Words in sentences that are longer than {maximum} words : {txt}")