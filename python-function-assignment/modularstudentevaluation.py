def greet_student(name):
    return f"Hello, {name}! Here is your performance report."

# Function 2: Return number of subjects and average score
def calculate_results(scores):
    total_subjects = len(scores)
    average_score = sum(scores) / total_subjects
    return total_subjects, average_score


def evaluate_performance(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    
    name = input("Enter student name: ")

    scores = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        score = float(input(f"Enter marks for subject {i+1}: "))
        scores.append(score)

    greeting = greet_student(name)
    subjects, average = calculate_results(scores)
    result = evaluate_performance(average)

    print("\n----- Student Performance Report -----")
    print(greeting)
    print("Number of Subjects:", subjects)
    print("Average Score:", round(average, 2))
    print("Final Result:", result)


main()