from dataclasses import dataclass

@dataclass
class Allele:
    name: str
    valeur: float
    dominance: float