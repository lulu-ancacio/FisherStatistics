# conceitos aplicados que imagino que você não conheça:
#  - tuplas: conjunto de elementos
#  - compreensão de listas: é um pouco chato de explicar por texto,
#    pergunta amanhã na escola ou te mando mensagem
# feito isso, arrumei os nomes de funções e variáveis para o considerado "correto"
# pela linguagem, snake_case

import math
import matplotlib.pyplot as plt
from functools import reduce

def add(v, n):
    v.append(n)
    return v

def maximo(v):
    return max(v)

def minimo(v):
    return min(v)

def quant_elem(v):
    return len(v)

def soma_elem(v):
    return sum(v)

def soma_elem_quadrado(v):
    return sum(x ** 2 for x in v)

def media(v):
    return sum(v) / len(v)

def media_geo(v):
    return reduce(lambda mg, e: mg * math.pow(e, 1 / len(v)), v, 1)

def media_harm(v):
    return len(v) / sum(1 / x for x in v)

def media_quad(v):
    return math.sqrt(sum(x ** 2 for x in v) / len(v))

def mediana(v):
    v_cresc = cresc(v)
    if len(v) % 2 == 0:
        return (v_cresc[len(v) // 2 - 1] + v_cresc[len(v) // 2]) / 2
    else:
        return v_cresc[len(v) // 2]

def quartil(v):
    if len(v) > 2:
        v_cresc = cresc(v)
        if len(v) % 2 == 0:
            v1 = v_cresc[:len(v) // 2]
            v2 = v_cresc[len(v) // 2:]
        else:
            v1 = v_cresc[:(len(v) + 1) // 2 - 1]
            v2 = v_cresc[(len(v) + 1) // 2:]
        q1 = mediana(v1)
        q2 = mediana(v)
        q3 = mediana(v2)
        return (q1, q2, q3)
    else:
        return None

def moda(v):
    if not v:
        return []
    else:
        highest = max(v.count(x) for x in v)
        return [x for x in v if v.count(x) == highest]

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
    return sum((i - m) ** 2 for i in v) / len(v)

def varianAmostral(v):
    m = media(v)
    return sum((i - m) ** 2 for i in v) / (len(v) - 1)

def desvioPadrao(v):
    m = media(v)
    return math.sqrt(sum((i - m) ** 2 for i in v) / len(v))

def desvioPadraoAmostral(v):
    m = media(v)
    return math.sqrt(sum((i - m) ** 2 for i in v) / (len(v) - 1))

def intervalo(v):
    v_cresc = cresc(v)
    minimo = v_cresc[0]
    maximo = v_cresc[-1]
    intervalo = maximo - minimo
    return intervalo

def coefiVarian(v):
    dp = desvioPadrao(v)
    m = media(v)
    cv = dp / m * 100
    return cv

def frequencia_abs(v):
    # (valor, frequencia%)
    return list(set((x, v.count(x)) for x in v))

def frequencia_relativa(v):
    # (valor, frequencia%)
    return list(set((x, v.count(x) / len(v) * 100) for x in cresc(v)))

def covariancia(v1, v2):
    if len(v1) == len(v2):
        m1 = media(v1)
        m2 = media(v2)
        numerador = sum((v1[i] - m1) * (v2[i] - m2) for i in range(len(v1)))
        return numerador / (len(v1) - 1)
    else:
        # return None
        # acredito que verificar a covariancia de duas listas
        # de tamanho diferente seja um erro no programa do usuário
        # portanto, sugiro que o correto seria lançar uma erro
        raise ValueError("os argumentos de covariancia() sao de diferentes tamanhos")

def correlacao(v1, v2):
    cov = covariancia(v1, v2)
    dp1 = desvioPadraoAmostral(v1)
    dp2 = desvioPadraoAmostral(v2)

    return cov / (dp1 * dp2)

def correlacao_pearson(v1, v2):
    if len(v1) == len(v2):
        m1 = media(v1)
        m2 = media(v2)
        denominador1 = sum((i - m1) ** 2 for i in v1)
        denominador2 = sum((i - m2) ** 2 for i in v2)
        numerador = covariancia(v1, v2)
        return numerador / math.sqrt(denominador1 * denominador2)
    else:
        return None

def grafico(v, titulo, nome):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(titulo)
    ax.plot(v, marker='o', label = nome)
    ax.legend()

def grafico_freq_relativa(v, titulo):
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
