import numpy as np

class ADE:
    BASE_TAILLE = 1

    def __init__(self, genes=None):

        self.genes = self.set_genes(genes) if genes else self.set_genes()
        self.phenotype = self.set_phenotype(self.genes)


    def set_genes(self, genes=None):
        """
        Définit les gènes (immutables) de l'ADE
        """

        if genes:
            
            # === GÈNES RÉGULATEURS ===
            genes['croissance'] = max(0, min(1, genes['croissance'] + random.gauss(0, 0.1)))
            genes['agressivite'] = max(0, min(1, genes['agressivite'] + random.gauss(0, 0.15)))
            genes['sociabilite'] = max(0, min(1, genes['sociabilite'] + random.gauss(0, 0.15)))
            genes['stress'] = max(0, min(1, genes['stress'] + random.gauss(0, 0.15)))
            genes['fertilite'] = max(0, min(1, genes['fertilite'] + random.gauss(0, 0.05)))
            
            # === GÈNES STRUCTURELS ===
            genes['fibres_musculaires'] = max(0, min(1, genes['fibres_musculaires'] + random.gauss(0, 0.1)))
            genes['densite_os'] = max(0, min(1, genes['densite_os'] + random.gauss(0, 0.05)))
            genes['taille_os'] = max(0, min(1, genes['taille_os'] + random.gauss(0, 0.05)))
            genes['conductance_nerveuse'] = max(0, min(1, genes['conductance_nerveuse'] + random.gauss(0, 0.1)))
            genes['stockage_adipeux'] = max(0, min(1, genes['stockage_adipeux'] + random.gauss(0, 0.1)))
            genes['endurance'] = max(0, min(1, genes['endurance'] + random.gauss(0, 0.1)))
            genes['volatilite'] = max(0, min(1, genes['volatilite'] + random.gauss(0, 0.15)))
            
            # === GÈNES MÉTABOLIQUES ===
            genes['efficacite_digestion'] = max(0, min(1, genes['efficacite_digestion'] + random.gauss(0, 0.1)))
            genes['regulation_thermique'] = max(0, min(1, genes['regulation_thermique'] + random.gauss(0, 0.15)))
            genes['consommation_energetique'] = max(0, min(1, genes['consommation_energetique'] + random.gauss(0, 0.1)))
            genes['appetit'] = max(0, min(1, genes['appetit'] + random.gauss(0, 0.1)))
            genes['cout_maintenance'] = max(0, min(1, genes['cout_maintenance'] + random.gauss(0, 0.1)))

            # === GENES SENSORIELS ===
            genes['qualite_vision'] = max(0, min(1, genes['qualite_vision'] + random.gauss(0, 0.1)))
            genes['qualite_audition'] = max(0, min(1, genes['qualite_audition'] + random.gauss(0, 0.1)))

            # === GENES NEUROLOGIQUES ===
            genes['intelligence'] = max(0, min(1, genes['intelligence'] + random.gauss(0, 0.1)))
            genes['memoire'] = max(0, min(1, genes['memoire'] + random.gauss(0, 0.1)))

            return genes

        else:

            return {
                # === GÈNES RÉGULATEURS ===
                'croissance': np.random.beta(2, 3),
                'agressivite': np.random.beta(2, 3),
                'sociabilite': np.random.beta(3, 2),
                'stress': np.random.beta(2, 2),
                'fertilite': np.random.beta(6, 1),
                
                # === GÈNES STRUCTURELS ===
                'fibres_musculaires': np.random.beta(2, 3),
                'densite_os': np.random.beta(2, 3),
                'taille_os': np.random.beta(2, 2),
                'conductance_nerveuse': np.random.beta(2, 3),
                'stockage_adipeux': np.random.beta(2, 3),
                'endurance': np.random.beta(2, 3),
                'volatilite' : np.random.beta(2, 4),
                
                # === GÈNES MÉTABOLIQUES ===
                'efficacite_digestion': np.random.beta(2, 4),
                'regulation_thermique': np.random.beta(2, 5),
                'consommation_energetique': np.random.beta(2, 3),
                'appetit': np.random.beta(2, 2),
                'cout_maintenance': np.random.beta(2, 4),

                # === GENES SENSORIELS ===
                'qualite_vision': np.random.beta(2, 2),
                'qualite_audition': np.random.beta(2, 2),

                # === GENES NEUROLOGIQUES ===
                'intelligence': np.random.beta(2, 2),
                'memoire': np.random.beta(2, 2)
            }


    
    def set_phenotype(self, genes):
        
        return {
            # === PHYSIQUE ===
            "taille": self.compute_taille(),
            "force": "",
            "resistance_coups": "",
            "resistance_froid": "", 
            "vitesse": "",
            
            # === COMPORTEMENTAUX ===
            "agressivite": "",
            "altruisme": "",
            "courage": "",
            "memoire": "",
            "rancune": "",

            # === SURVIE === 
            "cout_energetique": "",
            "fertilite": "",
            "temps_de_reaction": "",
            "distance_detection": "",
        }

    def compute_taille(self):
        potentiel_genetique = 1

        terms = [
            (self.genes['croissance'], 0.5),
            (self.genes['taille_os'], 0.3)
        ]

        for nb, exp in terms:
            potentiel_genetique *= nb ** exp


        sigma = self.genes['volatilite']
        bruit = np.random.lognormal(mean=0, sigma=sigma)


        return potentiel_genetique * bruit
    
    def compute_force():

        return
    
    def compute_resistance_coups():

        return
    
    def compute_resistance_froid():

        return
    
    def compute_vitesse():

        return
    
    def compute_agressivite():

        return
    
    def compute_altruisme():

        return
    
    def compute_courage():

        return
    
    def compute_memoire():

        return
    
    def compute_rancune():

        return
    
    def compute_cout_energetique():

        return
    
    def compute_fertilite():

        return
    
    def compute_temps_de_reaction():

        return
    
    def compute_distance_détection():

        return




