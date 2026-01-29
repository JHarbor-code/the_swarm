import numpy as np
import random

class ADE:
    BASE_TAILLE = 1

    def __init__(self, genes=None):

        self.bruit_coef = random.gauss(0, 0.03)
        self.genes = self.set_genes(genes) if genes else self.set_genes()
        self.phenotype = self.set_phenotype(self.genes)


    def set_genes(self, genes=None):
        """
        Définit les gènes (immutables) de l'ADE
        """

        if genes:
            
            # === GÈNES RÉGULATEURS ===
            genes['growth_factor'] = max(0, min(1, genes['growth_factor'] + random.gauss(0, 0.1)))                 # évolution normale
            genes['aggression_gene'] = max(0, min(1, genes['aggression_gene'] + random.gauss(0, 0.15)))            # évolution rapide
            genes['social_gene'] = max(0, min(1, genes['social_gene'] + random.gauss(0, 0.15)))                    # évolution rapide
            genes['stress_gene'] = max(0, min(1, genes['stress_gene'] + random.gauss(0, 0.15)))                    # évolution rapide
            genes['fertility_gene'] = max(0, min(1, genes['fertility_gene'] + random.gauss(0, 0.05)))              # évolution lente
            
            # === GÈNES STRUCTURELS ===
            genes['muscle_fiber'] = max(0, min(1, genes['muscle_fiber'] + random.gauss(0, 0.1)))                   # évolution normale
            genes['bone_density'] = max(0, min(1, genes['bone_density'] + random.gauss(0, 0.05)))                  # évolution lente
            genes['bone_size'] = max(0, min(1, genes['bone_size'] + random.gauss(0, 0.05)))                        # évolution lente
            genes['nerve_conductance'] = max(0, min(1, genes['nerve_conductance'] + random.gauss(0, 0.1)))         # évolution normale
            genes['adipose_storage'] = max(0, min(1, genes['adipose_storage'] + random.gauss(0, 0.1)))             # évolution normale
            
            # === GÈNES MÉTABOLIQUES ===
            genes['digestive_efficiency'] = max(0, min(1, genes['digestive_efficiency'] + random.gauss(0, 0.1)))   # évolution normale
            genes['thermal_regulation'] = max(0, min(1, genes['thermal_regulation'] + random.gauss(0, 0.15)))      # évolution rapide

            return genes

        else:

            return {
                # === GÈNES RÉGULATEURS ===
                'croissance': np.random.beta(2, 3),        # biaisé vers 0.4
                'aggression_gene': np.random.beta(2, 3),      # biaisé vers 0.4
                'social_gene': np.random.beta(3, 2),          # biaisé vers 0.6
                'stress_gene': np.random.beta(2, 2),          # baisée vers 0.5
                'fertilite_gene': np.random.beta(6, 1),       # biaisé vers 0.85
                
                # === GÈNES STRUCTURELS ===
                'fibres_musculaires': np.random.beta(2, 3),         # biaisé vers 0.4
                'densité_os': np.random.beta(2, 3),         # biaisé vers 0.4
                'taille_os' : np.random.beta(2, 2),           # baisée vers 0.5
                'conductance_nerveuse': np.random.beta(2, 3),    # biaisé vers 0.4
                'stockage_adipeux ': np.random.beta(2, 3),      # biaisé vers 0.4
                'endurance' : np.random.beta(2, 3),           # biaisé vers 0.4
                
                # === GÈNES MÉTABOLIQUES ===
                'efficacite_digestion': np.random.beta(2, 4), # biaisé vers 0.35
                'regulation_thermique': np.random.beta(2, 5),   # biaisé vers 0.20
                'consommation_energetique': np.random.beta(2, 3),       # biaisé vers 0.4
                'appetit': np.random.beta(2, 2),             # biaisé vers 0.5 
                'maintenance_cost' : np.random.beta(2, 4),    # biaisé vers 0.35

                # === GENES SENSORIELS ===
                'qualité_vision' : np.random.beta(2, 2),      # biaisé vers 0.5
                'qualité_audition' : np.random.beta(2, 2),     # biaisé vers 0.5

                # === GENES NEUROLOGIQUES ===
                'intelligence' : np.random.beta(2, 2), # biaisé vers 0.5
                'memory' : np.random.beta(2, 2)               # biaisé vers 0.5
                }


    
    def set_phenotype(self, genes):
        
        return {
            # === PHYSIQUE ===
            "taille" : self.compute_size([genes['growth_factor'], genes['bone_density']], [0.5, 0.3]),
            "force" : "",
            "resistance_coups" : "",
            "resistance_froid" : "", 
            "vitesse" : "",
            
            # === COMPORTEMENTAUX ===
            "agressivite" : "",
            "altruisme" : "",
            "courage" : "",
            "memoire" : "",
            "rancune" : "",

            # === SURVIE === 
            "cout_energetique" : "",
            "fertilite" : "",
            "temps_de_reaction" : "",
            "distance_détection" : "",
            }

    def compute_size(self, genes: list[float], coefs: list[float]):

        base = self.genes['growth_factor'] * self.genes['bone_density']

        return base * (self.BASE_TAILLE + self.bruit_coef)
    
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

test = ADE()
total = 0
for i in range(10000):
    test.set_phenotype(test.genes)
    total += test.phenotype['taille']

moy = total / 10000
print(moy)

