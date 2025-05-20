import requests
import sqlite3 
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import Font
def relatorioDados(pais, nome, nome_oficial, capital, continente, regiao, sub_regiao,populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira):
    # conectar com BD / relatório
    # df = pd.DataFrame(pais)
    # df.to_excel('Relatorio_Paises.xlsx',index=False, engine='openpyxl')
    conexao = sqlite3.connect("paises.db")
    cursor = conexao.cursor()
    #Criando a tabela
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS paises(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   nome_oficial TEXT,
                   capital TEXT,
                   continente TEXT,
                   regiao TEXT,
                   sub_regiao TEXT,
                   populacao INTEGER,
                   area REAL,
                   moeda_nome TEXT,
                   moeda_simbolo TEXT,
                   idioma TEXT,
                   fuso TEXT,
                   url_bandeira TEXT)
                   ''')
    # Inserir no BD
    cursor.execute('''
                    INSERT INTO paises(nome, nome_oficial, capital, regiao, sub_regiao, populacao
                   area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeiro)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                   ''', (nome, nome_oficial, capital, continente, regiao, sub_regiao, populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira))
    conexao.commit()
    # Consultar as informações
    print("\n Dados inseridos no BD:")
    cursor.execute("SELECT * FROM paises")
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()



def solicitaDados(nome_pais):
    url = 'https://restcountries.com/v3.1/{nome_pais}'
    resposta = requests.get(url)
    dados = resposta.json()
    for pais in dados:
        nome = pais['name']['common']
        for nome_oficial in dados:
            nome_oficial = pais['name']['official']
            for capital in dados:
                capital = capital.get('capital',['Sem capital'])[0]
                for continente in dados:
                    continente = continente.get('continents','Outro planeta')
                    for regiao in dados:
                        regiao = regiao.get('region')
                        for sub_reg in dados:
                            sub_reg = ('subregion')
                            for populacao in dados:
                                populacao = populacao.get('population')
                                for area in dados:
                                    area = area.get('area')
                                    for name in dados:
                                        dict_moeda = name.get('currencies',{})
                                        for moeda_info in dict_moeda.values():
                                            simb = moeda_info.get('symbol', 'Sem moeda')
                                            moeda = moeda_info.get('name','Sem moeda')
                                            for country in dados:
                                                languages = country.get('languages',{})
                                                if languages:
                                                    first_lang_code = next(iter(languages))
                                                    idioma = languages[first_lang_code] # Este
                                                else:
                                                    idioma = 'Sem idioma'
                                                    for fuso in dados:
                                                        fuso = fuso['timezones'][0] 
                                                        for bandeira in dados:
                                                            bandeira = ['flags']['png']
                                                            relatorioDados(nome_pais,nome,nome_oficial,capital, continente,regiao,sub_reg, populacao, area, moeda, simb, idioma, fuso, bandeira)
                                                            print('Dados inseridos')
                                                            return
                                                            
                            
                                


            



pais = input("Digite o nome do país em Inglês")
i = 1
solicitaDados(pais)

while i <= 3:
    pais = input("Digite o nome de outro País em Inglês")
    solicitaDados(pais)
    i+=1
print("Fim")