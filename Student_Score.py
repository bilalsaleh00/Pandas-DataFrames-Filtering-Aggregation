import pandas as pd

data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)

print(df)


# 1
students_per_course = df.groupby("course")["student"].count()
print(students_per_course)

# 2
average_score = df.groupby("course")["score"].mean()
print(average_score)

# 3
top_three = df.sort_values("score", ascending=False).head(3)
print(top_three[["student", "score"]])

# 4
average_hours = df.groupby("passed")["hours_studied"].mean()
print(average_hours)

# 5
df["grade"] = pd.cut(
    df["score"],
    bins=[0, 70, 80, 90, 101],
    labels=["F", "C", "B", "A"],
    right=False
)

print(df[["student", "score", "grade"]])

# 6
grade_distribution = pd.crosstab(
    df["course"],
    df["grade"]
)

print(grade_distribution)