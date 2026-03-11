import numpy as np
import app.life.gene as gn
from pydantic import BaseModel, ValidationError







class ADE:

    def __init__(self, parent1: "ADE"=None, parent2: "ADE"=None, name=None):

        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2


    def set_genes(self, parent1: "ADE"=None, parent2: "ADE"=None):
        """
        Définit les gènes (immutables) de l'ADE
        """
        if not parent1 and not parent2:
            return GenesDict.set_gene(fondateur=True)

        else:
            return GenesDict.set_gene(parent1=parent1.genes, parent2=parent2.genes)




    
    def naitre(self):

        self.genes = self.set_genes()
        self.phenotype = self.set_phenotype()

        self.integrite = 1
        self.oxygenation = 1
        self.taux_co2 = 0
        self.hydratation = 1
        self.energie = 1
        self.stress = 0
        self.temperature = 0.5
        self.faim = 0
        self.soif = 0
        self.pression_sommeil = 0
        self.etat: str["normal", "course", "sommeil"] = "normal" 


    def calculer_oxygenation(self, etat):

        ...


    def maj(self):

        match self.etat:
            case "normal":
                ...

    def __str__(self):

        result = f"name : {self.name}\n"
        
        result += """
______________________________________________
|                                             |
|                   GENES                     |
|_____________________________________________|              

"""
        
        for key, value in self.genes.model_dump().items():
            result += f"{key} : {value}\n"
        
        result += """
______________________________________________
|                                             |
|                 PHENOTYPE                   |
|_____________________________________________|              

"""
        
        for key, value in self.phenotype.items():
            result += f"{key} : {value}\n"
        
        return result
    
test = ADE(name="test")
test.naitre()
print(test)