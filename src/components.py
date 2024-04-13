import plotly.express as px
from dash import dash_table
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


colors = {'light_blue': '#0d76bd',
          'dark_blue': '#0660a9',
          'red': '#ed1c23',
          'white': '#ffffff',
          'grey': '#888888',
          'light_grey': '#d3d3d3'
          }

def create_stacked_chart_race(df):
    party_colors = {'Republican': colors['red'],
                    'Democrat': colors['dark_blue'],
                    'DK/REF': colors['white'],
                    'Independent': colors['light_blue']}

    fig = px.bar(df, x='race', y='percentage', color='political_party',
                 title='Stacked Bar Chart of Political Party by Race',
                 labels={'percentage': 'Percentage', 'race': 'Race'},
                 category_orders={'race': sorted(df['race'].unique())},
                 hover_data={'percentage': ':.2%'},
                 barmode='relative',
                 color_discrete_map=party_colors)

    fig.update_yaxes(title='Percentage', tickformat='%')
    fig.update_layout(
        {
            "paper_bgcolor": colors['light_grey'],
            "plot_bgcolor": colors['light_grey'],
        },
        legend_title='Political Party',
    )

    return fig


def create_stacked_chart_education(df):
    party_colors = {'Republican': colors['red'],
                    'Democrat': colors['dark_blue'],
                    'DK/REF': colors['white'],
                    'Independent': colors['light_blue']}

    fig = px.bar(df, x='higher_education', y='percentage', color='political_party',
                 title='Stacked Bar Chart of Political Party by Highest Education',
                 labels={'percentage': 'Percentage',
                         'higher_education': 'Higher Education'},
                 category_orders={'higher_education': sorted(
                     df['higher_education'].unique())},
                 hover_data={'percentage': ':.2%'},
                 barmode='relative',
                 color_discrete_map=party_colors)

    fig.update_yaxes(title='Percentage', tickformat='%')
    fig.update_layout(
        {
            "paper_bgcolor": colors['light_grey'],
            "plot_bgcolor": colors['light_grey'],
        },
        legend_title='Political Party',
    )

    return fig


def create_donut_chart(df):
    # Calculate the counts for each category in the 'trump_2020' column
    counts = df['trump_2020'].value_counts().reset_index()
    counts.columns = ['trump_2020', 'counts']

    # Custom colors for different likelihood categories
    custom_colors = {
        'Very Likely': colors['red'],  
        'Somewhat Likely': colors['light_blue'],  
        'Very Unlikely': colors['dark_blue'],  
        'DK': colors['white']  
    }

    # Create the pie chart with a hole (donut chart)
    fig_donut = px.pie(counts, values='counts', names='trump_2020', hole=0.4)

    # Update the layout and trace for the donut chart appearance
    fig_donut.update_traces(textinfo='percent+label', pull=[0 for _ in range(len(counts))],
                            marker=dict(colors=list(colors.values())[:len(df['trump_2020'].unique())]))
    fig_donut.update_layout(
        {
            "paper_bgcolor": colors['light_grey'],
            "plot_bgcolor": colors['light_grey'],
        },
        title='Likelihood of Donald Trump Reelection in 2020',
        showlegend=False,
        annotations=[dict(text='Trump', x=0.5, y=0.5,
                          font_size=20, showarrow=False)],

        plot_bgcolor=colors['light_grey']



    )
    return fig_donut


def create_war_likelihood_chart(df):
    # Define colors for the opinions to match the American flag theme
    opinion_colors = {'Very Likely': colors['red'],
                      'Somewhat Likely': colors['white'],
                      'Not at all likely': colors['dark_blue']}

    # Map the numeric values to string categories if they represent categorical data
    likelihood_mapping = {0: 'Not at all likely',
                          1: 'Somewhat Likely', 2: 'Very Likely'}
    df['likelihood_of_war'] = df['likelihood_of_war'].map(likelihood_mapping)

    # Aggregate the data to get the count of responses for each category
    likelihood_counts = df['likelihood_of_war'].value_counts().reset_index()
    likelihood_counts.columns = ['Opinion', 'Count']

    # Sort the dataframe based on the opinion order you want in the chart
    ordered_opinions = ['Very Likely', 'Somewhat Likely', 'Not at all likely']
    likelihood_counts['Opinion'] = pd.Categorical(
        likelihood_counts['Opinion'], categories=ordered_opinions, ordered=True)
    likelihood_counts = likelihood_counts.sort_values('Opinion')

    # Create the horizontal bar chart using Plotly Express
    fig = px.bar(likelihood_counts, y='Opinion', x='Count',
                 title='Perceived Likelihood of War',
                 labels={'Count': 'Number of Responses',
                         'Opinion': 'Opinion on Likelihood of War'},
                 text='Count', orientation='h',
                 color='Opinion',
                 color_discrete_map=opinion_colors)

    fig.update_layout(
        {
            "paper_bgcolor": colors['light_grey'],
            "plot_bgcolor": colors['light_grey'],
        }
    )
    return fig


def create_heatmap(df):
    pivot_df = df.pivot_table(index='trump_approval', columns='fairness_voting', aggfunc='size', fill_value=0)
    fig = px.imshow(pivot_df,
                    labels=dict(x="Voting Fairness", y="Trump Approval"),
                    color_continuous_scale='RdBu_r',  # Blue-Red color scale,
                    text_auto=True
                    )
    
    fig.update_layout(
        title='Heatmap of Trump Approval vs. Voting Fairness',
        xaxis_title='Voting Fairness',
        yaxis_title='Trump Approval',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="/page-1", style={'color': colors['light_blue']})),
        dbc.NavItem(dbc.NavLink("Page 2", href="/page-2", style={'color': colors['light_blue']})),
    ],
    color='0660a9',
    dark=True
)

navbar_brand_style = {
    'color': colors['light_blue'],
    'fontSize':'24px'
}

