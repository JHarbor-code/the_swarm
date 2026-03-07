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



    def set_phenotype(self):
        phenotype = {}

        phenotype["agressivite"] = self.calculer_phenotype(
            genes=(
                self.genes.prod_testosterone.expression,
                self.genes.recep_testosterone.expression,
                self.genes.prod_serotonine.expression, 
                self.genes.recep_serotonine.expression,
                self.genes.ratio_cortex_prefrontal_amygdale.expression,
                self.genes.maoa.expression,
                self.genes.reactivite_amygdale.expression,
                self.genes.prod_vasopressine.expression, 
                self.genes.recep_vasopressine.expression,
                self.genes.voie_glutamatergique.expression
            ),
            poids=(
                0.7,
                0.7,
                -0.7,
                -0.7,
                0.4,
                0.3,
                0.2,
                0.15,
                0.15,
                0.15
            )
        )
        
        phenotype["sociabilité"] = ...

        phenotype["altruisme"] = self.calculer_phenotype(
            genes=(
                self.genes.prod_oxytocine.expression,
                self.genes.recep_oxytocine.expression,
                self.genes.densite_neurones_miroirs.expression,
                self.genes.prod_serotonine.expression,
                self.genes.recep_serotonine.expression,
                self.genes.ratio_cortex_prefrontal_amygdale.expression,
                self.genes.prod_testosterone.expression,
                self.genes.recep_testosterone.expression,
                self.genes.prod_vasopressine.expression,
                self.genes.recep_vasopressine.expression 
            ),
            
            poids=(
                0.7,
                0.7,
                0.6,
                0.4,
                0.4,
                0.3,
                -0.3,
                -0.3,
                0.15,
                0.15
            )
        )
        phenotype["curiosité"] = ...

        phenotype["courage"] = self.calculer_phenotype(
            genes=(
                self.genes.reactivite_amygdale.expression,
                self.genes.ratio_cortex_prefrontal_amygdale.expression,
                self.genes.prod_cortisol.expression,
                self.genes.recep_cortisol.expression,
                self.genes.prod_serotonine.expression,
                self.genes.recep_serotonine.expression,
                self.genes.prod_testosterone.expression,
                self.genes.recep_testosterone.expression,
                self.genes.prod_dopamine.expression,
                self.genes.recep_dopamine.expression
            ),
            poids=(
                -0.5,
                0.5,
                0.4,
                0.4,
                0.4,
                0.4,
                0.3,
                0.3,
                0.2,
                0.2
            )
        )

        phenotype["peur"] = ...

        phenotype["rancune"] = self.calculer_phenotype(
            genes=(
                self.genes.volume_hippocampe.expression,
                self.genes.plasticite_synaptique.expression,
                self.genes.reactivite_amygdale.expression,
                self.genes.maoa.expression,
                self.genes.prod_oxytocine.expression,
                self.genes.recep_oxytocine.expression,
                self.genes.prod_serotonine.expression,
                self.genes.recep_serotonine.expression
            ),
            poids=(
                0.6,
                0.5,
                0.4,
                -0.4,
                -0.15,
                -0.15,
                -0.15,
                -0.15
            )
        )

        phenotype["force"] = self.calculer_phenotype(
            genes=(
                self.genes.proportion_fibres_musculaires.expression,
                self.genes.section_transversale_muscle.expression,
                self.genes.efficacite_jonctions_neuromusculaires.expression,
                self.genes.stockage_adipeux.expression,
                self.genes.prod_testosterone.expression,
                self.genes.recep_testosterone.expression,
                self.genes.densite_osseuse.expression,
                self.genes.prod_croissance.expression,
                self.genes.recep_croissance.expression    
                ),
            poids=(
                0.6,
                0.6,
                0.5,
                0.4,
                0.3,
                0.3,
                0.2,
                0.15,
                0.15,

            )
        )

        phenotype["taille"] = self.calculer_phenotype(
            genes=(
                self.genes.prod_croissance.expression,
                self.genes.recep_croissance.expression,
                self.genes.prod_igf1.expression,
                self.genes.recep_igf1.expression,
                self.genes.taille_osseuse.expression,
                self.genes.longueur_leviers_osseux.expression
            ),
            poids=(
                0.6, 
                0.6, 
                -0.5,
                -0.5,
                0.4,
                0.2
            )
        )
        

            
        phenotype["masse"] = self.calculer_phenotype(
            genes=(
                self.genes.prod_croissance.expression,
                self.genes.recep_croissance.expression,
                self.genes.stockage_adipeux.expression, 
                self.genes.taille_osseuse.expression,
                self.genes.proportion_fibres_musculaires.expression,
                self.genes.prod_testosterone.expression,
                self.genes.recep_testosterone.expression,
                self.genes.efficacite_digestive.expression
            ),
            poids=(
                0.5,
                0.5,
                0.5,
                0.4,
                0.4,
                0.2,
                0.2,
                0.15
            )
        )

        phenotype["vitesse"] = self.calculer_phenotype(
            genes=(
                self.genes.proportion_fibres_rapides.expression,
                phenotype['taille'],
                phenotype['masse'],
                self.genes.conductance_nerveuse.expression,
                self.genes.efficacite_mitochondriale.expression,
                self.genes.stockage_glycogene.expression
            ),
            poids=(
                0.6,
                0.4,
                -0.4, 
                0.3,
                0.2, 
                0.2
            )
        )

        phenotype['endurance'] = self.calculer_phenotype(
            genes=(
                self.genes.efficacite_mitochondriale.expression,
                self.genes.proportion_fibres_lentes.expression,
                phenotype['masse'],
                self.genes.capacite_pulmonaire.expression,
                self.genes.efficacite_cardiovasculaire.expression,
                phenotype['taille'],
                self.genes.stockage_glycogene.expression,
                self.genes.regulation_lactate.expression
            ),
            poids=(
                0.5,
                0.5,
                -0.4,
                0.4,
                0.4,
                0.3,
                0.2,
                0.15
            )
        )
        
        # capacités 
        phenotype["resistance_coups"] = self.calculer_phenotype(
            genes=(
                self.genes.densite_osseuse.expression,
                self.genes.capacite_reparation_tissulaire.expression,
                self.genes.proportion_fibres_musculaires.expression,
                self.genes.reactivite_coagulation.expression,
                self.genes.elasticite_tissus_conjonctif.expression
            ),
            poids=(
                0.6,
                0.5,
                0.4,
                0.3,
                0.2
            )
        )

        phenotype['immunité'] = self.calculer_phenotype(
            genes=(
                self.genes.reactivite_systeme_immunitaire.expression,
                self.genes.production_anticorps.expression,
                self.genes.diversite_cmh.expression,
                self.genes.barrieres_epitheliales.expression,
                self.genes.production_peptides_antimicrobiens.expression,
                self.genes.regulation_inflammation.expression
            ),
            poids=(
                0.5,
                0.5,
                0.4,
                0.4,
                0.3,
                0.3
            )
        )
        
        sv = phenotype['taille']**2 / (phenotype['taille']**2 + phenotype['masse'])
        phenotype["regulation_temperature"] = self.calculer_phenotype(
            genes=(
                self.genes.densite_graisse_brun.expression,
                self.genes.regulation_thermique_active.expression,
                self.genes.vasoconstriction_peripherique.expression,
                self.genes.densite_glandes_sudoripares.expression,
                sv,
                self.genes.taux_metabolique_basal.expression,
            ),
            poids=(
                0.5,
                0.5,
                0.4,
                0.4,
                0.3,
                0.3
            )
        ) 


            
        # === COMPORTEMENTAUX ===

        

            
        phenotype["memoire"] = self.calculer_phenotype(
            genes=(
                self.genes.volume_hippocampe.expression,
                self.genes.plasticite_synaptique.expression,
                self.genes.conductance_nerveuse.expression,
                self.genes.traitement_sensoriel_cortical.expression,
                self.genes.densite_neurones_miroirs.expression,
            ),
            poids=(
                0.4,
                0.3, 
                0.15,
                0.1,  
                0.05,  
            )
        )
                


            # === SURVIE === 
        phenotype["cout_energetique"] = self.calculer_phenotype(
            genes=(
                self.genes.taux_metabolique_basal.expression,
                phenotype['masse'],
                self.genes.efficacite_mitochondriale.expression,
                self.genes.proportion_fibres_lentes.expression,
                self.genes.proportion_fibres_musculaires.expression,
                self.genes.proportion_fibres_rapides.expression,
                self.genes.regulation_thermique_active.expression,
                self.genes.production_anticorps.expression, 
                self.genes.production_peptides_antimicrobiens.expression,
                self.genes.prod_cortisol.expression,
                self.genes.prod_croissance.expression,
                self.genes.prod_igf1.expression,
                self.genes.prod_testosterone.expression,
            ),
            poids=(
                0.5,
                0.5,
                -0.4,
                0.05,
                0.1,
                0.15,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1
            )
        )

        phenotype["fertilite"] = self.calculer_phenotype(
            genes=(
                self.genes.production_gametes.expression,
                self.genes.prod_sexuelles.expression,
                self.genes.recep_sexuelles.expression,
                self.genes.qualite_gametes.expression,
            ),
            poids=(
                0.5,
                0.4,
                0.4,
                0.4,
            )
        )

        phenotype["temps_de_reaction"] = self.calculer_phenotype(
            genes=(
                self.genes.conductance_nerveuse.expression,
                self.genes.densite_canaux_ioniques.expression,
                self.genes.voie_glutamatergique.expression,
                self.genes.volume_matiere_blanche.expression,
                self.genes.efficacite_jonctions_neuromusculaires.expression
            ),
            poids=(
                0.6,
                0.5,
                0.4,
                0.3,
                0.3
            )
        )

        phenotype["distance_detection"] = self.calculer_phenotype(
            genes=(
                self.genes.densite_photorcepteurs.expression,
                self.genes.sensibilite_cellules_auditives.expression,
                phenotype['taille'],
                self.genes.acuite_retinienne.expression,
                self.genes.taille_globe_oculaire.expression,
                self.genes.traitement_sensoriel_cortical.expression,
            ),
            poids=(
                0.5,
                0.5,
                0.4,
                0.4,
                0.3,
                0.2
            )
        )

        return phenotype
    
    def calculer_phenotype(self, genes: tuple, poids: tuple, bruit=True):

        score = np.dot(genes, poids)

        # calculés dynamiquement par les poids 
        MIN_THEO = sum(p for p in poids if p < 0)
        MAX_THEO = sum(p for p in poids if p > 0)
        
        if bruit:
            # action hypothétique d'autres gènes non-représentés 
            score += np.random.normal(1, 0.05)

        # normalisation entre [0;1]
        score = (score - MIN_THEO) / (MAX_THEO - MIN_THEO)

        return np.clip(score, 0, 1)
    
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