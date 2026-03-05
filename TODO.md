## En cours
- [ ] Compute phenotype
- [ ] calculer la résistance aux coup a partir de l'imc de l'intechte en temps reel ratio = taille / (taille + poids)

## Prochaines étapes
- [ ] GUI pygame basique (wrap-around)
- [ ] système d'inventaire pour stocker de la nourriture
- [ ] Reproduction sexuée
- [ ] Système combat + fuite + appel à l'aide
- [ ] système d'altruisme : possibilité de donner de la nourriture
- [ ] Saisons + température (température plus froide : les intechtes peuvent se blottir entre eux)

## Futures features
- [ ] Prédateurs
- [ ] CLI stats
- [ ] Sauvegarde/chargement
- [ ] GUI soignée (carte du monde etc)
- [ ] gestation (malus force, vitesse...)

# Idée pour transformer potentiel génétique en grandeur physique : 

Récupérer les gènes de l’individu

Liste ou tuple genes = [g1, g2, ..., gn]

Chaque gène normalisé ∈ [0,1]

Récupérer les poids associés à chaque gène

Liste ou tuple weights = [w1, w2, ..., wn]

Calculer le score génétique brut

score = sum(g * w for g, w in zip(genes, weights))

Calculer les bornes théoriques

min_score = sum(w for w in weights if w < 0)

max_score = sum(w for w in weights if w > 0)

Normaliser le score pour obtenir G ∈ [0,1]

G = (score - min_score) / (max_score - min_score)

G = clip(G, 0, 1) pour sécurité

Calculer la taille asymptotique individuelle

Linf_ind = Linf_species * (0.5 + 0.5 * G)

Calculer le coefficient de croissance

k = k_base * (0.5 + G)

Récupérer le facteur environnemental au tick t

E = facteur_environnement(t)

Par ex. entre 0.7 et 1.2

Calculer le coefficient effectif

k_effectif = k * E

Calculer le grandissement du tick

delta_L = k_effectif * (Linf_ind - taille_actuelle)

Mettre à jour la taille de l’individu

taille_actuelle += delta_L

Optionnel : ajouter du bruit développemental

taille_actuelle += random.normal(0, sigma)

Répéter pour chaque tick


# Phénotype : 

Le but de cette simulation est d'observer l'apparition de comportements émergents. Ainsi il nous semble plus utile de modéliser un phénotype ontologiquement significatif que biologiquement ; à savoir représenter un phénotype de haut niveau (avec une tendance plus comportementale) plutôt que des attributs biologique. 

Aussi, il est important de noter quand dans une visée de simplification du modèle tout en gardant un certain réalisme biologique, seul un nombre limité de gène a été séléctionné ; de facto, et en vue des connaissances intellectuelles actuelles, il nous a fallu sélectionner des coefficients arbitraires bien que scientifiquement inspiré pour déterminer leur expression. 


### 1. Comportement

**1.1 Agressivité** 

*tendance à attaquer* 

Genes : 

* prod_testosterone (poids: 0.7)
* recep_testosterone (0.7)
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

**1.3 Altruisme**

*tendance à donner* 

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
*dépend de force, taille*

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