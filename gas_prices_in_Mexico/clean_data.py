import os
import pandas as pd


def read_data():
    if os.path.exists("raw_data.csv"):
        df = pd.read_csv("raw_data.csv")
        postal_codes = pd.read_csv("postal_codes.csv")
        return df, postal_codes
    else:
        return None, None


def clean_data():
    df, postal_codes = read_data()
    if df is not None:

        df["regular"] = pd.to_numeric(df["regular"])
        df["premium"] = pd.to_numeric(df["premium"])
        df["longitude_int"] = df["longitude"].astype(int)
        df["latitude_int"] = df["latitude"].astype(int)
        df = df[(df["regular"] > 0) & (df["premium"] > 0)]  # remove 0 price values

        # Add state name based on postal code
        postal_codes.rename(columns={"d_codigo": "codigopostal"}, inplace=True)
        postal_codes["codigopostal"] = pd.to_numeric(
            postal_codes["codigopostal"], errors="coerce"
        )
        df["codigopostal"] = pd.to_numeric(df["codigopostal"], errors="coerce")
        df = df.drop_duplicates(subset=["_id"])
        codigopostal_estado = postal_codes[
            ["codigopostal", "d_estado"]
        ].drop_duplicates(subset=["codigopostal"])
        df = df.merge(codigopostal_estado, on=["codigopostal"])

        df.to_csv("clean_data.csv")

        # aggregate data by latitude and longitue, for heatmap
        aggr_df = df
        aggr_df = df[
            (df["longitude_int"] != 0) & (df["latitude_int"] != 0)
        ]  # remove missing lat & longitude rows
        aggregate_data = aggr_df.groupby(["latitude_int", "longitude_int"]).agg(
            {"regular": ["mean"]}
        )
        aggregate_data.columns = ["regular_mean"]
        aggregate_data = aggregate_data.reset_index()

        aggregate_data.to_csv("aggregate_data.csv")

        # Summarize data
        summary_df = pd.DataFrame()
        summary_df.at[0, "n_rows"] = len(df.index)
        summary_df.at[0, "min_regular"] = df["regular"].min()
        summary_df.at[0, "max_regular"] = df["regular"].max()
        summary_df.at[0, "min_premium"] = df["premium"].min()
        summary_df.at[0, "max_premium"] = df["premium"].max()

        # Summarize data by state
        state_data = df.groupby(["d_estado"]).agg(
            {"regular": ["count", "mean"], "premium": ["count", "mean"]}
        )
        state_data.columns = [
            "regular_count",
            "regular_mean",
            "premium_count",
            "premium_mean",
        ]
        state_data = state_data.reset_index()
        state_data.to_csv("state_data.csv")


if __name__ == "__main__":
    clean_data()
