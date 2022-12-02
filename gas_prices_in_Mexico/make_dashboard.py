import os
import dash

# import dash_core_components as dcc
from dash import dcc

# import dash_html_components as dhtml
from dash import html
import plotly.graph_objs as go
import pandas as pd


def get_data():
    if os.path.exists("clean_data.csv"):
        df = pd.read_csv("clean_data.csv")
        return df
    else:
        return None


def assign_colors():
    colors = {"background": "#111111", "text": "#7FDBFF"}
    return colors


def get_regular_premium_scatterplot(df):
    regular_premium_scatterplot = dcc.Graph(
        id="regular_premium_scatterplot",
        figure={
            "data": [
                go.Scatter(
                    x=df["regular"],
                    y=df["premium"],
                    mode="markers",
                    marker={
                        "size": 12,
                        "color": "rgb(51,204,153)",
                        "symbol": "pentagon",
                    },
                )
            ],
            "layout": go.Layout(
                title="Regular vs. Premium gas prices",
                xaxis={"title": "Regular gas"},
                yaxis={"title": "Premium gas"},
            ),
        },
    )
    return regular_premium_scatterplot


def run_dash_app(host, port, debug):
    df = get_data()

    if df is None:
        print("Datafile does not exist")
    else:
        colors = assign_colors()

        app = dash.Dash()
        app.layout = html.Div(
            children=[
                html.H1(
                    "Gas prices in Mexico",
                    style={"textAlign": "center", "color": colors["text"]},
                ),
                get_regular_premium_scatterplot(df),
            ],
            style={"backgroundColor": colors["background"]},
        )
        app.run_server(host=host, port=port, debug=debug)
