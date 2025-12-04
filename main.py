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
#-----------------------------------
# Membro 4 - Israel Silva Rodrigues
#-----------------------------------
def editar_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            idx = int(input("digite o número da tarefa a editar: ")) - 1
            if 0 <= idx < len(tarefas):
                nova = input("Digite a nova descrição: ")
                tarefas[idx]['descrição'] = nova 
                print("tarefa atualizada!")
            else:
                print("Número inválido.")
except ValueError:
print("Digite um número válido.")

------------------------------------------
# Membro 5 - Ayllon Victor Santos Araujo
------------------------------------------
def remover_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            idx = int(input("Digite o número da tarefa a remover: ")) - 1
            if 0 <= idx < len(tarefas):
                t = tarefas.pop(idx)
                print(f"Tarefa'{t['descricao']}' removida!")
            else:
                print("Número inválido. ")
        except ValueError:
            print("Digite um número válido.")
-----------------------------------------------------
# Membro 6 - Emile Silva Carvalho
-----------------------------------------------------
def salvar_tarefas():
    with open("tarefas.json", "w") as f:
        json.dump(tarefas, f)
    print("Tarefas salvas!")
        
#----------------------------------------------------
# Membro 7 - Editado por Giullio Nicolau Rocha Mouta
#----------------------------------------------------
def carregar_tarefas():
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
