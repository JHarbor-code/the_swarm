import numpy as np
from app.life.genotype import Genotype
from app.life.gene import Gene


class MicroComportements:
    """
    Classe contenant l'expression des caractères de l'individu exprimé génétiquement pour servir de base au calcul du phénotype. 
    Certains attributs font aussi partit du phénotype, mais ne sont ici représentés que génétiquement 
    """

    _MICRO_COMPORTEMENTS_FORMULE = {
        "domination": {
                "prod_testosterone" : 0.6,
                "recep_testosterone" : 0.5,
                "prod_dopamine" : 0.5,
                "recep_dopamine" : 0.4,
                "prod_oxytocine" : -0.5,
                "recep_oxytocine" : -0.4
        },
        "competitivite" : {
            "prod_dopamine" : 0.6,
            "recep_dopamine" : 0.5,
            "prod_serotonine" : 0.5,
            "recep_serotonine" : 0.4
        },
        "stress_ressentit" :"",
        "impulsivite":"",
        "empathie":"",
        "motivation_sociale":"",
        "peur_ressentie":"",
        "reconnaissance_emotions":"",
        "anxiete_sociale":"",
        "peur_rejet":"", 
        "compréhension":"",
        "niveau_aspiration":""
    } 

    def __init__(self, genotype: Genotype):
            
        self.genotype: Genotype = genotype
        self.GENE_INDEX = {g:i for i,g in enumerate(Gene.REGISTRY)}

        nb_micro = len(self._MICRO_COMPORTEMENTS_FORMULE)
        nb_genes = len(self.GENE_INDEX)
        self.W = np.zeros((nb_micro, nb_genes))





    def calculer_expression(self, genes: np.ndarray, bruit=True) -> tuple:


        for i, (micro, influence) in enumerate(self._MICRO_COMPORTEMENTS_FORMULE.items()):
            for gene, poids in influence.items():
                j = self.GENE_INDEX[gene]
                self.W[i, j] = poids


        
        score = W @ genes
        
        if bruit:
            # action hypothétique d'autres gènes non-représentés 
            score += np.random.normal(0, 0.05, size=score.shape)

        score = 1 / (1 + np.exp(-score))


        return tuple(score)
    

    def construire_systeme(self):
        
        micro_comportements = {}

        for nom, valeurs in self._MICRO_COMPORTEMENTS_FORMULE.items(): 

            expression_genes = np.array([self.genotype[e].expression for e in valeurs["genes"]])
            poids_genes = np.array(valeurs["poids"])

            micro_comportements[nom] = self.calculer_expression(genes=expression_genes, poids=poids_genes)

        return micro_comportements