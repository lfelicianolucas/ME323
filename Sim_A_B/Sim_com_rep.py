#Nomes:Lucas Feliciano da Silva     RA:182487
#      Nicolas de Sousa Imagawa     RA:204147

#Simulação candidatos A e B com reposição.

#Importações necessárias para o gráfico.
from random import choices
import matplotlib.pyplot as plt
import scipy.stats as spst
from matplotlib.offsetbox import AnchoredText

#Votos no candidato A são tratados como 1. Em B, 0.
votos = [1,0]
proporcao = [0.3,0.7]


n1 = 50
n2 = 500
lista_1 = []
lista_2 = []
for i in range (0, 2000):
	auxlist = choices(population = votos,
					  weights = proporcao,
					  k=n1,
					  )
	lista_1.append(sum(auxlist))
vm_1 = sum(lista_1)/2000

#Lista auxiliar para calcular o desvio padrão.
auxlist = []
for i in range(0, 2000):
    aux = ((lista_1[i]) - (vm_1))**2
    auxlist.append(aux)
#Cálculo do desvio padrão.
sd_1 = (sum(auxlist)/1999)**(0.5)

#Plot do Histograma.

fig1 = plt.figure(figsize=(8,6))
num_bins = 8
n, bins, patches = plt.hist(lista_1, num_bins,density=1, facecolor='blue', edgecolor='black', linewidth=1.2)
y = spst.norm.pdf(bins, vm_1, sd_1)
plt.plot(bins, y, 'r--')
plt.xlabel('nº Eleitores')
plt.ylabel('Probabilidade')
plt.title(r'Eleitores de A em amostras com reposicao de tamanho 50')
ax = fig1.add_subplot(111)
textstr = r'$\mu = $'+"{:7.3f}".format(vm_1) +'\n' + r'$\sigma = $'+"{:8.3f}".format(sd_1)
at = AnchoredText(textstr, prop=dict(size=12), frameon=True, loc=2)
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)
plt.show()

for i in range (0, 2000):
	auxlist = choices(population = votos,
					  weights = proporcao,
					  k=n2,
					  )
	lista_2.append(sum(auxlist))
vm_2 = sum(lista_2)/2000
#Lista auxiliar para calcular o desvio padrão.
auxlist = []
for i in range(0, 2000):
    aux = ((lista_2[i]) - (vm_2))**2
    auxlist.append(aux)
#Cálculo do desvio padrão.
sd_2 = (sum(auxlist)/1999)**(0.5)
#Plot do Histograma.
fig2 = plt.figure(figsize=(8,6))
num_bins = 20
n, bins, patches = plt.hist(lista_2, num_bins,density=1, facecolor='blue', edgecolor='black', linewidth=1.2)
y = spst.norm.pdf(bins, vm_2, sd_2)
plt.plot(bins, y, 'r--')
plt.xlabel('nº Eleitores')
plt.ylabel('Probabilidade')
plt.title(r'Eleitores de A em amostras com reposicao de tamanho 500')
ax = fig2.add_subplot(111)
textstr = r'$\mu = $'+"{:7.3f}".format(vm_2) +'\n' + r'$\sigma = $'+"{:8.3f}".format(sd_2)
at = AnchoredText(textstr, prop=dict(size=12), frameon=True, loc=2)
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)
plt.show()
