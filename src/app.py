from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table
from callbacks import update_donut_chart, update_stacked_chart_race, update_stacked_chart_education, update_heatmap_data
from dash import Dash
from dash.dependencies import Input, Output

from data import df, df_pct, df_pct_education, min_age, max_age, race_, ideology_, higher_education_
from components import create_donut_chart, create_stacked_chart_race, create_stacked_chart_education, create_war_likelihood_chart, create_heatmap


# Initialize the app
app = Dash(__name__,
           external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'])
server = app.server


 # Use the function to create the figure
donut_chart_figure = create_donut_chart(df)
stacked_chart_race = create_stacked_chart_race(df_pct)
stacked_chart_education = create_stacked_chart_education(df_pct_education)
war_likelihood_chart = create_war_likelihood_chart(df)
heat_map = create_heatmap(df)

# Donut chart component
donut_chart_component = dcc.Graph(
    id='donut-chart',
    figure=donut_chart_figure
)

stacked_chart_component_race = dcc.Graph(
    id='stacked-chart-race',
    figure=stacked_chart_race
)

stacked_chart_component_education = dcc.Graph(
    id='stacked-chart-education',
    figure=stacked_chart_education
)

war_likelihood_chart_component = dcc.Graph(
    id='war-likelihood-chart',
    figure=war_likelihood_chart
)
heatmap_component = dcc.Graph(
    id='heatmap',
    figure=heat_map
)

colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }


app.layout = html.Div([
    html.Link(
        href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.2/css/bootstrap.min.css',
        rel='stylesheet'
    ),
    # Header Row with title and filters
    dbc.Row([
        dbc.Col(html.H1("Cards Against Humanity: Future of Democracy and Elections in America",
                        style={'textAlign': 'center', 'color': '#0660a9', 'fontSize': '24px'}))
    ]),

    # Filters row
    dbc.Row([
        dbc.Col(html.Label("Age Range", htmlFor="age-slider",
                            style={'color': colors['white']}), width=1),
        dbc.Col(dcc.RangeSlider(id='age-slider', min=min_age, max=max_age, step=1, value=[min_age, max_age],
                                marks={i: str(i) for i in range(min_age, max_age + 1, 10)}), width=10),
    ], style={'backgroundColor': colors['light_blue'], 'padding': '5px'}, justify='center'),

    dbc.Row([
        dbc.Col(html.Label("Racial Group", htmlFor="racial-group-dropdown",
                            style={'color': colors['white']}), width=2),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in race_],
                             value=['White', 'Black'], id="racial-group-dropdown", multi=True), width=2),
        html.Div(style={'width': '1px', 'background-color': 'white', 'height': '100%', 'margin': 'auto'}),  # Vertical line
        dbc.Col(html.Label("Political Ideology", htmlFor="ideology-dropdown",
                            style={'color': colors['white']}), width=2),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in ideology_],
                             value=['Conservative', 'Liberal'], id="ideology-dropdown", multi=True), width=2),
        dbc.Col(html.Label("Level of Higher Education",
                            htmlFor="higher-education-dropdown", style={'color': colors['white']}), width=2),
        dbc.Col(dcc.Dropdown(options=[{'label': range_val, 'value': range_val} for range_val in higher_education_],
                             value=['College degree', 'Some college'], id="higher-education-dropdown", multi=True),
                width=2),
    ], style={'backgroundColor': colors['light_blue'], 'padding': '5px'}, justify='center'),

    # Main content row with two columns for the two main sections
    dbc.Row([
        # Column for "General Correlations" with both charts side by side
        dbc.Col([
            html.H2("General Correlations", style={'textAlign': 'center'}),
            dbc.Row([
                dbc.Col(dcc.Graph(id='stacked-chart-race',
                                  figure=stacked_chart_race), md=6),
                dbc.Col(dcc.Graph(id='stacked-chart-education',
                                  figure=stacked_chart_education), md=6),
            ], style={'margin': '20px'}),  # Add margin to the inner row
            dbc.Row(war_likelihood_chart_component),
        ], md=6),
      
        # Column for "Elections: Donald Trump Focused"
        dbc.Col([
            html.H2("Elections: Donald Trump Focused",
                    style={'textAlign': 'center'}),
            dbc.Row(dcc.Graph(id='donut-chart', figure=donut_chart_figure), justify='center'),  # Center align the graph
            dbc.Row(heatmap_component, justify='center'),  # Center align the heatmap
        ], md=6),
    ], style={'marginTop': 30, 'marginBottom': 30},className='vertical-line-row'),  # Add margin to the main content row
], style={'backgroundColor': colors['light_grey'], 'overflow': 'hidden'})



# Link the callbacks
app.callback(
    Output('donut-chart', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_donut_chart)

app.callback(
    Output('stacked-chart-race', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_stacked_chart_race)

app.callback(
    Output('stacked-chart-education', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_stacked_chart_education)


app.callback(
    Output('heatmap', 'figure'),
    [Input('age-slider', 'value'),
     Input('higher-education-dropdown', 'value'),
     Input('ideology-dropdown', 'value'),
     Input('racial-group-dropdown', 'value')]
)(update_heatmap_data)

if __name__ == '__main__':
    app.run_server(debug=False)