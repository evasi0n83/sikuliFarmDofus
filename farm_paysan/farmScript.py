reg_map = Region(0,23,349,133)
reg_sort = Region(825,926,496,111)
reg_centre = Region(861,215,694,560)
reg_combat= Region(359,97,1231,816)
reg_pret = Region(1130,643,677,392)

regFinCombat = Region(523,350,916,565)

imgBarreSort="barreSort.png"
imgCaseSort="caseSort.png"
imgCloseCombat="fermerCombat.png"
imgFinTour="finTour.png"
imgPosMap="posMap.PNG"
imgSortInvoc="sortInvoc.png"
imgCaseDeplacement="caseDeplacement.png"

pathToScript="C:\\Users\\Nmane\\Documents\\sikulix\\farm_paysan\\"



#listeObjetsQuiSerontCliques=("orgeGauche.png", "orgeDroite.png", "orge.png", "avoine.png", "avoineHaut.png", "avoineBas.png", "avoinePrecis.png", "avoinePrecis2.png","avoineHautDroite.png")
#listeObjetsQuiSerontCliques=("houblon.png", "houblon1.png", "houblon2.png", "houblon3.png", "ortie.png")
#listeObjetsQuiSerontCliques=("lin.png","lin1.png", "lin2.png", "lin3.png", "lin4.png", "lin5.png", "lin6.png", "lin7.png", "lin8.png", "lin9.png")

import random
import os

randomTime = random.uniform(-0.2,0.2)
randomTime2 = random.uniform(-0.2,0.2)

def combat():
    while True:
        wait(1+randomTime)        
        if reg_sort.exists(imgBarreSort):
            if reg_sort.exists(imgSortInvoc):
                reg_sort.click(imgSortInvoc)
                wait(0.5+randomTime2)
                if reg_combat.exists(imgCaseSort):
                    reg_combat.click(imgCaseSort)
                    if reg_combat.exists(imgCaseDeplacement) :
                        wait(0.5+randomTime2)
                        reg_combat.click(imgCaseDeplacement)
            wait(0.3+randomTime)
        if reg_pret.exists(imgFinTour):
            click(imgFinTour)
            wait(2+randomTime2)
        if regFinCombat.exists(imgCloseCombat):
            regFinCombat.click(imgCloseCombat)
            return

cpt = 0
compteurFin=0
objectifFin=3600

dossier1 = pathToScript + "orge"
dossier2 = pathToScript + "ortie"
dossier3 = pathToScript + "poisson"
listeObjetsQuiSerontCliques = [(dossier1 + "/" + e) for e in os.listdir(dossier1)]
listeObjetsQuiSerontCliques.extend([(dossier2 + "/" + e) for e in os.listdir(dossier2)])
listeObjetsQuiSerontCliques.extend([(dossier3 + "/" + e) for e in os.listdir(dossier3)])

#while reg_map.exists(imgPosMap):
while compteurFin < objectifFin :
    
    r1 = random.randint(-2,2)
    r2 = random.randint(-2,2)    
    randomTime = random.uniform(-0.2,0.2)
    randomTime2 = random.uniform(-0.2,0.2)
    for objectToFind in listeObjetsQuiSerontCliques:        
        resultsList = reg_centre.findAll(Pattern(objectToFind).similar(0.7))
        for match in resultsList:   
            x = match.getTarget().getX()
            y = match.getTarget().getY()
            click(Location(x+r1, y-r2))            
            wait(2+randomTime2)
            wait(2+randomTime)
    if cpt >= 10:
        if reg_sort.exists(imgBarreSort):
            combat()
        cpt=0
    else:
        wait(0.3+randomTime)
    cpt+=1
    compteurFin+=1

