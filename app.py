import time
from prime_number_generator import PrimeNumberGenerator
from random_number_generator import RandomNumberGenerator

def main():
    # Parâmetros para os geradores
    p = 383
    q = 503
    s = 101355

    a = 1664525
    c = 1013904223
    m = 2**32
    seed = 104729

    tamanhos_bits = [20, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
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
    for num_bits in tamanhos_bits:
        print(f"\nGerando número primo de {num_bits} bits com Blum Blum Shub...")
        start_time = time.time()
        prime_number = prime_generator.generate_prime(num_bits)
        generation_time = time.time() - start_time

        print(f"Número primo gerado: {prime_number}")
        print(f"Tempo de geração: {generation_time:.6f} segundos")

        test_results = prime_generator.test_prime(prime_number, num_bits)
        print(f"Número de {num_bits} bits: {prime_number}")
        print(f"Fermat: {'Primo' if test_results['fermat_result'] else 'Composto'}, Tempo: {test_results['fermat_time']:.6f} segundos")
        print(f"Miller-Rabin: {'Primo' if test_results['miller_rabin_result'] else 'Composto'}, Tempo: {test_results['miller_rabin_time']:.6f} segundos")
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()
