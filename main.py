from flask import Flask, render_template, request, jsonify
import requests

# inicialização do app Flask
app = Flask(__name__)


def requisicao_dia(cidade): # Função para pegar os dados da API
    # dados iniciais
    url_base = 'http://api.weatherapi.com/v1'
    metodo_api = '/forecast.json'
    chave_api = '98492e51f99b4760aa5115145231305'

    # Parâmetros da API
    params = {
        'key': chave_api,
        'q': cidade,
        'lang': 'pt'
    }

    # Juntando as url base com o método de busca
    url = url_base + metodo_api

    # Fazendo a requisição get com os parâmetros
    response = requests.get(url, params=params)

    # Verificando status da resposta
    if response.status_code == 200:  # Requisição bem sucedida
        return response.json() # Retorno da conversão de Json para python
    else: # Falha da requisição
        return f'Erro na requisição: {response.status_code}' # retorna o código de erro

# rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# rota para obter dados da API e enviar para o JavaScript
@app.route('/dados')
def obter_dados():
    cidade = request.args.get('pesquisa', default='')
    if cidade:
        cidade = cidade.encode('latin1').decode('latin1')
        data = requisicao_dia(cidade)# ativando função com o nome da cidade requisitada

# dicionário com os dados da previsão a serem convertidos para json e enviados ao front-end
        previsao = {
            'temperatura_atual': data['current']['temp_c'],
            'descricao_tempo': data['current']['condition']['text'],
            'icone_tempo': data['current']['condition']['icon'],
            'velocidade_vento': data['current']['wind_kph'],
            'direcao_vento': data['current']['wind_dir'],
            'grau_vento': data['current']['wind_degree'],
            'umidade_ar': data['current']['humidity'],
            'precipitacao': data['current']['precip_mm'],

            'temperatura_maxima': data['forecast']['forecastday'][0]['day']['maxtemp_c'],
            'temperatura_minima': data['forecast']['forecastday'][0]['day']['mintemp_c'],
            'descricao_geral': data['forecast']['forecastday'][0]['day']['condition']['text'],
            'precipitacao_esperada': data['forecast']['forecastday'][0]['day']['totalprecip_mm'],

            'indice_uv': data['forecast']['forecastday'][0]['day']['uv'],
            'vento_maximo': data['forecast']['forecastday'][0]['day']['maxwind_kph'],
            'visibilidade_prevista': data['forecast']['forecastday'][0]['day']['avgvis_km'],
            'fases_lua': data['forecast']['forecastday'][0]['astro']['moon_phase'],

            'cidade': data['location']['name'],
            'estado': data['location']['region'],
            'pais': data['location']['country'],
            'hora': data['location']['localtime']
        }
        return jsonify(previsao)
    else:
        return 'Cidade não especificada'


if __name__ == '__main__':
    app.run()
