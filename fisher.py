import numpy as np
import math
import matplotlib.pyplot as plt

def maximo(v):
    return max(v)

def minimo(v):
    return min(v)

def quantElem(v):
    return len(v)

def somaElem(v):
    return sum(v)

def somaElemQuadrado(v):
    soma = sum(x**2 for x in v)
    return soma

def media(v):
    media = sum(v)/len(v)
    return media

def mediaGeo(v):
    tam = len(v)
    mg = 1
    for i in range(tam):
        mg *= math.pow(v[i], 1/tam)
    return mg
    
def mediaHarm(v):
    mh = sum(1/x for x in v)
    mh = len(v)/mh
    return mh
    
def mediaQuad(v):
    mq = sum(x**2 for x in v)
    mq = math.sqrt(mq/len(v))
    return mq

def mediana(v):
    v_cresc = cresc(v)
    tam = len(v)
    if tam%2 != 0:
        mediana = v_cresc[int((tam+1)/2)-1]
    else:
        mediana = (v_cresc[int(tam/2)-1]+v_cresc[int((tam/2))])/2
    return mediana

def quartil(v):
    tam = len(v)
    if tam>2:
        v_cresc = cresc(v)
        v1 = []
        v2 = []
        q2 = mediana(v)
        if tam%2 != 0:
            for i in range(int((tam+1)/2)-1):
                v1.append(v_cresc[i])
            for i in range(int((tam+1)/2), tam):
                v2.append(v_cresc[i])
        else:
            for i in range(int(tam/2)):
                v1.append(v_cresc[i])
            for i in range(int((tam+1)/2), tam):
                v2.append(v_cresc[i])
        q1 = mediana(v1)
        q3 = mediana(v2)
        quartil = [q1, q2, q3]
        return quartil
    else:
        return None

def moda(v):
    tam = len(v)
    n = 0
    valores = []
    quantidades = []
    v_cresc = cresc(v)
    for i in range(tam):
        if v_cresc[n] != v_cresc[i]:
            valores.append(v_cresc[n])
            quantidades.append(i-n)
            n = i
        if  i==(tam-1):
            valores.append(v_cresc[n])
            quantidades.append(i-n+1)
    maximo = 0
    quant_valores = []
    moda = []
    for i in range(len(quantidades)):
        if maximo < quantidades[i]:
            maximo = quantidades[i]
    for i in range(len(quantidades)):
        if maximo == quantidades[i]:
            quant_valores.append(i)
    for i in quant_valores:
        moda.append(valores[i])
    return moda

def cresc(v):
    cont = 0
    armz = 0
    tam = len(v)
    repeticao = (tam-1)**2
    while cont < repeticao:
        for i in range(tam-1):
            if v[i] > v[i+1]:
                armz = v[i]
                v[i] = v[i+1]
                v[i+1] = armz
        cont += 1
    return v

def decresc(v):
    cont = 0
    armz = 0
    tam = len(v)
    repeticao = (tam-1)**2
    while cont < repeticao:
        for i in range(tam-1):
            if v[i] < v[i+1]:
                armz = v[i]
                v[i] = v[i+1]
                v[i+1] = armz
        cont += 1
    return v

def varianPopulacional(v):
    m = media(v)
    soma = sum((x-m)**2 for x in v)
    v = soma/len(v)
    return v

def varianAmostral(v):
    m = media(v)
    soma = sum((x-m)**2 for x in v)
    v = soma/(len(v)-1)
    return v

def desvioPadrao(v):
    m = media(v)
    soma = sum((x-m)**2 for x in v)
    dp = math.sqrt(soma/len(v))
    return dp

def desvioPadraoAmostral(v):
    m = media(v)
    soma = sum((x-m)**2 for x in v)
    dp = math.sqrt(soma/(len(v)-1))
    return dp

def intervalo(v):
    return max(v)-min(v)

def coefiVarian(v):
    dp = desvioPadrao(v)
    m = media(v)
    cv = (dp/m)*100
    return cv

def frequenciaAbs(v):
    # [valor, frequencia]
    tam = len(v)
    n = 0
    valor_freq = []
    v_cresc = cresc(v)
    for i in range(tam):
        if v_cresc[n] != v_cresc[i]:
            valor_freq.append([v_cresc[n], i-n])
            n = i
        if  i==(tam-1):
            valor_freq.append([v_cresc[n], i-n+1])
    return valor_freq

def frequenciaRelativa(v):
    # [valor, frequencia%]
    tam = len(v)
    n = 0
    valor_rel = []
    v_cresc = cresc(v)
    for i in range(tam):
        if v_cresc[n] != v_cresc[i]:
            valor_rel.append([v_cresc[n], (i-n)*100/tam])
            n = i
        if  i==(tam-1):
            valor_rel.append([v_cresc[n], (i-n+1)*100/tam])
    return valor_rel

def covariancia(v1, v2):
    if len(v1) == len(v2):
        m1 = media(v1)
        m2 = media(v2)
        v = zip(v1, v2)
        numerador = sum((x-m1)*(y-m2) for x, y in v)
        c = numerador/(len(v1)-1)
        return c
    else:
        raise ValueError('Número de elementos dos conjuntos desiguais.')

def correlacao(v1, v2):
    cov = covariancia(v1, v2)
    dp1 = desvioPadraoAmostral(v1)
    dp2 = desvioPadraoAmostral(v2)
    correlacao = cov/(dp1*dp2)
    return correlacao
    
def graficoLinhaCorresp(categorias, v, titulo, nome):
    # Fornece um gráfico de linhas com a correspondência categorias (horizontal) -> valores (vertical).
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(titulo)
    ax.plot(categorias, v, marker='o', label = nome)
    ax.legend()
    
def graficoLinha(v, titulo, nome):
    # Fornece um gráfico de linha correspondente à posição da sequência.
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(titulo)
    ax.plot(v, marker='o', label = nome)
    ax.legend()
    
def graficoFreqRelativa(v, titulo):
    # Fornece um gráfico de setores com a frequência de cada elemento da sequência.
    _, ax = plt.subplots()
    freq = frequenciaRelativa(v)
    porcentagem = []
    valores = []
    tam = len(freq)
    for i in range(tam):
        porcentagem.append(freq[i][1])
        valores.append(freq[i][0])     
    ax.pie(porcentagem, labels=valores, autopct='%.2f%%')
    ax.set_title(titulo)
    plt.show()

def graficoBarraCorresp(categorias, v, titulo, titulox, tituloy):
    # Fornece um gráfico de barras com a correspondência categorias (horizontal) -> valores (vertical).
    if len(v)==len(categorias):
        plt.bar(categorias, v, hatch='/')
        plt.xlabel(titulox)
        plt.ylabel(tituloy)
        plt.title(titulo)
        plt.show()
    else:
        raise ValueError('Número de elementos dos conjuntos desiguais.')
