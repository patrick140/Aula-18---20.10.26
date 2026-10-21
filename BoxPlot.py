import numpy as np

# Dados de exemplo

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40, 80])

# Calculando os quartis
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print("Primeiro Quartil\n")
print(q1)
print("\nMediana\n")
print(q2)
print("\nTerceiro Quartil\n")
print(q3)

i = q3 - q1
Limite_inferior = q1 - 1.5 * i

Limite_max = q3 + 1.5 * i

outliers = dados[(dados < Limite_inferior) | (dados > Limite_max)]

dentro = dados[(dados >= Limite_inferior) & (dados <= Limite_max)]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print("Limite inferior: \n")
print(Limite_inferior)
print("\nLimite Superior: \n")
print(Limite_max)
print("\nOutliers: \n")
print(outliers)
print("\nBigode inferior: \n")
print(bigode_inf)
print("\nbigode superior: \n")
print(bigode_sup)



