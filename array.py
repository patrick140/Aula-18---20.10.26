import numpy as np

dados_vendas = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 150])

print(dados_vendas)

media = np.mean(dados_vendas)

mediana = np.median(dados_vendas)

print(f"A media é {media}")

print(f"A mediana é {mediana}")

q1 = np.percentile(dados_vendas, 25)
q2 = np.percentile(dados_vendas, 50)
q3 = np.percentile(dados_vendas, 75)

print(q1, q2, q3)