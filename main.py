import pandas as pd

# Create student data
data = {
    "Name": ["Sai", "Ravi", "Anu", "Priya", "Kiran"],
    "Maths": [85, 78, 92, 70, 60],
    "Science": [90, 88, 95, 65, 70],
    "English": [80, 75, 85, 60, 65],
    "Attendance": [90, 85, 95, 80, 75]
}

df = pd.DataFrame(data)
print(df)
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Total marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Average marks
df["Average"] = df["Total"] / 3

print(df)

top_student = df.loc[df["Average"].idxmax()]

print("Top Performer:")
print(top_student)
weak_students = df[df["Average"] < 70]

print("Weak Students:")
print(weak_students)
import matplotlib.pyplot as plt

# Bar chart of average marks
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

plt.scatter(df["Attendance"], df["Average"])
plt.title("Attendance vs Performance")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()
df.to_csv("students.csv", index=False)