age_input = input("Enter your age: ")
age = int(age_input)  

id_input = input("Do you have an ID card (True/False)? ")

if id_input.strip().lower() == "true":
    has_id = True
elif id_input.strip().lower() == "false":
    has_id = False
else:
    print("Invalid input for ID status! Please enter True or False.")
    exit()
    
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")