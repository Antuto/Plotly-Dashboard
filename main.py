from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

colorscales = px.colors.named_colorscales()

# Add data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = [
        html.H1(children='Global Dashboard'),
        html.P("Color Scale"),
        dcc.Dropdown(id="dropdown", options=colorscales, value="viridis",style={'width': '30%'}),
        dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
        dcc.Graph(id='graph',style={'width': '100%', 'height': '80vh'})
    ]

# Add controls to build the interaction
@app.callback(
    Output("graph", "figure"),
    Input('controls-and-radio-item','value'),
    Input("dropdown","value")
)
def change_colorscale(scale,color):
    fig = px.scatter(
        df,
        x="country",
        y=scale,
        color=scale,
        color_continuous_scale=color,
        template = "plotly_dark"
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
