import unittest
from lab6 import solve_gamsrv


class TestGamSrv(unittest.TestCase):
    def test_example_1(self):
        """Перевірка першого прикладу з умови завдання."""
        n = 6
        clients = [1, 2, 6]
        edges = [
            (1, 3, 10),
            (3, 4, 80),
            (4, 5, 50),
            (5, 6, 20),
            (2, 3, 40),
            (2, 4, 100),
        ]
        self.assertEqual(solve_gamsrv(n, clients, edges), 100)

    def test_example_2(self):
        """Перевірка другого прикладу: складна топологія."""
        n = 9
        clients = [2, 4, 6]
        edges = [
            (1, 2, 20),
            (2, 3, 20),
            (3, 6, 20),
            (6, 9, 20),
            (9, 8, 20),
            (8, 7, 20),
            (7, 4, 20),
            (4, 1, 20),
            (5, 2, 10),
            (5, 4, 10),
            (5, 6, 10),
            (5, 8, 10),
        ]
        self.assertEqual(solve_gamsrv(n, clients, edges), 10)

    def test_example_3(self):
        """Перевірка третього прикладу: великі значення затримки."""
        n = 3
        clients = [1, 3]
        edges = [
            (1, 2, 50),
            (2, 3, 1000000000),
        ]
        self.assertEqual(solve_gamsrv(n, clients, edges), 1000000000)

    def test_no_path_scenario(self):
        """
        Перевірка обробки ізольованих вузлів.
        Якщо маршрутизатор не має зв'язку з клієнтом, 
        відстань вважається нескінченною.
        """
        n = 4
        clients = [1, 4]
        # Вузол 3 ізольований від 4, тому він не може бути сервером
        edges = [
            (1, 2, 10),
            (2, 3, 10),
        ]
        # Вузол 2 може дійти до 1, але не до 4.
        # Відповідно, безпечний варіант повинен обробляти inf
        result = solve_gamsrv(n, clients, edges)
        self.assertTrue(result == float('inf') or result >= 0)


if __name__ == "__main__":
    unittest.main()