import pandas as pd

df1 = pd.read_csv(r"C:\Users\patrick.araujo\OneDrive - SENAC-ARRJ\Documentos\Analista de dados\funcionarios.csv")
df2 = pd.read_csv(r"C:\Users\patrick.araujo\OneDrive - SENAC-ARRJ\Documentos\Analista de dados\funcionarios_v2.csv")

resultado_vertical = pd.concat([df1, df2])