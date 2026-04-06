import pandas as pd

# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [5000, 6000, 7000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# 1.data cleaning
# Check for missing values
print("\nMissing values:\n", df.isnull().sum())
print(df.fillna(0,inplace=True))

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
df = df.drop('Age+10', axis=1)
print("\nAfter dropping column:\n", df)

# 7. Sort by Age
print("\nSort by Age descending:\n", df.sort_values('Age', ascending=False))

# 8. Basic stats
print("\nMean Age:", df['Age'].mean())
print("Max Salary:", df['Salary'].max())

print(df.describe())
# Grouping
grouped = df.groupby('Name')['Age'].mean()
print("\nAverage Age by Name:\n", grouped)