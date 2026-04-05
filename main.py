import matplotlib.pyplot as plt
from analysis import load_data, calculate_average, top_students, weak_students

df = load_data()
df = calculate_average(df)

print("\nFull Data:\n", df)
print("\nTop Students:\n", top_students(df))
print("\nWeak Students:\n", weak_students(df))

# 📊 Graph
plt.bar(df["Name"], df["Average"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("performance.png")
plt.show()
