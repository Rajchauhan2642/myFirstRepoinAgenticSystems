def calculate_averages(users):
    averages = []

    for user in users:
        name = user["name"]
        scores = user["scores"]

        average_score = sum(scores) / len(scores)
        averages.append((name, average_score))  

    return averages


def has_admin_access(roles):
    return "admin" in roles


def main():
    
    users = [
        {
            "name": "Ravi",
            "scores": [75, 80, 85],
            "roles": {"viewer", "editor"}
        },
        {
            "name": "Anita",
            "scores": [90, 88, 92],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Suresh",
            "scores": [60, 65, 70],
            "roles": {"viewer"}
        }
    ]

    user_averages = calculate_averages(users)

    print("----- User Data Report -----")

    for name, average in user_averages:
        
        for user in users:
            if user["name"] == name:
                admin_status = has_admin_access(user["roles"])

        print("Name:", name)
        print("Average Score:", round(average, 2))
        print("Admin Access:", "Yes" if admin_status else "No")
        print("----------------------------")



main()