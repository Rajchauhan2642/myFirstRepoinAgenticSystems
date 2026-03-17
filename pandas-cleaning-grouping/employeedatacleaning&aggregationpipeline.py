import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Divyansh", "Purva", "Raj", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("🔹 Original DataFrame:\n")
print(df)

print("\n🔹 Missing Values in Each Column:\n")
print(df.isnull().sum())

mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\n🔹 DataFrame after filling missing Salary:\n")
print(df)

df.drop(columns=["Temporary_Notes"], inplace=True)

df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\n🔹 Cleaned DataFrame:\n")
print(df)


summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n🔹 Final Summary Table:\n")
print(summary)