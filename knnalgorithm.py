#!/usr/local/bin/python3

import pandas as pd

# 5.7,2.8,4.1,1.3,versicolor
# 4.6,3.4,1.4,0.3,setosa
# 6.3,3.3,6.0,2.5,virginica


def calcDist(listaEntrada, conjunto):
    dist = 0
    for i in range(4):
        dist += (listaEntrada[i] - conjunto[i])**2
    return(dist**(1/2))


def main():
    dados = pd.read_csv("iris.csv")
    # Tamanho(P),Largura(P),Tamanho(S),Largura(S),Espécie
    tamanhoP = float(input("Tamanho da pétala "))
    larguraP = float(input("Largura da pétala "))
    tamanhoS = float(input("Tamanho da sépala "))
    larguraS = float(input("Largura da sépala "))
    infoEntrada = [tamanhoP, larguraP, tamanhoS, larguraS]
    setosa = 0
    versicolor = 0
    virginica = 0
    for i in range(149):
        tP = dados.loc[i, "Tamanho(P)"]
        lP = dados.loc[i, "Largura(P)"]
        tS = dados.loc[i, "Tamanho(S)"]
        lS = dados.loc[i, "Largura(S)"]
        conjunto = [tP, lP, tS, lS]
        if dados.loc[i, "Espécie"] == "setosa":
            setosa += 1/(calcDist(infoEntrada, conjunto))
        elif dados.loc[i, "Espécie"] == "versicolor":
            versicolor += 1/(calcDist(infoEntrada, conjunto))
        else:
            virginica += 1/(calcDist(infoEntrada, conjunto))
    if setosa > versicolor and setosa > virginica:
        print("setosa")
    elif virginica > versicolor and virginica > setosa:
        print("virginica")
    else:
        print("versicolor")


main()
