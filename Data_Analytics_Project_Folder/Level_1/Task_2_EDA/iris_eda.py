
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("1) iris.csv")

print(df.describe())

print(df.corr(numeric_only=True))

df.hist(figsize=(10,8))
plt.tight_layout()
plt.savefig("iris_histograms.png")

plt.figure(figsize=(8,6))
plt.scatter(df["sepal_length"], df["petal_length"])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length")
plt.savefig("iris_scatter.png")

print("EDA completed successfully")
