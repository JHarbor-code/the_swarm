from dataclasses import dataclass

@dataclass
class Allele:
    """
    Objet permettant de définir l'expression d'un gène.
    """
    name: str
    valeur: float
    dominance: float