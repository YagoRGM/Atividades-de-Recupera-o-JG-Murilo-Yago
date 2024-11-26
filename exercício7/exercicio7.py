# João Gustavo Mota Ramos, Murilo Henrique de Souza Silva e Yago Roberto Gomes Moraes
produtos = []

def cadastra_produto(nome_produto, preco_produto, quantidade_produto):
    informacoes = {"nome": nome_produto, "preço": preco_produto, "quantidade": quantidade_produto}
    return informacoes

for i in range(1, 6):
    print(f"Cadastro do produto {i}:")
    nome_digitado = input(f"Digite o nome do produto {i}: ")
    preco_digitado = int(input(f"Digite o preço do produto {i}: "))
    quantidade_digitada = int(input(f"Digite a quantidade do produto {i}: "))
    print(f"Produto {i} adicionado com sucesso!")
    cadastrar = cadastra_produto(nome_digitado, preco_digitado, quantidade_digitada)
    produtos.append(cadastrar)

for produto in produtos:
    print (f"Produtos cadastrados: {produto}")