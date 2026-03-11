contacts = {
    "Ravi": "9876543218",
    "Anita": "9123456788",
    "Suresh": "9988776655"
}

print("----- Contact List -----")
for name, number in contacts.items():
    print(name, ":", number)

search_name = input("\nEnter the name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")