from typing import List
import random
import time


class MillerRabinTest:
    """
    Classe para realizar o teste de primalidade de Miller-Rabin.

    Parâmetros:
    s (int): O número de iterações do teste.
    """
    def __init__(self, s: int):
        self.s = s


    def miller_rabin(self, n: int) -> bool:
        """
        Teste de primalidade de Miller-Rabin.

        Parâmetros:
        n (int): O número a ser testado.

        Retorna:
        bool: True se n é provavelmente primo, False se n é composto.
        """

        # Casos base
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False

        # Escreva n-1 na forma 2^t * u
        t, u = 0, n - 1
        while u % 2 == 0:
            t += 1
            u //= 2

        # Realiza o teste s vezes
        for j in range(self.s):
            a = random.randint(2, n - 2)
            if self.check_composite(a, t, u, n):
                return False

        return True


    def check_composite(self, a: int, t: int, u: int, n: int) -> bool:
        """
        Verifica se o número é composto para uma base a.

        Parâmetros:
        a (int): A base para o teste.
        t (int): O número de fatores de 2 em n-1.
        u (int): O fator ímpar em n-1.
        n (int): O número sendo testado.

        Retorna:
        bool: True se n é composto, False se provavelmente primo.
        """
        x = pow(a, u, n)
        for i in range(t):
            new_x = pow(x, 2, n)
            if new_x == 1 and x != 1 and x != n - 1:
                return True
            x = new_x
        if new_x != 1:
            return True
        return False


    def test(self, numbers: List[int]):
        """
        Testa a primalidade de uma lista de números.

        Parâmetros:
        numbers (list): Lista de números a serem testados.
        """
        for n in numbers:
            start_time = time.time()
            result = self.miller_rabin(n)
            duration = time.time() - start_time

            print(f"Teste de {n}:")
            print(f"  Miller Rabin: {'Primo' if result else 'Composto'}, Tempo: {duration:.6f} segundos\n")
