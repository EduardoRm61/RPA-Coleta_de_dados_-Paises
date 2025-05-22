import requests
import sqlite3
import pandas as pd

dados_coletados = []  # Lista global para armazenar os dados de cada país

def relatorioDados(nome, nome_oficial, capital, continente, regiao, sub_regiao, populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira):
    conexao = sqlite3.connect("paises.db")
    cursor = conexao.cursor()

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
            url_bandeira TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO paises(
            nome, nome_oficial, capital, continente, regiao, sub_regiao,
            populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        nome, nome_oficial, capital, continente, regiao, sub_regiao,
        populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira
    ))

    conexao.commit()
    conexao.close()

    # Armazenar os dados na lista
    dados_coletados.append({
        "Nome": nome,
        "Nome Oficial": nome_oficial,
        "Capital": capital,
        "Continente": continente,
        "Região": regiao,
        "Sub-Região": sub_regiao,
        "População": populacao,
        "Área": area,
        "Moeda": moeda_nome,
        "Símbolo da Moeda": moeda_simbolo,
        "Idioma": idioma,
        "Fuso Horário": fuso,
        "URL da Bandeira": url_bandeira
    })

    print(f"Dados do país '{nome}' armazenados.")

def solicitaDados(nome_pais):
    url = f'https://restcountries.com/v3.1/name/{nome_pais}'
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Erro ao buscar dados do país '{nome_pais}'.")
        return

    dados = resposta.json()
    if not dados:
        print(f"Nenhum dado encontrado para o país '{nome_pais}'.")
        return

    pais = dados[0]

    try:
        nome = pais['name']['common']
        nome_oficial = pais['name']['official']
        capital = pais.get('capital', ['Sem capital'])[0]
        continente = pais.get('continents', ['Desconhecido'])[0]
        regiao = pais.get('region', 'Desconhecida')
        sub_regiao = pais.get('subregion', 'Desconhecida')
        populacao = pais.get('population', 0)
        area = pais.get('area', 0.0)

        currencies = pais.get('currencies', {})
        moeda_nome = 'Desconhecida'
        moeda_simbolo = 'N/A'
        if currencies:
            moeda_info = list(currencies.values())[0]
            moeda_nome = moeda_info.get('name', 'Desconhecida')
            moeda_simbolo = moeda_info.get('symbol', 'N/A')

        languages = pais.get('languages', {})
        idioma = list(languages.values())[0] if languages else 'Sem idioma'

        fuso = pais.get('timezones', ['Desconhecido'])[0]
        url_bandeira = pais.get('flags', {}).get('png', 'Sem URL')

        relatorioDados(
            nome, nome_oficial, capital, continente, regiao, sub_regiao,
            populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, url_bandeira
        )

    except Exception as e:
        print("Erro ao processar os dados:", e)


# Execução principal
pais = input("Digite o nome do país em Inglês: ")
solicitaDados(pais)

for i in range(2):
    pais = input("Digite o nome de outro País em Inglês: ")
    solicitaDados(pais)

# Gerar Excel
df = pd.DataFrame(dados_coletados)
df.to_excel("Relatorio_Paises.xlsx", index=False)
print("\nArquivo Excel 'Relatorio_Paises.xlsx' gerado com sucesso.")

print("Fim")
