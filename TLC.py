from scipy.stats import expon
import numpy as np
from matplotlib import pyplot


n = 40
qtd_amostras = 1000
lam = 0.2
medias = []

for i in range(qtd_amostras):
  amostra = expon.rvs(size = n,  scale= 1/lam)
  mediaAmostral = np.mean(amostra)
  medias.append(mediaAmostral)  

pyplot.hist(medias)
pyplot.title('Media das amostras com lambda = 0.2')
pyplot.show()

mediaDaAmostra = np.mean(medias)
print('Média aproximada: ', mediaDaAmostra)

varianciaAmostra = np.var(medias)
varianciaPopulacao = varianciaAmostra / n
print('Variancia aproximada: ', varianciaPopulacao)

# Os valores que obtivemos são próximos aos valores teóricos,  o TLC garante que as médias amostrais se aproximam da média da população e a variância das médias amostrais se aproxima da variância da população dividida pelo tamanho da amostra. No entanto, a precisão da aproximação depende do tamanho da amostra. Quanto maior o tamanho da amostra, mais precisa é a aproximação.