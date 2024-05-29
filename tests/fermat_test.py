from typing import List
import random
import time


class FermatTest:
    """
    Classe para realizar o teste de primalidade de Fermat.

    Parâmetros:
    s (int): O número de iterações do teste.
    """
    def __init__(self, s: int):
        self.s = s


    def fermat(self, n: int) -> bool:
        """
        Teste de primalidade de Fermat.

        Parâmetros:
        n (int): O número a ser testado.

        Retorna:
        bool: True se n é provavelmente primo, False se n é composto.
        """

        # Casos base: verifica números pequenos e pares
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False

        # Realiza o teste s vezes
        for i in range(self.s):
            a = random.randint(2, n - 2)
            if pow(a, n - 1, n) != 1:
                return False

        return True


    def test(self, numbers: List[int]):
        """
        Testa a primalidade de uma lista de números.

        Parâmetros:
        numbers (list): Lista de números a serem testados.
        """
        for n in numbers:
            start_time = time.time()
            result = self.fermat(n)
            duration = time.time() - start_time

            print(f"Teste de {n}:")
            print(f"  Fermat: {'Primo' if result else 'Composto'}, Tempo: {duration:.6f} segundos\n")
