import os
import io
import requests
import pandas as pd


def get_gas_data(n_results):
    url = "https://api.datos.gob.mx/v1/precio.gasolina.publico?pageSize={}".format(
        n_results
    )
    raw_data = requests.get(url)
    json_data = raw_data.json()
    df = pd.DataFrame(json_data["results"], index=list(range(0, n_results)))

    return df


def get_postal_code_data():
    url = "https://www.correosdemexico.gob.mx/datosabiertos/cp/cpdescarga.txt"
    urlData = requests.get(url)
    decoded = urlData.content.decode("latin-1")
    decoded = "\n".join(decoded.split("\n")[1:])  # remove 1st row, which is not data
    df = pd.read_csv(io.StringIO(decoded), sep="|")

    # df = pd.read_csv(urlData, encoding='latin1')
    # json_data = raw_data.json()
    # df = pd.DataFrame(json_data)
    return df


def make_data_file(n_results=5000):
    if not os.path.isfile("raw_data.csv"):
        df = get_data(n_results)
        df.to_csv("raw_data.csv")
    if not os.path.isfile("postal_codes.csv"):
        df = get_postal_code_data()
        df.to_csv("postal_codes.csv")


if __name__ == "__main__":
    make_data_file()
