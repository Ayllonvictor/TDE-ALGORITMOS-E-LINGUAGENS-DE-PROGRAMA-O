import json

#lista de tarefas
tarefas = []
#------------------------------------
# Membro 1 - João Neves Monteles Neto
#------------------------------------
def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa:")
    tarefas.append({"Descrição": descricao, "status": "pendente"})
print(f"Tarefa '{descricao}' adicionada!")
#------------------------------------------------
# Membro 2 - Paulo Rijkaard de Oliveira Rodrigues
#------------------------------------------------
def listar_tarefas():
if not tarefas:
        print("Nenhuma tarefa cadastrada.")
else:
        print("\n--- Lista de Tarefas ---")
        for i, t in enumerate(tarefas, 1):
                print(f"{i} - {t['descricao']}                
[{t['status']}]")
#----------------------------------------
# Membro 3 - Emmanuella Silva de Oliveira
#----------------------------------------
  def marcar_concluida():
        listar_tarefas()
        if tarefas:
            try:
                idx =  int(input("Digite o número da tarefa a marcar como concluída:")) - 1
                if 0 <= idx < len(tarefas):
                    tarefas[idx]['status'] = 'concluida'
                    print(f"Tarefa '{tarefas[idx] ['descricao']}' marcada como concluida!")
                    else:
                    print("número inválido.")
                    except ValueError:
                    print("Digite um número válido")

# Membro 4
def editar_tarefa():
    pass

# Membro 5
def remover_tarefa():
    pass

# Membro 6
def carregar_tarefas():
    pass

#----------------------------------------------------
# Membro 7 - Editado por Giullio Nicolau Rocha Mouta
#----------------------------------------------------
def salvar_tarefas():
   global tarefa
    try:
        with open("tarefas.json", "r") as f:
            tarefas = json.load(f)
except FileNotFoundError:
    tarefas = []

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
