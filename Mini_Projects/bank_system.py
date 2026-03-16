class BankAccount:
    
    def __init__(self,name,initial_balance):
        self.name = name
        self.__initial_balance = initial_balance
    
    def deposit(self,amount):
        self.__initial_balance = self.__initial_balance + amount
        print(f"{amount} is deposited sucessfully.")
    
    def withdraw(self,amount):
        self.__initial_balance = self.__initial_balance - amount
        print(f"{amount} is withdrawn sucessfully.")
    
    def show_balance(self):
        print(f"Your total bank balance is {self.__initial_balance}")
    
acc1 = BankAccount("Ram Prasad Mishra",10000)

print("Welcome to Prabhu Bank:\n")

while True:
    
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. View Total Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        amount = int(input("Enter amount to deposit: "))
        acc1.deposit(amount)
        
    elif choice == 2:
        
       amount = int(input("Enter amount to withdraw: ")) 
       acc1.withdraw(amount)
       
    elif choice == 3:
        
        acc1.show_balance()
        
    elif choice == 4:
        print("Thank you for using Prabhu bank.")
        break
    
    else:
        print("Invalid choice. Please try again.")