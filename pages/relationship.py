
import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")


# registering this page
dash.register_page(__name__, path = "/relationship")


# reading the data
data = pd.read_csv("telco-customer-churn-by-IBM.csv")


layout = html.Div(
    [
        dcc.Markdown("""
        # Relationship between two variables:
            - Tenure vs churn
            - Monthly charges vs total charges
            - Tenure vs monthly charges
            - Tenure vs total charges
        """)
    ]
)
