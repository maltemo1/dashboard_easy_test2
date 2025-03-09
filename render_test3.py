import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # WICHTIG: Server-Objekt exportieren

# Sidebar-Menüstruktur
menu_structure = {
    "Überblick über Deutschlands Handel": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": []
    },
    "Länderanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": {
            "Handelsbilanz-Überschuss/Defizit & Ranking": [],
            "Monatlicher Export-, Import- & Handelsvolumen-Verlauf": [],
            "Top 10 Export- und Importwaren": []
        },
        "Überblick nach bestimmter Ware": [],
        "Überblick nach bestimmtem Jahr & Ware": [],
        "Überblick nach Zeitraum, Waren & Zeitraum": []
    },
    "Warenanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick mit mehreren Waren über Zeitraum": [],
        "Überblick nach bestimmtem Jahr": [],
        "Überblick nach bestimmtem Land": [],
        "Überblick nach Zeitraum, Land & Waren": []
    }
}

# Layout und Callback-Funktion bleiben unverändert

if __name__ == "__main__":
    app.run_server(debug=True)
