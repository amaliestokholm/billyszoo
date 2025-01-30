import dash
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output, ClientsideFunction

# Sample data
data = {
    "x": [1, 2, 3, 4, 5],
    "y": [10, 15, 7, 12, 9],
    "z": [2, 3, 4, 5, 6],
    "label": ["A", "B", "C", "D", "E"],
    "category": ["cat1", "cat2", "cat1", "cat2", "cat1"],
    "description": [
        "Point A:\n- Important note\n- More details here",
        "Point B:\n- Another description\n- Click to explore",
        "Point C:\n- Data insights\n- Key metrics available",
        "Point D:\n- Interesting fact\n- Research link",
        "Point E:\n- Final point\n- Summary section",
    ],
    "qr_links": [
        "https://example.com/A",
        "https://example.com/B",
        "https://example.com/C",
        "https://example.com/D",
        "https://example.com/E",
    ],
}

# Create initial scatter plots
fig1 = px.scatter(x=data["x"], y=data["y"], text=data["label"])
fig1.update_traces(mode="markers+text", textposition="top center")
fig1.update_layout(dragmode=False)

fig2 = px.scatter(x=data["x"], y=data["z"], text=data["label"])
fig2.update_traces(mode="markers+text", textposition="top center")

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Interactive Scatter Plot with QR Codes"),
        dcc.Graph(
            id="scatter-plot1",
            figure=fig1,
            config={"scrollZoom": False, "displayModeBar": False},
        ),
        dcc.Graph(
            id="scatter-plot2",
            figure=fig2,
            config={"scrollZoom": False, "displayModeBar": False},
        ),
        html.Div(id="qr-container", children=[], style={"text-align": "center", "margin-top": "10px"}),
        dcc.Store(id="data-store", data=data),  # Store data client-side
    ]
)

# Clientside callback for handling click interactions
app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="updateAnnotationsAndQR"
    ),
    [
        Output("scatter-plot1", "figure"),
        Output("scatter-plot2", "figure"),
        Output("qr-container", "children"),
    ],
    [Input("scatter-plot1", "clickData"), Input("data-store", "data")],
)

if __name__ == "__main__":
    app.run_server(debug=True)
