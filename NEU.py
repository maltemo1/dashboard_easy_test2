import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Neue Kategorien-Struktur definieren
categories = {
    "Überblick über Deutschlands Handel": {
        "Gesamtüberblick seit 2008 bis 2024": [
            "Gesamter Export-, Import- und Handelsvolumen-Verlauf Deutschlands"
        ],
        "Überblick nach bestimmtem Jahr": [
            "Monatlicher Handelsverlauf",
            "Top 10 Handelspartner: Länder mit dem höchsten Export-, Import- und Handelsvolumen",
            "Länder mit größten Export- und Importzuwächsen bzw. -rückgängen (absolut)",
            "Länder mit größten Export- und Importzuwächsen bzw. -rückgängen (relativ)",
            "Top 10 Waren: Wichtigste Export- und Importwaren",
            "Waren mit größten Export- und Importzuwächsen bzw. -rückgängen (absolut)",
            "Waren mit größten Export- und Importzuwächsen bzw. -rückgängen (relativ)"
        ]
    },
    "Länderanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [
            "Gesamter Export-, Import- und Handelsvolumen-Verlauf mit Deutschland (2008-2024)",
            "Gesamter Export-, Import- und Handelsvolumen-Verlauf mit Deutschland (2008-2024) im Vergleich zu anderen Ländern",
            "Export- und Importwachstumsrate",
            "Platzierung im Export- und Importranking Deutschlands",
            "Deutschlands Top 10 Waren im Handel mit dem Land (im gesamten Zeitraum 2008-2024)"
        ],
        "Überblick nach bestimmtem Jahr": [
            "Handelsbilanz-Überschuss bzw. -Defizit und Ranking des Landes",
            "Monatlicher Export-, Import- und Handelsvolumen-Verlauf mit Deutschland",
            "Top 10 Export- und Importwaren",
            "Top 4 Waren nach Differenz zum Vorjahr",
            "Top 4 Waren nach Wachstum zum Vorjahr"
        ],
        "Überblick nach bestimmter Ware": [
            "Gesamter Export- und Importverlauf einer bestimmten Ware (2008-2024) für das gewählte Land"
        ],
        "Überblick nach bestimmtem Jahr und Ware": [
            "Monatlicher Verlauf von Export- und Importwerten für die Ware im Jahr im Land"
        ],
        "Überblick nach bestimmtem Zeitraum, Waren und Ländern": [
            "Export- und Importverlauf (jährlich) bestimmter Waren für ein Land",
            "Export- und Importverlauf (jährlich) einer Ware für bestimmte Länder"
        ]
    },
    "Warenanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [
            "Gesamter Export- und Importverlauf der Ware",
            "Deutschlands Top 5 Export- und Importländer der Ware mit Verlauf"
        ],
        "Überblick mit mehreren Waren über bestimmten Zeitraum": [
            "Export- und Importverlauf der Waren (jährlich)",
            "Export- und Importverlauf der Waren (monatlich)"
        ],
        "Überblick nach bestimmtem Jahr": [
            "Ranking der Ware im Vergleich zu anderen Waren",
            "Monatlicher Export- und Importverlauf der Ware"
        ],
        "Überblick nach bestimmtem Land": [
            "Export- und Importverlauf der Ware für ein Land"
        ],
        "Überblick nach bestimmtem Zeitraum, Land und Waren": [
            "Export- und Importverlauf (jährlich) mehrerer Waren für ein Land",
            "Export- und Importverlauf (jährlich) einer Ware für mehrere Länder"
        ]
    }
}

# Funktion zur Erstellung der Sidebar-Elemente
def generate_sidebar():
    items = []
    for category, subcategories in categories.items():
        items.append(html.H5(category, className="mt-3"))
        for subcategory, sub_subcategories in subcategories.items():
            items.append(html.H6(subcategory, className="mt-2"))
            for sub_subcategory in sub_subcategories:
                items.append(
                    dbc.Button(
                        sub_subcategory,
                        href="#",  # Hier kann später eine spezifische URL gesetzt werden
                        color="link",
                        className="d-block text-start mb-1"
                    )
                )
    return items

# Layout der Sidebar
sidebar = html.Div(
    [
        html.H2("Navigation", className="display-4"),
        html.Hr(),
        *generate_sidebar()
    ],
    className="sidebar p-3"
)

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
