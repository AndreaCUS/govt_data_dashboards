import os
import requests
import pandas as pd


def get_data(n_results):
    url = "https://api.datos.gob.mx/v1/precio.gasolina.publico?pageSize={}".format(
        n_results
    )
    raw_data = requests.get(url)
    json_data = raw_data.json()

    return json_data


def save_data(json_data, n_results):
    df = pd.DataFrame(json_data["results"], index=list(range(0, n_results)))
    df.to_csv("raw_data.csv")
    pass


def make_data_file(n_results=5000):
    if not os.path.isfile("raw_data.csv"):
        json_data = get_data(n_results)
        save_data(json_data, n_results)
