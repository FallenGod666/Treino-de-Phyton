# Cadastro de pessoas

cadastros = []

while True:
    print("\nMenu:")
    print("1. Inserir Cadastro")
    print("2. Sair e Mostrar Cadastros")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        sexo = input("Sexo (M/F): ")
        cadastro = {"Nome": nome, "Idade": idade, "Sexo": sexo}
        cadastros.append(cadastro)
        print("Cadastro adicionado com sucesso!")

    elif opcao == "2":
        print("\nLista de Cadastros:")
        for i, pessoa in enumerate(cadastros, start=1):
            print(f"{i}. Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Sexo: {pessoa['Sexo']}")
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")