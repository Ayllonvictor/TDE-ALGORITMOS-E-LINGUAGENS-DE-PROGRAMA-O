import json

#lista de tarefas
tarefas = []
#---------
# Membro 1
#---------
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa:")
    tarefas.append({"Descrição": descricao, "status": "pendente"})
print(f"Tarefa '{descricao}' adicionada!")
    
# Membro 2
def listar_tarefas():
    pass

# Membro 3
def marcar_concluida():
    pass

# Membro 4
def editar_tarefa():
    pass

# Membro 5
def remover_tarefa():
    pass

# Membro 6
def carregar_tarefas():
    pass

# Membro 7
def salvar_tarefas():
    pass

def main():
    while True:
        print("===== SISTEMA TO-DO =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar como concluída")
        print("4 - Editar tarefa")
        print("5 - Remover tarefa")
        print("6 - Sair")
        escolha = input("Escolha: ")

        if escolha == "6":
            break

if __name__ == "__main__":
    main()
