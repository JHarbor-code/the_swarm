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
    prod_croissance: gn.ProdCroissance
    recep_croissance: gn.RecepCroissance
    prod_igf1 = gn.ProdIGF1
    recep_igf1 = gn.RecepIGF1


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
            "taille": self.calculer_phenotype(
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
            ),
            "force": "",
            "resistance_coups": "",
            "resistance_froid": "", 
            "vitesse": "",
            "esperance_de_vie" : "",
            
            # === COMPORTEMENTAUX ===
            "agressivite": self.calculer_phenotype(
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
            ),
            "altruisme": self.calculer_phenotype(
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
            ),
            "courage": self.calculer_phenotype(
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
            ),
            "memoire": "",
            "rancune": "",

            # === SURVIE === 
            "cout_energetique": "",
            "fertilite": "",
            "temps_de_reaction": "",
            "distance_detection": "",
            "discretion" : ""
        }
    
    def calculer_phenotype(self, genes: tuple, poids: tuple, bruit=True):

        score = np.dot(genes, poids)

        # calculés dynamiquement par les poids 
        MIN_THEO = sum(p for p in poids if p < 0)
        MAX_THEO = sum(p for p in poids if p > 0)
        
        if bruit:
            # action hypothétique d'autres gènes non-représentés 
            score *= np.random.normal(1, 0.05)

        # normalisation entre [0;1]
        score = (score - MIN_THEO) / (MAX_THEO - MIN_THEO)

        return np.clip(score, 0, 1)






test = ADE()
test.creer_fondateur()

print(test.genes)