#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Equipe:
#   Everton Gualberto
#   Éverton Arruda
#   Felipe Cabral
#   Letícia Santos
#
# Cálculo de métricas de mostras obtidas
# de arquivos .csv, exportados do programa
# MyTracks, para plataforma Android
#
# Para mais informações, leia o arquivo README

import sys

def media_aritmetica(mostra):
    """
        Cálculo de média aritmética
    """
    return sum(mostra) / len(mostra)

def desvio_padrao(mostra):
    """
        Cálculo de desvio padrão
    """
    media = media_aritmetica(mostra)
    resultado = 0
    for registro in mostra:
        resultado = resultado + ((registro - media)**2)
    return (resultado / len(mostra))**0.5

def variancia(mostra):
    """
        Cálculo de variância
    """
    media = media_aritmetica(mostra)
    resultado = 0
    for registro in mostra:
        resultado = resultado + ((registro - media)**2)
    return resultado / (len(mostra) - 1)

def coeficiente_variacao(mostra):
    """
        Cálculo de coeficiente de variação
    """
    return (desvio_padrao(mostra) / media_aritmetica(mostra)) * 100

def valor_minimo(mostra):
    """
        Valor mínimo
    """
    return min(mostra)

def valor_maximo(mostra):
    """
        Valor máximo
    """
    return max(mostra)

def tamanho(mostra):
    """
        Tamanho da mostra
    """
    return len(mostra)

def ler_arquivos(nomesArquivos):
    """
        Lê dados dos arquivos para realizar os cálculos
        Separando dados de precisão(Accuracy) e velocidade(Speed)
    """
    mostraTotal = []
    for nomeArquivo in nomesArquivos:
        mostra = []
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                linha = linha.replace('"', "").split(",")
                mostra.append([linha[6], linha[7]])
            del mostra[0:2]
            mostraTotal = mostraTotal + mostra
    return mostraTotal

def separar_mostras(mostra):
    """
        Recebe lista de dados no formato:
            [precisão, velocidade]
        E separa em duas listas, uma somente com precisão e outra
        somente com velocidade
    """
    precisao = []
    velocidade = []
    for item in mostra:
        precisao.append(float(item[0]))
        velocidade.append(float(item[1]))
    return [precisao, velocidade]


#================ MAIN ==================
if len(sys.argv) < 2:
    print "Nenhum arquivo especificado"
    exit(1)

print "Arquivos:",
for nomeArquivo in sys.argv[1:]:
    print nomeArquivo,
print "\n"

mostraMista = ler_arquivos(sys.argv[1:])
mostraSeparada = separar_mostras(mostraMista)
for i in range(0, 2):
    if i == 0:
        print "Cálculos para Precisão(Accuracy):"
    elif i == 1:
        print "Cálculos para Velocidade(Speed):"

    mostra = mostraSeparada[i]
    print "\tMédia Aritmética: ", media_aritmetica(mostra)
    print "\tDesvio Padrão: ", desvio_padrao(mostra)
    print "\tVariância: ", variancia(mostra)
    print "\tCoeficiente de Variação: ", coeficiente_variacao(mostra)
    print "\tValor Mínimo: ", valor_minimo(mostra)
    print "\tValor Máximo: ", valor_maximo(mostra)
    print "\tTamanho da Mostra: ", tamanho(mostra), "\n"
