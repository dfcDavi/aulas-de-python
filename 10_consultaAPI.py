import json, requests

nome = input("Qual o seu nome?: ")
localidade = 0

while localidade < 1 or localidade > 2 :
    localidade = int(input('Você deseja selecionar uma localidade?\n1) Sim \n2)Não\n'))

if localidade == 1:
    uf = input("Qual UF deseja buscar?:\n35) SP\n33) RJ\n31) MG\n43) RS\n53) DF\n")
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={uf}')
if localidade == 2:
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

print('''

Escolha o período de tempo:

[1] - 1930
[2] - 1930 até 1940
[3] - 1940 até 1950
      .
      .
      .
[9] - 2000 até 2010

''')

periodo = int(input("Selecione um período: ")) - 1
dados = json.loads(resultado.text)

print(dados[0]['res'][periodo])