import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True)

sidebar_structure = {
    "Überblick über Deutschlands Handel": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": []
    },
    "Länderanalyse": {
        "Gesamtüberblick seit 2008 bis 2024": [],
        "Überblick nach bestimmtem Jahr": [
            "Anzeige_Handelsbilanz_Ueberschuss_Defizit_Ranking",
            "Monatlicher_Export_Import_Handelsvolumen_Verlaub",
            "Top_10_Export_Importwaren"
        ],
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

def generate_sidebar():
    sidebar = []
    for main_category, subcategories in sidebar_structure.items():
        subcategory_elements = []
        for subcategory, subsubcategories in subcategories.items():
            if subsubcategories:
                subsub_elements = [
                    html.Li(html.A(subsub, href=f"#{subsub}"), className="nav-subsubitem")
                    for subsub in subsubcategories
                ]
                subcategory_elements.append(
                    html.Li([
                        html.A(subcategory, href=f"#{subcategory}", className="nav-subitem"),
                        html.Ul(subsub_elements, className="nav-subsublist")
                    ])
                )
            else:
                subcategory_elements.append(html.Li(html.A(subcategory, href=f"#{subcategory}"), className="nav-subitem"))
        sidebar.append(
            html.Li([
                html.A(main_category, href=f"#{main_category}", className="nav-item"),
                html.Ul(subcategory_elements, className="nav-sublist")
            ])
        )
    return html.Ul(sidebar, className="nav-list")

app.layout = html.Div([
    html.Nav(generate_sidebar(), className="sidebar"),
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    [Input(f"{subcategory}", "n_clicks") for main_category in sidebar_structure.values() for subcategory in main_category]
)
def display_page(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "Wählen Sie eine Kategorie aus."
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    return html.Div(f"Inhalt für {button_id}")

if __name__ == "__main__":
    app.run_server(debug=True)
