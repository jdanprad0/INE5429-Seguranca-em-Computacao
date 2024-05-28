class LinearCongruential:
    """
    Implementação do gerador de números pseudo-aleatórios de congruência linear (LCG).

    Parâmetros:
    a (int): Multiplicador.
    c (int): Incremento.
    m (int): Módulo.
    seed (int): Semente inicial.
    """
    def __init__(self, a: int, c: int, m: int, seed: int):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed


    def generate(self, num_bits: int) -> int:
        """
        Gera um número pseudo-aleatório de tamanho num_bits.

        Parâmetros:
        num_bits (int): Número de bits do número pseudo-aleatório gerado.

        Retorna:
        int: Um número pseudo-aleatório de tamanho num_bits.
        """
        x = self.seed
        result = 0
        for i in range(num_bits):
            x = (self.a * x + self.c) % self.m # Calcular Xn+1 = (a * Xn + c) mod m
            bit = x % 2 # Extrair o bit menos significativo de x
            result = (result << 1) | bit # Construir o número resultante bit a bit
        return result
