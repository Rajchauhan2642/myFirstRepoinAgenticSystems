import pandas as pd

data = {
    "Name": ["Divyansh", "Purva", "Rahul", "Sneha", "Amit", "Neha"],
    "Score": [95, 99, 82, 88, 76, 91],
    "Passed": [True, True, True, True, False, True],
    "Category": ["A", "A", "B", "B", "C", "A"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

print("Single Column (Name):")
print(df["Name"])
print()

selected_df = df[["Name", "Score"]]

print("Multiple Columns (Name and Score):")
print(selected_df)
print()

print("First 3 rows using iloc:")
print(df.iloc[:3])
print()

df_indexed = df.set_index("Name")

print("Using loc with Name as index (Divyansh):")
print(df_indexed.loc["Divyansh"])
print()

high_score = df[df["Score"] > 85]

print("Students with Score > 85:")
print(high_score)
print()

high_pass = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Students with Score > 85 AND Passed:")
print(high_pass)
print()

sorted_students = high_pass.sort_values(by="Score", ascending=False)

print("High-performing students (Sorted by Score):")
print(sorted_students[["Name", "Score"]])
print()

print("Chained Filtering and Sorting:")
chained_result = df[(df["Score"] > 85) & (df["Passed"])].sort_values(by="Score", ascending=False)

print(chained_result[["Name", "Score"]])