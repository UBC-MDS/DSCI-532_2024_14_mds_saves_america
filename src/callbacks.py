from dash import Dash, html, dcc, Input, Output
from components import create_donut_chart, create_stacked_chart_race, create_stacked_chart_education, create_heatmap, create_war_likelihood_chart
from data import df, min_age, max_age


def update_donut_chart(age_range,
                       education,
                       ideology,
                       race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    return create_donut_chart(filtered_df)


def update_stacked_chart_race(age_range,
                              education,
                              ideology,
                              race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    df_pct = filtered_df.groupby(['race', 'political_party']).size().unstack(
        fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_race(df_pct)


def update_stacked_chart_education(age_range,
                                   education,
                                   ideology,
                                   race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]

    df_pct = filtered_df.groupby(['higher_education', 'political_party']).size().unstack(
        fill_value=0).apply(lambda x: x / x.sum(), axis=1).stack().reset_index(name='percentage')

    return create_stacked_chart_education(df_pct)


def update_heatmap_data(age_range, education, ideology, race):
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    filtered_df = filtered_df[filtered_df['higher_education'].isin(education)]
    filtered_df = filtered_df[filtered_df['ideology'].isin(ideology)]
    filtered_df = filtered_df[filtered_df['race'].isin(race)]
    df_subset = filtered_df[["trump_approval", "fairness_voting"]]

    return create_heatmap(df_subset)


def update_slider_marks(value):
    default_label_positions = range(min_age, max_age + 1, 10)
    new_marks = {}

    # Set default labels at defined positions and color them based on whether they are within the selected range
    for i in default_label_positions:
        if value[0] <= i <= value[1]:
            new_marks[i] = {'label': str(i), 'style': {'color': 'red'}}
        else:
            new_marks[i] = {'label': str(i), 'style': {'color': 'black'}}

    # Ensure that the start and end values have labels and are red
    if value[0] not in default_label_positions:
        new_marks[value[0]] = {'label': str(
            value[0]), 'style': {'color': 'red'}}
    else:
        new_marks[value[0]]['style']['color'] = 'red'

    if value[1] not in default_label_positions and value[1] != value[0]:
        new_marks[value[1]] = {'label': str(
            value[1]), 'style': {'color': 'red'}}
    elif value[1] != value[0]:
        new_marks[value[1]]['style']['color'] = 'red'

    return new_marks
