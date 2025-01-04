def adicionar_tarefas(tarefas, nome_tarefa):
    tarefas.append({"nome" : nome_tarefa, "check" : False})
    print(f"\nTarefa adicionada!")

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["check"] else " "
        print(f"{indice} - [{status}] {tarefa["nome"]}")

def atualizar_tarefas(tarefas, indice, nova_tarefa):
    tarefas[indice]["nome"] = nova_tarefa
    print("\nTarefa atualizada!")

def completar_tarefas(tarefas, indice):
    if tarefas[indice]["check"] == False:
        tarefas[indice]["check"] = True
        print("\nTarefa atualizada!")
    else:
        tarefas[indice]["check"] = False
        print("\nTarefa atualizada!")

def apagar_tarefas(tarefas, indice):
        del tarefas[indice]
        print("\nTarefa apagada!")


tarefas = []

while True:

    print("\nGerenciador de Lista de Tarefas\n")
    print("1 - Adicionar tarefas")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefas")
    print("4 - Completar tarefas")
    print("5 - Apagar tarefas")
    print("6 - Sair")

    opcao = input("\nDigite o número da sua opção: ")

    if opcao == "1":
        nome_tarefa = input("Digite a tarefa que deseja adicionar: ")
        adicionar_tarefas(tarefas, nome_tarefa)

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            ver_tarefas(tarefas)
    
    elif opcao =="3":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            ver_tarefas(tarefas)
            try:
                indice = int(input("\nDigite o número da tarefa que deseja atualizar: "))
                indice -= 1
                if indice >= 0 and indice < len(tarefas):
                    nova_tarefa = input("Digite a nova tarefa: ")
                    atualizar_tarefas(tarefas, indice, nova_tarefa)
                else:
                    print("Por favor, digite um número de tarefa válido.")
            except Exception as e:
                print("Por favor, digite um número de tarefa válido.")
            

    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            ver_tarefas(tarefas)
            try:
                indice = int(input("\nDigite o número da tarefa que deseja compeltar: "))
                indice -= 1
                if indice >= 0 and indice < len(tarefas):
                    completar_tarefas(tarefas, indice)
                else:
                    print("Por favor, digite um número de tarefa válido.")
            except Exception as e:
                print("Por favor, digite um número de tarefa válido.")

    elif opcao == "5":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            ver_tarefas(tarefas)
            try:
                indice = int(input("\nDigite o número da tarefa que deseja apagar: "))
                indice -= 1
                if indice >= 0 and indice < len(tarefas):
                    apagar_tarefas(tarefas, indice)
                else:
                    print("Por favor, digite um número de tarefa válido.")
            except Exception as e:
                print("Por favor, digite um número de tarefa válido.")
            
    elif opcao == "6":
        break
    
    else:
        print("Por favor, digite uma opção válida.")

print("\nAté mais!")