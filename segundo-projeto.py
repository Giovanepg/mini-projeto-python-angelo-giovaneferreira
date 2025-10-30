alunos = {}
nomes_cadastrados = set()

opcao = -1
while opcao != 0:
    print("1 - Cadastrar Aluno")
    print("2 - Registrar Nota")
    print("3 - Listar alunos e média ")
    print("4 - Mostrar aprovados e reprovados")
    print("0 - Sair")

    opcao = int(input("\nEscolha uma opção: "))
    
    # Cadastrar alunos
    if opcao == 1:
        matricula = input("Digite sua matricula: ")
        nome = input("Digite seu Nome: ")

        if nome in nomes_cadastrados:
            print("Nome ja cadastrado")
        else:
            nomes_cadastrados.add(nome)
            alunos[matricula] = (nome, ())
            print("\nAluno cadastrado com sucesso")
            
    # Registrar Notas
    elif opcao == 2:
        matricula = input("\nDigite sua matricula: ")

        if matricula in alunos:
            notas= []
            for i in range(3):
                nota = float(input(f"Digite a {i+1}° nota: "))
                notas.append(nota)
        
            nome = alunos[matricula][0]
            alunos[matricula] = (nome, tuple(notas))
            print("\nNotas registradas com sucesso")
        
        else:
            print("\nAluno não encontrado")
    
    # Listar alunos e Notas
    elif opcao == 3:
        print("\n--- LISTA DE ALUNOS ---")
        print()
        for matricula in alunos:
            nome, notas = alunos[matricula]

            if len(notas) > 0:
                media = sum(notas) / len(notas)
                print(f"{matricula} - {nome}: Média = {media:.1f}")
            else:
                print(f"{matricula} - {nome}: não existe notas para essa matricula ainda.")

     # Mostrar aprovados e reprovados        
    elif opcao == 4:
        print("\n--- APROVADOS E REPROVADOS ---")
        print()
        for matricula in alunos:
            nome, notas = alunos[matricula]

            if len(notas) > 0 :
                media = sum(notas) / len(notas)

                if media >= 7:
                    print(f"{nome} - Média {media:.1f} Aprovado")
                else:
                    print(f"{nome} - Média {media:.1f} Reprovado")

            else:
                print(f"{nome} - não existe notas ainda.")
     #Sair       
    elif opcao == 0:
        print("\n Saindo do sitema...")
    else:
        print("Opção invalida. Tente novamente")            

