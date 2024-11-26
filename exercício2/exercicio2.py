#Joao Gustavo Mota Ramos, Murilo Henrique de Souza Silva, Yago Roberto Gomes Morais
eventos = [
    {"tipo": "Enchente", "local": "Salvador", "intensidade": 5, "data": "2024-01-15"},
    {"tipo": "Furacão", "local": "Estados Unidos", "intensidade": 8, "data": "2024-02-10"},
    {"tipo": "Enchente", "local": "São Paulo", "intensidade": 9, "data": "2024-03-05"},
    {"tipo": "Furacão", "local": "Santa-Catarina", "intensidade": 6, "data": "2024-04-20"},
    {"tipo": "Enchente", "local": "Rio de Janeiro", "intensidade": 10, "data": "2024-05-15"}
]

for evento in [evento for evento in eventos if evento['intensidade'] > 7]:
    print(f"{evento['tipo']} em {evento['local']} com intensidade {evento['intensidade']} na data {evento['data']}")
