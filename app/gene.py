from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class Allele:
    name: str
    valeur: float
    dominance: float


class Gene: 

    alleles_possibles: list[Allele] = []

    def __init__(self, allele1: Allele, allele2: Allele):

        self.allele1 = allele1
        self.allele2 = allele2


    def calculer_expression(self):
        
        a1, a2 = self.allele1, self.allele2

        if a1.valeur <= a2.valeur:
            ref, alt = a1, a2
        else:
            ref, alt = a2, a1

        h = alt.dominance
        return ref.valeur + h * (alt.valeur - ref.valeur)
    
        
    @classmethod
    def ajouter_allele(cls, valeur: float, parent:Allele | None = None) -> Allele:
        """
        Ajoute un nouvel allèle à la liste de classe `alleles_possibles` en générant un nom automatiquement.

        Le nom de l'allèle est choisi dynamiquement selon sa valeur :
        - supérieure à 0.5 → commence par "A"
        - inférieure ou égale à 0.5 → commence par "a"
        Un suffixe numérique est ajouté si plusieurs allèles du même type existent.

        Args:
            valeur (float): La valeur de l'allèle, comprise entre 0 et 1.

        Returns:
            Allele: L'instance d'`Allele` créée et ajoutée à `cls.alleles_possibles`.
        """

        if valeur > 0.5:
            nb = sum(1 for a in cls.alleles_possibles if a.name.startswith("A"))
            name = f"A{nb}" if nb > 0 else "A"

        else:
            nb = sum(1 for a in cls.alleles_possibles if a.name.startswith("a"))
            name = f"a{nb}" if nb > 0 else "a"

        if parent:
            dominance = np.clip(
                parent.dominance + np.random.normal(0, 0.1),
                0, 1
            )
        else:
            # centré autour de 5 (codominant) par défaut
            dominance = np.random.beta(3, 3)

        allele = Allele(name, valeur, dominance)

        cls.alleles_possibles.append(allele)

        return allele

    @classmethod
    def heriter(cls, gene1: Gene, gene2: Gene) -> Gene:
        """
        Gère l'héritage des gènes selon l'héritage biparental. 
        
        Args:
            gene1 (Gene) : le gène du parent 1 dont on utilisera les allèles
            gene2 (Gene) : le gène du parent 2 dont on utilisera les allèles

        Returns: 
            Gene: la nouvelle instance de `Gene` utilisable par l'enfant 
        """

        allele_p1 = cls.get_random_allele(gene1.allele1, gene1.allele2)
        allele_p2 = cls.get_random_allele(gene2.allele1, gene2.allele2)


        allele_p1 = cls.mutation(allele_p1)
        allele_p2 = cls.mutation(allele_p2)

        return cls(allele_p1, allele_p2)
    
    @staticmethod
    def get_random_allele(allele1, allele2):

        return allele1 if np.random.random() < 0.5 else allele2

    @classmethod
    def mutation(cls, allele: Allele) -> Allele:
        """
        Calcule une chance de mutation pour chaque allèle. 
        La probabilité de mutation est de : 1/1000
        
        Args: 
            allele (Allele) : l'instance de la classe `Alelle` pouvant muter 

        Return : 
            Allele : l'instance de la classe allele qui a muté ou pas
        """

        if np.random.random() < 0.001:
            valeur = np.clip(
            allele.valeur + np.random.normal(0, 0.05),
            0, 1
        )
            
            return cls.ajouter_allele(
                valeur = valeur,
                parent = allele
            )
        
        else: 
            return allele


    @classmethod
    def init_alleles_liste(cls):
        """
        initialise cls.alleles_possibles pour le gène en la remplissant aléatoirement si elle est vide.
        """

        if len(cls.alleles_possibles) == 0:
            
            liste = cls.creer_alleles_base()

            for valeur in liste:

                cls.ajouter_allele(valeur=valeur)

                
    
    @classmethod
    def creer_alleles_base(cls) -> list[float]:
        """
        Crée une liste d'un nombre aléatoire de valeurs d'allèle (centrées autour de 0.5 avec distribution beta)
        """
        
        liste = []
        for _ in range(np.random.randint(3, 8)):
            
            valeur = np.random.beta(2, 2)

            liste.append(valeur)

        return liste




class Recep_Serotonine(Gene):
    pass

