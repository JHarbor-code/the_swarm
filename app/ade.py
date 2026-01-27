import numpy as np

class ADE:
    def __init__(self):
        pass

    def set_genes(self):

        self.genes = {
            # === GÈNES RÉGULATEURS ===
            'growth_factor': np.random.beta(0, 1),      # IGF-GH
            'aggression_gene': np.random.beta(0, 1),        # MAOA, 5-HTT
            'social_gene': np.random.beta(0, 1),            # OXTR, AVPR1A
            'stress_gene': np.random.beta(0, 1),            # CRHR1, NR3C1
            'fertility_gene': np.random.beta(0, 1),     # FSH, LH
            
            # === GÈNES STRUCTURELS ===
            'muscle_fiber_type': np.random.beta(0, 1),  # ACTN3, ACEE
            'bone_density_gene': np.random.beta(0, 1),  # VDR, COL1A1
            'nerve_conductance': np.random.beta(0, 1),  # SCN9A
            'adipose_storage': np.random.beta(0, 1),    # FTO, MC4R
            
            # === GÈNES MÉTABOLIQUES ===
            'digestive_efficiency': np.random.beta(0.6, 1.4),
            'thermal_regulation': np.random.beta(0.5, 1.5),
        }

