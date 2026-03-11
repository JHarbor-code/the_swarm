Le but de cette simulation est d'observer l'apparition de comportements émergents. Ainsi il nous semble plus utile de modéliser un phénotype ontologiquement significatif que biologiquement ; à savoir représenter un phénotype de haut niveau (avec une tendance plus comportementale) plutôt que des attributs biologique. 

Aussi, il est important de noter quand dans une visée de simplification du modèle tout en gardant un certain réalisme biologique, seul un nombre limité de gène a été séléctionné ; de facto, et en vue des connaissances intellectuelles actuelles, il nous a fallu sélectionner des coefficients arbitraires bien que scientifiquement inspiré pour déterminer leur expression. 

### Choix de modélisation : 

ADE
 |
 ├ Genotype
 │    └ Gene
 │         └ Allele
 │
 ├ Phenotype
 │    ├ MicroComportements
 │    ├ Caracteres
 │    └ VariablesVitales
 │
 └ Comportements

 ## Allele 

 Dataclasse qui modélise un allèle

 #### Attributs : 
 * name (str) : nom de l'allèle, définit automatiquement dans Gene dès qu'un nouvel allèle est créé 
 * valeur (float ∈ [0;1]) : expression de l'allèle susceptible de devenir celle du gène si l'allèle est dominante
 * dominance (float ∈ [0;1]) : simule un effet simple de dominance plus le nombre se rapproche de 1

#### Méthodes : 
(-)

 ## Gene 

Classe qui modélise un gène. 
> Elle n'est pas destinée à modéliser un gène précis : pour cela, utiliser les gènes générés à partir de Gene.Registry

#### Attributs : 
* MUTATION_RATE (float ∈ [0;1]) : chance qu'une mutation s'applique
* REGISTRY (list) : liste des différents gènes possibles
* allele1 (Allele) : première allèle du gène 
* allele2 (Allele) : seconde allèle du gène
* expression (float ∈ [0;1]) : expression définitive du gène
* alleles_possibles (list) : définit dans enfants de la classe. Liste les différentes allèles possible pour tel gène afin de suivre l'évolution

#### Méthodes : 
* \_\_init__ 
définit allele1 et allele2 donnés en argument, définit expression en appelant calculer_expression
Args: 
    allele1: Allele
    allele2: Allele
    
###### \_\_init_subclass__ 
définit l'attribut alleles_possibles des sous-classes

##### creer_fondateurs : 
crée les deux première allèles du gène au tout début de la simulation. Appelle ajouter_allele. Renvoie



### 1. Comportement

**1.1 Agressivité** 

*tendance à attaquer* 
Directement influencée par les gènes

Systèmes biologiques : 
* domination (+)
    
    prod_testosterone (+0.6)
    recep_testosterone (+0.5)
    prod_dopamine (+0.5)
    recep_dopamine (+0.4)
    prod_oxytocine (-0.5)
    recep_oxytocine (-0.4)

* compétitivité (+)

    prod_dopamine (+0.6)
    recep_dopamine (+0.5)
    prod_serotonine (-0.5) 
    recep_serotonine (-0.4)

* stress (+)

    prod_cortisol(+)
    recep_cortisol(+)
    prod_serotonine (-) 
    recep_serotonine (-)

* impulsivité (+)

    prod_dopamine (+)
    recep_dopamine (+)
    ratio_cortex_prefrontal_amygdale (-)
    prod_serotonine (-) 
    recep_serotonine (-)

* empathie (-)

    prod_oxytocine (+)
    recep_oxytocine (+)
    densite_neurones_miroirs (+)
    prod_testosterone (-)
    recep_testosterone (-)

* motivation sociale (-)

    prod_oxytocine (+)
    recep_oxytocine (+)
    prod_dopamine (+)
    recep_dopamine (+)
    prod_cortisol(-)
    recep_cortisol(-)

* peur_ressentie (+)

    ratio_cortex_prefrontal_amygdale (+)
    reactivite_amygdale (+)
    prod_cortisol(+)
    recep_cortisol(+)
    prod_serotonine (-) 
    recep_serotonine (-)


* prod_serotonine (-0.7)
* recep_serotonine (-0.7)
* ratio_cortex_prefrontal_amygdale (0.4)
* maoa (0.3)
* reactivite_amygdale (0.2)
* prod_vasopressine (0.15)
* recep_vasopressine (0.15)
* voie_glutamatergique (0.15)

**1.2 Sociabilité**

*tendance à rester groupé*

Systèmes biologiques : 
* motivation sociale (+)
* empathie (+)
* reconnaissance emotions (+)
* anxiete sociale (-)
* peur du rejet (-)
* stress (-)

**1.3 Altruisme**

*tendance à donner* 

Systèmes biologiques : 
* empathie (+)
* compréhension (+)
* niveau aspiration (-)
* anxiete sociale (-)
* peur du rejet (-)

Genes : 

* prod_oxytocine (0.7)
* recep_oxytocine (0.7)
* densite_neurones_miroirs (0.6)
* prod_serotonine (0.4)
* recep_serotonine (0.4)
* ratio_cortex_prefrontal_amygdale (0.3)
* prod_testosterone (-0.3)
* recep_testosterone (-0.3)
* prod_vasopressine (0.15)
* recep_vasopressine (0.15)

**1.4 Curiosité**

*tendance à explorer*

**1.5 Courage**

*tendance à se défendre / secourir* 

Genes : 

* reactivite_amygdale (-0.5)
* ratio_cortex_prefrontal_amygdale (0.5)
* prod_cortisol (0.4)
* recep_cortisol (0.4)
* prod_serotonine (0.4) 
* recep_serotonine (0.4)
* prod_testosterone (0.3)
* recep_testosterone (0.3)
* prod_dopamine (0.2)
* recep_dopamine (0.2)

**1.6 Peur**

*tendance à fuir / au stress*

**1.7 Rancune**

*determine le poids des actions négatives dans la mémoire* 

Genes : 

* volume_hippocampe (0.6)
* plasticite_synaptique (0.5)
* reactivite_amygdale (0.4)
* maoa (-0.4)
* prod_oxytocine (-0.15)
* recep_oxytocine (-0.15)
* prod_serotonine (-0.15)
* recep_serotonine (-0.15)

### 2. Performance physique (4 phénotypes)


**2.1 Force**

Genes : 

* 

**2.2 Taille**

**2.3 Masse**

 ```
 masse = f(
    force,
    taille, 
    stock_calories
 )
 ```

**2.4 Vitesse**
*dépend de masse, taille*

**2.5 Endurance**
*dépend de masse, taille*



### 3. Survie (4 phénotypes)


**3.1 Résistance froid**

**3.2 Résistance chaud**

**3.3 Résistance coups**
*Dépend de masse*

**3.4 Immunité**

**3.5 Regénération**

**3.6 Temps de réaction**

**3.7 Distance de détection**
*dépend de taille*


### 4. Vie & Reproduction (2 phénotypes)


**4.1 Coup Énérgétique**

**4.2 Fertilité**

**4.3 Longévité**

**4.4 Mémoire**
