from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import dash 
from dash_iconify import DashIconify
import dash_mantine_components as dmc

# designing the frontend page with dash for customer chrun data
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX, dbc_css],
    title="dash holiday challenge",
    use_pages=True,
    update_title="...🎄",
)

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-RWE73D8GQY"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-RWE73D8GQY');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""

application = app.server
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
        html.Br(),
        html.H2("Telco", className="display-4"),
        html.Hr(),
        html.P(
            "This dashboard based on the data provided by telco via IBM.",
            className="lead",
        ),
        dbc.Nav(
            [
                dbc.NavLink(
                    "📈 Visualizations",
                    href="/",
                    id="visualization_click",
                    n_clicks=0,
                    style={"font-weight": "bold"},
                ),
                dbc.Collapse(
                    dbc.Nav(
                        dbc.Row([
                            dbc.NavLink(
                                "Page-1",
                                href="/",
                                active="exact",
                            ),
                            dbc.NavLink(
                                "Page-2", href="/relationship", active="exact"
                            ),
                        ]),
                        style={"margin-left": "25px"},
                        horizontal="center",
                    ),
                    id="collapse",
                    is_open=True,
                ),
                dbc.NavLink("🤖 Predictions", href="/prediction", active="exact"),
                dbc.NavLink("📕 Data", href="/data_render", active="exact"),
                html.Hr(), 
                html.Br(), 
                html.Br(),
                dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    "👨‍🎓 Resume",
                                    href="https://drive.google.com/file/d/1qiwgoT_KfCb9rA6S-8bOT25Jeh7Z7ayG/view?usp=sharing",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "🕸️ LinkedIn",
                                    href="https://www.linkedin.com/in/somesh-9188",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "😺 GitHub",
                                    href="https://github.com/someshfengde",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "🌐 Portfolio",
                                    href="https://somesh.gitbook.io/somesh-fengade/",
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "⬆️ Upwork",
                                    href="https://www.upwork.com/freelancers/~01d21fd7991660718f",
                                    target="_blank",
                                ),
                            ],
                            vertical=True,
                        ),
                        title="My Socials",
                    )
                ],
                always_open = True
                
            ),
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
                        width=11,
                    ),
                    dbc.Col([
                            dbc.NavLink(DashIconify("github", icon="ion:logo-github",width = 50 ,  color = "white",),href = "https://github.com/someshfengde/plotly_holiday_app_build", target = "_blank"),
                    ])
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
                    [dash.page_container],
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
    if n > 10:
        return not is_open
    return is_open

if __name__ == "__main__":
    application.run(debug=False , port = 8080)
