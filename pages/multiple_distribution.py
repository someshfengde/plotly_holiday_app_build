import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")

data = pd.read_csv("telco-customer-churn-by-IBM.csv")
# registering this page
dash.register_page(__name__, path = "/multiple_distribution")
# reading the data
# data = pd.read_csv("telco-customer-churn-by-IBM.csv")


layout = html.Div(
    [
        dcc.Markdown("# Distribution of a variable by two or more features"),
        dcc.Markdown("## Heatmap showing the relationship between churn and various features"),
        dcc.Graph(figure = px.density_heatmap(data, y = "Churn", marginal_x = "histogram", marginal_y = "histogram")),
        dcc.Markdown("## Stacked bar chart showing the distribution of churn by multiple features"),
        dcc.Graph(figure = px.bar(data, x = "Churn", y = "tenure", color = "Contract", barmode = "group")),
        dcc.Markdown("## Box plot showing the distribution of total charges by churn status and internet service type"),
        dcc.Graph(figure = px.box(data, x = "Churn", y = "TotalCharges", color = "InternetService")),
        dcc.Markdown("## Violin plot showing the distribution of monthly charges by contract type and churn status"),
        dcc.Graph(figure = px.violin(data, x = "Contract", y = "MonthlyCharges", color = "Churn", box = True, points = "all")),

        dcc.Markdown("""
            # Distribution of a variable by two or more features:
                - Heatmap showing the relationship between churn and various features (e.g. gender, senior citizen status, phone service status, internet service type).-
                - Stacked bar chart showing the distribution of churn by multiple features (e.g. internet service type, contract type, and payment method).
                - Box plot showing the distribution of total charges by churn status and internet service type.
                - Violin plot showing the distribution of monthly charges by contract type and churn status.
        """)
    ]
)
