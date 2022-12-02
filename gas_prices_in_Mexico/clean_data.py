import pandas as pd

df = None  # read file
df["regular"] = pd.to_numeric(df["regular"])
df["premium"] = pd.to_numeric(df["premium"])
df = df[(df["regular"] > 0) & (df["premium"] > 0)]  # remove 0 price values

# write df
