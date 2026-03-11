user_name = input("Enter your name: ")

age_input = input("Enter your age: ")
user_age = int(age_input)

active_input = input("Are you an active user (True/False)? ")
is_active = active_input.strip().lower() == "true"  

print(f"User {user_name} is {user_age} years old. Active status: {is_active}")