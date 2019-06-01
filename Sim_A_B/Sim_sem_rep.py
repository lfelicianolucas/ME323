#Nomes:Lucas Feliciano da Silva     RA:182487
#      Nicolas de Sousa Imagawa     RA:204147

#Simulação candidatos A e B

#Importações necessárias para o gráfico.
import random
import matplotlib.pyplot as plt
import scipy.stats as spst
from matplotlib.offsetbox import AnchoredText

#Votos no candidato A são tratados como 1. Em B, 0.
votoa = [1]*3000
votob = [0]*7000

#Lista com os 10000 votos.
votototal = votoa + votob

#Lista de valores em A.
lista = []

for n in range (0, 2000):
    #Embaralhamento da lista.
    random.shuffle(votototal)
    #Lista embaralhada para variar os dados amostrais.
    rlist = votototal
    #Valores de P "chapéu".
    pch = rlist[0:49]
    #Como trabalhamos como 0s e 1s, a soma dos valores da lista dá o número de eleitores de A.
    suma = sum(pch)
    #Salva-se isso na lista dos eleitores de A.
    lista.append(suma)

#Cálculo do valor médio.
vm = sum(lista)/2000
#Lista auxiliar para calcular o desvio padrão.
auxlist = []

for e in range(0, len(lista)):
    aux = ((lista[e]) - (vm))**2
    auxlist.append(aux)

#Cálculo do desvio padrão.
sd = (sum(auxlist)/1999)**(0.5)

#Plot do Histograma.
fig = plt.figure(figsize=(8,6))
num_bins = 8
n, bins, patches = plt.hist(lista, num_bins,density=1, facecolor='blue', edgecolor='black', linewidth=1.2)
y = spst.norm.pdf(bins, vm, sd)
plt.plot(bins, y, 'r--')
plt.xlabel('nº Eleitores')
plt.ylabel('Probabilidade')
plt.title(r'Eleitores de A em amostras sem reposicao de tamanho 50')

ax = fig.add_subplot(111)
textstr = r'$\mu = $'+"{:7.3f}".format(vm) +'\n' + r'$\sigma = $'+"{:8.3f}".format(sd)
at = AnchoredText(textstr, prop=dict(size=12), frameon=True, loc=2)
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

plt.show()

#Reset de variáveis que serão reutilizadas.
suma = 0
lista = []


for n in range (0, 2000):
    # Embaralhamento da lista.
    random.shuffle(votototal)
    # Lista embaralhada para variar os dados amostrais.
    rlist = votototal
    # Valores de P "chapéu".
    pch = rlist[0:499]
    # Como trabalhamos como 0s e 1s, a soma dos valores da lista dá o número de eleitores de A.
    suma = sum(pch)
    # Salva-se isso na lista dos eleitores de A.
    lista.append(suma)

#Cálculo do valor médio.
vm = sum(lista)/2000
#Lista auxiliar para calcular o desvio padrão.
auxlist = []

for e in range(0, len(lista)):
    aux = ((lista[e]) - (vm))**2
    auxlist.append(aux)

#Cálculo do desvio padrão.
sd = ((sum(auxlist))/(1999))**(0.5)

#Plot do Histograma.

fig = plt.figure(figsize=(8,6))
x = lista
num_bins = 20
n, bins, patches = plt.hist(lista, num_bins,density=1, facecolor='blue', edgecolor='black', linewidth=1.2)
y = spst.norm.pdf(bins, vm, sd)
plt.plot(bins, y, 'r--')
plt.xlabel('nº Eleitores')
plt.ylabel('Probabilidade')
plt.title(r'Eleitores de A em amostras sem reposicao de tamanho 500')

ax = fig.add_subplot(111)
textstr = r'$\mu = $'+"{:7.3f}".format(vm) +'\n' + r'$\sigma = $'+"{:8.3f}".format(sd)
at = AnchoredText(textstr, prop=dict(size=12), frameon=True, loc=2)
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

plt.show()