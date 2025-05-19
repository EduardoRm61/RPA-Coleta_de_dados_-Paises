# 1 - Solicitar ao usuário a entreada de três paises para consultar
# 2 - Utilize a API: https://restcountries.com/v3.1
# para coletar as seguintes infomações:
# Nome commum e nome oficial ok
# Capital ok
# Continente ok
# Região e sub-região ok
# Populaão ok
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

# Aqui temos o continente
# for continente in dados:
#     continente = continente.get('region','Outro Planete rs')
#     print(continente)

# Aqui temos sub-região:
# for sub_reg in dados:
#     sub = sub_reg.get('subregion')
#     print(sub)

# Aqui temos a população:
# for populacao in dados:
#     populacao = populacao.get('population')
#     if populacao == 0 or populacao == None:
#         print("Sem população")
#     else:
#         print(populacao)

# Aqui temos área total:
# for area in dados:
#     area = area.get('area')
#     print(area) # Editar print para contemplar km^2
