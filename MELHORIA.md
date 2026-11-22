# Melhoria: modularização do comando de busca

Projeto original: todo-cli, de François Chalifour (licença MIT)
https://github.com/francoischalifour/todo-cli (commit 8376541)

Alteração: o filtro de tarefas saiu de SearchCommand.get_matches
(todo/commands/search.py) e virou a função pura filter_todos
(todo/utils/filters.py). get_matches agora só chama essa função.

Verificação: python -m unittest test_filter_todos
