import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.graph_objs as go


def assign_colors():
    colors = {"background": "#111111", "text": "#7FDBFF"}
    return colors


def make_scatterplot():
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


def run_app(df, colors):
    app = dash.Dash()
    app.layout = dhtml.Div(
        children=[
            dhtml.H1(
                "Gas prices in Mexico",
                style={"textAlign": "center", "color": colors["text"]},
            ),
            regular_premium_scatterplot,
        ],
        style={"backgroundColor": colors["background"]},
    )
    app.run_server()


def main():
    df = None  # read data
    colors = assign_colors()
    run_app(df, colors)


if __name__ == "__main__":
    main()
