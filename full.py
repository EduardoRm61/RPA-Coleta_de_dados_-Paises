# 1 - Solicitar ao usuário a entreada de três paises para consultar
# 2 - Utilize a API: https://restcountries.com/v3.1
# para coletar as seguintes infomações:
# Nome commum e nome oficial ok
# Capital ok
# Continente 
# Região e sub-região
# Populaão
# Área total (em km2)
# Moeda principal (nome e símblo)
# Idioma principal
# Fuso horário
# URL da bandeira

#Imprtando bibliotecas:
import requests
# pais = []
# url = f'https://restcountries.com/v3.1/name{pais}'
url = 'https://restcountries.com/v3.1/all'
resposta = requests.get(url)
dados = resposta.json()

# Aqui temos o nome:
# for pais in dados: 
#     nome = pais['name']['common']
#     print(nome)

# Aqui temos o nome oficial:
# for pais in dados:
#     nome_ofc = pais['name']['official']
#     print(nome_ofc)

# Aqui temos a capital:
# for capital in dados:
#     capital = capital.get('capital',['Sem capital'])[0]
#     print(capital)

