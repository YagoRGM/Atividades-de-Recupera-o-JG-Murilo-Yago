#Joao Gustavo Mota Ramos, Murilo Henrique de Souza Silva, Yago Roberto Gomes Morais
try:
    reducao_diaria = float(input("Digite o valor que você quer economizar diariamente (em reais): "))
    if reducao_diaria >= 0:
        print(f"Você economizaria R$ {reducao_diaria * 365:.2f} em 1 ano.")
    else:
        print("O valor de redução diária não pode ser negativo.")
except:
    print("Por favor, insira um valor válido.")
