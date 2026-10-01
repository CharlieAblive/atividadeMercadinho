from Produto import Produto
usuario = input("Usuário: ")
listaDeCompras = []


#sistema de instanciamento de produtos
opcao = input(f"Adicionar um produto ao carrinho(s/n): \n")
while True:
    if opcao != 'n':
        produto = Produto(input("Nome do produto:\n"), float(input("Valor do produto:\n")))
        listaDeCompras.append(produto)
        opcao = input("Deseja adicionar um novo produto ao carrinho? (s/n): ")
        total = 0
        for produto in listaDeCompras:
            total += produto.preco
    else:
        with open("pagamento.txt", 'w', encoding='utf-8') as arquivo:
                    arquivo.write(f"======== MERCADINHO ========\n\n")
                    arquivo.write(f"---{usuario}---\n")
                    for produto in listaDeCompras:
                        arquivo.write(f"{produto.nome} -------- {produto.preco}\n")
                    arquivo.write(f"-------------------------------------\n\n")
                    arquivo.write(f"TOTAL: R$ {total:.2f}\n")
                    
        with open("pagamento.txt", 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            posicao = texto.find("TOTAL: R$")
            valorTotal = texto[posicao + len("TOTAL: R$ "):posicao+(len("TOTAL:R$ ")+5)]

            print(f"Compra confirmada com sucesso! Valor total: {valorTotal:.2f}")
            print(f"Obrigado por escolher o MERCADINHO\nVolte sempre!")

        break 







