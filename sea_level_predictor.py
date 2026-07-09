import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("epa-sea-level.csv")

x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]
res = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
xpred = range(1880, 2051)
ypred = [res.slope*x + res.intercept for x in xpred]

x2000 = df["Year"][df["Year"] >= 2000]
y2000 = df["CSIRO Adjusted Sea Level"][df["Year"] >= 2000]
res2000 = stats.linregress(x2000, y2000)
xpred2000 = range(2000, 2051)
ypred2000 = [res2000.slope*x2000 + res2000.intercept for x2000 in xpred2000]

plt.scatter(x, y)
plt.plot(xpred, ypred, 'r--')
plt.plot(xpred2000, ypred2000, 'g--')
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.show()