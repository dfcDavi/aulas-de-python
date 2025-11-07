import dash
from dash import dcc, html
import plotly.graph_objs as go

app = dash.Dash()

#definindo o layout do dashboard(gráfico)
#dcc > dashcorecomponent

app.layout = html.Div([html.H1('Gráfico interativo com Dash e Plotly'),
    dcc.Graph (
        id = 'grafico-1',
        figure = {
            'data': [
                go.Scatter(
                    x = [1,2,3,4,5], 
                    y = [11,12,13,14,15],
                    mode = 'lines+markers',
                    name = 'Linha 1'
                )
            ],
            'layout': 
                go.Layout(

                    title='Gráfico de Linha Interativo',
                    xaxis= {'title':'Eixo X'},
                    yaxis= {'title':'Eixo Y'}
                )
        }

    ) 

])

if __name__ == '__main__' :
    app.run()

