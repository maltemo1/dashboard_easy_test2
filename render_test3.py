import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
