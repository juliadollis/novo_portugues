import pandas as pd

# Le o arquivo CSV
df = pd.read_csv("train.csv", delimiter="|")

# Salva como arquivo Excel
df.to_excel("train.xlsx", index=False)
