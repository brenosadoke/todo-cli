import unittest
from todo.utils.filters import filter_todos

TAREFAS = [{'title': 'Comprar pão'}, {'title': 'Pagar conta'},
           {'title': 'Comprar leite'}]


class TestFilterTodos(unittest.TestCase):
    def test_um_resultado(self):
        self.assertEqual(filter_todos('pão', TAREFAS), [{'title': 'Comprar pão'}])

    def test_varios_resultados(self):
        self.assertEqual(len(filter_todos('comprar', TAREFAS)), 2)

    def test_sem_resultado(self):
        self.assertEqual(filter_todos('xyz', TAREFAS), [])

    def test_busca_vazia(self):
        self.assertEqual(filter_todos('', TAREFAS), [])

    def test_maiusculas(self):
        self.assertEqual(len(filter_todos('PAGAR', TAREFAS)), 1)


if __name__ == '__main__':
    unittest.main()
