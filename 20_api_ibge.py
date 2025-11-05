from flask import Flask, request, jsonify, Response
import requests
import io
#pandas biblioteca para lidar com estrutura de dados
import pandas as pd
#matplotlib biblioteca para plotar gráfico
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#iniciar o app
app = Flask(__name__)

@app.route('/consultar_ibge/<string:nome>', methods = ['GET'])
def consultar_ibge(nome):
    
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}'
    r = requests.get(url, timeout=50)

    #verificações básicas
    if r.status_code != 200 :
        return jsonify ({'erro' : 'Falha ao consultar IBGE', 'status code' : r.status_code}), 502

    try:
        data = r.json()
        
    except ValueError:
        return jsonify({'erro':'Resposta do IBGE não é um json válido'}),502
      
    if not isinstance(data, list) or len(data) == 0 :
        return jsonify({'erro':'Nenhum dado retornado para esse nome'}), 404

    bloco = data[0]
    localidade = bloco.get('localidade', 'BR')
    res = bloco.get('res',[])

    if not res :
        return jsonify({'erro': 'Sem resultados em "res" para esse nome'}), 404
    
    #tranforma em uma tabela. Monta o dataframe com as colunas disponíveis (normalmente, 'periodo' e 'frequência')
    df = pd.DataFrame(res)

    #se o usuario pediu png (?formato=png)
    if request.args.get('formato') == 'png' :
        
        #iniciar um gráfico. Primeiro valor figura e segundo valor conjunto de eixos
        fig, ax = plt.subplots()
        
        #ordena por período, se existir
        if 'periodo' in df.columns:
            #converte período para string para ordenar consistentemente
            df = df.sort_values(by='periodo')
            x = df['periodo'].astype(str)
        else:
            x = range(len(df))
        y = df['frequencia']

        ax.bar(x,y)
        ax.set_title(f'Frequencia do nome {nome}')
        ax.set_xlabel('Periodo') #titulo do eixo X
        ax.set_ylabel('Frequencia') #titulo do eixo Y
        plt.xticks(rotation=45,ha='right')

        #gera uma imagem temporariamente em um buffer de memoria para evitar ter de salvar em disco
        buf = io.BytesIO()
        FigureCanvas(fig).print_png(buf)
        plt.close(fig)
        buf.seek(0)

        return Response(buf.getvalue(), mimetype='image/png')

    #retorna JSON com um resumo dos dados
    return jsonify({
        'nome': bloco.get('nome', nome),
        'localidade' : localidade,
        'dados' : df.to_dict(orient='records')
        })


if (__name__ == '__main__') :
    app.run(debug=True)

#http://127.0.0.1:5000/consultar_ibge/caio?formato=png
