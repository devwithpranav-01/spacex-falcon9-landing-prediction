"""
SpaceX Launch Records Dashboard
Author: Pranav Vyankatesh Jagdale
IBM Applied Data Science Capstone

Run:  pip install dash pandas plotly
      python spacex_dash_app.py
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
sites = sorted(spacex_df['Launch Site'].unique())

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 36}),
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + [{'label': s, 'value': s} for s in sites],
                 value='ALL', placeholder='Select a Launch Site here', searchable=True),
    html.Br(),
    dcc.Graph(id='success-pie-chart'),
    html.P('Payload range (kg):'),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),
    dcc.Graph(id='success-payload-scatter-chart'),
])


@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def update_pie(selected_site):
    if selected_site == 'ALL':
        return px.pie(spacex_df, values='class', names='Launch Site',
                      title='Total successful launches by site')
    site_df = spacex_df[spacex_df['Launch Site'] == selected_site]
    counts = site_df['class'].value_counts().rename_axis('class').reset_index(name='count')
    counts['outcome'] = counts['class'].map({1: 'Success', 0: 'Failure'})
    return px.pie(counts, values='count', names='outcome',
                  title=f'Success vs failure for {selected_site}')


@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'), Input('payload-slider', 'value')])
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    df = spacex_df[spacex_df['Payload Mass (kg)'].between(low, high)]
    if selected_site != 'ALL':
        df = df[df['Launch Site'] == selected_site]
    return px.scatter(df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                      title='Payload vs outcome (1 = landed)')


if __name__ == '__main__':
    app.run(debug=True)
