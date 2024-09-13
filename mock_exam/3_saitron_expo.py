import sys

def print_ticket(age, parent, ticket, pay):
    if age >= 18:
        if ticket == 'VIP':
            session = 1
        else:
            if pay >= 1000:
                session = 2
            else:
                session = 3
    elif parent == 'Y':
        if ticket == 'VIP':
            session = 4
        else:
            if pay >= 500:
                session = 5
            else:
                session = 6
    else:
        session = 'No Entry'
    
    print("--------------------------")
    print(f"| {'Age':<12}|{age:>9} |")
    print(f"| {'Parent?':<12}|{parent:>9} |")
    print(f"| {'Ticket Type':<12}|{ticket:>9} |")
    print(f"| {'Souvenir':<12}|{pay:>9.2f} |")
    print(f"| {'Session':<12}|{session:>9} |")
    print("--------------------------")


age = int(input("Age: "))
if age <= 0:
    print("Age must greater than 0!")
    sys.exit()

parent = input("Parent? (Y/N): ")
if parent != 'Y' and parent != 'N':
    print("Parent input must be 'Y' or 'N'!")
    sys.exit()

ticket = input("Ticket Type (Normal/VIP): ")
if ticket != 'Normal' and ticket != 'VIP':
    print("Ticket Type must be 'Normal' or 'VIP'!")
    sys.exit()

pay = float(input("Souvenir Pay: "))
if pay < 0:
    print("Souvenir input must be 0 or positive number!")
    sys.exit()

print_ticket(age, parent, ticket, pay)
