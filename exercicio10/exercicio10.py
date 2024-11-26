#João Gustavo Mota Ramos, Murilo Henrique De Souza Silva, Yago Roberto Gomes Moraes

import matplotlib.pyplot as plt

def gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(dias, temperaturas_maximas, width=0.3, label="Temperatura Máxima", align="center", color="red")
    ax.bar(dias, temperaturas_minimas, width=0.3, label="Temperatura Mínima", align="edge", color="blue")

    ax.set_title('Temperaturas Máximas e Mínimas dos Últimos 7 Dias')
    ax.set_xlabel('Dias')
    ax.set_ylabel('Temperatura (°C)')

    ax.legend()

    plt.tight_layout()
    plt.show() 
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
temperaturas_maximas = []
temperaturas_minimas = []

for dia in dias:
    temp_max = float(input(f"Digite a temperatura máxima para {dia}: "))
    temp_min = float(input(f"Digite a temperatura mínima para {dia}: "))
    
    temperaturas_maximas.append(temp_max)
    temperaturas_minimas.append(temp_min)
gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias)

 