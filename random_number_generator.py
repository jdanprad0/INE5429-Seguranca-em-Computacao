import time
from typing import Dict, Tuple, List

from generators.blum_blum_shub import BlumBlumShub
from generators.linear_congruential import LinearCongruential


class RandomNumberGenerator:
    """
    Classe para gerar números aleatórios usando Blum Blum Shub e Congruência Linear.
    
    Parâmetros:
    p (int): Um número primo onde p ≡ 3 (mod 4) para Blum Blum Shub.
    q (int): Um número primo onde q ≡ 3 (mod 4) para Blum Blum Shub.
    s (int): Semente inicial para Blum Blum Shub.
    a (int): Multiplicador para Congruência Linear.
    c (int): Incremento para Congruência Linear.
    m (int): Módulo para Congruência Linear.
    seed (int): Valor inicial (semente) para Congruência Linear.
    """
    def __init__(self, p: int, q: int, s: int, a: int, c: int, m: int, seed: int):
        self.blum_blum_shub = BlumBlumShub(p, q, s)
        self.linear_congruential = LinearCongruential(a, c, m, seed)


    def generate_numbers(self, tamanhos_bits: List[int]) -> Dict[str, Tuple[int, float]]:
        """
        Gera números aleatórios para cada tamanho de bits especificado.

        Parâmetros:
        tamanhos_bits (int): Lista de tamanhos de bits.

        Retorna:
        dict[str, (int, float)]: dict[nome do algoritmo, (número gerado, tempo de geração em segundos)].
        """
        results = {
            "blum_blum_shub": [],
            "linear_congruential": []
        }

        for tamanho in tamanhos_bits:
            start_time = time.time()
            random_number = self.blum_blum_shub.generate(tamanho)
            duration = time.time() - start_time
            results["blum_blum_shub"].append((random_number, duration))

            start_time = time.time()
            random_number = self.linear_congruential.generate(tamanho)
            duration = time.time() - start_time
            results["linear_congruential"].append((random_number, duration))

        return results
