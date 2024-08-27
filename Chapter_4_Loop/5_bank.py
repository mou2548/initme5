balance = int(input("Enter the starting balance : "))
while True:
    print(f"Current balance : {balance:.1f}")
    print("Please choose an option\n1. Deposit money\n2. Withdraw money\n3. Exit")
    choice = int(input("Enter your choice (1/2/3) : "))
    if choice == 1:
        deposit = int(input("Enter amount to deposit : "))
        balance += deposit
    elif choice == 2:
        withdraw = int(input("Enter amount to withdraw : "))
        if withdraw > balance:
            print("Insufficient balance!")
            continue
        balance -= withdraw
    elif choice == 3:
        print(f"Final balance : {balance:.1f}")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue