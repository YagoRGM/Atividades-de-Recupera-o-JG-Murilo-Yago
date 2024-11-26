#Joao Gustavo Mota Ramos, Murilo Henrique de Souza Silva, Yago Roberto Gomes Morais
dados_climaticos = {
    "São Paulo": {
        'clima_atual': 'Chuva',
        'temperatura_maxima': 30,
        'temperatura_minima': 20,
        'umidade_relativa': 80,
        'pressao_atmosferica': 1013,
        'precipitacao': 0.5
    },
    "Rio de Janeiro": {
        'clima_atual': 'Ensolarado',
        'temperatura_maxima': 25,
        'temperatura_minima': 15,
        'umidade_relativa': 60,
        'pressao_atmosferica': 1010,
        'precipitacao': 1.2
    },
    "Belo Horizonte": {
        'clima_atual': 'Ensolarado',
        'temperatura_maxima': 28,
        'temperatura_minima': 15,
        'umidade_relativa': 60,
        'pressao_atmosferica': 1010,
        'precipitacao': 1.2
    },
}

cidade_mais_quente = None
maior_temperatura = float('-inf')

for cidade, dados in dados_climaticos.items():
    temperatura_maxima = dados.get('temperatura_maxima', float('-inf'))
    if temperatura_maxima > maior_temperatura:
        maior_temperatura = temperatura_maxima
        cidade_mais_quente = cidade

print(f"A cidade com a maior temperatura máxima é: {cidade_mais_quente}")
