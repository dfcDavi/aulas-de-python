import plotly.graph_objects as go

dado_x = [1,2,3,4,5]
dado_y = [10,11,12,13,14]

#criar grafico de linha
figura = go.Figure(data=go.Scatter(x=dado_x,y=dado_y, mode='lines+markers', name='Linha 01'))

#adicionar titulo e rótulo aos eixos

figura.update_layout(title='Gráfico de linha interativo', xaxis_title='Eixo X', yaxis_title='Eixo Y')
figura.show()


