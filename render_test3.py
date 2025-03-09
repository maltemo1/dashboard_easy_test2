import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Kategorien-Struktur definieren
categories = {
    "Überblick über Deutschlands Handel": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": []
    },
    "Länderanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": {
            "Anzeige über Handelsbilanz-Überschuss bzw. -Defizit und Ranking des Landes (im Vergleich zu anderen Ländern)": [],
            "Monatlicher Export-, Import- und Handelsvolumen-Verlauf mit Deutschland": [],
            "Top 10 Export- und Importwaren": []
        },
        "Überblick nach bestimmter Ware": [],
        "Überblick nach bestimmtem Jahr und Ware": [],
        "Überblick nach bestimmtem Zeitraum und Waren und Zeitraum": []
    },
    "Warenanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick mit mehreren Waren über bestimmten Zeitraum": [],
        "Überblick nach bestimmtem Jahr": [],
        "Überblick nach bestimmtem Land": [],
        "Überblick nach bestimmtem Zeitraum und Land und Waren": []
    }
}

# Layout der Sidebar
sidebar = html.Div([
    html.H2("Navigation", className="display-4"),
    html.Hr(),
    html.Div([
        dbc.Button(
            category, id=f"category-{category}", color="primary", className="mb-2", n_clicks=0
        )
        for category in categories.keys()
    ], className="d-grid gap-2"),
    html.Div(id="subcategory-container")
], className="sidebar")

# Callback für das Anzeigen der Unterkategorien
@app.callback(
    Output("subcategory-container", "children"),
    [Input(f"category-{category}", "n_clicks") for category in categories.keys()]
)
def display_subcategories(*clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    category = button_id.replace("category-", "")
    
    subcategories = categories.get(category, {})
    return html.Div([
        dbc.Button(
            subcategory, id=f"subcategory-{subcategory}", color="secondary", className="mb-1", n_clicks=0
        )
        for subcategory in subcategories.keys()
    ], className="d-grid gap-2")

# Callback für das Anzeigen der Sub-Subkategorien
@app.callback(
    Output("subcategory-container", "children", allow_duplicate=True),
    [Input(f"subcategory-{subcategory}", "n_clicks") for subcategory in categories["Länderanalyse"]["Überblick nach bestimmtem Jahr"].keys()],
    prevent_initial_call=True
)
def display_sub_subcategories(*clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    subcategory = button_id.replace("subcategory-", "")
    
    sub_subcategories = categories["Länderanalyse"].get("Überblick nach bestimmtem Jahr", {}).get(subcategory, [])
    return html.Div([
        dbc.Button(
            sub_subcategory, id=f"sub-subcategory-{sub_subcategory}", color="info", className="mb-1", n_clicks=0
        )
        for sub_subcategory in sub_subcategories
    ], className="d-grid gap-2")

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(sidebar, width=3),
            dbc.Col(html.Div("Inhalt des Dashboards"), width=9)
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
