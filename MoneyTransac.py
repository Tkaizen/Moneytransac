class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"The current balance is {self.balance}.")

def main():
    print("Welcome to the Bank!")
    owner = input("Enter the account owner's name: ")
    account = BankAccount(owner)

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting... Thank you for using the bank.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
