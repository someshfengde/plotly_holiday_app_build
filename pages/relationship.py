import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")


# registering this page
dash.register_page(__name__, path="/relationship")


# reading the data
data = pd.read_csv("telco-customer-churn-by-IBM.csv")
data["TotalCharges"] = data["TotalCharges"].replace(" ", 0)
data["TotalCharges"] = data["TotalCharges"].astype("float")
data["MonthlyCharges"] = data["MonthlyCharges"].astype("float")
data["tenure"] = data["tenure"].astype("int")


internet_services_plot = px.histogram(
    data, x="InternetService", color="Churn", barmode="group"
)

contract_types_plot = px.histogram(data, x="Contract", color="Churn", barmode="group")

contract_payment_figure = px.sunburst(
    data, values="TotalCharges", path=["Contract", "PaymentMethod"]
)

tenure_vs_churn_figure = px.pie(
    data, values="tenure", names="Churn", title="Tenure vs churn", hole=0.3
)

streaming_movies_data = (
    pd.DataFrame(data["StreamingMovies"].value_counts())
    .reset_index(drop=False)
    .rename(columns={"index": "Type"})
)
streaming_services_fig = px.pie(
    streaming_movies_data, values="StreamingMovies", color="Type", hole=0.3
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("## contract, total charges and payment method."),
                        dcc.Graph(figure=contract_payment_figure),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("## relationship between tenure and churn"),
                        dcc.Graph(figure=tenure_vs_churn_figure),
                    ],
                    width=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("## How many customers have streaming services"),
                        dcc.Graph(figure=streaming_services_fig),
                    ], 
                    width = 6
                ),
                dbc.Col(
                    [
                        dcc.Markdown(
                            "## Which type of internet service customers are using?"
                        ),
                        dcc.Graph(figure=internet_services_plot),
                    ], 
                    width = 6
                ),
            ]
        ),
        dcc.Markdown("## Exploring the types of contracts"),
        dcc.Graph(figure=contract_types_plot),
    ]
)
