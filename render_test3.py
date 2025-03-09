import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Kategorien-Struktur
categories = {
    "Überblick über Deutschlands Handel": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": []
    },
    "Länderanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": {
            "Anzeige über Handelsbilanz-Überschuss bzw. -Defizit und Ranking des Landes": "#",
            "Monatlicher Export-, Import- und Handelsvolumen-Verlauf mit Deutschland": "#",
            "Top 10 Export- und Importwaren": "#"
        },
        "Überblick nach bestimmter Ware": [],
        "Überblick nach bestimmtem Jahr und Ware": []
    },
    "Warenanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": [],
        "Überblick nach bestimmtem Land": []
    }
}

# Layout der Sidebar
sidebar = html.Div([
    html.H2("Navigation", className="display-4"),
    html.Hr(),
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                html.Div(
                                    [
                                        dbc.Button(
                                            subcategory, 
                                            id={"type": "toggle-subcategory", "index": subcategory}, 
                                            color="link", className="mb-1"
                                        ),
                                        dbc.Collapse(
                                            html.Div(
                                                [
                                                    html.A(name, href=link, target="_blank", className="d-block")
                                                    for name, link in subsubcategories.items()
                                                ],
                                            ),
                                            id={"type": "collapse-subcategory", "index": subcategory},
                                            is_open=False
                                        )
                                    ]
                                ),
                                title=subcategory
                            )
                            for subcategory, subsubcategories in subcategories.items()
                        ], start_collapsed=True
                    )
                ],
                title=category
            )
            for category, subcategories in categories.items()
        ], start_collapsed=True
    )
], className="sidebar")

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(sidebar, width=3),
            dbc.Col(html.Div("Inhalt des Dashboards"), width=9)
        ])
    ])
])

# Callbacks zum Öffnen/Schließen der Subkategorien
@app.callback(
    Output({"type": "collapse-subcategory", "index": dash.dependencies.ALL}, "is_open"),
    Input({"type": "toggle-subcategory", "index": dash.dependencies.ALL}, "n_clicks"),
    prevent_initial_call=True
)
def toggle_subcategory(n_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return [False] * len(n_clicks)
    index = ctx.triggered[0]["prop_id"].split(".")[0]
    return [not n if idx == index else False for idx, n in zip(n_clicks, n_clicks)]

if __name__ == "__main__":
    app.run_server(debug=True)
