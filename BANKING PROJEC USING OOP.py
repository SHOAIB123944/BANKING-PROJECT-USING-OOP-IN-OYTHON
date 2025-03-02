print("-------------------------------------------------------------------------------NATIONAL BANK ZAFARWAL---------------------------------------------------------------------------------------------")
print("                                                                               _____________________                                                              ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

class Bank:
    bank_name = "NATIONAL BANK ZAFARWAL"

    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"\n₹{amount} has been credited to your account.")
        print(f"Your new balance is: ₹{self.balance}\n")

    def debit(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance! Transaction failed.\n")
        else:
            self.balance -= amount
            print(f"\n₹{amount} has been debited from your account.")
            print(f"Your new balance is: ₹{self.balance}\n")
name = input("Enter the person's name: ")
account = int(input("Enter the account number: "))
balance = int(input("Enter the initial balance: "))
person1 = Bank(name, account, balance)
print("\n-------------------------------------------")
print("MENU:")
print("1. View Personal Information")
print("2. Credit Amount")
print("3. Debit Amount")
print("4. Exit")
print("-------------------------------------------")
while True:
    op = int(input("\nPlease enter your choice (1/2/3/4): "))

    if op == 1:
        print("\n-----------------------")
        print("PERSON BANK DETAILS")
        print("-----------------------")
        print(f"Name: {person1.name}")
        print(f"Account Number: {person1.account}")
        print(f"Balance: ₹{person1.balance}")
        print("-----------------------")

    elif op == 2:
        print("----------------------------------------")
        print("-           ^CEDIT PORTAL^            -")
        print("----------------------------------------")
        amount = int(input("Enter the amount to credit: "))
        person1.credit(amount)

    elif op == 3:
        print("----------------------------------------")
        print("-           ^DEBIT PORTAL^             -")
        print("----------------------------------------")
        amount = int(input("Enter the amount to debit:-"))
        person1.debit(amount)

    elif op == 4:
        print("\nThank you for using NATIONAL BANK ZAFARWAL!")
        break

    else:
        print("\nInvalid choice! Please try again.")

   
                                                            