import numpy as np
from app.life.allele import Allele




class Gene: 

    MUTATION_RATE: float = 0.001
    REGISTRY = [
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

        self.allele1 = allele1
        self.allele2 = allele2

        self.expression = self.calculer_expression()

    def __init_subclass__(cls, **kwargs):

        super().__init_subclass__(**kwargs)
        cls.alleles_possibles = []


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

        if parent is not None:
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

        if np.random.random() < cls.MUTATION_RATE:
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

for name in Gene.REGISTRY:

    cls = type(
        name.title().replace("_", ""), (Gene,), {"alleles_possibles" : []}
    )
    globals()[cls.__name__] = cls   

