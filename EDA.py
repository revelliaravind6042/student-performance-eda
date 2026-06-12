import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("studentsData.csv")

print("Dataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

plt.figure(figsize=(10,8))
corr = df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(
    df["exam_score"],
    bins=range(20, 110, 5)
)
plt.title("Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("exam_score_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(
    x="study_hours",
    data=df, 
    width=0.4
)
plt.title("Study Hours Distribution")
plt.grid(True)
plt.savefig("study_hours_distribution.png")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(
    x="study_hours",
    y="exam_score",
    data=df
)
plt.title("Exam Score by Study Hours")
plt.grid(True)
plt.savefig("exam_score_by_study_hours.png")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(
    x="previous_score",
    y="exam_score",
    data=df
)
plt.title("Previous Score vs Exam Score")
plt.grid(True)
plt.savefig("previous_score_vs_exam_score.png")
plt.show()

plt.figure(figsize=(6,5))
ax = sns.countplot(
    x="placement_status",
    data=df,
    width=0.2
)
ax.bar_label(ax.containers[0])
plt.title("Placement Status Distribution")
plt.grid(True)
plt.savefig("placement_status_distribution.png")
plt.show()

plt.figure(figsize=(6,5))
sns.barplot(
    x="placement_status",
    y="exam_score",
    data=df,
    width=0.2
)
plt.title("Average Exam Score by Placement Status")
plt.grid(True)
plt.savefig("avg_exam_score_by_placement.png")
plt.show()
