
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("2) Stock Prices Data Set.csv")

df["date"] = pd.to_datetime(df["date"])

aapl = df[df["symbol"] == "AAPL"]

aapl = aapl.sort_values("date")

aapl.set_index("date", inplace=True)

plt.figure(figsize=(10,6))
plt.plot(aapl["close"])
plt.title("AAPL Closing Prices")
plt.savefig("aapl_close_prices.png")

aapl["moving_average"] = aapl["close"].rolling(window=30).mean()

plt.figure(figsize=(10,6))
plt.plot(aapl["close"], label="Close Price")
plt.plot(aapl["moving_average"], label="30 Day Moving Average")
plt.legend()
plt.savefig("moving_average.png")

decomposition = seasonal_decompose(aapl["close"], model="additive", period=30)
decomposition.plot()
plt.savefig("seasonal_decomposition.png")

print("Time Series Analysis completed")
