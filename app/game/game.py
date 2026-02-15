from ade.ade import ADE
pop = {}
def creer_pop(name:list[str]):

    for i in name:
        pop[i] = ADE(name=i) 
