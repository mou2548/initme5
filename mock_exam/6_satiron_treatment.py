from math import ceil, floor
file = input("File Name: ")
with open(file) as f:
    data = f.readlines()
    rows = [i.strip().split(",") for i in data[1:] if i.strip()]

info = {}
for row in rows:
    name, age, disease, riskplan, riskamount = row[0], row[1], row[2], row[3], row[4]
    positive, negative, neutral = 0, 0, 0
    if disease == 'Cancer':
        positive = 10 * 10**3
    elif disease == "Alzheimer's":
        negative = 100 * 10**3
        neutral = 50
    elif disease == 'SLE':
        neutral = 1 * 10**6
    elif disease == 'HIV':
        neutral = 1 * 10**3
        positive = 500
    
    if riskplan == 'Yes':
        divider = float(riskamount)
    elif float(age) >= 18:
        divider = 10
    else:
        divider = 7
    pweek, nweek, oweek = ceil(positive/divider), ceil(negative/divider), ceil(neutral/divider)


    print("======================================================")
    print(f"| {'Name':<28}|{name:^22}|")
    print(f"| {'Age':<28}|{age:^22}|")
    print(f"| {'Disease':<28}|{disease:^22}|")
    print("------------------------------------------------------")
    print(f"| {'Risk Plan':<28}|{riskplan:^22}|")
    print(f"| {'Risk Amount (J)':<28}|{riskamount:^22}|")
    print("------------------------------------------------------")
    print(f"| {'Positive Ray Total Dose (J)':<28}|{positive:^22}|")
    print(f"| {'Negative Ray Total Dose (J)':<28}|{negative:^22}|")
    print(f"| {'Neutral Ray Total Dose (J)':<28}|{neutral:^22}|")
    print("------------------------------------------------------")
    print(f"| {'Positive Ray Total Week(s)':<28}|{pweek:^22}|")
    print(f"| {'Negative Ray Total Week(s)':<28}|{nweek:^22}|")
    print(f"| {'Neutral Ray Total Week(s)':<28}|{oweek:^22}|")
    print("======================================================")