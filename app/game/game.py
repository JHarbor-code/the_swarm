from app.life.ade import ADE
pop = {}
def creer_pop(name:list[str]):

    for i in name:
        pop[i] = ADE(name=i) 

creer_pop(["test"])

for v in pop.values():
    print(v)

