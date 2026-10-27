
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("1) iris.csv")

species_counts = df["species"].value_counts()

plt.figure(figsize=(6,5))
species_counts.plot(kind="bar")
plt.title("Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.savefig("species_barplot.png")

plt.figure(figsize=(8,6))
plt.plot(df["sepal_length"])
plt.title("Sepal Length Line Plot")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.savefig("sepal_length_lineplot.png")

plt.figure(figsize=(8,6))
plt.scatter(df["petal_length"], df["petal_width"])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Petal Width")
plt.savefig("petal_scatter.png")

print("Visualizations saved successfully")
