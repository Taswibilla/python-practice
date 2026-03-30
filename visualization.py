import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

# Sample dataset
data = {
    "age": [22, 25, 30, 35, 40, 22, 23, 31, 45, 50],
    "salary": [20000, 25000, 30000, 35000, 40000, 22000, 24000, 32000, 45000, 50000],
    "experience": [1, 2, 5, 7, 10, 1, 2, 6, 12, 15],
    "department": ["IT", "HR", "IT", "HR", "IT", "IT", "HR", "IT", "HR", "IT"]
}

df = pd.DataFrame(data)

# Create subplots
plt.figure(figsize=(15, 10))

# 1. Histogram
plt.subplot(3, 3, 1)
sns.histplot(df["salary"], kde=True)
plt.title("Histogram")

# 2. Box Plot
plt.subplot(3, 3, 2)
sns.boxplot(x=df["salary"])
plt.title("Box Plot")

# 3. Scatter Plot
plt.subplot(3, 3, 3)
plt.scatter(df["experience"], df["salary"])
plt.title("Scatter Plot")

# 4. KDE Plot
plt.subplot(3, 3, 4)
sns.kdeplot(df["salary"])
plt.title("KDE Plot")

# 5. Count Plot
plt.subplot(3, 3, 5)
sns.countplot(x=df["department"])
plt.title("Count Plot")

# 6. Heatmap (separate figure for clarity)
plt.subplot(3, 3, 6)
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.title("Heatmap")

plt.tight_layout()
plt.show()

# 7. Pairplot (separate window)
pair = sns.pairplot(df)
plt.show(block=True)