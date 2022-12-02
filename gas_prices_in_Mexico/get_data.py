import requests
import pandas as pd


def get_data(n_results):
    url = "https://api.datos.gob.mx/v1/precio.gasolina.publico?pageSize={}".format(
        n_results
    )
    raw_data = requests.get(url)
    json_data = raw_data.json()
    df = pd.DataFrame(json_data["results"], index=list(range(0, n_results)))

    df["regular"] = pd.to_numeric(df["regular"])
    df["premium"] = pd.to_numeric(df["premium"])
    df = df[(df["regular"] > 0) & (df["premium"] > 0)]  # remove 0 price values
    return df


def save_data(df):
    if not os.path.isfile("raw_data.csv"):
        # write file
        pass


def main():
    df = get_data(n_results=5000)
    save_data(df)


if __name__ == "__main__":

    main()
