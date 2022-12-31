from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import dash

# designing the frontend page with dash for customer chrun data
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX, dbc_css],
    title="dash holiday challenge",
    use_pages=True,
    update_title="...🎄",
)
server = app.server
app._favicon = "favicon.ico"
# creating the layout of the page

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 70,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "border-radius": "30px",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Telco", className="display-4"),
        html.Hr(),
        html.P(
            "This dashboard based on the data provided by telco via IBM.",
            className="lead",
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Predictions", href="/prediction", active="exact"),
                dbc.NavLink("Data", href="/data_render", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

app.layout = html.Div(
    [
        # adding the dbc navbar to the page
        dbc.Row(
            dbc.Navbar(
                children=[
                    dbc.Col(
                        [
                            html.H1(
                                "🎄Customer Segmentation Dashboard🎄",
                                className="text-white text-center",
                            )
                        ],
                        width=12,
                    )
                ],
                sticky="top",
                color="primary",
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar,
                    ],
                    width=2,
                ),
                dbc.Col([dash.page_container], width=10),
            ]
        ),
    ]
)
app.run_server(debug=True)
