import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Initialisierung der Dash-App
app = dash.Dash(__name__)
server = app.server

# Struktur der Navigation mit Kategorien, Unterkategorien und Sub-Unterkategorien
navigation = {
    "Handelsstatistiken": {
        "Importe": {"Deutschland - Iran": "#", "Deutschland - EU": "#"},
        "Exporte": {"Deutschland - Iran": "#", "Deutschland - EU": "#"},
    },
    "Wirtschaftsanalysen": {
        "Markttrends": {"Automobilindustrie": "#", "Pharmaindustrie": "#"},
        "Wettbewerbsfähigkeit": {"Unternehmensanalysen": "#", "Branchenreports": "#"},
    },
    "Politische Rahmenbedingungen": {
        "Handelsabkommen": {"EU - Iran Abkommen": "#", "Deutschland - Iran Verträge": "#"},
        "Sanktionen": {"Aktuelle Maßnahmen": "#", "Historische Entwicklungen": "#"},
    },
}

# Layout der App mit versteckten Unterkategorien und Sub-Unterkategorien
app.layout = html.Div([
    html.H1("Dashboard Navigation"),
    html.Div(id="nav-container"),
    dcc.Store(id="selected-category", data=""),
    dcc.Store(id="selected-subcategory", data=""),
])

@app.callback(
    Output("nav-container", "children"),
    [Input("selected-category", "data"), Input("selected-subcategory", "data"),]
)
def update_navigation(selected_category, selected_subcategory):
    elements = []
    for category, subcategories in navigation.items():
        elements.append(html.Button(category, id={"type": "category-button", "index": category}))
        
        if selected_category == category:
            for subcategory, subsubcategories in subcategories.items():
                elements.append(html.Button("-- " + subcategory, id={"type": "subcategory-button", "index": subcategory}))
                
                if selected_subcategory == subcategory:
                    if isinstance(subsubcategories, dict):
                        for name, link in subsubcategories.items():
                            elements.append(html.A("---- " + name, href=link, target="_blank"))
    
    return elements

@app.callback(
    Output("selected-category", "data"),
    [Input({"type": "category-button", "index": dash.dependencies.ALL}, "n_clicks")],
    prevent_initial_call=True
)
def select_category(n_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    return ctx.triggered[0]["prop_id"].split(".")[0]

@app.callback(
    Output("selected-subcategory", "data"),
    [Input({"type": "subcategory-button", "index": dash.dependencies.ALL}, "n_clicks")],
    prevent_initial_call=True
)
def select_subcategory(n_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""
    return ctx.triggered[0]["prop_id"].split(".")[0]

if __name__ == "__main__":
    app.run_server(debug=True)
