class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.accounts = []

    def create_account(self, name, balance):
        account = Account(name, balance)
        self.accounts.append(account)

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account

        raise ValueError(f"No account found with name {name}")


class Account:
    def __init__(self, name, balance):
        super().__init__()
        self.name = name
        self.balance = balance

    def show_amount(self):
        message = "Your account balance: " + str(self.balance) if self.balance > 0 else "You are broke"
        print("Hello, " + self.name + "!")
        print(message + "\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to {self.name} account")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} from {self.name} is successful")
            return True
        else:
            print("Daym u broke")
            return False

    def transfer(self, other_account, amount):
        if self.balance < amount:
            print("\nTransfer failed\n")
            return False
        self.balance -= amount
        other_account.balance += amount
        print(f"\n{self.name} transferred {amount} to {other_account.name} successfully\n")
        return True


def main():
    # Create a bank object
    privat_bank = Bank("Privat Bank")

    # Create an account for the user
    account_name = input("Enter your name: ")
    initial_balance = float(input("Enter your initial balance: "))
    privat_bank.create_account(account_name, initial_balance)
    account = privat_bank.get_account(account_name)

    while True:
        # Display menu options
        print("Welcome to Privat Bank, " + account_name + "!")
        print("1. Show amount")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        # Perform action based on user's choice
        if choice == 1:
            account.show_amount()
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            recipient_name = input("Enter the name of the recipient: ")
            recipient_account = privat_bank.get_account(recipient_name)
            amount = float(input("Enter the amount to transfer: "))
            account.transfer(recipient_account, amount)
        elif choice == 5:
            print("Thank you for using Privat Bank. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

