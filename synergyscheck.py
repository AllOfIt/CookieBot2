from cookiebot2 import *

def checkSynergies():
    testgame  = Game()
    synergies = []
    for name in testgame.upgrades:
        if type(testgame.upgrades[name]) == SynergyUpgrade:
            synergies.append(testgame.upgrades[name])
    finalResult = 0
    for upgrade in synergies:
        if testgame.buildings[upgrade.target1].basePrice<testgame.buildings[upgrade.target2].basePrice:
            result = 'Good'
        else:
            finalResult+=1
            result = "Bad"
        print("{}  {}: target1:{}    target2:{}".format(result,upgrade.name,upgrade.target1,upgrade.target2))
    print("{} bad synergies detected".format(finalResult))


checkSynergies()