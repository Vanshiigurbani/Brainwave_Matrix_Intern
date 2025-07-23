class ATM:
    def __init__(self):
        self.accounts = {}  #store accounts by pin
        self.logged_in_user = None

    def add_account(self, pin, balance=0):
        if pin not in self.accounts:
            self.accounts[pin] = {
                "balance": balance,
                "transaction_history": []  #a list to store transaction history
            }
            print(f"Account is successfully created for PIN {pin}.")
        else:
            print("Account with this PIN already exists.")
        
    def check_balance(self):
        if self.logged_in_user:
            balance = self.accounts[self.logged_in_user]["balance"]
            print(f"Your current balance is: ${balance}")
        else:
            print("No user logged in.")
        
    def withdraw(self, amount):
        if self.logged_in_user:
            if amount <= self.accounts[self.logged_in_user]["balance"]:
                self.accounts[self.logged_in_user]["balance"] -= amount
                self.accounts[self.logged_in_user]["transaction_history"].append(f"Withdrew ${amount}")
                print(f"Successfully withdrew ${amount}.")
            else:
                print("Insufficient balance!")
        else:
            print("No user logged in.")
        
    def deposit(self, amount):
        if self.logged_in_user:
            self.accounts[self.logged_in_user]["balance"] += amount
            self.accounts[self.logged_in_user]["transaction_history"].append(f"Deposited ${amount}")
            print(f"Successfully deposited ${amount}.")
        else:
            print("No user logged in.")
    
    def view_transaction_history(self):
        
        if self.logged_in_user:
            history = self.accounts[self.logged_in_user]["transaction_history"]
            if history:
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions performed yet.")
        else:
            print("No user logged in.")
        
    def login(self, pin):
        if pin in self.accounts:
            self.logged_in_user = pin
            print(f"Account logged in successfully with PIN number {pin}.")
        else:
            print("Invalid PIN.")
        
    def logout(self):
        if self.logged_in_user:
            print(f"Account logged out successfully from PIN {self.logged_in_user}.")
            self.logged_in_user = None
        else:
            print("No user is logged in.")
        
    def get_account_details(self):
        if self.logged_in_user:
            balance = self.accounts[self.logged_in_user]["balance"]
            print(f"Current balance: ${balance}")
        else:
            print("No user logged in.")
        
def atm_interface(atm):
    while True:
        print("Please select the service you would like us to provide:")
        print("1. Login")
        print("2. Create an Account")
        print("3. Check Balance")
        print("4. Withdraw Funds")
        print("5. Deposit Funds")
        print("6. View Transaction History")
        print("7. Logout")
        print("8. Exit")
        try:
            option = int(input("Enter option (1-8): "))
            if option == 1:  
                pin = int(input("Enter your PIN: "))
                atm.login(pin)
            elif option == 2:  
                pin = int(input("Enter a new PIN: "))
                balance = int(input("Enter initial balance: $"))
                atm.add_account(pin, balance)
            elif option == 3:  
                atm.check_balance()
            elif option == 4:  
                amount = int(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            elif option == 5:  
                amount = int(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            elif option == 6: 
                atm.view_transaction_history()
            elif option == 7:  
                atm.logout()
            elif option == 8:  
                print("Thank you for using PyATM. We appreciate your trust ad hope to serve you again soon!")
                break
            else:
                print("Invalid option. Please choose between 1-8.")
        except ValueError:
            print("Invalid input. Please enter a valid option or amount.")
        
if __name__ == "__main__":
    atm = ATM()
    #adding some accounts 
    atm.add_account(300501, 1000)
    atm.add_account(200509, 500)
    atm.add_account(400801,100)
    print("Welcome to the PyATM! - A smarter way to access your money, anytime, anywhere.")
    atm_interface(atm)