import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_auth
from user_password import user_pw_pair


app = dash.Dash(__name__)
# auth = dash_auth.BasicAuth(app, user_pw_pair)

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

app.layout = html.Div([
    html.P('甘特图'),
    html.Div(id='gantt_graph'),
    dcc.Graph(id='test_graph', figure=fig)
])

if __name__ == "__main__":
    app.run_server()
