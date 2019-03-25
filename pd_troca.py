#Nomes:Lucas Feliciano da Silva     RA:182487
#      Nicolas de Sousa Imagawa     RA:204147

#Porta dos Desesperados - Probabilidade de Acerto com troca de porta.

import random
import matplotlib.pyplot as plt

v = []			# Vetor de vitorias a cada tentativa, 1 para acerto, 0 para erro
prob = []		# Vetor de probabilidade acumulada de cada tentativa

i = 0
n = 50000		# Numero de tentativas
a = [0, 0 ,1]	# Vetor das portas, com 1 sendo o premio e zero o resto
b = [0, 0 ,1]	# Vetor de escolha, com 1 sendo a escolha do jogador

while i < n:
	random.shuffle(a)				# Embaralhamento do vetor de premio e do vetor de escolha da porta
	random.shuffle(b)
	v.append(a != b)				# O jogador so ganhara nessa rodada se tiver errado a 1a escolha da porta,
	prob.append(sum(v)/(i + 1))		# e trocado depois, visto que a porta revelada sempre sera uma errada,
	i += 1							# ao trocar o jogador automaticamente ganha pois escolheu uma porta diferente
									# da primeira escolhida e diferente da porta revelada.
plt.plot(range(0, n), prob, label= 'Trocou de porta')
plt.legend()
plt.title("Analise do Problema de Monty Hall")
plt.xlabel("Namero de tentativas")
plt.ylabel("Probabilidade acumulada de acertos")
plt.show()