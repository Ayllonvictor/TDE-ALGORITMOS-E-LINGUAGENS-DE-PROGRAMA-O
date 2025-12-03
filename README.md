# Gerenciador de Tarefas CLI em Python

## 📝 Descrição  
Este projeto é um sistema simples de linha de comando (CLI) em Python para gerenciar tarefas: adicionar, listar, editar e marcar como concluída.  
Útil para quem quer um gerenciador de tarefas leve, sem interface gráfica, e que salva tudo em memória (ou arquivo, se adicionar persistência).

## 📂 Funcionalidades implementadas  
- Adicionar uma nova tarefa com descrição e status “pendente”.  
- Listar todas as tarefas cadastradas.  
- Editar a descrição de uma tarefa existente.  
- Marcar uma tarefa como “concluída”.  

## 🛠 Tecnologias / Linguagem  
- Python 3.x  
- Biblioteca padrão (`json`, `input`, etc — se expandir para salvar em arquivo json)  

## 📥 Como executar  
1. Clone este repositório  
```bash
  https://github.com/Ayllonvictor/TDE-ALGORITMOS-E-LINGUAGENS-DE-PROGRAMA-O/invitations

````
2.Acesse a pasta do projeto



3.Execute com Python
python: main.py


▶️ Exemplos de uso
Para adicionar uma tarefa:

-Digite a descrição da tarefa: Estudar lógica proposicional
 
Tarefa 'Estudar lógica proposicional' adicionada!

**Para listar tarefas:
--- Lista de Tarefas ---
1 - Estudar lógica proposicional [pendente]


**Para editar a tarefa:
Digite o número da tarefa a editar: 1  
Digite a nova descrição: Estudar lógica proposicional – capítulo 2  
Tarefa atualizada!  


**Para marcar como concluída:**
Digite o número da tarefa a marcar como concluída: 1  
Tarefa 'Estudar lógica proposicional – capítulo 2' marcada como concluída!  


**Digite o número da tarefa a marcar como concluída: 1  
Tarefa 'Estudar lógica proposicional – capítulo 2' marcada como concluída!  



🧑‍💻 Estrutura do código
- adicionar_tarefa(): adiciona nova tarefa à lista  
- listar_tarefas(): exibe todas as tarefas, com index e descrição  
- editar_tarefa(): altera a descrição de uma tarefa já existente  
- marcar_concluída(): altera o status da tarefa para “concluída”  
- tarefas: lista global que armazena todas as tarefas como dicionários { "descricao": ..., "status": ... }

  
















