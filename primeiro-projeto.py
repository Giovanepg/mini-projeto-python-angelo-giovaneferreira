lista_produtos = []
set_produtos = set()
tup_categorias = ('Alimentos', 'Bebidas', 'Limpeza', 'Vestuário', 'N/A')

# Função para categorizar produtos
def adiciona_categoria(produto):
    print("Categorias")
    print("1 - Alimentos")
    print("2 - Bebidas")
    print("3 - Limpeza")
    print("4 - Vestuário")
    categoria = int(input("Digite a opção para a categoria do produto: "))
    if categoria == 1:
        produto['categoria'] = tup_categorias[0]
    elif categoria == 2:
        produto['categoria'] = tup_categorias[1]
    elif categoria == 3:
        produto['categoria'] = tup_categorias[2]
    elif categoria == 4:
        produto['categoria'] = tup_categorias[3]
    else:
        print("Opção inválida, adicionando à categoria: N/A")
        produto['categoria'] = tup_categorias[4]

# Função que exibe o menu no terminal
def menu_principal():
    print("Opções:")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar item")
    print("5 - Excluir")
    print("0 - Sair [encerrar programa]")

# Funções do menu, executam ações
def opcao1():
    codigo = int(input("Insira o número de código do produto: "))
    nome = input("Insira o nome do produto: ")
    preco = float(input("Insira o preço do produto: "))
    qtde = int(input("Insira a quantidade: "))

    novo_produto = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": qtde, "categoria": ""}
    adiciona_categoria(novo_produto)

    set_produtos.add(nome)
    lista_produtos.append(novo_produto)

    print(f"Produto {novo_produto['nome']} adicionado à lista!")

def opcao2():
    if len(lista_produtos) == 0:
        print("Não há nenhum produto cadastrado!")
    for categoria in tup_categorias:
        print(f"Categoria: {categoria}")
        for produto in lista_produtos:
            if produto['categoria'] == categoria:
                print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']} | Quantidade: {produto['quantidade']}")
        print("-------------------------")

def opcao3():
    cod_busca = int(input("Digite o código do produto que deseja buscar: "))
    for produto in lista_produtos:
        if produto['codigo'] == cod_busca:
            print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']}")
            print(f"Preço: {produto['preco']} | Quantidade: {produto['quantidade']}")
            print(f"Categoria: {produto['categoria']}")
        else:
            print(f"Produto de código {cod_busca} não encontrado!")
            break

def opcao4():
    cod_atualiza = int(input("Digite o código do produto a ser atualizado: "))
    for produto in lista_produtos:
        if produto['codigo'] == cod_atualiza:
            print("Digite os novos dados a seguir: ")
            novo_codigo = int(input("Insira o novo número de código do produto: "))
            novo_nome = input("Insira o novo nome para o produto: ")
            novo_preco = float(input("Insira o preço do produto: "))
            novo_qtde = int(input("Insira a quantidade: "))
            
            produto = {'codigo': novo_codigo, 'nome': novo_nome, 'preco': novo_preco, 'quantidade': novo_qtde, 'categoria': ''}
            adiciona_categoria(produto)

            lista_produtos.pop()
            lista_produtos.append(produto)

            print("Novos dados: ")
            print(f"Codigo: {produto['codigo']} | Nome: {produto['nome']}")
            print(f"Preço: {produto['preco']} | Quantidade: {produto['quantidade']}")

def opcao5():
    cod_exclusao = int(input("Digite o código do produto que deseja excluir: "))
    qtde_excluido = 0
    for produto in lista_produtos:
        if produto['codigo'] == cod_exclusao:
            lista_produtos.remove(produto)
            qtde_excluido += 1
    print(f"{qtde_excluido} produto(s) excluído(s).")

# LOOP PRINCIPAL
while True:
    menu_principal()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        opcao1()
    elif escolha == 2:
        opcao2()
    elif escolha == 3:
        opcao3()
    elif escolha == 4:
        opcao4()
    elif escolha == 5:
        opcao5()
    elif escolha == 0:
        print("Encerrando o programa. Adeus!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 5, ou 0 para sair.")
