Gerenciador de Tarefas CLI em Python
----------------------------------------------

📝 Descrição

👥 Colaboradores e Responsáveis pelas Funções
----------------------------------------------------

João Neves Monteles Neto — adicionar tarefa

Paulo Rijkaard de Oliveira Rodrigues — listar tarefas

Emmanuella Silva de Oliveira — marcar concluída, README

Israel Silva Rodrigues — editar tarefa

Ayllon Victor Santos Araujo — remover tarefa, estrutura base + integração

Emile Silva Carvalho — salvar/ler arquivo

Giulio Nicolau Rocha Mouta — melhorias no menu

-------------------------------------

Projeto da disciplina Algoritmos e Linguagens de Programação
-----------------------------------------------------------------------------

Este projeto é um Gerenciador de Tarefas em linha de comando (CLI) desenvolvido em Python.
Com ele você pode adicionar, listar, editar e marcar tarefas como concluídas, tudo através de um menu simples no terminal.

📚 Funcionalidades
--------------------------------------------------------------------

✔️ Adicionar novas tarefas

✔️ Listar tarefas cadastradas

✔️ Editar descrição de uma tarefa

✔️ Marcar uma tarefa como concluída

✔️ Interface simples no terminal

🛠️ Tecnologias utilizadas

Python 3.x

Nenhuma biblioteca externa — somente módulos nativos do Python.

▶️ Como executar o programa
----------------------------------------------------------------------

Certifique-se de ter o Python instalado:

python --version


Clone o repositório:
----------------------------------------------------------

git clone https://github.com/Ayllonvictor/TDE-ALGORITMOS-E-LINGUAGENS-DE-PROGRAMA-O


Entre na pasta:
-------------------------------------------------------------

cd TDE-ALGORITMOS-E-LINGUAGENS-DE-PROGRAMA-O


Execute o arquivo principal:
----------------------------------------------------------------------------

python main.py

🧭 Menu de opções
--------------------------------------------------------------------
1 - Adicionar tarefa

2 - Listar tarefas

3 - Editar tarefa

4 - Marcar como concluída

5 - Sair

📂 Estrutura Interna
---------------------------------------------------------------------------------------
As tarefas são armazenadas em uma lista de dicionários:

{
    "descricao": "Exemplo de tarefa",
    "status": "pendente"
}

🚧 Limitações do projeto
-----------------------------------------------------------------------------------------

❌ As tarefas não são salvas em arquivo

❌ Não há função de excluir tarefa

❌ Entradas inválidas podem gerar erros

🎯 Objetivo acadêmico
-----------------------------------------------------------------------------------------

Trabalho desenvolvido para praticar:

Estruturas condicionais

Laços de repetição

Manipulação de listas e dicionários

Entrada e saída de dados

---------------------------------------------
📜 Licença
----------------------------------------------
Uso livre para fins acadêmicos.
