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

        self.expression = self.calculer_expression()

    @classmethod
    def creer_fondateurs(cls) -> "Gene":

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

        return round(ref.valeur + h * (alt.valeur - ref.valeur), 2)
    
        
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
    def heriter(cls, gene1: "Gene", gene2: "Gene") -> "Gene":
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

    def __str__(self):

        return str(self.expression)




# === NEURO-TRANSMETTEURS / HORMONES ===

class ProdSerotonine(Gene):
    alleles_possibles = []

class RecepSerotonine(Gene):
    alleles_possibles = []

class ProdDopamine(Gene):
    alleles_possibles = []

class RecepDopamine(Gene):
    alleles_possibles = []

class ProdTestosterone(Gene):
    alleles_possibles = []

class RecepTestosterone(Gene):
    alleles_possibles = []

class ProdOcytocine(Gene):
    alleles_possibles = []

class RecepOcytocine(Gene):
    alleles_possibles = []

class ProdVasopressine(Gene):
    alleles_possibles = []

class RecepVasopressine(Gene):
    alleles_possibles = []

class ProdCortisol(Gene):
    alleles_possibles = []

class RecepCortisol(Gene):
    alleles_possibles = []

class ProdCroissance(Gene):
    alleles_possibles = []

class RecepCroissance(Gene):
    alleles_possibles = []
    
class ProdIGF1(Gene):
    alleles_possibles = []

class RecepIGF1(Gene):
    alleles_possibles=[]

class ProdSexuelles(Gene):
    alleles_possibles = []

class RecepSexuelles(Gene):
    alleles_possibles = []


# === STRUCTURE CEREBRALE ===
class DensiteGraisseBrune(Gene):
    alleles_possibles = []

class VasoconstrictionPeripherique(Gene):
    alleles_possibles = []

class DensiteGlandesSudoripares(Gene):
    alleles_possibles = []

class RegulationThermiqueActive(Gene):
    alleles_possibles = []

class RatioCortexPrefrontalAmygdale(Gene):
    alleles_possibles = []

class ReactiviteAmygdale(Gene):
    alleles_possibles = []

class VolumeHippocampe(Gene):
    alleles_possibles = []

class PlasticiteSynaptique(Gene):
    alleles_possibles = []

class DensiteNeuronesMiroirs(Gene):
    alleles_possibles = []

class TraitementSensorielCortical(Gene):
    alleles_possibles = []

class VolumeMatiereBlanche(Gene):
    alleles_possibles = []

DensiteGraisseBrune
# === NEUROPHYSIOLOGIE ===

class ConductanceNerveuse(Gene):
    alleles_possibles = []

class DensiteCanauxIoniques(Gene):
    alleles_possibles = []

class VoieGlutamatergique(Gene):
    alleles_possibles = []

class EfficaciteJonctionsNeuromusculaires(Gene):
    alleles_possibles = []


# === MUSCLE / FORCE / MOUVEMENT ===

class ProportionFibresMusculaires(Gene):
    alleles_possibles = []

class ProportionFibresRapides(Gene):
    alleles_possibles = []

class ProportionFibresLentes(Gene):
    alleles_possibles = []

class SectionTransversaleMuscle(Gene):
    alleles_possibles = []

class MasseMusculaire(Gene):
    alleles_possibles = []


# === OS / STRUCTURE / TAILLE === 

class DensiteOsseuse(Gene):
    alleles_possibles = []

class TailleOsseuse(Gene):
    alleles_possibles = []

class LongueurLeviersOsseux(Gene):
    alleles_possibles = []

class ElasticiteTissusConjonctif(Gene):
    alleles_possibles = []


# === METABOLISME ===

class EfficaciteMitochondriale(Gene):
    alleles_possibles = []

class TauxMetaboliqueBasal(Gene):
    alleles_possibles = []

class StockageGlycogene(Gene):
    alleles_possibles = []

class StockageAdipeux(Gene):
    alleles_possibles = []

class EfficaciteDigestive(Gene):
    alleles_possibles = []

class RegulationLactate(Gene):
    alleles_possibles = []


# === CARDIO / RESPIRATION ===

class CapacitePulmonaire(Gene):
    alleles_possibles = []

class EfficaciteCardiovasculaire(Gene):
    alleles_possibles = []


# === IMMUNITE ===

class ReactiviteSystemeImmunitaire(Gene):
    alleles_possibles = []

class ProductionAnticorps(Gene):
    alleles_possibles = []

class DiversiteCMH(Gene):
    alleles_possibles = []

class ProductionPeptidesAntimicrobiens(Gene):
    alleles_possibles = []

class RegulationInflammation(Gene):
    alleles_possibles = []

class CapaciteReparationTissulaire(Gene):
    alleles_possibles = []

class ReactiviteCoagulation(Gene):
    alleles_possibles = []

class BarrieresEpithéliales(Gene):
    alleles_possibles = [] 


# === SENSORIELS ===

class DensitePhotorcepteurs(Gene):
    alleles_possibles = []

class AcuiteRetinienne(Gene):
    alleles_possibles = []

class SensibiliteCellulesAuditives(Gene):
    alleles_possibles = []

class TailleGlobeOculaire(Gene):
    alleles_possibles = []


# === VIE ===

class LongueurTelomeres(Gene):
    alleles_possibles = []

class EfficaciteReparationADN(Gene):
    alleles_possibles = []

class ResistanceStressOxydatif(Gene):
    alleles_possibles = []

class AutophagieCellulaire(Gene):
    alleles_possibles = []

class ApoptoseCellulesDefectueuses(Gene):
    alleles_possibles = []

class ProductionGametes(Gene):
    alleles_possibles = []

class QualiteGametes(Gene):
    alleles_possibles = []



# === COMPORTEMENT === 

class MAOA(Gene):
    alleles_possibles = []


