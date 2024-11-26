# João Gustavo Mota Ramos, Murilo Henrique de Souza Silva e Yago Roberto Gomes Moraes
import csv
from statistics import mean

def calcular_media_temperaturas(arquivo_csv):
    try:
        with open("temperatura.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                media = mean(map(int, row[1:]))
                print(f"Média de {row[0]}: {media:.2f}°C")

    except FileNotFoundError:
        print("O arquivo 'temperatura.csv' não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")

calcular_media_temperaturas("temperatura.csv")