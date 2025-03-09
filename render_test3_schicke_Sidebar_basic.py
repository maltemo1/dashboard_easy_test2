import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

# Dash-App erstellen
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Wichtig für Render

# Kategorien-Struktur definieren
categories = {
    "Export": {
        "Nach Waren": ["Maschinen", "Chemikalien", "Fahrzeuge"],
        "Nach Ländern": ["China", "USA", "Frankreich"]
    },
    "Import": {
        "Nach Waren": ["Energie", "Elektronik", "Textilien"],
        "Nach Ländern": ["Japan", "Russland", "Indien"]
    },
    "Handelsvolumen": {
        "Nach Regionen": ["Europa", "Asien", "Amerika"]
    }
}

# Funktion zum Erstellen der Sidebar
def create_sidebar():
    return html.Div([
        html.H2("Navigation", className="display-4"),
        html.Hr(),
        dbc.Accordion([
            dbc.AccordionItem([
                html.Div([
                    dbc.Button(
                        subcategory, id=f"subcategory-{subcategory}", color="secondary", className="mb-1",
                        n_clicks=0
                    ) for subcategory in subcategories.keys()
                ], className="d-grid gap-2")
            ], title=category)
            for category, subcategories in categories.items()
        ])
    ], className="sidebar")

# Beispiel-Funktion für einen Graphen
def create_gesamtueberblick_graph():
    df = pd.read_csv('data/1gesamt_deutschland.csv')
    fig = go.Figure()
    for col, name, color in zip(['gesamt_export', 'gesamt_import', 'gesamt_handelsvolumen'],
                                 ['Exportvolumen', 'Importvolumen', 'Gesamthandelsvolumen'],
                                 ['#1f77b4', '#ff7f0e', '#2ca02c']):
        fig.add_trace(go.Scatter(x=df['Jahr'], y=df[col], mode='lines+markers', name=name, line=dict(width=2, color=color)))
    return fig

# Layout der App
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Container([
        dbc.Row([
            dbc.Col(create_sidebar(), width=3),
            dbc.Col(html.Div(id='content'), width=9)
        ])
    ])
])

# Callback zur Navigation und zum Graphen-Update
@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)
def update_content(pathname):
    if pathname == '/gesamtueberblick':
        return dcc.Graph(figure=create_gesamtueberblick_graph())
    elif pathname == '/ueberblick_nach_jahr':
        return html.Div("Monatlicher Handelsverlauf nach Jahr (noch nicht implementiert)")
    elif pathname == '/laenderanalyse':
        return html.Div("Länderanalyse (noch nicht implementiert)")
    else:
        return html.Div("Wähle eine Kategorie aus der Sidebar")

if __name__ == '__main__':
    app.run_server(debug=True)
