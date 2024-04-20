from dash import Dash, html, dcc, Input, Output
from flask_caching import Cache
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'tmp'
})
timeout = 300
