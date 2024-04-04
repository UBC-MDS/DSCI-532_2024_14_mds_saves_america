from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.express as px


# Initialize the app
app = Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'])

# Sample data (replace this with your actual data loading logic)
df = pd.read_csv("data/processed/data_cleaned.csv")


# Charts 
# Calculate percentages for each political party within each race
df_pct = df.groupby(['race', 'political_party']).size().unstack(fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

# Create Altair chart
race_pol_party_chart1 = alt.Chart(df_pct).mark_bar().encode(
    x=alt.X('race', axis=alt.Axis(title='Race')),
    y=alt.Y('percentage:Q', axis=alt.Axis(format='%'), stack='normalize', title='Percentage'),
    color=alt.Color('political_party', legend=alt.Legend(title='Political Party'))
).properties(
    title='100% Stacked Bar Chart of Political Party by Race'
)

# Create Donut chart
# Create a donut chart function
def create_donut_chart(df):
    # Calculate the counts for each category in the 'trump_2020' column
    counts = df['trump_2020'].value_counts().reset_index()
    counts.columns = ['trump_2020', 'counts']
    
    # Create the pie chart with a hole (donut chart)
    fig_donut = px.pie(counts, values='counts', names='trump_2020', hole=0.3)
    
    # Update the layout and trace for the donut chart appearance
    fig_donut.update_traces(textinfo='percent+label', pull=[0.1 if i == 0 else 0 for i in range(len(counts))])
    fig_donut.update_layout(
        title='Likelihood of Donald Trump Reelection in 2020',
        showlegend=True,
        annotations=[dict(text='Trump 2020', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    
    return fig_donut

# Use the function to create the figure for the initial state of the donut chart
donut_chart_figure = create_donut_chart(df)

# Donut chart component
donut_chart_component = dcc.Graph(
    id='donut-chart',
    figure=donut_chart_figure
)

# Get unique age range values for drop downs
age_range_ = df['age_range'].unique().tolist()
race_ = df['race'].unique().tolist()
ideology_ = df['ideology'].unique().tolist()
higher_education_ = df['higher_education'].unique().tolist()


# Layout
app.layout = html.Div(
    style={'backgroundColor': '#A6CAEC'},  # Change background color here
    children=[
    html.H1("Cards Against Humanity: Future of Democracy and Elections in America", style={'textAlign': 'center','color': '#0660a9', 'fontSize':'24px'}),  # Add header
    html.Label('Age Range'),  # A label for the slider
   dcc.Dropdown(
        options=[{'label': range_val, 'value': range_val} for range_val in age_range_],  #pass the age here
        value=age_range_[0],  # Default value
    ),
    html.Label('Racial Group'),
    dcc.Dropdown(
        options=[{'label': range_val, 'value': range_val} for range_val in race_],  #pass the race here
        value=race_[0],  # Default value
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
    html.Br(),
        dcc.Graph(id='donut-chart', figure=donut_chart_figure),
    html.Br(),  # Add whitespace; br = "break",
    html.Br(),  # Add whitespace; br = "break",
    dvc.Vega(spec=race_pol_party_chart1.to_dict())
])

# Server side callbacks/reactivity
# ...
# Callback to update donut chart based on age range
@app.callback(
    Output('donut-chart', 'figure'),
    [Input('age-slider', 'value')]
)

def update_donut_chart(age_range):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    return create_donut_chart(filtered_df)

# Run the app/dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
