marks = [78, 85, 92, 67, 88, 74, 90, 81]

print("Full List of Marks:", marks)

print("First 3 Marks:", marks[:3])

print("Last 3 Marks:", marks[-3:])

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)


print("\n----- Marks Analysis -----")
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", round(average, 2))