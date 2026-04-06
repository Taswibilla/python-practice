import numpy as np
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Math': [80, 70, 90, 60, 85],
    'Science': [75, 65, 95, 55, 80],
    'English': [78, 68, 88, 58, 82],
    'Gender': ['M', 'F', 'M', 'F', 'M']
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

print("CSV file created!")  

df = pd.read_csv("students.csv")

# Convert column to NumPy array
math_scores = df['Math'].to_numpy()

# Basic stats
mean = np.mean(math_scores)
median = np.median(math_scores)
std = np.std(math_scores)

print("Mean:", mean)
print("Median:", median)
print("Std Dev:", std)

# Increase by 10%
increased_scores = math_scores * 1.10

# Normalization (Min-Max)
normalized = (math_scores - np.min(math_scores)) / (np.max(math_scores) - np.min(math_scores))

print("Normalized:", normalized[:5])

# Load dataset
df = pd.read_csv("students.csv")

#pandas operations

# Filtering (students with marks > 70)
high_scores = df[df['Math'] > 70]
print(high_scores)

# Grouping
avg_by_gender = df.groupby('Gender')['Math'].mean()
print(avg_by_gender)

# New column 1: Total Marks
df['Total'] = df['Math'] + df['Science'] + df['English']

# New column 2: Pass/Fail
df['Result'] = df['Total'].apply(lambda x: "Pass" if x > 120 else "Fail")

print(df.head())