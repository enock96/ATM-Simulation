#!/usr/bin/env python3

import hashlib
import getpass  # Module for secure password input

# ATM simulation
# User data (stored in a dictionary)
users = {
    "Darrel": {"pin": 1234, "balance": {"ksh": 20000, "usd": 200}},
    "Norman": {"pin": 2345, "balance": {"ksh": 39999, "usd": 300}},
    "Brian": {"pin": 4567, "balance": {"ksh": 40000, "usd": 500}},
    "Christine": {"pin": 7689, "balance": {"ksh": 50000, "usd": 400}},
    "Hilda": {"pin": 6789, "balance": {"ksh": 60000, "usd": 600}}
}

# Function to hash PIN
def hash_pin(pin):
    hashed = hashlib.sha256(str(pin).encode()).hexdigest()
    return hashed

# Function to get masked PIN input
def get_masked_pin_input(prompt="Enter your PIN: "):
    pin = getpass.getpass(prompt)
    return pin

# Login function with masked input
def login():
    username = input("Enter your username: ")
    pin = get_masked_pin_input()

    # Convert input PIN to integer for comparison
    try:
        pin = int(pin)
    except ValueError:
        print("Invalid PIN format.")
        return None

    if username in users and users[username]['pin'] == pin:
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None

# Currency selection function
def select_currency():
    while True:
        currency = input("Select currency (ksh or usd): ").lower()
        if currency in ["ksh", "usd"]:
            return currency
        else:
            print("Invalid currency selection. Please choose ksh or usd.")

# Withdraw function
def withdraw(username, currency):
    amount = float(input(f"Enter the withdrawal amount ({currency}): "))
    if amount <= users[username]['balance'][currency]:
        users[username]['balance'][currency] -= amount
        print(f"Withdrawal successful. New balance: {users[username]['balance'][currency]} {currency}")
    else:
        print("Insufficient funds.")

# Check balance function
def check_balance(username, currency):
    print(f"Your balance: {users[username]['balance'][currency]} {currency}")

# Main program
def main():
    print("Welcome to the ATM!")
    username = login()
    if username:
        currency = select_currency()
        while True:
            print("\nOptions:")
            print("1. Withdraw money")
            print("2. Check balance")
            print("3. Quit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                withdraw(username, currency)
            elif choice == '2':
                check_balance(username, currency)
            elif choice == '3':
                print("Thank you for using the ATM. Have a great day!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
