import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Create Result column (if not already created)
df['Total'] = df['Math'] + df['Science'] + df['English']
df['Result'] = df['Total'].apply(lambda x: "Pass" if x > 120 else "Fail")

# Set style
sns.set(style="whitegrid")

# 1. Histogram (Matplotlib)
plt.figure()
plt.hist(df['Math'], bins=10)
plt.title("histogram for Distribution of Math Scores")
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.show()


# 2. Scatter Plot (Matplotlib)
plt.figure()
plt.scatter(df['Math'], df['Science'])
plt.title("scatter plot of Math vs Science Scores")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()


# 3. Boxplot (Seaborn)
plt.figure()
sns.boxplot(x=df['Math'])
plt.title("Boxplot of Math Scores")
plt.xlabel("Math Marks")
plt.show()


# 4. Count Plot (Seaborn)
plt.figure()
sns.countplot(x='Result', data=df)
plt.title("count plot for Pass vs Fail Count")
plt.xlabel("Result")
plt.ylabel("Count")
plt.show()
