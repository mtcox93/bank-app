import banking_pkg
from banking_pkg import account
import time


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automate Teller Machine ===            ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = float(0)
print(str(name), "has been registered with a starting balance of $", str(balance))
database = {name: pin}
time.sleep(0.25)
while True:
    print("\nPlease login")
    login_name = input("Enter name: ")
    if login_name in database:
        print("User selected: ", login_name)
    pin_number = input("Enter PIN: ")
    if(database[login_name] == pin_number):
        print("Login successful")
        break
    else:
        print("Invalid credentials")
        continue

time.sleep(0.25)
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        print("\n")
        account.show_balance(balance)
        time.sleep(0.25)
    elif option == "2":
        print("\n")
        balance = account.deposit(balance)
        print("Current balance: ", balance)
        time.sleep(0.25)
    elif option == "3":
        print("\n")
        balance = account.withdraw(balance)
        print("Current balance: ", balance)
        time.sleep(0.25)
    else:
        print("\n")
        account.logout(name)
        break
    continue
