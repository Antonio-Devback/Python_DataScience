# -*- coding: utf-8 -*-
"""Exercicio 8 (Produção 1) - Aplicações em numpy

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kjrLK47pNR-ZPR_b_Khinpk4j3u05GTz
"""

import statistics as st
import numpy as np
import random as rd

# Gerar dados aleatórios de produção para 4 semanas e 3 tipos de peças (A, B e C)
# Cada número representa a quantidade produzida naquele semana para a peça
#linhas: semanas (0 = semana 1, ..., 3 = semana 4)
#Colunas: 0 = peça A, 1 = peça B, 2 = peça C

rd.seed(10)  # Para resultados reproduzíveis
dados = np.array([[rd.randint(80, 200) for _ in range(30)] for _ in range(40)])

# Mostrar a tabela de produção
print("Tabela de Produção (Semanas x Peças [A, B, C]):\n", dados)

# 1. Total de peças produzidas por semana
total_semana = np.sum(dados, axis=1)
print("\nTotal de peças por semana:", total_semana)

# 2. Produção total de cada tipo de peça
total_por_peça = np.sum(dados, axis=0)
print("Total por tipo de peça (A, B, C):", total_por_peça)

# 3. Semana com maior produção total
semana_maior_producao = np.argmax(total_semana) + 1  # +1 porque semana começa em 1
print("Semana com maior produção total: Semana", semana_maior_producao)

# 4. Média semanal de produção por tipo de peça
media_por_peça = np.mean(dados, axis=0)
print("Média semanal por tipo de peça(A, B, C):", media_por_peça)

# 5. Peça com maior média de produção
indice_maior_media = np.argmax(media_por_peça)
# Supondo que existam 30 tipos de peças com base no formato de media_por_peça
pecas = [f'Peça {i}' for i in range(len(media_por_peça))]
print("Peça com maior média de produção:", pecas[indice_maior_media])

# 6. Crescimento semanal da produção da peça A (coluna 0)
peca_A = dados[:, 0]
crescimento = []
for i in range(1, len(peca_A)):
    variacao = ((peca_A[i] - peca_A[i - 1]) / peca_A[i - 1]) * 100
    crescimento.append(round(variacao, 2))
print("Crescimento percentual semanal da peça A:", crescimento)

# 7. Peças abaixo da média (listar semanas onde alguma peça ficou abaixo da média)
semanas_abaixo_media = []
for i in range(len(dados)):
    for j in range(len(dados[i])): # Iterar sobre todas as peças da semana
        if dados[i][j] < media_por_peça[j]:
            semanas_abaixo_media.append((i + 1, pecas[j]))

print("Peças abaixo da média por semana:")
for semana, peca in semanas_abaixo_media:
    print (f"Semana {semana}, Peça {peca}")

