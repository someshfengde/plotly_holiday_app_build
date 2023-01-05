
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
data["TotalCharges"] = data["TotalCharges"].replace(" ", 0)
data["TotalCharges"] = data["TotalCharges"].astype("float")
data["MonthlyCharges"] = data["MonthlyCharges"].astype("float")
data["tenure"] = data["tenure"].astype("int")


tenure_vs_churn_figure = px.scatter(data, x = "tenure", y = "Churn", color = "Churn", opacity = 0.8)

layout = html.Div(
    [
        dcc.Markdown("# Relationship between two variables"),
        dcc.Markdown("## tenure and churn relationship"), 
        dcc.Graph(id = "tenure_vs_churn", figure = tenure_vs_churn_figure),
        dcc.Markdown("## Monthly charges and total charges relationship"),
        dcc.Graph(figure = px.scatter(data, x = "MonthlyCharges", y = "TotalCharges", color = "Churn", opacity = 0.8, size = "TotalCharges")),
        dcc.Markdown("## tenure and monthly charges relationship"),
        dcc.Graph(figure = px.scatter(data, x = "tenure", y = "MonthlyCharges", color = "Churn", opacity = 0.8)),
        dcc.Markdown("## tenure and total charges relationship"),
        dcc.Graph(figure = px.scatter(data, x = "tenure", y = "TotalCharges", color = "Churn", opacity = 0.8)),

        dcc.Markdown("""
        # Relationship between two variables:
            - Tenure vs churn
            - Monthly charges vs total charges
            - Tenure vs monthly charges
            - Tenure vs total charges
        """)
    ]
)
