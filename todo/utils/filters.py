# -*- coding: UTF-8 -*-


def filter_todos(query, todos):
    """Função pura: devolve as tarefas cujo título contém a busca.

    Não lê arquivo nem imprime. Sempre devolve uma lista
    (vazia se a busca for vazia ou não houver resultado).
    """
    if not query:
        return []
    query_lower = query.lower()
    return [t for t in todos if query_lower in t['title'].lower()]
