import os
import dash

# import dash_core_components as dcc
from dash import dcc

# import dash_html_components as dhtml
from dash import html
import plotly.graph_objs as go
import pandas as pd


def get_data():
    if os.path.exists("clean_data.csv") and os.path.exists("aggregate_data.csv"):
        df = pd.read_csv("clean_data.csv")
        df_aggr = pd.read_csv(("aggregate_data.csv"))
        return df, df_aggr
    else:
        return None, None


def assign_colors():
    colors = {"background": "#d0d2d6", "text": "#292d33"}
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


def get_price_heatmap(df):
    price_heatmap = dcc.Graph(
        id="price_heatmap",
        figure={
            "data": [
                go.Heatmap(
                    x=df["longitude_int"],
                    y=df["latitude_int"],
                    z=df["regular_mean"].values.tolist(),
                    # zsmooth = 'fast',
                )
            ],
            "layout": go.Layout(
                title="Mean gas prices by latitude and longitude",
                xaxis={"title": "Longitude"},
                yaxis={"title": "Latitude", "scaleanchor": "x"},
            ),
        },
    )
    return price_heatmap


def run_dash_app(host, port, debug):
    df, aggr_df = get_data()

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
                # get_KPIs(df),
                get_regular_premium_scatterplot(df),
                get_price_heatmap(aggr_df),
            ],
            style={"backgroundColor": colors["background"]},
        )
        app.run_server(host=host, port=port, debug=debug)
