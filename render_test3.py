import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Neue Kategorien-Struktur definieren
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

# Funktion, um Unterkategorien zu rendern
def render_subcategories(subcategories):
    return [
        dbc.AccordionItem(
            dbc.Button(
                subcategory, id=f"subcategory-{subcategory}", color="secondary", className="mb-1", n_clicks=0
            ),
            title=subcategory
        )
        for subcategory in subcategories.keys()
    ]

# Layout der Sidebar
sidebar = html.Div([
    html.H2("Navigation", className="display-4"),
    html.Hr(),
    dbc.Accordion([
        dbc.AccordionItem(
            dbc.Accordion([
                *render_subcategories(subcategories)
            ], start_collapsed=True),
            title=category
        )
        for category, subcategories in categories.items()
    ], start_collapsed=True)
], className="sidebar")

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
