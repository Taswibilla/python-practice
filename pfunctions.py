import pandas as pd

# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [5000, 6000, 7000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. View first rows
print("\nFirst 2 rows:\n", df.head(2))

# 3. Select column
print("\nNames column:\n", df['Name'])

# 4. Filter rows
print("\nAge > 25:\n", df[df['Age'] > 25])

# 5. Add new column
df['Age+10'] = df['Age'] + 10
print("\nAfter adding column:\n", df)

# 6. Drop column
df.drop('Age+10', axis=1, inplace=True)
print("\nAfter dropping column:\n", df)

# 7. Sort by Age
print("\nSort by Age descending:\n", df.sort_values('Age', ascending=False))

# 8. Basic stats
print("\nMean Age:", df['Age'].mean())
print("Max Salary:", df['Salary'].max())