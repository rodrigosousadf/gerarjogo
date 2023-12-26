import pandas as pd
import random
import numpy as np

def analisar_frequencia_recente(dados, num_jogos_recentes=10):
    dados_recentes = dados.tail(num_jogos_recentes)
    numeros = dados_recentes[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']].values.flatten()
    return pd.Series(numeros).value_counts()

def gerar_jogo_balanceado(numeros_pares, numeros_impares, proporcoes):
    tipo_jogo = np.random.choice(a=list(proporcoes.keys()), p=list(proporcoes.values()))

    jogo = []
    if tipo_jogo == '4p_2i':
        if len(numeros_pares) >= 4 and len(numeros_impares) >= 2:
            jogo += random.sample(numeros_pares, 4)
            jogo += random.sample(numeros_impares, 2)
        else:
            return None
    elif tipo_jogo == '4i_2p':
        if len(numeros_impares) >= 4 and len(numeros_pares) >= 2:
            jogo += random.sample(numeros_impares, 4)
            jogo += random.sample(numeros_pares, 2)
        else:
            return None
    elif tipo_jogo == '3p_3i':
        if len(numeros_pares) >= 3 and len(numeros_impares) >= 3:
            jogo += random.sample(numeros_pares, 3)
            jogo += random.sample(numeros_impares, 3)
        else:
            return None

    jogo.sort()
    return jogo

def gerar_jogos_balanceados(numeros_frequentes, num_jogos, proporcoes):
    numeros_pares = [n for n in numeros_frequentes if n % 2 == 0]
    numeros_impares = [n for n in numeros_frequentes if n % 2 != 0]

    jogos = []
    for _ in range(num_jogos):
        jogo = gerar_jogo_balanceado(numeros_pares, numeros_impares, proporcoes)
        if jogo:
            jogos.append(jogo)
    return jogos

# Carregar os dados históricos da Mega Sena
caminho_arquivo = '/home/rodrigosousa/Mega-Sena.xlsx'
dados_mega_sena = pd.read_excel(caminho_arquivo)

# Analisar a frequência dos números nos últimos 10 jogos
frequencia_numeros_recentes = analisar_frequencia_recente(dados_mega_sena, 10)
numeros_mais_frequentes = frequencia_numeros_recentes.index.tolist()

# Proporções para cada tipo de jogo
proporcoes_jogos = {
    '4p_2i': 0.3,
    '4i_2p': 0.3,
    '3p_3i': 0.4
}

# Gerar 100 jogos balanceados
jogos_balanceados = gerar_jogos_balanceados(numeros_mais_frequentes, 100, proporcoes_jogos)

# Visualizar os jogos gerados
for i, jogo in enumerate(jogos_balanceados, start=1):
    print(f"Jogo {i}: {jogo}")
