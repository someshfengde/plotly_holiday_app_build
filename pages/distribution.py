import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# adding theme to the page
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")


# registering this page
dash.register_page(__name__, path="/")
# reading the data
data = pd.read_csv("telco-customer-churn-by-IBM.csv")

churn_tenure_figure = px.histogram(
    data,
    x="tenure",
    color="Churn",
    marginal="box",
    hover_data=data.columns,
    opacity=0.8
    # title="Relationship between churn and tenure",
)

gender_churn_figure = px.histogram(
    data,
    x="gender",
    color="Churn",
)


columns_sorted_feat_imp = [
    "tenure",
    "MonthlyCharges",
    "InternetService",  # high in case of fiber optic # mid
    "Contract",  # high in case of tag is year # mid in month to month
    "StreamingMovies",
    "PaperlessBilling",
    "MultipleLines",
    "StreamingTV",
    "PaymentMethod",
    "OnlineSecurity",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "TotalCharges",
    "PhoneService",
    "gender",
]

married_unmarried_dist = px.pie(
    data,
    names="Partner",
    title="Married vs unmarried clients",
)

gender_male_female = px.pie(data, names="gender", title="Male vs female clients")

layout = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("## How many customers are married?"),
                        # Let's see distribution of married vs unmarried clients
                        dcc.Graph(
                            id="married-unmarried-dist", figure=married_unmarried_dist
                        ),
                    ],
                    width=5,
                ),
                dbc.Col(
                    [
                        dcc.Markdown("## What's the gender distribution in data?"),
                        dcc.Graph(figure=gender_male_female),
                    ],
                    width=5,
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Number of customers"),
                                dbc.CardBody(html.H1(len(data))),
                            ],
                            style={"text-align": "center"},
                        ),
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Maximum tenure"),
                                dbc.CardBody(html.H1(data["tenure"].max())),
                            ],
                            style={"text-align": "center"},
                        ),
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader("Maximum monthly charges"),
                                dbc.CardBody(html.H1(data["MonthlyCharges"].max())),
                            ],
                            style={"text-align": "center"},
                        ),
                    ],
                    width=2,
                ),
            ]
        ),
        dcc.Markdown(
            """
        # Distribution of churn by single feature
        > Sorted top to bottom based on `feature importance`. 
        """
        ),
        dcc.Markdown(
            "Select feature to see distribution of churn across that feature:"
        ),
        dcc.Dropdown(
            id="distribution_feature",
            options=columns_sorted_feat_imp,
            value="tenure",
            clearable=False,
        ),
        dcc.Graph(id="churn_dist"),
        # dcc.Markdown(
        #     """
        # # Distribution of churn by a single feature:
        #     - Gender distribution
        #     - Senior citizen distribution
        #     - Dependents distribution
        #     - Phone service distribution
        #     - Internet service distribution
        #     - Contract type distribution
        #     - Paperless billing distribution
        #     - Payment method distribution
        # """
        # ),
    ]
)


@callback(
    Output("churn_dist", "figure"),
    Input("distribution_feature", "value"),
)
def update_churn_dist(feature):
    return px.histogram(
        data,
        x=feature,
        color="Churn",
        marginal="violin",
        hover_data=data.columns,
        opacity=0.8,
        title=f"Relationship between churn and {feature}",
    )
