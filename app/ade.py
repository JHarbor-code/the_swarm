import numpy as np
import random

class ADE:
    def __init__(self, genes=None):

        self.genes = self.set_genes(genes) if genes else self.set_genes()

    def set_genes(self, genes):
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
            genes['nerve_conductance'] = max(0, min(1, genes['nerve_conductance'] + random.gauss(0, 0.1)))         # évolution normale
            genes['adipose_storage'] = max(0, min(1, genes['adipose_storage'] + random.gauss(0, 0.1)))             # évolution normale
            
            # === GÈNES MÉTABOLIQUES ===
            genes['digestive_efficiency'] = max(0, min(1, genes['digestive_efficiency'] + random.gauss(0, 0.1)))   # évolution normale
            genes['thermal_regulation'] = max(0, min(1, genes['thermal_regulation'] + random.gauss(0, 0.15)))      # évolution rapide

            return genes

        else:

            return {
                # === GÈNES RÉGULATEURS ===
                'growth_factor': np.random.beta(2, 3),        # biaisé vers 0.4
                'aggression_gene': np.random.beta(2, 3),      # biaisé vers 0.4
                'social_gene': np.random.beta(3, 2),          # biaisé vers 0.6
                'stress_gene': np.random.beta(1, 1),          # uniforme
                'fertility_gene': np.random.beta(6, 1),       # biaisé vers 0.85
                
                # === GÈNES STRUCTURELS ===
                'muscle_fiber': np.random.beta(2, 3),         # biaisé vers 0.4
                'bone_density': np.random.beta(2, 3),         # biaisé vers 0.4
                'nerve_conductance': np.random.beta(2, 3),    # biaisé vers 0.4
                'adipose_storage': np.random.beta(2, 3),      # biaisé vers 0.4
                
                # === GÈNES MÉTABOLIQUES ===
                'digestive_efficiency': np.random.beta(2, 4), # biaisé vers 0.35
                'thermal_regulation': np.random.beta(2, 5),   # biaisé vers 0.20
                }


    
    def set_pheno(self, genes):
        
        pass



