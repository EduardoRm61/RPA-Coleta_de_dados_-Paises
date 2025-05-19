# 1 - Solicitar ao usuário a entreada de três paises para consultar
# 2 - Utilize a API: https://restcountries.com/v3.1
# para coletar as seguintes infomações:
# Nome commum e nome oficial ok
# Capital ok
# Continente ok
# Região e sub-região ok
# Populaão ok
# Área total (em km2) ok
# Moeda principal (nome e símblo) ok
# Idioma principal ok
# Fuso horário ok
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
#     continente = continente.get('continents','Outro Planete rs')
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

#Aqui temos o nome e símbolo da moeda:

# for name in dados:
#     dict_moeda = name.get('currencies',{})

#     for moeda_info in dict_moeda.values():
#         simb = moeda_info.get('symbol','sem símbolo')
#         moeda = moeda_info.get('name','Sem moeda')
#         print(f"Moeda: {moeda} \nSímbolo: {simb}")

# Aqui está para Idioma Principal:

# for country in dados:
#     languages = country.get("languages", {})
#     if languages:
#         first_lang_code = next(iter(languages))
#         main_language = languages[first_lang_code]
#         print(main_language)
#     else:
#         print("Sem Idioma")


# Aqui está o fuso horário

# for fuso in dados:
#     fuso = fuso['timezones'][0]
#     print(fuso)

# Aqui está para bandeira:
for bandeiras in dados:
    bandeira = bandeiras['flags']['png']
    print(bandeira)