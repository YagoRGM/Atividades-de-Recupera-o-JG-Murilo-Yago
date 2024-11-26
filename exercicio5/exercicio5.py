#João Gustavo Mota Ramos, Murilo Henrique De Souza Silva, Yago Roberto Gomes Moraes

import statistics

print("Insira os níveis do rio (em metros) para os 12 meses:")
niveis_rio = []
for mes in range(1, 13):
    nivel = float(input(f"Nivel do Mês {mes}: "))
    niveis_rio.append(nivel)

def calcular_media_mediana(niveis):
    media = statistics.mean(niveis)           
    mediana = statistics.median(niveis)
    return media, mediana

media, mediana = calcular_media_mediana(niveis_rio)

print("\nNíveis do rio ao longo do ano:", niveis_rio)
print(f"Média do nível do rio: {media:.2f} metros")
print(f"Mediana do nível do rio: {mediana:.2f} metros")
