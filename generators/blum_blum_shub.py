class BlumBlumShub:
    """
    Implementação do algoritmo Blum Blum Shub (BBS) para geração de números pseudo-aleatórios.

    Parâmetros:
    p (int): Um número primo onde p ≡ 3 (mod 4).
    q (int): Um número primo onde q ≡ 3 (mod 4).
    s (int): Semente inicial.
    """
    def __init__(self, p: int, q: int, s: int):
        self.p = p
        self.q = q
        self.m = p * q # Calcular m = p * q
        self.s = s


    def generate(self, num_bits: int) -> int:
        """
        Gera um número pseudo-aleatório de tamanho num_bits.

        Parâmetros:
        num_bits (int): Número de bits do número pseudo-aleatório gerado.

        Retorna:
        int: Um número pseudo-aleatório de tamanho num_bits.
        """
        x = (self.s * self.s) % self.m # Calcular x0 = s^2 mod m
        result = 0
        for i in range(num_bits):
            x = (x * x) % self.m # Calcular xi+1 = xi^2 mod m
            bit = x % 2 # Extrair o bit menos significativo de x
            result = (result << 1) | bit # Construir o número resultante bit a bit
        return result
