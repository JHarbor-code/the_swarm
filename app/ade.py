import numpy as np
import random
import gene as gn
from pydantic import BaseModel, ValidationError

class GenesDict(BaseModel):
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



class ADE:

    def __init__(self, genes=None):

        self.TAILLE_MIN = 0.5
        self.TAILLE_MAX = 1.60
        self.genes = self.set_genes(genes) if genes else self.set_genes()
        self.phenotype = self.set_phenotype(self.genes)


    def set_genes(self, genes_parent1=None, genes_parent2=None):
        """
        Définit les gènes (immutables) de l'ADE
        """

        recep_serotonine = Recep_Serotonine.heriter(genes_parent1['recep_serotonine'], genes_parent2["recep_serotonine"])
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

        force_score = 

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
print(test.phenotype)