Le but de cette simulation est d'observer l'apparition de comportements émergents. Ainsi il nous semble plus utile de modéliser un phénotype ontologiquement significatif que biologiquement ; à savoir représenter un phénotype de haut niveau (avec une tendance plus comportementale) plutôt que des attributs biologique.

  

Aussi, il est important de noter quand dans une visée de simplification du modèle tout en gardant un certain réalisme biologique, seul un nombre limité de gène a été séléctionné ; de facto, et en vue des connaissances intellectuelles actuelles, il nous a fallu sélectionner des coefficients arbitraires bien que scientifiquement inspiré pour déterminer leur expression.

  

# Choix de modélisation :

  
```
ADE
 |
 ├ Genotype
 |     ├ Gene
 |     └ Allele
 |
 ├ Phenotype
 |     ├ MicroComportements
 |     ├ Caracteres
 |     └ VariablesVitales
 |
 └ Comportements
```

___
## Allele

Dataclasse qui modélise un allèle

### Attributs :

* name (str) : nom de l'allèle, définit automatiquement dans Gene dès qu'un nouvel allèle est créé

* valeur (float $\in [0;1]$) : expression de l'allèle susceptible de devenir celle du gène si l'allèle est dominante

* dominance (float $\in [0;1]$) : simule un effet simple de dominance plus le nombre se rapproche de 1

### Méthodes :

(-)

___
## Gene

Classe qui modélise un gène.

> [!warning] La création de gènes fonctionne par un système de registre implémenté dans Genotype, via `creer_gene_fondateur`ou `heriter`

### Attributs :

* `CHANCE_MUTATION` (float ∈ [0;1]) : chance qu'une mutation s'applique

* `REGISTRE` (list) : liste des différents gènes possibles

* `allele1` (Allele) : première allèle du gène

* `allele2` (Allele) : seconde allèle du gène

* `expression` (float ∈ [0;1]) : expression définitive du gène

* `alleles_possibles` (list) : définit dans enfants de la classe. Liste les différentes allèles possible pour tel gène afin de suivre l'évolution

  

### Méthodes :

* `__init__`
	Définit `allele1` et `allele2`, définit expression en appelant calculer_expression
	Args:
	    `allele1` : `Allele`
        `allele2` : `Allele`
___
* ` __init_subclass__`
	Définit l'attribut `alleles_possibles` des sous-classes
___
* `calculer_expression`
	Calcule l'expression du gène en prenant en compte une forme de dominance linéaire entre allèles (attribut  `dominance`) 
	Use-case : calculer l'expression du gène à l'instanciation de la classe
	Returns :
	    float
___
* `creer_gene_fondateur` :
	Crée un objet Gene dans le cas ou aucun parent n'est spécifié
	Crée les deux allèles du gène si moins de 2 allèles existent dans alleles_possibles
	Use-case : commencement de la simulation, création instantanée d'un individu
	Returns :
	    Gene
___
*  `heriter`
	Crée un objet `Gene`
	Sélectionne aléatoirement les deux allèles à partir des quatre allèles des parents en appliquant une chance de mutation
	Use-case : naissance d'un individu à partir de parent
	Returns : 
	    `Gene`
___
* `get_random_allele
	Choisit aléatoirement un allèle entre deux allèles passés en arguments
	Probabilité : $\frac{1}{2}$
	Use-case : sélectionner les allèles parents aléatoirement dans `heriter`
	Args : 
		`allele1` : `Allele`
		`allele2` : `Allele`
	Returns : 
		`Allele`
___
* `mutation`
	Applique une chance de mutation à un allèle (`CHANCE_MUTATION`) et l'ajoute si muté à la liste de classe `alleles_possibles`. La valeur de l'allèle ainsi que sa dominance mutent. 
	Use-case : Calculer une chance de mutation pour l'allèle transmise par les parents lors de la reproduction
	Args :
	    `allele` : `Allele` l'instance de la classe `Alelle` pouvant muter
	Returns : 
	    `Allele` : l'instance de la classe allele qui a muté ou pas
___
* `ajouter_allele`
	Ajoute un nouvel allèle à la liste de classe `alleles_possibles` en générant un nom automatiquement.
	Le nom de l'allèle est choisi dynamiquement selon sa valeur :
	    - supérieure à 0.5 → commence par "A"
	    - inférieure ou égale à 0.5 → commence par "a"
	Un suffixe numérique est ajouté si plusieurs allèles du même type existent.
	Use-case : ajouter une allèle qui vient d'être créée dans la liste `alleles_possibles`
	Args :
	    `valeur` : `float`
	Returns : 
	    `Allele` : l'instance d'`Allele` créée et ajoutée à `cls.alleles_possibles`
___
* `__str__` 
	Affiche une version lisible du gène, de la forme : 
```
Expression : 0.5
```
___



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