import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# displaying dash table of hte telco customer churrn data
# Path: pages/data_render.py

df = pd.read_csv("telco-customer-churn-by-IBM.csv")

# registering this page
dash.register_page(__name__, path="/data_render")

layout = html.Div(
    [
        html.H1("Data"),
        html.Hr(),
        html.P("This is the data used for the predictions"),
        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            editable=True,
            cell_selectable=True,
            filter_action="native",
            sort_action="native",
            page_size=20,  # we have less data in this example, so setting to 20
            style_table={"overflowY": "auto"},
        ),
    ]
)
