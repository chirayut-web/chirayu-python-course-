account = None

class banking:
    def __init__(self, id, intake):
        self.id = id
        self.intake = intake

    def create_account(self, id, intake):

        new_id = id
        new_intake = intake

        new_account = banking(
            new_id,
            new_intake
        )

        return new_account

    def deposit_amount(self, deposit):
        if deposit <= 0:
            print("Deposit must be greter then 0")
            return

        
        self.intake += deposit
        return (f"Deposited: {deposit} baht")

    def withdraw_amount(self, withdraw):
        if withdraw > self.intake or withdraw < 0:
            print("Withdrawal must be greater than 0 or Greter then current balacne")
            return
        
        self.intake -= withdraw
        return (f"withdraw: {withdraw} baht")
    
    def check_balance(self):
        return (f"Current balnce: {self.intake}")

while True:
    if account is None:
        id = int(input("Please create your id: "))
        intake = int(input("please deposit your money atleast 1000 baht: "))
        account = banking(id, intake)
    try:
        user_choice = int(input("Choose your next action\n1. To deposit\n2. To withdraw\n3. To check you balance\n4. Exit\nEnter: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if user_choice == 1:
        deposit = int(input("Enter amount you want to deposit: "))
        print(account.deposit_amount(deposit))
        print("")
    elif user_choice == 2:
        withdraw = int(input("Enter amount you want to withdraw: "))
        print(account.withdraw_amount(withdraw))
        print("")
    elif user_choice == 3:
        print(account.check_balance())
        print("")
    elif user_choice == 4:
        print("Exit succesfully")
        break
