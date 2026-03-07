from typing import Optional
import app.life.gene as gn

class Genotype:

    GENES: dict[str: gn.Gene] = gn.Gene.REGISTRY



    def __init__(self, parent1: Optional["Genotype"]=None, parent2: Optional["Genotype"]=None):

        self.genotype: dict[str: gn.Gene] = self.build_genotype(parent1, parent2)

    @classmethod
    def build_genotype(cls, parent1: Optional["Genotype"] = None, parent2: Optional["Genotype"] = None) -> dict[str: gn.Gene]:
        
        if parent1 and parent2:

            return {
                gene_name: gene_cls.heriter(
                    parent1.genotype[gene_name], 
                    parent2.genotype[gene_name]
                    )
                for gene_name, gene_cls in cls.GENES.items()
            }


        return {
            gene_name: gene_cls.creer_fondateurs()
            for gene_name, gene_cls in cls.GENES.items()
        }

    
    def __str__(self) -> str:

        return "\n".join(
             f"{n}: {g.expression}"
             for n, g in sorted(self.genotype.items())
        )
