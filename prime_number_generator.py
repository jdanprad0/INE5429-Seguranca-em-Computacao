import time
from typing import Dict, Union

from generators.blum_blum_shub import BlumBlumShub
from generators.linear_congruential import LinearCongruential
from tests.fermat_test import FermatTest
from tests.miller_rabin_test import MillerRabinTest
from utils.generator_type import GeneratorType
from utils.prime_check_algorithm_type import PrimeCheckAlgorithmType


class PrimeNumberGenerator:
    """
    Classe para geração de números primos usando Miller-Rabin e Blum Blum Shub até que o resultado de Fermat seja True.
    
    Parâmetros:
    p (int): Um número primo onde p ≡ 3 (mod 4) para Blum Blum Shub.
    q (int): Um número primo onde q ≡ 3 (mod 4) para Blum Blum Shub.
    s (int): Semente inicial para Blum Blum Shub.
    a (int): Multiplicador para Congruência Linear.
    c (int): Incremento para Congruência Linear.
    m (int): Módulo para Congruência Linear.
    seed (int): Semente inicial para Congruência Linear.
    miller_rabin_iterations (int): Número de iterações do teste para Miller-Rabin
    fermat_iterations (int): Número de iterações do teste para Fermat
    """
    def __init__(self, p: int, q: int, s: int, a: int, c: int, m: int, seed: int, miller_rabin_iterations: int, fermat_iterations: int):
        self.blum_blum_shub = BlumBlumShub(p, q, s)
        self.linear_congruential = LinearCongruential(a, c, m, seed)
        self.miller_rabin_test = MillerRabinTest(miller_rabin_iterations)
        self.fermat_test = FermatTest(fermat_iterations)


    def generate_prime(self, num_bits: int, algoritmo_gerador: GeneratorType, algoritmo_verificador: PrimeCheckAlgorithmType) -> int:
        """
        Gera um número primo de tamanho num_bits.

        Parâmetros:
        num_bits (int): Número de bits do número primo gerado
        algoritmo_gerador (GeneratorType): Tipo de algoritmo gerador de número pseudo-aleatório utilizado para gerar o número primo
        algoritmo_verificador (PrimeCheckAlgorithmType): Tipo de algoritmo para verificar a primalidade de um número

        Retorna:
        int: Número primo
        """
        while True:
            if (algoritmo_gerador == GeneratorType.BLUM_BLUM_SHUB):
                candidate = self.blum_blum_shub.generate(num_bits)

                isPrime = False
                if (algoritmo_verificador == PrimeCheckAlgorithmType.FERMAT):
                    isPrime = self.fermat_test.fermat(candidate)
                else:
                    isPrime = self.miller_rabin_test.miller_rabin(candidate)
                
                if isPrime:
                    return candidate
                else:
                    self.blum_blum_shub.s += 1 # Apenas muda a semente baseada no horário
            elif (algoritmo_gerador == GeneratorType.LINEAR_CONGRUENTIAL):
                candidate = self.linear_congruential.generate(num_bits)
                
                isPrime = False
                if (algoritmo_verificador == PrimeCheckAlgorithmType.FERMAT):
                    isPrime = self.fermat_test.fermat(candidate)
                else:
                    isPrime = self.miller_rabin_test.miller_rabin(candidate)

                if isPrime:
                    return candidate
                else:
                    self.linear_congruential.seed += 1 # Apenas muda a semente baseada no horário
            else:
                return 0


    def test_prime(self, prime_number: int, num_bits: int) -> Dict[str, Union[int, bool]]:
        """
        Re-testa um número primo gerado usando Fermat e Miller-Rabin.

        Parâmetros
        prime_number (int): Número primo testado.
        num_bits (int): Número de bits do número primo testado.

        Retorna:
        dict[str, int | bool]: dict[número primo testado | resultado do teste por Fermat | tempo de execução de Fermat em segundos | resultado do teste por Miller-Rabin | tempo de execução de Miller-Rabin em segundos | tamanho em bits do número testado, valor retornado].
        """
        start_time = time.time()
        fermat_result = self.fermat_test.fermat(prime_number)
        fermat_time = time.time() - start_time

        start_time = time.time()
        miller_rabin_result = self.miller_rabin_test.miller_rabin(prime_number)
        miller_rabin_time = time.time() - start_time

        return {
            "prime_number": prime_number,
            "fermat_result": fermat_result,
            "fermat_time": fermat_time,
            "miller_rabin_result": miller_rabin_result,
            "miller_rabin_time": miller_rabin_time,
            "num_bits": num_bits
        }
