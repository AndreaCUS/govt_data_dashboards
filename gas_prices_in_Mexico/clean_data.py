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
        df["longitude_int"] = df["longitude"].astype(int)
        df["latitude_int"] = df["latitude"].astype(int)
        df = df[(df["regular"] > 0) & (df["premium"] > 0)]  # remove 0 price values
        df.to_csv("clean_data.csv")

        aggr_df = df
        aggr_df = aggr_df[
            (aggr_df["longitude_int"] > 0) & (aggr_df["latitude_int"] > 0)
        ]
        grouped_multiple = aggr_df.groupby(["latitude_int", "longitude_int"]).agg(
            {"regular": ["mean"]}
        )
        grouped_multiple.columns = ["regular_mean"]
        grouped_multiple = grouped_multiple.reset_index()

        grouped_multiple.to_csv("aggregate_data.csv")
