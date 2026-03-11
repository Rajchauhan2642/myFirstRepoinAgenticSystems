import pandas as pd

def main():
    print("Step 1: Creating a sample dataset and saving as CSV...\n")

    data = {
        "Name": ["Ravi", "Anita", "Suresh", "Priya", "Karan", "Neha", "Amit", "Divya"],
        "Age": [22, 25, 21, 23, 24, 22, 26, 23],
        "Score": [85, 90, 67, 78, 88, 92, 70, 95],
        "Label": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
    }

    df = pd.DataFrame(data)

    df.to_csv("sample_dataset.csv", index=False)

    print("Step 2: Loading the dataset using pd.read_csv()...\n")
    df = pd.read_csv("sample_dataset.csv")

    print("Step 3: Displaying first 5 rows (head())\n")
    print(df.head(), "\n")

    print("Displaying last 5 rows (tail())\n")
    print(df.tail(), "\n")

    print("Displaying structural information (info())\n")
    print(df.info(), "\n")

    print("Displaying summary statistics (describe())\n")
    print(df.describe(), "\n")

    print("Step 4: Selecting a single column (Score)\n")
    score_column = df["Score"]
    print(score_column, "\n")

    print("Step 5: Selecting multiple columns (Age and Score)\n")
    selected_columns = df[["Age", "Score"]]
    print(selected_columns, "\n")

    print("Step 6: Filtering rows where Score > 80\n")
    filtered_data = df[df["Score"] > 80]
    print(filtered_data, "\n")


main()