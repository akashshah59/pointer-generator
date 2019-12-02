import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from chart_studio import plotly as py
from dash.dependencies import Input, Output, State
import os
#Import summarizer here


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)


"""
Initial Configuration:

"""


app.layout = html.Div(
    [
        dcc.Input(
            id="article",
            value = ""
        ),
        html.Div(id='my-div')
    ]
)

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='article', component_property='value')]
)
def update_output_div(input_value):
    file = open('temp.story','w+')


    return 'Summarized sentence - "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050,debug=True)
