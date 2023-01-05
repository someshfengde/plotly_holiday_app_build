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
                dbc.NavLink("📈 Visualizations", href="/", id = "visualization_click", n_clicks = 0, style = {"font-weight": "bold"} ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink("Distribution", href="/", active="exact", ),
                            dbc.NavLink("Relationship", href="/relationship", active="exact"),
                            dbc.NavLink("Multiple distribution", href="/multiple_distribution", active="exact"),
                            dbc.NavLink("Trend", href="/trend", active="exact"),
                        ],
                        # vertical=True,
                        # pills=True,
                        # align the nav links to the left
                        style={"margin-left": "25px"},
                        horizontal = "center",
                    ),
                    id="collapse",

                    is_open=True,
                ),
                dbc.NavLink("🤖 Predictions", href="/prediction", active="exact"),
                dbc.NavLink("📕 Data", href="/data_render", active="exact"),
                 
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
                # only the page container will be updated with default page is home
                dbc.Col(
                    [
                        dash.page_container
                    ],
                    width=10,
                ),
            ]
        ),
    ]
)

@app.callback(
    Output("collapse", "is_open"),
    [Input("visualization_click", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n> 10:
        return not is_open
    return is_open


app.run_server(debug=True)


