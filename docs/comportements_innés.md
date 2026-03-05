Les comportements innés sont hardcodés. Ils suivent un certain réalisme biologique. Est considéré inné tout comportement qu'un animal effectue à l'instinct pour lui permettre de satisfaire ses envies. 

### 1. Influence sur les constantes vitales 

**1.1 Dormir**
* réduis la variable pression_sommeil 
calcul : pression_sommeil -= 0.02 par tick
* augmente la variable energie (en fonction de la capacité de réparation de l'ADE)
calcul : 
* augmente la variable integrite (en fonction de la capacité de réparation, trait génétique, de l'ADE)

**1.2 Manger** 
* augmente la variable energie (en fonction de la capacité de digestion de l'ADE)
* réduit la variable pression_faim 

**1.3 Boire** 
* augmente la variable hydratation (en fonction de la capacité de digestion de l'ADE)
* réduit la variable pression_soif

### 2. Autres

**2.1 Attaquer**
* inflige des dégâts à un autre ADE
* diminue la variable energie
* diminue la variable hydratation
*permet ensuite à l'ade de manger la dépouille de son adversaire*
*peut être commis en mémoire d'une action hostile de la part de l'ADE attaqué

