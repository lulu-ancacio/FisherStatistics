<div align="center">
<img width=460px src='https://user-images.githubusercontent.com/110111018/267866057-56f1bf60-7067-4b36-813e-9a9bfc4b9e94.png'>
<br>
<img src="https://img.shields.io/github/license/lulu-ancacio/numbersOf?style=plastic">
<img src="http://img.shields.io/static/v1?label=language&message=python&color=rgb(0, 154, 69)&style=plastic">
</div>

<h2>Módulo</h2>
<p>
Estatística é um campo muito decimal da matemática, nessa área os cálculos realmente exigem milimetros de precisão e atenção. Pensando nesta complexidade, <strong>FisherStatistics</strong> trás um acervo de operações estatísticas e representações gráficas de um conjunto de dados, trabalhando com MatPlotLib.
<br>
Quais cálculos este módulo oferece?
<ul>
<li>Média aritmética</li>
<li>Média geométrica</li>
<li>Média harmônica</li>
<li>Média quadrática</li>
<li>Mediana</li>
<li>Moda</li>
<li>Quartil</li>
<li>Organização crescente</li>
<li>Organização decrescente</li>
<li>Variação populacional</li>
<li>Variação amostral</li>
<li>Desvio padrão</li>
<li>Desvio padrão amostral</li>
<li>Intervalo</li>
<li>Coeficiente de Variação</li>
<li>Frequência absoluta</li>
<li>Frequência relativa</li>
<li>Correlação</li>
<li>Gráfico de dados</li>
<li>Gráfico de frequência</li>
</ul>
</p>

<br>
<p>
  <h2>Utilidades</h2>
  <h3>Exemplo 1: Gráfico pluviométrico de São Paulo em barras.</h3>
    
```python
meses = ['Jan', 'Fev', 'Mai', 'Abr', 'Mar', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
precipitacao = [224,183,158,76,74,49,55,42,99,129,144,189]
graficoBarraCorresp(meses, precipitacao,'Precipitação mensal em São Paulo - SP (2022)','Mês', 'Pluviosidade (mm)')
```

  <img src='https://user-images.githubusercontent.com/110111018/269766241-4032ebb9-8aa5-4253-bd85-3acf59e5952b.png'>

  <h3>Exemplo 2: Análise de dados aleatórios.</h3>

```python
import random
v = []

for i in range(50):
    v.append(random.randint(1,1000))
graficoLinha(v, 'Gráfico aleatório', 'Exemplo')
print(f'Média: {media(v)} \n Moda: {moda(v)} \n Mediana: {mediana(v)} \n Quartil: {quartil(v)} \n Desvio padrão: {desvioPadrao(v)} \n Frequência Absoluta: {frequenciaAbs(v)}')
```

<img src='https://user-images.githubusercontent.com/110111018/268543588-8ef76a23-0acc-42a4-90b1-1d0a0d5060ee.png'>

  <h3>Exemplo 3: Análise de frequência de valores.</h3>

```python
notas = [97, 92, 92, 97, 100, 42, 86, 92, 100, 42, 97, 92]
graficoFreqRelativa(notas, 'Frequência de Notas')
nota_porcent = frequenciaRelativa(notas)

for i in range(len(nota_porcent)):
    print(f'Porcentagem de frequência do valor {nota_porcent[i][0]}: {nota_porcent[i][1]}%')
```

<img src='https://user-images.githubusercontent.com/110111018/269792619-489b8c7c-5e83-4af8-bb13-4aba2d513d4d.png'>
  
  </p>
