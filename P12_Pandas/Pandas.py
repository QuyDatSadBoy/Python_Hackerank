import pandas as pd

col = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(col)
data = {
    "Uni": ["BKHN", "DHCN", "KTMM", "CN", "PTIT"],
    "Score": [30, 20, 30, 25, 28],
    "SL": [5000, 3000, 2000, 4000, 3000],
}
df = pd.DataFrame(data, index=["top1", "top2", "top3", "top4", "top5"])
print(df)
print(df.loc["top2"])
