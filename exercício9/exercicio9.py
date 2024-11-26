# João Gustavo Mota Ramos, Murilo Henrique de Souza Silva e Yago Roberto Gomes Moraes
def classifica_desastre(desastre, intensidade):
    if desastre == "Tremor de terra":
        if intensidade < 4.0:
            return "Baixo impacto"
        elif 4.0 <= intensidade <= 6.0:
            return "Médio impacto"
        else:
            return "Alto impacto"
    elif desastre == "Tsunami":
        if intensidade < 1.0:
            return "Baixo impacto"
        elif 1.0 <= intensidade <= 3.0:
            return "Médio impacto"
        else:
            return "Alto impacto"
    elif desastre == "Deslizamento":
        if intensidade < 10000:
            return "Baixo impacto"
        elif 10000 <= intensidade <= 100000:
            return "Médio impacto"
        else:
            return "Alto impacto"
    elif desastre == "Ciclone":
        if intensidade < 154:
            return "Baixo impacto"
        elif 154 <= intensidade <= 208:
            return "Médio impacto"
        else:
            return "Alto impacto"
    elif desastre == "Tempestade":
        if intensidade < 50:
            return "Baixo impacto"
        elif 50 <= intensidade <= 100:
            return "Médio impacto"
        else:
            return "Alto impacto"
    elif desastre == "Onda de calor":
        if intensidade < 5:
            return "Baixo impacto"
        elif 5 <= intensidade <= 10:
            return "Médio impacto"
        else:
            return "Alto impacto"
    else:
        return "Desastre desconhecido"

desastres = ["Tremor de terra", "Tsunami", "Deslizamento", "Ciclone", "Tempestade", "Onda de calor"]

print("Escolha um dos seguintes desastres:")
for i, desastre in enumerate(desastres, 1):
    print(f"{i}. {desastre}")

while True:
    try:
        escolha = int(input("Digite o número do desastre escolhido: "))
        if 1 <= escolha <= len(desastres):
            desastre_escolhido = desastres[escolha - 1]
            break
        else:
            print("Escolha inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

try:
    intensidade = float(input(f"Digite a intensidade do {desastre_escolhido}: "))
    classificacao = classifica_desastre(desastre_escolhido, intensidade)
    print(f"O impacto do {desastre_escolhido} é classificado como: {classificacao}")
except ValueError:
    print("Entrada inválida para a intensidade. Certifique-se de digitar um número.")
