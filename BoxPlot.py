import numpy as np

# Dados de exemplo

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

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
