import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")


# registering this page
dash.register_page(__name__, path = "/")
# reading the data
data = pd.read_csv("telco-customer-churn-by-IBM.csv")

churn_tenure_figure = px.histogram(
    data,
    x="tenure",
    color="Churn",
    marginal="box",
    hover_data=data.columns,
    opacity= 0.8
    # title="Relationship between churn and tenure",
)


layout = html.Div(
    [
        html.H2("Relationship between churn and tenure"),
        # html.Hr(),
        dcc.Graph(figure=churn_tenure_figure),
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
