import time
import sys

from logger import Logger
from prime_number_generator import PrimeNumberGenerator
from random_number_generator import RandomNumberGenerator
from utils.generator_type import GeneratorType
from utils.prime_check_algorithm_type import PrimeCheckAlgorithmType


def main():
    # Escreve saídas do console em um arquivo
    sys.stdout = Logger("output.txt")

    # Parâmetros para os geradores
    p = 383
    q = 503
    s = 101355

    a = 15005
    c = 8371
    m = 19993
    seed = 135

    tamanhos_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    miller_rabin_iterations = 50
    fermat_iterations = 50

    prime_generator = PrimeNumberGenerator(p, q, s, a, c, m, seed, miller_rabin_iterations, fermat_iterations)
    random_generator = RandomNumberGenerator(p, q, s, a, c, m, seed)

    # Gerando números aleatórios com Blum Blum Shub e Congruência Linear
    random_numbers = random_generator.generate_numbers(tamanhos_bits)

    print("Números gerados com Blum Blum Shub:")
    for i, (num, duration) in enumerate(random_numbers["blum_blum_shub"]):
        print(f"Número de {tamanhos_bits[i]} bits: {num} (Tempo: {duration:.6f} segundos)")

    print("\nNúmeros gerados com Congruência Linear:")
    for i, (num, duration) in enumerate(random_numbers["linear_congruential"]):
        print(f"Número de {tamanhos_bits[i]} bits: {num} (Tempo: {duration:.6f} segundos)")

    # Gerando e testando números primos
    print("\n\n" + "-"*50 + "\n")
    for algoritmo_gerador in [GeneratorType.BLUM_BLUM_SHUB, GeneratorType.LINEAR_CONGRUENTIAL]:
        for algoritmo_verificador in [PrimeCheckAlgorithmType.MILLER_RABIN, PrimeCheckAlgorithmType.FERMAT]:
            for num_bits in tamanhos_bits:
                # Resetando semente
                prime_generator.blum_blum_shub.s = s
                prime_generator.linear_congruential.seed = seed
                
                print(f"\nGerando número primo de {num_bits} bits com {algoritmo_gerador.value} e verificando com {algoritmo_verificador.value}...")
                start_time = time.time()
                prime_number = prime_generator.generate_prime(num_bits, algoritmo_gerador, algoritmo_verificador)
                generation_time = time.time() - start_time

                print(f"Número primo gerado: {prime_number}")
                print(f"Tempo de geração: {generation_time:.6f} segundos")

                test_results = prime_generator.test_prime(prime_number, num_bits)
                print(f"Fermat: {'Primo' if test_results['fermat_result'] else 'Composto'}, Tempo: {test_results['fermat_time']:.6f} segundos")
                print(f"Miller-Rabin: {'Primo' if test_results['miller_rabin_result'] else 'Composto'}, Tempo: {test_results['miller_rabin_time']:.6f} segundos\n")
                print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()
