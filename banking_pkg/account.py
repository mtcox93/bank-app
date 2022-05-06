
def show_balance(balance):
    """This function will show the current balance in my account"""
    print("Current account balance: ", balance)


def deposit(balance):
    """Running the deposit function will take my input and assign it as a float value to the variable amount.
       It will then add the balance plus the amount and return that number
       balance variable will be updated in the app.py file to show this change"""
    amount = float(input("Enter amount to deposit: "))
    return balance + amount


"""When calling the withdraw function, the function will take my input, turn it to a float number, and then subtract that
from the current balance. If the balance would be a negative number, the function tells the user
they don't have enough funds to withdraw"""


def withdraw(balance):
    """When calling the withdraw function, the function will take my input, turn it to a float number, and then subtract that
       from the current balance. If the balance would be a negative number, the function tells the user
       they don't have enough funds to withdraw"""
    with_draw = float(input("Enter amount to withdraw: "))
    if with_draw <= balance:
        return balance - with_draw
    elif with_draw > balance:
        print("You do not currently have the funds to make this withdraw")
        return balance


def logout(name):
    print("Goodbye", name, "!")
