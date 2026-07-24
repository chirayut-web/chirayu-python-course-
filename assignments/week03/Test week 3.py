# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = int(input("Choose option: "))

        if choice == 1:
            print("Balance:",balance)
        elif choice == 2:
            user_choice = int(input("Amount to withdraw:"))
            balance = balance - user_choice
        elif choice == 3:
            user_choice = int(input("Amount to Deposiut"))
            balance = balance + user_choice
        elif choice == 4:
            break
        else:
            print("invalid choice please Choose again")
            choice = int(input("Choose option: "))
else:
    print("Invalid PIN")

