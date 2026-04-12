import numpy as np
from app.life.allele import Allele

class Gene: 
    """
    Modélisation un gène.
    """

    CHANCE_MUTATION: float = 0.001
    REGISTRE = [
        # === NEURO-TRANSMETTEURS / HORMONES ===
        'prod_serotonine',
        'recep_serotonine',
        'prod_dopamine', 
        'recep_dopamine', 
        'prod_testosterone', 
        'recep_testosterone', 
        'prod_oxytocine', 
        'recep_oxytocine',
        'prod_vasopressine', 
        'recep_vasopressine', 
        'prod_cortisol', 
        'recep_cortisol', 
        'prod_croissance', 
        'recep_croissance', 
        'prod_igf1', 
        'recep_igf1', 
        'prod_sexuelles', 
        'recep_sexuelles', 

        # === STRUCTURES CÉRÉBRALES ===
        'ratio_cortex_prefrontal_amygdale', 
        'reactivite_amygdale', 
        'volume_hippocampe', 
        'plasticite_synaptique', 
        'densite_neurones_miroirs', 
        'traitement_sensoriel_cortical', 
        'volume_matiere_blanche', 

        # === NEUROPHYSIOLOGIE ===
        'conductance_nerveuse', 
        'densite_canaux_ioniques', 
        'voie_glutamatergique', 
        'efficacite_jonctions_neuromusculaires', 

        # === MUSCLE / FORCE / MOUVEMENT ===
        'proportion_fibres_musculaires', 
        'proportion_fibres_rapides', 
        'proportion_fibres_lentes', 
        'section_transversale_muscle', 
        'masse_musculaire', 

        # === OS / STRUCTURE ===
        'densite_osseuse', 
        'taille_osseuse', 
        'longueur_leviers_osseux', 
        'elasticite_tissus_conjonctif',

        # === METABOLISME ===
        'efficacite_mitochondriale', 
        'taux_metabolique_basal', 
        'stockage_glycogene', 
        'stockage_adipeux', 
        'efficacite_digestive', 
        'regulation_lactate', 

        # === CARDIO / RESPIRATION ===
        'capacite_pulmonaire', 
        'surfactant_pulmonaire', 
        'structure_pulmonaire', 
        'efficacite_cardiovasculaire', 

        # === IMMUNITE ===
        'reactivite_systeme_immunitaire', 
        'production_anticorps', 
        'diversite_cmh', 
        'production_peptides_antimicrobiens', 
        'regulation_inflammation', 
        'capacite_reparation_tissulaire', 
        'reactivite_coagulation', 
        'barrieres_epitheliales', 

        # === THERMOREGULATION ===
        'densite_graisse_brune', 
        'vasoconstriction_peripherique', 
        'densite_glandes_sudoripares', 
        'regulation_thermique_active', 
        
        # === SENSORIEL ===
        'densite_photorcepteurs', 
        'acuite_retinienne', 
        'sensibilite_cellules_auditives', 
        'taille_globe_oculaire', 
        'longueur_telomeres', 

        # === VIE / VIEILLISSEMENT ===
        'efficacite_reparation_adn', 
        'resistance_stress_oxydatif', 
        'autophagie_cellulaire', 
        'apoptose_cellules_defectueuses', 
        'production_gametes', 
        'qualite_gametes', 

        # === COMPORTEMENT ===
        'maoa'
        ]

    def __init__(self, allele1: Allele, allele2: Allele):
        """
        Définit allele1 et allele2, définit expression en appelant calculer_expression
        
        Args:
            allele1 (Allele)
            allele2 (Allele)
        """

        self.expression = self._calculer_expression(allele1, allele2)

    def __init_subclass__(cls, **kwargs):
        """
        Définit l'attribut alleles_possibles des sous-classes
        """

        super().__init_subclass__(**kwargs)
        cls.alleles_possibles = []

    def _calculer_expression(self, a1: Allele, a2:Allele) -> float:
        """
        Calcule l'expression du gène en prenant en compte une forme de dominance linéaire entre allèles (attribut  `dominance`) 
        Use-case : calculer l'expression du gène à l'instanciation de la classe
        
        Args: 
            a1 (Allele) : l'allèle du parent 1
            a2 (Allele) : l'allèle du parent 2
            
        Returns :
            float
        """

        if a1.valeur <= a2.valeur:
            ref, alt = a1, a2
        else:
            ref, alt = a2, a1

        h = alt.dominance

        return ref.valeur + h * (alt.valeur - ref.valeur)

    @classmethod
    def creer_gene_fondateur(cls) -> "Gene":
        """
        Crée un objet Gene dans le cas ou aucun parent n'est spécifié
        Crée les deux allèles du gène si moins de 2 allèles existent dans alleles_possibles
        Use-case : commencement de la simulation, création instantanée d'un individu

        Returns : 
            Gene
        """

        if len(cls.alleles_possibles) < 2:
            liste = []
            for _ in range(np.random.randint(3, 8)):
                
                valeur = np.random.beta(2, 2)

                liste.append(valeur)

            for valeur in liste:
                cls._ajouter_allele(valeur=valeur)

        return cls(
            np.random.choice(cls.alleles_possibles),
            np.random.choice(cls.alleles_possibles)
        )

    @classmethod
    def heriter(cls, gene1: "Gene", gene2: "Gene") -> "Gene":

        """
        Crée un objet Gene
        Sélectionne aléatoirement les deux allèles à partir des quatre allèles des parents en appliquant une chance de mutation
        Use-case : naissance d'un individu à partir de parent

        Returns : 
            Gene
        """

        allele_p1 = cls._get_random_allele(gene1.allele1, gene1.allele2)
        allele_p2 = cls._get_random_allele(gene2.allele1, gene2.allele2)


        allele_p1 = cls._mutation(allele_p1)
        allele_p2 = cls._mutation(allele_p2)

        return cls(allele_p1, allele_p2)
    
    @classmethod
    def _ajouter_allele(cls, valeur: float, parent:Allele | None = None) -> Allele:
        """
        Ajoute un nouvel allèle à la liste de classe alleles_possibles en générant un nom automatiquement
        Le nom de l'allèle est choisi dynamiquement selon sa valeur :
            - supérieure à 0.5 → commence par "A"
            - inférieure ou égale à 0.5 → commence par "a"
        Un suffixe numérique est ajouté si plusieurs allèles du même type existent.
        Use-case : ajouter une allèle qui vient d'être créée dans la liste `alleles_possibles`
        
        Args :
            valeur (float)

        Returns : 
            Allele : l'instance d'Allele créée et ajoutée à cls.alleles_possibles
        """

        if valeur > 0.5:
            nb = sum(1 for a in cls.alleles_possibles if a.name.startswith("A"))
            name = f"A{nb}" if nb > 0 else "A"

        else:
            nb = sum(1 for a in cls.alleles_possibles if a.name.startswith("a"))
            name = f"a{nb}" if nb > 0 else "a"

        if parent is not None:
            dominance = np.clip(
                parent.dominance + np.random.normal(0, 0.1),
                0, 1
            )
        else:
            # centré autour de 0.5 (codominant) par défaut
            dominance = np.random.beta(3, 3)

        allele = Allele(name, valeur, dominance)

        cls.alleles_possibles.append(allele)

        return allele
    
    @staticmethod
    def _get_random_allele(allele1: Allele, allele2: Allele) -> Allele:
        """
        Choisit aléatoirement un allèle entre deux allèles passés en arguments
        Probabilité : 1/2
        Use-case : sélectionner les allèles parents aléatoirement dans heriter
        
        Args : 
            allele1 (Allele)
            allele2 (Allele)
        
        Returns : 
            Allele
        """

        return allele1 if np.random.random() < 0.5 else allele2

    @classmethod
    def _mutation(cls, allele: Allele) -> Allele:
        """
        Applique une chance de mutation à un allèle (CHANCE_MUTATION) et l'ajoute si muté à la liste de classe `alleles_possibles`. La valeur de l'allèle ainsi que sa dominance mutent. 
        Use-case : Calculer une chance de mutation pour l'allèle transmise par les parents lors de la reproduction
        
        Args :
            allele (Allele) : l'instance de la classe `Alelle` pouvant muter

        Returns : 
            Allele : l'instance de la classe allele qui a muté ou pas
        """

        if np.random.random() < cls.CHANCE_MUTATION:
            valeur = np.clip(
            allele.valeur + np.random.normal(0, 0.05),
            0, 1
        )
            
            return cls._ajouter_allele(
                valeur = valeur,
                parent = allele
            )
        
        else: 
            return allele

    def __str__(self) -> str:
        """
        Affiche une version lisible du gène, de la forme : 
        Expression : 0.5

        Returns: 
            str
        """

        return f"Expression : {self.expression}"
    


GENES_DICT: dict[str: type[Gene]] = {
    name: type(
        name.title().replace("_", ""), 
        (Gene,), 
        {}
    )
    for name in Gene.REGISTRE
} 
