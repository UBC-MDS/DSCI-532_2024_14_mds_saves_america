from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px

# Initialize the app
app = Dash(__name__,
           external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'])

colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }

server = app.server

# Sample data (replace this with your actual data loading logic)
df = pd.read_csv("data/processed/data_cleaned.csv")

age_range_ = df['age_range'].unique().tolist()
race_ = df['race'].unique().tolist()
ideology_ = df['ideology'].unique().tolist()
higher_education_ = df['higher_education'].unique().tolist()

# Get min and max age for the slider from the 'age' column
min_age = df['age'].min()
max_age = df['age'].max()

# Add RangeSlider for age selection
age_slider = dcc.RangeSlider(
    id='age-slider',
    min=min_age,
    max=max_age,
    step=1,  # step by 1 year
    value=[min_age, max_age],  # Default slider values set to min and max ages
    marks={i: str(i) for i in range(min_age, max_age + 1, 10)}  
)


# Layout
app.layout = html.Div(
    style={'backgroundColor': '#A6CAEC'},  # Change background color here
    children=[
    html.H1("Cards Against Humanity: Future of Democracy and Elections in America", style={'textAlign': 'center','color': '#0660a9', 'fontSize':'24px'}),  # Add header
    html.Label('Age Range'),  # A label for the slider
    dcc.RangeSlider(
        id='age-slider',
        min=min_age,
        max=max_age,
        step=1,
        value=[min_age, max_age],
        marks={i: str(i) for i in range(min_age, max_age + 1, 10)}
        ),
    html.Label('Political Ideology'),
    dcc.Dropdown(
        options=[{'label': range_val, 'value': range_val} for range_val in ideology_],  #pass the ideology here
        value=ideology_[0],  # Default value
    ),
    html.Label('Level of Higher Education'),
    dcc.Dropdown(
        options=[{'label': range_val, 'value': range_val} for range_val in higher_education_],  #pass the higher_education here
        value=higher_education_[0],  # Default value
    ),
    html.Br(),  # Add whitespace; br = "break",
    html.Br(),  # Add whitespace; br = "break",
    dvc.Vega(spec=race_pol_party_chart1.to_dict())
])


if __name__ == '__main__':
    app.run_server()
