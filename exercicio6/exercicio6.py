#João Gustavo Mota Ramos, Murilo Henrique De Souza Silva, Yago Roberto Gomes Moraes

import statistics

def calcula_media_temperatura(temperaturas):  
    return statistics.mean(temperaturas)

cidades = {
    "Caçapava": [22.5, 23.0, 22.8, 23.2, 23.5, 22.7, 22.9, 23.1, 23.4, 23.3, 22.6, 23.0],
    "São José dos Campos": [24.0, 24.2, 23.8, 24.1, 24.3, 24.5, 24.7, 24.6, 24.4, 24.0, 23.9, 24.1],
    "Taubaté": [23.5, 23.7, 23.6, 23.9, 24.0, 24.2, 23.8, 23.6, 23.7, 24.1, 24.0, 23.9],
    "Jacareí": [22.0, 22.5, 21.8, 22.3, 22.7, 22.4, 22.6, 22.1, 22.8, 22.3, 22.2, 22.5],
    "São Paulo": [25.0, 25.2, 24.8, 25.1, 25.3, 25.5, 25.6, 25.4, 25.7, 25.0, 25.1, 25.2],
}

for cidade, temperaturas in cidades.items():
    media = calcula_media_temperatura(temperaturas)
    print(f"A média de temperatura anual em {cidade} é {media:.2f}°C")

