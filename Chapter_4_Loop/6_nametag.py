text = ''
for i in range(4):
    text += input(f"Name of friend {i+1} : ")
    text += ', '
text += input(f"Name of friend {5} : ")
print(f"List of friends : {text}")