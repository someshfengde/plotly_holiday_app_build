import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")


# registering this page
dash.register_page(__name__, path = "/multiple_distribution")
# reading the data
# data = pd.read_csv("telco-customer-churn-by-IBM.csv")


layout = html.Div(
    [
        dcc.Markdown("""
        # Distribution of churn by a single feature:
            - Gender distribution
            - Senior citizen distribution
            - Dependents distribution
            - Phone service distribution
            - Internet service distribution
            - Contract type distribution
            - Paperless billing distribution
            - Payment method distribution
        """)
    ]
)
