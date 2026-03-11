balance_input = input("Enter your account balance: ")
account_balance = int(balance_input)  

withdrawal_input = input("Enter withdrawal amount: ")
withdrawal_amount = int(withdrawal_input)  

verification_input = input("Are you verified (True/False)? ")

if verification_input.strip().lower() == "true":
    is_verified = True
elif verification_input.strip().lower() == "false":
    is_verified = False
else:
    print("Invalid input for verification status! Please enter True or False.")
    exit()

if is_verified and withdrawal_amount <= account_balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")