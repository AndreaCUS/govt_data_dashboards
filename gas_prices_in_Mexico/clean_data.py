import os
import pandas as pd


def read_data():
    if not os.path.exists("clean_data.csv"):
        df = pd.read_csv("raw_data.csv")
        return df
    else:
        return None


def clean_data():
    df = read_data()
    if df is not None:

        df["regular"] = pd.to_numeric(df["regular"])
        df["premium"] = pd.to_numeric(df["premium"])
        df = df[(df["regular"] > 0) & (df["premium"] > 0)]  # remove 0 price values

        df.to_csv("clean_data.csv")
