import numpy as np
import random
import gene as gn
from pydantic import BaseModel, ValidationError


class GenesDict(BaseModel):

    model_config = {
        "arbitrary_types_allowed": True 
    }

    # Neurotransmetteurs & hormones
    prod_serotonine: gn.ProdSerotonine
    recep_serotonine: gn.RecepSerotonine
    prod_dopamine: gn.ProdDopamine
    recep_dopamine: gn.RecepDopamine
    prod_testosterone: gn.ProdTestosterone
    recep_testosterone: gn.RecepTestosterone
    prod_oxytocine: gn.ProdOcytocine
    recep_oxytocine: gn.RecepOcytocine
    prod_vasopressine: gn.ProdVasopressine
    recep_vasopressine: gn.RecepVasopressine
    prod_cortisol: gn.ProdCortisol
    recep_cortisol: gn.RecepCortisol

    # Structures cérébrales & traitement
    ratio_cortex_prefrontal_amygdale: gn.RatioCortexPrefrontalAmygdale
    reactivite_amygdale: gn.ReactiviteAmygdale
    volume_hippocampe: gn.VolumeHippocampe
    plasticite_synaptique: gn.PlasticiteSynaptique
    densite_neurones_miroirs: gn.DensiteNeuronesMiroirs
    traitement_sensoriel_cortical: gn.TraitementSensorielCortical
    volume_matiere_blanche: gn.VolumeMatiereBlanche

    # Neurophysiologie
    conductance_nerveuse: gn.ConductanceNerveuse
    densite_canaux_ioniques: gn.DensiteCanauxIoniques
    voie_glutamatergique: gn.VoieGlutamatergique
    efficacite_jonctions_neuromusculaires: gn.EfficaciteJonctionsNeuromusculaires

    # Muscle, force, mouvement
    proportion_fibres_musculaires: gn.ProportionFibresMusculaires
    proportion_fibres_rapides: gn.ProportionFibresRapides
    proportion_fibres_lentes: gn.ProportionFibresLentes
    section_transversale_muscle: gn.SectionTransversaleMuscle
    masse_musculaire: gn.MasseMusculaire

    # Os, structure, taille
    densite_osseuse: gn.DensiteOsseuse
    taille_osseuse: gn.TailleOsseuse
    longueur_leviers_osseux: gn.LongueurLeviersOsseux
    taille_globale: gn.TailleGlobale

    # Métabolisme & énergie
    efficacite_mitochondriale: gn.EfficaciteMitochondriale
    taux_metabolique_basal: gn.TauxMetaboliqueBasal
    stockage_glycogene: gn.StockageGlycogene
    stockage_adipeux: gn.StockageAdipeux
    efficacite_digestive: gn.EfficaciteDigestive
    regulation_lactate: gn.RegulationLactate

    # Cardio / respiration
    capacite_pulmonaire: gn.CapacitePulmonaire
    efficacite_cardiovasculaire: gn.EfficaciteCardiovasculaire

    # Immunité & réparation
    reactivite_systeme_immunitaire: gn.ReactiviteSystemeImmunitaire
    production_anticorps: gn.ProductionAnticorps
    diversite_cmh: gn.DiversiteCMH
    production_peptides_antimicrobiens: gn.ProductionPeptidesAntimicrobiens
    regulation_inflammation: gn.RegulationInflammation
    capacite_reparation_tissulaire: gn.CapaciteReparationTissulaire
    reactivite_coagulation: gn.ReactiviteCoagulation

    # Thermorégulation
    densite_graisse_brun: gn.DensiteGraisseBrune
    vasoconstriction_peripherique: gn.VasoconstrictionPeripherique
    densite_glandes_sudoripares: gn.DensiteGlandesSudoripares
    regulation_thermique_active: gn.RegulationThermiqueActive

    # Sensoriel
    densite_photorcepteurs: gn.DensitePhotorcepteurs
    acuite_retinienne: gn.AcuiteRetinienne
    sensibilite_cellules_auditives: gn.SensibiliteCellulesAuditives
    taille_globe_oculaire: gn.TailleGlobeOculaire

    # Vie, vieillissement, fertilité
    longueur_telomeres: gn.LongueurTelomeres
    efficacite_reparation_adn: gn.EfficaciteReparationADN
    resistance_stress_oxydatif: gn.ResistanceStressOxydatif
    autophagie_cellulaire: gn.AutophagieCellulaire
    apoptose_cellules_defectueuses: gn.ApoptoseCellulesDefectueuses
    production_gametes: gn.ProductionGametes
    qualite_gametes: gn.QualiteGametes

    # Psycho-comportemental
    maoa: gn.MAOA

    @classmethod
    def set_gene(cls, parent1: "GenesDict" = None, parent2: "GenesDict" = None, fondateur=False):
        fields = {}  

        if fondateur:
            for name, type_ in cls.__annotations__.items():
                fields[name] = type_.creer_fondateurs()
        else:
            for name, type_ in cls.__annotations__.items():
                g1 = getattr(parent1, name)
                g2 = getattr(parent2, name)
                fields[name] = type_.heriter(g1, g2)

        return cls(**fields)
    
    def __repr__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.dict().items())




class ADE:

    def __init__(self, parent1: "ADE"=None, parent2: "ADE"=None):

        #self.TAILLE_MIN = 0.5
        #self.TAILLE_MAX = 1.60
        self.parent1 = parent1
        self.parent2 = parent2
        self.genes = self.set_genes(fondateur=True)


    def set_genes(self, parent1: "ADE"=None, parent2: "ADE"=None, fondateur=False):
        """
        Définit les gènes (immutables) de l'ADE
        """
        if fondateur:
            return GenesDict.set_gene(fondateur=True)

        else:
            return GenesDict.set_gene(parent1=parent1.genes, parent2=parent2.genes)



    def set_phenotype(self, genes):
        
        return {
            # === PHYSIQUE ===
            "taille": self.compute_taille(),
            "force": self.compute_force(),
            "resistance_coups": "",
            "resistance_froid": "", 
            "vitesse": "",
            "esperance_de_vie" : "",
            
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
            "discretion" : ""
        }

    def compute_taille(self):

        taille_score = 0.6 * self.genes['croissance'] + 0.25 * self.genes['taille_os'] + 0.1 * self.genes['densite_os'] 

        bruit = np.random.normal(1, 0.05)  
        taille_score *= bruit

        taille_score_norm = np.clip(taille_score, 0, 1)

        return self.TAILLE_MIN + taille_score_norm * (self.TAILLE_MAX - self.TAILLE_MIN)

    
    def compute_force():

        force_score = ""

        return
    
    def compute_resistance_coups():

        return
    
    def compute_resistance_froid():

        return
    
    def compute_vitesse():

        return
    
    def compute_agressivite(self):

        effet_testosterone = (
            0.5*self.genes.prod_testosterone.expression 
            + 0.5*self.genes.recep_testosterone.expression
        )
        effet_serotonine = (
            0.5*self.genes.prod_serotonine.expression 
            + 0.5*self.genes.recep_serotonine.expression
        )
        effet_vasopressine = (
            0.5*self.genes.prod_vasopressine.expression 
            + 0.5*self.genes.recep_vasopressine.expression
        )

        score_brut = (
            0.7*effet_testosterone
            - 0.7*effet_serotonine
            + 0.4*self.genes.ratio_cortex_prefrontal_amygdale.expression
            + 0.3*self.genes.maoa.expression
            + 0.2*self.genes.reactivite_amygdale.expression
            + 0.15*effet_vasopressine
            + 0.15*self.genes.voie_glutamatergique.expression
        )

        MIN_THEO = -0.7
        MAX_THEO = 1.9
        
        # action hypothétique d'autres gènes non-représentés 
        SIGMA_BRUT = 0.05 * (MAX_THEO - MIN_THEO)
        score_brut += np.random.normal(0, SIGMA_BRUT)

        # normalisation entre [0;1]
        score_genetique = (score_brut - MIN_THEO) / (MAX_THEO - MIN_THEO)

        return np.clip(score_genetique, 0, 1)
    
    def compute_altruisme(self):

        effet_oxytocine = (
            0.5*self.genes.prod_oxytocine.expression 
            + 0.5*self.genes.recep_oxytocine.expression
        )
        effet_serotonine = (
            0.5*self.genes.prod_serotonine.expression 
            + 0.5*self.genes.recep_serotonine.expression
        )
        effet_vasopressine = (
            0.5*self.genes.prod_vasopressine.expression 
            + 0.5*self.genes.recep_vasopressine.expression
        )
        effet_testosterone = (
            0.5*self.genes.prod_testosterone.expression 
            + 0.5*self.genes.recep_testosterone.expression
        )

        score_brut = (
            0.7*effet_oxytocine
            + 0.6*self.genes.densite_neurones_miroirs.expression
            + 0.4*effet_serotonine
            + 0.3*self.genes.ratio_cortex_prefrontal_amygdale.expression
            - 0.3*effet_testosterone
            + 0.15*effet_vasopressine
        )

        # calculés à partir des poids à reprendre en compte après chaque modification
        MIN_THEO = -0.3
        MAX_THEO = 2.15
        
        # action hypothétique d'autres gènes non-représentés 
        SIGMA_BRUT = 0.05 * (MAX_THEO - MIN_THEO)
        score_brut += np.random.normal(0, SIGMA_BRUT)

        # normalisation entre [0;1]
        score_genetique = (score_brut - MIN_THEO) / (MAX_THEO - MIN_THEO)

        return np.clip(score_genetique, 0, 1)
    
    def compute_courage(self):

        effet_serotonine = (
            0.5*self.genes.prod_serotonine.expression 
            + 0.5*self.genes.recep_serotonine.expression
        )
        effet_cortisol = (
            0.5*self.genes.prod_cortisol.expression 
            + 0.5*self.genes.recep_cortisol.expression
        )
        effet_testosterone = (
            0.5*self.genes.prod_testosterone.expression 
            + 0.5*self.genes.recep_testosterone.expression
        )

        score_brut = (
            -0.5*self.genes.reactivite_amygdale.expression
            + 0.5*self.genes.ratio_cortex_prefrontal_amygdale
            + 0.4*effet_cortisol
            + 0.6*self.genes.densite_neurones_miroirs.expression
            + 0.4*effet_serotonine
            + 0.3*self.genes.ratio_cortex_prefrontal_amygdale.expression
            - 0.3*effet_testosterone
            + 0.15*effet_vasopressine
        )

        # calculés à partir des poids à reprendre en compte après chaque modification
        MIN_THEO = -0.3
        MAX_THEO = 2.15
        
        # action hypothétique d'autres gènes non-représentés 
        SIGMA_BRUT = 0.05 * (MAX_THEO - MIN_THEO)
        score_brut += np.random.normal(0, SIGMA_BRUT)

        # normalisation entre [0;1]
        score_genetique = (score_brut - MIN_THEO) / (MAX_THEO - MIN_THEO)

        return np.clip(score_genetique, 0, 1)
    
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
test.creer_fondateur()

print(test.genes)