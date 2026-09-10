import pandas as pd

df = pd.read_csv("sales.csv")

df["total_amount"] = df["quantity"] * df["price"]

print(df)