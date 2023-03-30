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
pyplot.show()


