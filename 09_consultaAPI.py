import json, requests

resposta = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/davi")
json_data = json.loads(resposta.text)
print(json_data[0]['res'][0])