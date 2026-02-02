from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class Allele:
    name: str
    valeur: float
    dominance: float


class Gene: 

    alleles_possibles: list[Allele] = None

    def __init__(self, allele1: Allele, allele2: Allele):

        self.allele1 = allele1
        self.allele2 = allele2

    @classmethod
    def creer_fondateurs(cls):

        if not cls.alleles_possibles:
            liste = []
            for _ in range(np.random.randint(3, 8)):
                
                valeur = np.random.beta(2, 2)

                liste.append(valeur)

            for valeur in liste:
                cls.ajouter_allele(valeur=valeur)

        return cls(
            np.random.choice(cls.alleles_possibles),
            np.random.choice(cls.alleles_possibles)
        )


    def calculer_expression(self) -> float:
        """
        Calcule l'expression du gène en prenant en code une forme de dominance linéaire entre allèles (attribut `dominance`)

        Returns: 
            float: l'expression du gène comprise entre 0 et 1
        
        :param self: Description
        """
        
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



# === NEURO-TRANSMETTEURS / HORMONES ===

class ProdSerotonine(Gene):
    pass

class RecepSerotonine(Gene):
    pass

class ProdDopamine(Gene):
    pass

class RecepDopamine(Gene):
    pass

class ProdTestosterone(Gene):
    pass

class RecepTestosterone(Gene):
    pass

class ProdOcytocine(Gene):
    pass

class RecepOcytocine(Gene):
    pass

class ProdVasopressine(Gene):
    pass

class RecepVasopressine(Gene):
    pass

class ProdCortisol(Gene):
    pass

class RecepCortisol(Gene):
    pass


# === STRUCTURE CEREBRALE ===
class DensiteGraisseBrune(Gene):
    pass

class VasoconstrictionPeripherique(Gene):
    pass

class DensiteGlandesSudoripares(Gene):
    pass

class RegulationThermiqueActive(Gene):
    pass

class RatioCortexPrefrontalAmygdale(Gene):
    pass

class ReactiviteAmygdale(Gene):
    pass

class VolumeHippocampe(Gene):
    pass

class PlasticiteSynaptique(Gene):
    pass

class DensiteNeuronesMiroirs(Gene):
    pass

class TraitementSensorielCortical(Gene):
    pass

class VolumeMatiereBlanche(Gene):
    pass


# === NEUROPHYSIOLOGIE ===

class ConductanceNerveuse(Gene):
    pass

class DensiteCanauxIoniques(Gene):
    pass

class VoieGlutamatergique(Gene):
    pass

class EfficaciteJonctionsNeuromusculaires(Gene):
    pass


# === MUSCLE / FORCE / MOUVEMENT ===

class ProportionFibresMusculaires(Gene):
    pass

class ProportionFibresRapides(Gene):
    pass

class ProportionFibresLentes(Gene):
    pass

class SectionTransversaleMuscle(Gene):
    pass

class MasseMusculaire(Gene):
    pass


# === OS / STRUCTURE / TAILLE === 

class DensiteOsseuse(Gene):
    pass

class TailleOsseuse(Gene):
    pass

class LongueurLeviersOsseux(Gene):
    pass

class TailleGlobale(Gene):
    pass


# === METABOLISME ===

class EfficaciteMitochondriale(Gene):
    pass

class TauxMetaboliqueBasal(Gene):
    pass

class StockageGlycogene(Gene):
    pass

class StockageAdipeux(Gene):
    pass

class EfficaciteDigestive(Gene):
    pass

class RegulationLactate(Gene):
    pass


# === CARDIO / RESPIRATION ===

class CapacitePulmonaire(Gene):
    pass

class EfficaciteCardiovasculaire(Gene):
    pass


# === IMMUNITE ===

class ReactiviteSystemeImmunitaire(Gene):
    pass

class ProductionAnticorps(Gene):
    pass

class DiversiteCMH(Gene):
    pass

class ProductionPeptidesAntimicrobiens(Gene):
    pass

class RegulationInflammation(Gene):
    pass

class CapaciteReparationTissulaire(Gene):
    pass

class ReactiviteCoagulation(Gene):
    pass


# === THERMOREGULATION ===

class DensiteGraisseBrune(Gene):
    pass

class VasoconstrictionPeripherique(Gene):
    pass

class DensiteGlandesSudoripares(Gene):
    pass

class RegulationThermiqueActive(Gene):
    pass


# === SENSORIELS ===

class DensitePhotorcepteurs(Gene):
    pass

class AcuiteRetinienne(Gene):
    pass

class SensibiliteCellulesAuditives(Gene):
    pass

class TailleGlobeOculaire(Gene):
    pass


# === VIE ===

class LongueurTelomeres(Gene):
    pass

class EfficaciteReparationADN(Gene):
    pass

class ResistanceStressOxydatif(Gene):
    pass

class AutophagieCellulaire(Gene):
    pass

class ApoptoseCellulesDefectueuses(Gene):
    pass

class ProductionGametes(Gene):
    pass

class QualiteGametes(Gene):
    pass


# === COMPORTEMENT === 

class MAOA(Gene):
    pass


