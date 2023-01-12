import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from pycaret.classification import *

# registering this page
dash.register_page(__name__)
model = load_model("lr_model")

# collecting the information on gender, Seniorcitizen, partner, dependents, tenure, phone serivice, multiplephonelines, internetservice, online backup, deviceprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges
demographics = dbc.Row(
    [
        html.H1("Demographics"),
        html.Br(),
        html.Br(),
        dbc.Col(
            [
                html.H3("Gender"),
                dbc.RadioItems(
                    options=[
                        {"label": "Female", "value": "Female"},
                        {"label": "Male", "value": "Male"},
                    ],
                    value="Female",
                    id="gender-selection",
                ),
            ],
            width=2,
        ),
        dbc.Col(
            [
                html.H3("Senior Citizen"),
                dbc.RadioItems(
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    id="seniorcitizen-selection",
                    value=1,
                ),
            ],
            width=3,
        ),
        dbc.Col(
            [
                html.H3("Married"),
                dbc.RadioItems(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                    ],
                    value="Yes",
                    id="married-selection",
                ),
            ],
            width=2,
        ),
        dbc.Col(
            [
                html.H3("Dependents"),
                dbc.RadioItems(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                    ],
                    value="Yes",
                    id="dependents-selection",
                ),
            ]
        ),
    ]
)

services = dbc.Col(
    [
        html.H1("Services"),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Tenure"),
                        dbc.Input(
                            type="number",
                            id="tenure-selection",
                            value=1,
                            min=1,
                            max=72,
                            step=1,
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Phone Service"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                            ],
                            value="Yes",
                            id="phoneservice-selection",
                        ),
                    ],
                    width=2,
                ),
                # if the phone service is no then hide multiple phone service
                dbc.Col(
                    [
                        html.H3("Multiple Phone Lines"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Phone Service",
                                    "value": "No Phone Service",
                                },
                            ],
                            value="Yes",
                            id="multiplephonelines-selection",
                        ),
                    ],
                    id="multiplephonelines-col",
                    width=3,
                ),
                dbc.Col(
                    [
                        html.H3("Internet Service"),
                        dbc.RadioItems(
                            options=[
                                {"label": "DSL", "value": "DSL"},
                                {"label": "Fiber Optic", "value": "Fiber Optic"},
                                {"label": "No", "value": "No"},
                            ],
                            value="DSL",
                            id="internetservice-selection",
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Online Security"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="onlinesecurity-selection",
                        ),
                    ],
                    id="onlinesecurity-col",
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Online Backup"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="onlinebackup-selection",
                        ),
                    ],
                    width=2,
                    id="onlinebackup-col",
                ),
                dbc.Col(
                    [
                        html.H3("Device Protection"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="deviceprotection-selection",
                        ),
                    ],
                    id="deviceprotection-col",
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Tech Support"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="techsupport-selection",
                        ),
                    ],
                    width=2,
                    id="techsupport-col",
                ),
                dbc.Col(
                    [
                        html.H3("Streaming TV"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="streamingtv-selection",
                        ),
                    ],
                    width=2,
                    id="streamingtv-col",
                ),
                dbc.Col(
                    [
                        html.H3("Streaming Movies"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {
                                    "label": "No Internet Service",
                                    "value": "No Internet Service",
                                },
                            ],
                            value="Yes",
                            id="streamingmovies-selection",
                        ),
                    ],
                    width=2,
                    id="streamingmovies-col",
                ),
            ],
            id="internet-services-row",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Contract"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Month-to-month", "value": "Month-to-month"},
                                {"label": "One year", "value": "One year"},
                                {"label": "Two year", "value": "Two year"},
                            ],
                            value="Month-to-month",
                            id="contract-selection",
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Paperless Billing"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                            ],
                            value="Yes",
                            id="paperlessbilling-selection",
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Payment Method"),
                        dbc.RadioItems(
                            options=[
                                {
                                    "label": "Bank Transfer (automatic)",
                                    "value": "Bank Transfer (automatic)",
                                },
                                {
                                    "label": "Credit Card (automatic)",
                                    "value": "Credit Card (automatic)",
                                },
                                {
                                    "label": "Electronic Check",
                                    "value": "Electronic Check",
                                },
                                {"label": "Mailed Check", "value": "Mailed Check"},
                            ],
                            value="Bank Transfer (automatic)",
                            id="paymentmethod-selection",
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Monthly Charges"),
                        dbc.Input(
                            type="number",
                            id="monthlycharges-selection",
                            value=18.8,
                            min=18.8,
                            max=118.75,
                            step=0.1,
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        html.H3("Total Charges"),
                        dbc.Input(
                            type="number",
                            id="totalcharges-selection",
                            value=18.8,
                            min=18.8,
                            max=118.75,
                            step=0.1,
                        ),
                    ],
                    width=2,
                ),
            ]
        ),
    ],
)

predict_button = dbc.Button(
    "Predict",
    id="predict_button",
    color="primary",
    n_clicks=0,
)

# callback for phone service
# hiding multiple phone lines if no phone service
@callback(
    Output("multiplephonelines-col", "style"),
    Output("multiplephonelines-selection", "value"),
    [Input("phoneservice-selection", "value")],
    supress_initial_call=True,
)
def hide_multiplephonelines(value):
    if value == "No":
        return {"display": "none"}, "No phone service"
    else:
        return {"display": "block"}, "No"


# callback for internet service
# hiding internet services if no internet service
@callback(
    [
        [
            Output("onlinebackup-col", "style"),
            Output("onlinebackup-selection", "value"),
        ],
        [
            Output("deviceprotection-col", "style"),
            Output("deviceprotection-selection", "value"),
        ],
        [Output("techsupport-col", "style"), Output("techsupport-selection", "value")],
        [Output("streamingtv-col", "style"), Output("streamingtv-selection", "value")],
        [
            Output("streamingmovies-col", "style"),
            Output("streamingmovies-selection", "value"),
        ],
        [
            Output("onlinesecurity-col", "style"),
            Output("onlinesecurity-selection", "value"),
        ],
    ],
    [Input("internetservice-selection", "value")],
    supress_initial_call=True,
)
def hide_internetservices(value):
    if value == "No":
        return [[{"display": "none"}, "No Internet Service"]] * 6
    else:
        return [[{"display": "block"}, "Yes"]] * 6


@callback(
    Output("prediction_content", "children"),
    [
        Input("predict_button", "n_clicks"),
    ],
    [
        State("gender-selection", "value"),
        State("seniorcitizen-selection", "value"),
        State("married-selection", "value"),
        State("dependents-selection", "value"),
        State("tenure-selection", "value"),
        State("phoneservice-selection", "value"),
        State("multiplephonelines-selection", "value"),
        State("internetservice-selection", "value"),
        State("onlinesecurity-selection", "value"),
        State("onlinebackup-selection", "value"),
        State("deviceprotection-selection", "value"),
        State("techsupport-selection", "value"),
        State("streamingtv-selection", "value"),
        State("streamingmovies-selection", "value"),
        State("contract-selection", "value"),
        State("paperlessbilling-selection", "value"),
        State("paymentmethod-selection", "value"),
        State("monthlycharges-selection", "value"),
        State("totalcharges-selection", "value"),
    ],
    supress_initial_call=True,
)
def predict_churn(
    n_click,
    gender,
    seniorcitizen,
    partner,
    dependents,
    tenure,
    phoneservice,
    multiplephonelines,
    internetservice,
    onlinesecurity,
    onlinebackup,
    deviceprotection,
    techsupport,
    streamingtv,
    streamingmovies,
    contract,
    paperlessbilling,
    paymentmethod,
    monthlycharges,
    totalcharges,
):
    if n_click > 0:
        # create dataframe from inputs
        cols = [
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges",
        ]
        df = pd.DataFrame(
            columns=cols,
            data=[
                [
                    gender,
                    seniorcitizen,
                    partner,
                    dependents,
                    tenure,
                    phoneservice,
                    multiplephonelines,
                    internetservice,
                    onlinesecurity,
                    onlinebackup,
                    deviceprotection,
                    techsupport,
                    streamingtv,
                    streamingmovies,
                    contract,
                    paperlessbilling,
                    paymentmethod,
                    monthlycharges,
                    totalcharges,
                ]
            ],
        )
        # predict churn
        prediction = predict_model(model, data=df)
        # print(prediction)
        # return prediction
        return html.H2(f"Predicted Churn: {prediction['prediction_label'][0]}")


information_collection_form = dbc.Form([demographics, services, predict_button])

layout = html.Div(
    [
        html.Br(),
        html.H1("Predicting new customer churn with Logistic Regression model"),
        html.Hr(),
        information_collection_form,
        html.Hr(),
        html.Div(id="prediction_content", className="lead"),
    ]
)
