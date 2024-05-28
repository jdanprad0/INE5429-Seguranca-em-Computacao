from enum import Enum


class PrimeCheckAlgorithmType(Enum):
    MILLER_RABIN = "Miller-Rabin"
    FERMAT = "Fermat"