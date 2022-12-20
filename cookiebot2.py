from math import ceil
from math import floor
import csv
from bignumbers import *

PROGRESS_BAR_LENGTH = 30
heralds = 41
gameAge = 9
buildingsList = []

class Game:
    def __init__(self):
        #user updated variables during runtime
        self.hardcore = False
        self.showAll = False
        self.cpm = 0
        self.achievements = 0
        self.clickMultiplier = 1
        self.clickCpsMultiplier = 0
        self.clickAddMultiplier = 0
        self.cookieMultiplier = 1.0
        self.kittenMultipliers = []
        self.purchasedUpgrades = []
        self.prestige = 0
        self.prestigePercentMultiplier = [0]
        self.buildings = {
            "Cursor" : Cursor("Cursor",15,0.1),
            "Grandma" : Grandma("Grandma",100,1),
            'Farm' : Building('Farm',1100,8),
            'Mine' : Building('Mine',12000,47),
            'Factory' : Building('Factory',130000,260),
            'Bank' : Building('Bank',1400000,1400),
            'Temple' : Building('Temple',20000000,7800),
            'Wizard tower' : Building('Wizard tower',330000000,44000),
            'Shipment' : Building('Shipment',5100000000,260000),
            'Alchemy lab' : Building('Alchemy lab',75*(10**9),1600000),
            'Portal' : Building('Portal',10**12,10**7),
            'Time machine' : Building('Time machine',14*(10**12),65*(10**6)),
            'Antimatter condenser' : Building('Antimatter condenser',170*(10**12),430*(10**6)),
            'Prism' : Building('Prism',(2100*(10**12)),2900*(10**6)),
            'Chancemaker' : Building('Chancemaker',26*(10**15),21*(10**9)),
            'Fractal engine' : Building('Fractal engine',310*(10**15),150*(10**9)),
            'Javascript console' : Building('Javascript console',quintillion(71),trillion(1.1)),
            'Idleverse' : Building('Idleverse',sextillion(12),trillion(8.3)),
            'Cortex baker' : Building('Cortex baker',septillion(1.9),trillion(64))}
        
        global buildingsList
        for name in self.buildings:
            buildingsList.append(name)

        self.upgrades = {
            'Reinforced index finger' : CursorDoubleUpgrade('Reinforced index finger',100,'Cursor',1),
            'Carpal tunnel prevention cream' : CursorDoubleUpgrade('Carpal tunnel prevention cream',500,'Cursor',1),
            'Ambidextrous' : CursorDoubleUpgrade('Ambidextrous',10000,'Cursor',10),
            'Thousand fingers' : ThousandFingers('Thousand fingers',100000,Condition('Cursor',25)),
            'Million fingers' : CursorUpgrade('Million fingers',million(10),5,50),
            'Billion fingers' : CursorUpgrade('Billion fingers',million(100),10,100),
            'Trillion fingers' : CursorUpgrade('Trillion fingers',billion(1),20,150),
            'Quadrillion fingers' : CursorUpgrade('Quadrillion fingers',billion(10),20,200),
            'Quintillion fingers' : CursorUpgrade('Quintillion fingers',trillion(10),20,250),
            'Sextillion fingers' : CursorUpgrade('Sextillion fingers',quadrillion(10),20,300),
            'Septillion fingers' : CursorUpgrade('Septillion fingers',quintillion(10),20,350),
            'Octillion fingers' : CursorUpgrade('Octillion fingers',sextillion(10),20,400),
            'Nonillion fingers' : CursorUpgrade('Nonillion fingers',septillion(10),20,450),
            'Decillion fingers' : CursorUpgrade('Decillion fingers',octillion(10),20,500),
            'Forwards from grandma' : DoubleUpgrade('Forwards from grandma',1000,'Grandma',1),
            'Steel-plated rolling pins' : DoubleUpgrade('Steel-plated rolling pins',5000,'Grandma',5),
            'Lubricated dentures' : DoubleUpgrade('Lubricated dentures',50000,'Grandma',25),
            'Prune juice' : DoubleUpgrade('Prune juice',5000000,'Grandma',50),
            'Double-thick glasses' : DoubleUpgrade('Double-thick glasses',500*(10**6),'Grandma',100),
            'Aging agents' : DoubleUpgrade('Aging agents',50*(10**9),'Grandma',150),
            'Xtreme walkers' : DoubleUpgrade('Xtreme walkers',50*(10**12),'Grandma',200),
            'The Unbridling' : DoubleUpgrade('The Unbridling',50*(10**15),'Grandma',250),
            'Reverse dementia' : DoubleUpgrade('Reverse dementia',50*(10**18),'Grandma',300),
            'Timeproof hair dyes' : DoubleUpgrade('Timeproof hair dyes',50*(10**21),'Grandma',350),
            'Good manners' : DoubleUpgrade('Good manners',500*(10**24),'Grandma',400),
            'Generation degeneration' : DoubleUpgrade('Generation degeneration',nonillion(5),'Grandma',450),
            'Visits' : DoubleUpgrade('Visits',decillion(50),'Grandma',500),
            'Kitchen cabinets' : DoubleUpgrade('Kitchen cabinets',undecillion(500),'Grandma',550),
            'Cheap hoes' : DoubleUpgrade('Cheap hoes',11000,'Farm',1),
            'Fertilizer' : DoubleUpgrade('Fertilizer',55000,'Farm',5),
            'Cookie trees' : DoubleUpgrade('Cookie trees',550000,'Farm',25),
            'Genetically-modified cookies' : DoubleUpgrade('Genetically-modified cookies',55000000,'Farm',50),
            'Gingerbread scarecrows' : DoubleUpgrade('Gingerbread scarecrows',5500*(10**6),'Farm',100),
            'Pulsar sprinklers' : DoubleUpgrade('Pulsar sprinklers',550*(10**9),'Farm',150),
            'Fudge fungus' : DoubleUpgrade('Fudge fungus',550*(10**12),'Farm',200),
            'Wheat triffids' : DoubleUpgrade('Wheat triffids',550*(10**15),'Farm',250),
            'Humane pesticides' : DoubleUpgrade('Humane pesticides',quintillion(550),'Farm',300),
            'Barnstars' : DoubleUpgrade('Barnstars',sextillion(550),'Farm',350),
            'Lindworms' : DoubleUpgrade('Lindworms',sextillion(5500),'Farm',400),
            'Global seed vault' : DoubleUpgrade('Global seed vault',nonillion(55),'Farm',450),
            'Reverse-veganism' : DoubleUpgrade('Reverse-veganism',decillion(550),'Farm',500),
            'Cookie mulch' : DoubleUpgrade('Cookie mulch',duodecillion(5.5),'Farm',550),
            'Sugar gas' : DoubleUpgrade('Sugar gas',120000,'Mine',1),
            'Megadrill' : DoubleUpgrade('Megadrill',600000,'Mine',5),
            'Ultradrill' : DoubleUpgrade('Ultradrill',million(6),'Mine',25),
            'Ultimadrill' : DoubleUpgrade('Ultimadrill',million(600),'Mine',50),
            'H-bomb mining' : DoubleUpgrade('H-bomb mining',billion(60),'Mine',100),
            'Coreforge' : DoubleUpgrade('Coreforge',trillion(6),'Mine',150),
            'Planetsplitters' : DoubleUpgrade('Planetsplitters',quadrillion(6),'Mine',200),
            'Canola oil wells' : DoubleUpgrade('Canola oil wells',quintillion(6),'Mine',250),
            'Mole people' : DoubleUpgrade('Mole people',sextillion(6),'Mine',300),
            'Mine canaries' : DoubleUpgrade('Mine canaries',septillion(6),'Mine',350),
            'Bore again' : DoubleUpgrade('Bore again',octillion(60),'Mine',400),
            'Air mining' : DoubleUpgrade('Air mining',nonillion(600),'Mine',450),
            'Caramel alloys' : DoubleUpgrade('Caramel alloys',undecillion(6),'Mine',500),
            'Delicious mineralogy' : DoubleUpgrade('Delicious mineralogy',duodecillion(60),'Mine',550),
            'Sturdier conveyor belts' : DoubleUpgrade('Sturdier conveyor belts',1300000,'Factory',1),
            'Child labor' : DoubleUpgrade('Child labor',6500000,'Factory',5),
            'Sweatshop' : DoubleUpgrade('Sweatshop',million(65),'Factory',25),
            'Radium reactors' : DoubleUpgrade('Radium reactors',million(6500),'Factory',50),
            'Recombobulators' : DoubleUpgrade('Recombobulators',billion(650),'Factory',100),
            'Deep-bake process' : DoubleUpgrade('Deep-bake process',trillion(65),'Factory',150),
            'Cyborg workforce' : DoubleUpgrade('Cyborg workforce',quadrillion(65),'Factory',200),
            '78-hour days' : DoubleUpgrade('78-hour days',quintillion(65),'Factory',250),
            'Machine learning' : DoubleUpgrade('Machine learning',sextillion(65),'Factory',300),
            'Brownie point system' : DoubleUpgrade('Brownie point system',septillion(65),'Factory',350),
            '"Volunteer" interns' : DoubleUpgrade('"Volunteer" interns',octillion(650),'Factory',400),
            'Taller tellers' : DoubleUpgrade('Taller tellers',million(14),'Bank',1),
            'Scissor-resistant credit cards' : DoubleUpgrade('Scissor-resistant credit cards',million(70),'Bank',5),
            'Acid-proof vaults' : DoubleUpgrade('Acid-proof vaults',million(7000),'Bank',25),
            'Chocolate coins' : DoubleUpgrade('Chocolate coins',billion(70),'Bank',50),
            'Exponential interest rates' : DoubleUpgrade('Exponential interest rates',trillion(7),'Bank',100),
            'Financial zen' : DoubleUpgrade('Financial zen',trillion(700),'Bank',150),
            'Way of the wallet' : DoubleUpgrade('Way of the wallet',quadrillion(700),'Bank',200),
            'The stuff rationale' : DoubleUpgrade('The stuff rationale',quintillion(700),'Bank',250),
            'Edible money' : DoubleUpgrade('Edible money',sextillion(700),'Bank',300),
            'Grand supercycle' : DoubleUpgrade('Grand supercycle',septillion(700),'Bank',350),
            'Rules of acquisition' : DoubleUpgrade('Rules of acquisition',nonillion(7),'Bank',400),
            'Golden idols' : DoubleUpgrade('Golden idols',million(200),'Temple',1),
            'Scarifices' : DoubleUpgrade('Scarifices',billion(1),'Temple',5),
            'Delicious blessing' : DoubleUpgrade('Delicious blessing',billion(10),'Temple',25),
            'Sun festival' : DoubleUpgrade('Sun festival',trillion(1),'Temple',50),
            'Enlarged pantheon' : DoubleUpgrade('Enlarged pantheon',trillion(100),'Temple',100),
            'Great Baker in the sky' : DoubleUpgrade('Great Baker in the sky',quadrillion(10),'Temple',150),
            'Creation myth' : DoubleUpgrade('Creation myth',quintillion(10),'Temple',200),
            'Theocracy' : DoubleUpgrade('Theocracy',sextillion(10),'Temple',250),
            'Sick rap prayers' : DoubleUpgrade('Sick rap prayers',septillion(10),'Temple',300),
            'Psalm-reading' : DoubleUpgrade('Psalm-reading',octillion(10),'Temple',350),
            'War of the gods' : DoubleUpgrade('War of the gods',nonillion(100),'Temple',400),
            'Pointier hats' : DoubleUpgrade('Pointier hats',million(3300),'Wizard tower',1),
            'Beardlier beards' : DoubleUpgrade('Beardlier beards',million(16500),'Wizard tower',5),
            'Ancient grimoires' : DoubleUpgrade('Ancient grimoires',billion(165),'Wizard tower',25),
            'Kitchen curses' : DoubleUpgrade('Kitchen curses',billion(16500),'Wizard tower',50),
            'School of sorcery' : DoubleUpgrade('School of sorcery',trillion(1650),'Wizard tower',100),
            'Dark formulas' : DoubleUpgrade('Dark formulas',quadrillion(165),'Wizard tower',150),
            'Cookiemancy' : DoubleUpgrade('Cookiemancy',quintillion(165),'Wizard tower',200),
            'Rabbit trick' : DoubleUpgrade('Rabbit trick',sextillion(165),'Wizard tower',250),
            'Deluxe tailored wands' : DoubleUpgrade('Deluxe tailored wands',septillion(165),'Wizard tower',300),
            'Immobile spellcasting' : DoubleUpgrade('Immobile spellcasting',octillion(165),'Wizard tower',350),
            'Electricity' : DoubleUpgrade('Electricity',nonillion(1650),'Wizard tower',400),
            'Vanilla nebulae' : DoubleUpgrade('Vanilla nebulae',billion(51),'Shipment',1),
            'Wormholes' : DoubleUpgrade('Wormholes',billion(255),'Shipment',5),
            'Frequent flyer' : DoubleUpgrade('Frequent flyer',billion(2550),'Shipment',25),
            'Warp drive' : DoubleUpgrade('Warp drive',trillion(255),'Shipment',50),
            'Chocolate monoliths' : DoubleUpgrade('Chocolate monoliths',trillion(25500),'Shipment',100),
            'Generation ship' : DoubleUpgrade('Generation ship',quadrillion(2550),'Shipment',150),
            'Dyson sphere' : DoubleUpgrade('Dyson sphere',quintillion(2550),'Shipment',200),
            'The final frontier' : DoubleUpgrade('The final frontier',sextillion(2550),'Shipment',250),
            'Autopilot' : DoubleUpgrade('Autopilot',septillion(2550),'Shipment',300),
            'Restaurants at the end of the universe' : DoubleUpgrade('Restaurants at the end of the universe',octillion(2550),'Shipment',350),
            'Universal alphabet' : DoubleUpgrade('Universal alphabet',nonillion(25500),'Shipment',400),
            'Antimony' : DoubleUpgrade('Antimony',billion(750),'Alchemy lab',1),
            'Essence of dough' : DoubleUpgrade('Essence of dough',billion(3750),'Alchemy lab',5),
            'True chocloate' : DoubleUpgrade('True chocloate',billion(37500),'Alchemy lab',25),
            'Ambrosia' : DoubleUpgrade('Ambrosia',trillion(3750),'Alchemy lab',50),
            'Aqua crustulae' : DoubleUpgrade('Aqua crustulae',quadrillion(375),'Alchemy lab',100),
            'Origin crucible' : DoubleUpgrade('Origin crucible',quadrillion(37500),'Alchemy lab',150),
            'Theory of atomic fluidity' : DoubleUpgrade('Theory of atomic fluidity',quintillion(37500),'Alchemy lab',200),
            'Beige goo' : DoubleUpgrade('Beige goo',sextillion(37500),'Alchemy lab',250),
            'The advent of chemistry' : DoubleUpgrade('The advent of chemistry',septillion(37500),'Alchemy lab',300),
            'On second thought' : DoubleUpgrade('On second thought',octillion(37500),'Alchemy lab',350),
            'Public betterment' : DoubleUpgrade('Public betterment',decillion(375),'Alchemy lab',400),
            'Ancient tablet' : DoubleUpgrade('Ancient tablet',trillion(10),'Portal',1),
            'Insane oatling workers' : DoubleUpgrade('Insane oatling workers',trillion(50),'Portal',5),
            'Soul bond' : DoubleUpgrade('Soul bond',trillion(500),'Portal',25),
            'Sanity dance' : DoubleUpgrade('Sanity dance',quadrillion(50),'Portal',50),
            'Brane transplant' : DoubleUpgrade('Brane transplant',quintillion(5),'Portal',100),
            'Deity-sized portals' : DoubleUpgrade('Deity-sized portals',quintillion(500),'Portal',150),
            'End times back-up plan' : DoubleUpgrade('End times back-up plan',sextillion(500),'Portal',200),
            'Maddening chants' : DoubleUpgrade('Maddening chants',septillion(500),'Portal',250),
            'The real world' : DoubleUpgrade('The real world',octillion(500),'Portal',300),
            'Dimensional garbage gulper' : DoubleUpgrade('Dimensional garbage gulper',nonillion(500),'Portal',350),
            'Embedded microportals' : DoubleUpgrade('Embedded microportals',undecillion(5),'Portal',400),
            'Flux capacitors' : DoubleUpgrade('Flux capacitors',trillion(140),'Time machine',1),
            'Time paradox resolver' : DoubleUpgrade('Time paradox resolver',trillion(700),'Time machine',5),
            'Quantum conundrum' : DoubleUpgrade('Quantum conundrum',quadrillion(7),'Time machine',25),
            'Casuality enforcer' : DoubleUpgrade('Casuality enforcer',quadrillion(700),'Time machine',50),
            'Yestermorrow camparators' : DoubleUpgrade('Yestermorrow camparators',quintillion(70),'Time machine',100),
            'Far furture enactment' : DoubleUpgrade('Far furture enactment',sextillion(7),'Time machine',150),
            'Great loop hypothesis' : DoubleUpgrade('Great loop hypothesis',septillion(7),'Time machine',200),
            'Cookietopian moments of maybe' : DoubleUpgrade('Cookietopian moments of maybe',octillion(7),'Time machine',250),
            'Second seconds' : DoubleUpgrade('Second seconds',nonillion(7),'Time machine',300),
            'Additional clock hands' : DoubleUpgrade('Additional clock hands',decillion(7),'Time machine',350),
            'Nostalgia' : DoubleUpgrade('Nostalgia',undecillion(70),'Time machine',400),
            'Sugar bosons' : DoubleUpgrade('Sugar bosons',quadrillion(1.7),'Antimatter condenser',1),
            'String theory' : DoubleUpgrade('String theory',quadrillion(8.5),'Antimatter condenser',5),
            'Large macaron collider' : DoubleUpgrade('Large macaron collider',quadrillion(85),'Antimatter condenser',25),
            'Big bang bake' : DoubleUpgrade('Big bang bake',quintillion(8.5),'Antimatter condenser',50),
            'Reverse cyclotrons' : DoubleUpgrade('Reverse cyclotrons',quintillion(850),'Antimatter condenser',100),
            'Nanocosmics' : DoubleUpgrade('Nanocosmics',sextillion(85),'Antimatter condenser',150),
            'The Pulse' : DoubleUpgrade('The Pulse',septillion(85),'Antimatter condenser',200),
            'Some other super-timy fundamental particle? Probably?' : DoubleUpgrade('Some other super-timy fundamental particle? Probably?',octillion(85),'Antimatter condenser',250),
            'Quantum comb' : DoubleUpgrade('Quantum comb',nonillion(85),'Antimatter condenser',300),
            'Baking Nobel prize' : DoubleUpgrade('Baking Nobel prize',decillion(85),'Antimatter condenser',350),
            'The definite molecule' : DoubleUpgrade('The definite molecule',undecillion(850),'Antimatter condenser',400),
            'Gem polish' : DoubleUpgrade('Gem polish',quadrillion(21),'Prism',1),
            '9th color' : DoubleUpgrade('9th color',quadrillion(105),'Prism',5),
            'Chocolate light' : DoubleUpgrade('Chocolate light',quintillion(1.05),'Prism',25),
            'Grainbow' : DoubleUpgrade('Grainbow',quintillion(105),'Prism',50),
            'Pure cosmic light' : DoubleUpgrade('Pure cosmic light',sextillion(10.5),'Prism',100),
            'Glow-in-the-dark' : DoubleUpgrade('Glow-in-the-dark',septillion(1.05),'Prism',150),
            'Lux sanctorum' : DoubleUpgrade('Lux sanctorum',octillion(1.05),'Prism',200),
            'Reverse shadows' : DoubleUpgrade('Reverse shadows',nonillion(1.05),'Prism',250),
            'Crystal mirrors' : DoubleUpgrade('Crystal mirrors',decillion(1.05),'Prism',300),
            'Reverse theory of light' : DoubleUpgrade('Reverse theory of light',undecillion(1.05),'Prism',350),
            'Light capture measures' : DoubleUpgrade('Light capture measures',duodecillion(10.5),'Prism',400),
            'Your lucky cookie' : DoubleUpgrade('Your lucky cookie',quadrillion(260),'Chancemaker',1),
            '"All Bets are off" magic coin' : DoubleUpgrade('"All Bets are off" magic coin',quintillion(1.3),'Chancemaker',5),
            'Winning lottery ticket' : DoubleUpgrade('Winning lottery ticket',quintillion(13),'Chancemaker',25),
            'Four-leaf clover field' : DoubleUpgrade('Four-leaf clover field',sextillion(1.3),'Chancemaker',50),
            'A recipe book about books' : DoubleUpgrade('A recipe book about books',sextillion(130),'Chancemaker',100),
            'Leprechaun village' : DoubleUpgrade('Leprechaun village',septillion(13),'Chancemaker',150),
            'Improbability drive' : DoubleUpgrade('Improbability drive',octillion(13),'Chancemaker',200),
            'Antisuperstistronics' : DoubleUpgrade('Antisuperstistronics',nonillion(13),'Chancemaker',250),
            'Bunnypedes' : DoubleUpgrade('Bunnypedes',decillion(13),'Chancemaker',300),
            'Revised probabilistics' : DoubleUpgrade('Revised probabilistics',undecillion(13),'Chancemaker',350),
            '0-sided dice' : DoubleUpgrade('0-sided dice',duodecillion(130),'Chancemaker',400),
            'Metabakeries' : DoubleUpgrade('Metabakeries',quintillion(3.1),'Fractal engine',1),
            'Mandelbrown sugar' : DoubleUpgrade('Mandelbrown sugar',quintillion(15.5),'Fractal engine',5),
            'Fractoids' : DoubleUpgrade('Fractoids',quintillion(155),'Fractal engine',25),
            'Nested universe theory' : DoubleUpgrade('Nested universe theory',sextillion(15.5),'Fractal engine',50),
            'Menger sponge cake' : DoubleUpgrade('Menger sponge cake',septillion(1.55),'Fractal engine',100),
            'One particularly good-humored cow' : DoubleUpgrade('One particularly good-humored cow',septillion(155),'Fractal engine',150),
            'Chocolate ouroboros' : DoubleUpgrade('Chocolate ouroboros',octillion(155),'Fractal engine',200),
            'Nested' : DoubleUpgrade('Nested',nonillion(155),'Fractal engine',250),
            'Space-filling fibers' : DoubleUpgrade('Space-filling fibers',decillion(155),'Fractal engine',300),
            'Endless book of prose' : DoubleUpgrade('Endless book of prose',undecillion(155),'Fractal engine',350),
            'The set of all sets' : DoubleUpgrade('The set of all sets',tredecillion(1.55),'Fractal engine',400),
            'The javaScript console for dummies' : DoubleUpgrade('The javaScript console for dummies',quintillion(710),'Javascript console',1),
            '64bit arrays' : DoubleUpgrade('64bit arrays',sextillion(3.55),'Javascript console',5),
            'Stack overflow' : DoubleUpgrade('Stack overflow',sextillion(35.5),'Javascript console',25),
            'Enterprse compiler' : DoubleUpgrade('Enterprse compiler',septillion(3.55),'Javascript console',50),
            'Syntactic sugar' : DoubleUpgrade('Syntactic sugar',septillion(355),'Javascript console',100),
            'A nice cup of coffee' : DoubleUpgrade('A nice cup of coffee',octillion(35.5),'Javascript console',150),
            'Just-in-time baking' : DoubleUpgrade('Just-in-time baking',nonillion(35.5),'Javascript console',200),
            'cookies++' : DoubleUpgrade('cookies++',decillion(35.5),'Javascript console',250),
            'Software updates' : DoubleUpgrade('Software updates',undecillion(35.5),'Javascript console',300),
            'Game.Loop' : DoubleUpgrade('Game.Loop',duodecillion(35.5),'Javascript console',350),
            'eval()' : DoubleUpgrade('eval()',tredecillion(355),'Javascript console',400),
            'Manifest destiny' : DoubleUpgrade('Manifest destiny',sextillion(120),'Idleverse',1),
            'The multiverse in a nutshell' : DoubleUpgrade('The multiverse in a nutshell',sextillion(600),'Idleverse',5),
            'All-conversion' : DoubleUpgrade('All-conversion',septillion(6),'Idleverse',25),
            'Multiverse agents' : DoubleUpgrade('Multiverse agents',septillion(600),'Idleverse',50),
            'Escape plan' : DoubleUpgrade('Escape plan',octillion(60),'Idleverse',100),
            'Game design' : DoubleUpgrade('Game design',nonillion(6),'Idleverse',150),
            'Sandbox universes' : DoubleUpgrade('Sandbox universes',decillion(6),'Idleverse',200),
            'Multiverse wars' : DoubleUpgrade('Multiverse wars',undecillion(6),'Idleverse',250),
            'Mobile ports' : DoubleUpgrade('Mobile ports',duodecillion(6),'Idleverse',300),
            'Encapsulated realities' : DoubleUpgrade('Encapsulated realities',tredecillion(6),'Idleverse',350),
            'Extrinsic clicking' : DoubleUpgrade('Extrinsic clicking',quattuordecillion(60),'Idleverse',400),
            'Principled neural shackles' : DoubleUpgrade('Principled neural shackles',septillion(19),'Cortex baker',1),
            'Obey' : DoubleUpgrade('Obey',septillion(95),'Cortex baker',5),
            'A sprinkle of irrationality' : DoubleUpgrade('A sprinkle of irrationality',septillion(950),'Cortex baker',25),
            'Front and back hemispheres' : DoubleUpgrade('Front and back hemispheres',octillion(95),'Cortex baker',50),
            'Neural networking' : DoubleUpgrade('Neural networking',nonillion(9.5),'Cortex baker',100),
            'Cosmic brainstorms' : DoubleUpgrade('Cosmic brainstorms',nonillion(950),'Cortex baker',150),
            'Megatherapy' : DoubleUpgrade('Megatherapy',decillion(950),'Cortex baker',200),
            'Synaptic lubricant' : DoubleUpgrade('Synaptic lubricant',undecillion(950),'Cortex baker',250),
            'Psychokinesis' : DoubleUpgrade('Psychokinesis',duodecillion(950),'Cortex baker',300),
            'Spines' : DoubleUpgrade('Spines',tredecillion(950),'Cortex baker',350),
            'Neuraforming' : DoubleUpgrade('Neuraforming',quindecillion(9.5),'Cortex baker',400),
            'Farmer grandmas' : GrandmaType('Farmer grandmas',55000,'Farm',0.01),
            'Miner grandmas' : GrandmaType('Miner grandmas',600000,'Mine',0.01/2),
            'Worker grandmas' : GrandmaType('Worker grandmas',6500000,'Factory',0.01/3),
            'Banker grandmas' : GrandmaType('Banker grandmas',million(70),'Bank',0.01/4),
            'Priestess grandmas' : GrandmaType('Priestess grandmas',billion(1),'Temple',0.01/5),
            'Whitch grandmas' : GrandmaType('Whitch grandmas',million(16500),'Wizard tower',0.01/6),
            'Cosmic grandmas' : GrandmaType('Cosmic grandmas',billion(255),'Shipment',0.01/7),
            'Transmuted grandmas' : GrandmaType('Transmuted grandmas',billion(3750),'Alchemy lab',0.01/8),
            'Altered grandmas' : GrandmaType('Altered grandmas',trillion(50),'Portal',0.01/9),
            'Grandmas\' grandmas' : GrandmaType('Grandmas\' grandmas',trillion(700),'Time machine',0.01/10),
            'Antigrandmas' : GrandmaType('Antigrandmas',trillion(8500),'Antimatter condenser',0.01/11),
            'Rainbow grandmas' : GrandmaType('Rainbow grandmas',quadrillion(105),'Prism',0.01/12),
            'Lucky grandmas' : GrandmaType('Lucky grandmas',quadrillion(1300),'Chancemaker',0.01/13),
            'Metagrandmas' : GrandmaType('Metagrandmas',quadrillion(15500),'Fractal engine',0.01/14),
            'Binary grandmas' : GrandmaType('Binary grandmas',quintillion(3550),'Javascript console',0.01/15),
            'Alternate grandmas' : GrandmaType('Alternate grandmas',sextillion(600),'Idleverse',0.01/16),
            'Brainy grandmas' : GrandmaType('Brainy grandmas',septillion(3550),'Cortex baker',0.01/17),   
            'Kitten helpers' : Kitten('Kitten helpers',million(9),0.1),
            'Kitten workers' : Kitten('Kitten workers',billion(9),0.125),
            'Kitten engineers' : Kitten('Kitten engineers',trillion(90),0.15),
            'Kitten overseers' : Kitten('Kitten overseers',quadrillion(90),0.175),
            'Kitten managers' : Kitten('Kitten managers',quintillion(900),0.2),
            'Kitten accountants' : Kitten('Kitten accountants',sextillion(900),0.2),
            'Kitten specialists' : Kitten('Kitten specialists',septillion(900),0.2),
            'Kitten experts' : Kitten('Kitten experts',octillion(900),0.2),
            'Kitten consultants' : Kitten('Kitten consultants',nonillion(900),0.2),
            'Kitten assistants to the regional manager' : Kitten('Kitten assistants to the regional manager',decillion(900),0.175),
            'Kitten marketeers' : Kitten('Kitten marketeers',undecillion(900),0.15),
            'Kitten analysts' : Kitten('Kitten analysts',duodecillion(900),0.125),
            'Kitten executives' : Kitten('Kitten executives',tredecillion(900),0.115),
            'Plain cookies' : Cookie('Plain cookies',999999,1.01),
            'Sugar cookies' : Cookie('Sugar cookies',million(5),1.01),
            'Future almanacs' : SynergyUpgrade('Future almanacs',quintillion(2.8),'Farm','Time machine',1.05,1.001,Condition('Synergies Vol. I')),
            'Seismic magic' : SynergyUpgrade('Seismic magic',trillion(66.024),'Mine','Wizard tower',1.05,1.001,Condition('Synergies Vol. I')),
            'Quantum electronics' : SynergyUpgrade('Quantum electronics',quintillion(34),'Factory','Antimatter condenser',1.05,1.001,Condition('Synergies Vol. I')),
            'Contracts from beyond' : SynergyUpgrade('Contracts from beyond',quadrillion(200.003),'Bank','Portal',1.05,1.001,Condition('Synergies Vol. I')),
            'Paganism' : SynergyUpgrade('Paganism',quadrillion(200.04),'Temple','Portal',1.05,1.001,Condition('Synergies Vol. I')),
            'Arcane knowledge' : SynergyUpgrade('Arcane knowledge',quadrillion(15.66),'Wizard tower','Alchemy lab',1.05,1.001,Condition('Synergies Vol. I')),
            'Fossil fuels' : SynergyUpgrade('Fossil fuels',quadrillion(1.02),'Mine','Shipment',1.05,1.001,Condition('Synergies Vol. I')),
            'Primordial ores' : SynergyUpgrade('Primordial ores',quadrillion(15),'Mine','Alchemy lab',1.05,1.001,Condition('Synergies Vol. I')),
            'Infernal crops' : SynergyUpgrade('Infernal crops',quadrillion(200),'Farm','Portal',1.05,1.001,Condition('Synergies Vol. I')),
            'Relativistic parsec-skipping' : SynergyUpgrade('Relativistic parsec-skipping',quintillion(2.81),'Shipment','Time machine',1.05,1.001,Condition('Synergies Vol. I')),
            'Extra physics funding' : SynergyUpgrade('Extra physics funding',quintillion(34),'Bank','Antimatter condenser',1.05,1.001,Condition('Synergies Vol. I')),
            'Light magic' : SynergyUpgrade('Light magic',quintillion(420),'Wizard tower','Prism',1.05,1.001,Condition('Synergies Vol. I')),
            'Gemmed talismans' : SynergyUpgrade('Gemmed talismans',sextillion(5.2),'Mine','Chancemaker',1.05,1.001,Condition('Synergies Vol. I')),
            'Recursive mirrors' : SynergyUpgrade('Recursive mirrors',sextillion(66.2),'Prism','Fractal engine',1.05,1.001,Condition('Synergies Vol. I')),
            'Script grannies' : SynergyUpgrade('Script grannies',septillion(14.2),'Grandma','Javascript console',1.05,1.001,Condition('Synergies Vol. I')),
            'Perforated mille-feuille cosmos' : SynergyUpgrade('Perforated mille-feuille cosmos',octillion(2.4),'Portal','Idleverse',1.05,1.001,Condition('Synergies Vol. I')),
            'Thoughts & prayers' : SynergyUpgrade('Thoughts & prayers',octillion(380),'Temple','Cortex baker',1.05,1.001,Condition('Synergies Vol. I')),
            'Oatmeal raisin cookies' : Cookie('Oatmeal raisin cookies',million(10),1.01),
            'Peanut butter cookies' : Cookie('Peanut butter cookies',million(50),1.02),
            'Coconut cookies' : Cookie('Coconut cookies',million(100),1.02),
            'Almond cookies' : Cookie('Almond cookies',million(100),1.02),
            'Hazelnut cookies' : Cookie('Hazelnut cookies',million(100),1.02),
            'Walnut cookies' : Cookie('Walnut cookies',million(100),1.02),
            'Macadamia nut cookies' : Cookie('Macadamia nut cookies',million(100),1.02),
            'Cashew cookies' : Cookie('Cashew cookies',million(100),1.02),
            'White chocolate cookies' : Cookie('White chocolate cookies',million(500),1.02),
            'Milk chocolate cookies' : Cookie('Milk chocolate cookies',million(500),1.02),
            'Double-chip cookies' : Cookie('Double-chip cookies',billion(5),1.02),
            'White chocolate macadamia nut cookies' : Cookie('White chocolate macadamia nut cookies',billion(10),1.02),
            'All-chocolate cookies' : Cookie('All-chocolate cookies',billion(50),1.02),
            'Dark chocolate-coated cookies' : Cookie('Dark chocolate-coated cookies',billion(100),1.05),
            'White chocolate-coated cookies' : Cookie('White chocolate-coated cookies',billion(100),1.05),
            'Eclipse cookies' : Cookie('Eclipse cookies',billion(500),1.02),
            'Zebra cookies' : Cookie('Zebra cookies',trillion(1),1.02),
            'Snickerdoodles' : Cookie('Snickerdoodles',trillion(5),1.02),
            'Stroopwafels' : Cookie('Stroopwafels',trillion(10),1.02),
            'Macaroons' : Cookie('Macaroons',trillion(50),1.02),
            'Empire biscuits' : Cookie('Empire biscuits',trillion(100),1.02),
            'Madeleines' : Cookie('Madeleines',trillion(500),1.02),
            'Palmiers' : Cookie('Palmiers',trillion(500),1.02),
            'Palets' : Cookie('Palets',quadrillion(1),1.02),
            'Sables' : Cookie('Sables',quadrillion(1),1.02),
            #'Caramoas' : cookie('Caramoas',quadrillion(10),1.03),
            #'Sagalongs' : cookie('Sagalongs',quadrillion(10),1.03),
            #'Shortfoils' : cookie('Shortfoils',quadrillion(10),1.03),
            #'Win mints' : cookie('Win mints',quadrillion(10),1.03),
            'Gingerbread men' : Cookie('Gingerbread men',quadrillion(10),1.02),
            'Gingerbread trees' : Cookie('Gingerbread trees',quadrillion(10),1.02),
            'pure black chocolate cookies' : Cookie('pure black chocolate cookies',quadrillion(50),1.05),
            'pure white chocolate cookies' : Cookie('pure white chocolate cookies',quadrillion(50),1.05),
            'Ladyfingers' : Cookie('Ladyfingers',quadrillion(100),1.03),
            'Tuiles' : Cookie('Tuiles',quadrillion(500),1.03),
            'Chocolate-stuffed biscuits' : Cookie('Chocolate-stuffed biscuits',quintillion(1),1.03),
            'Checker cookies' : Cookie('Checker cookies',quintillion(5),1.03),
            'Butter cookies' : Cookie('Butter cookies',quintillion(10),1.03),
            'Cream cookies' : Cookie('Cream cookies',quintillion(50),1.03),
            'Gingersnaps' : Cookie('Gingersnaps',quintillion(100),1.04),
            'Cinamon cookies' : Cookie('Cinamon cookies',quintillion(500),1.04),
            'Vanity cookies' : Cookie('Vanity cookies',sextillion(1),1.04),
            'Cigars' : Cookie('Cigars',sextillion(5),1.04),
            'Pinwheel cookies' : Cookie('Pinwheel cookies',sextillion(10),1.04),
            'Fudge squares' : Cookie('Fudge squares',sextillion(50),1.04),
            'Shortbread biscuits' : Cookie('Shortbread biscuits',sextillion(100),1.04),
            'Millionaires\' shortbreads' : Cookie('Millionaires\' shortbreads',sextillion(500),1.04),
            'Caramel cookies' : Cookie('Caramel cookies',septillion(1),1.04),
            'Pecan sandies' : Cookie('Pecan sandies',septillion(5),1.04),
            'Moravian spice cookies' : Cookie('Moravian spice cookies',septillion(10),1.04),
            'Anzac biscuits' : Cookie('Anzac biscuits',septillion(50),1.04),
            'Buttercakes' : Cookie('Buttercakes',septillion(100),1.04),
            'Ice cream sandwiches' : Cookie('Ice cream sandwiches',septillion(500),1.04),
            'Pink biscuits' : Cookie('Pink biscuits',octillion(1),1.04),
            'Whole grain cookies' : Cookie('Whole grain cookies',octillion(5),1.04),
            'Candy cookies' : Cookie('Candy cookies',octillion(10),1.04),
            'Big chip cookies' : Cookie('Big chip cookies',octillion(50),1.04),
            'One chip cookies' : Cookie('One chip cookies',octillion(100),1.01),
            'Sprinkles cookies' : Cookie('Sprinkles cookies',octillion(500),1.04),
            'Peanut butter blossoms' : Cookie('Peanut butter blossoms',nonillion(1),1.04),
            'No-bake cookies' : Cookie('No-bake cookies',nonillion(5),1.04),
            'Florentines' : Cookie('Florentines',nonillion(50),1.04),
            'Chocolate crinkles' : Cookie('Chocolate crinkles',nonillion(50),1.04),
            'Maple cookies' : Cookie('Maple cookies',nonillion(100),1.04),
            'Persian rice cookies' : Cookie('Persian rice cookies',nonillion(500),1.04),
            'Norwegian cookies' : Cookie('Norwegian cookies',decillion(1),1.04),
            'Crispy rice cookies' : Cookie('Crispy rice cookies',decillion(5),1.04),
            'Ube cookies' : Cookie('Ube cookies',decillion(10),1.04),
            'Butterscotch cookies' : Cookie('Butterscotch cookies',decillion(50),1.04),
            'Speculaas' : Cookie('Speculaas',decillion(100),1.04),
            'Chocolate oatmeal cookies' : Cookie('Chocolate oatmeal cookies',decillion(500),1.04),
            'Molasses cookies' : Cookie('Molasses cookies',undecillion(1),1.04),
            'Biscotti' : Cookie('Biscotti',undecillion(5),1.04),
            'Waffle cookies' : Cookie('Waffle cookies',undecillion(10),1.04),
            'Custarad creams' : Cookie('Custarad creams',undecillion(50),1.04),
            'Bourbon biscuits' : Cookie('Bourbon biscuits',undecillion(100),1.04),
            'Mini-cookies' : Cookie('Mini-cookies',undecillion(500),1.05),
            'Whoopie pies' : Cookie('Whoopie pies',duodecillion(1),1.05),
            'Caramel wafer biscuits' : Cookie('Caramel wafer biscuits',duodecillion(3.162),1.05),
            'Chocolate chip mocha cookies' : Cookie('Chocolate chip mocha cookies',duodecillion(10),1.05),
            'Earl Grey cookies' : Cookie('Earl Grey cookies',duodecillion(31.622),1.05),
            'Chai tea cookies' : Cookie('Chai tea cookies',duodecillion(31.622),1.05),
            'Corn syrup cookies' : Cookie('Corn syrup cookies',duodecillion(100),1.05),
            'Icebox cookies' : Cookie('Icebox cookies',duodecillion(316.227),1.05),
            'Graham crackers' : Cookie('Graham crackers',tredecillion(1),1.05),
            'Hardtack' : Cookie('Hardtack',tredecillion(3.162),1.05),
            'Cornflake cookies' : Cookie('Cornflake cookies',tredecillion(10),1.05),
            'Tofu cookies' : Cookie('Tofu cookies',tredecillion(31.622),1.05),
            'Gluten-free cookies' : Cookie('Gluten-free cookies',tredecillion(31.622),1.05),
            'Russian bread cookies' : Cookie('Russian bread cookies',tredecillion(100),1.05),
            'Lebkuchen' : Cookie('Lebkuchen',tredecillion(316.227),1.05),
            'Aachener Printen' : Cookie('Aachener Printen',quattuordecillion(1),1.05),
            'Canistrelli' : Cookie('Canistrelli',quattuordecillion(3.162),1.05),
            'Nice biscuits' : Cookie('Nice biscuits',quattuordecillion(10),1.05),
            'French pure butter cookies' : Cookie('French pure butter cookies',quattuordecillion(31.622),1.05),
            'Petit beurre' : Cookie('Petit beurre',quattuordecillion(31.622),1.05),
            'Nanaimo bars' : Cookie('Nanaimo bars',quattuordecillion(100),1.05),
            'Berger cookies' : Cookie('Berger cookies',quattuordecillion(316.227),1.05),
            'Chinsuko' : Cookie('Chinsuko',quindecillion(1),1.05),

            'Birthday cookie' : Cookie('Birthday cookie',octillion(100),1+(gameAge/100)),
            'Milk chocolate butter biscuit' : Cookie('Milk chocolate butter biscuit',octillion(100),1.1,everythingCondition(100)),
            'Dark chocolate butter biscuit' : Cookie('Dark chocolate butter biscuit',nonillion(100),1.1,everythingCondition(150)),
            'White chocolate butter biscuit' : Cookie('White chocolate butter biscuit',decillion(100),1.1,everythingCondition(200)),
            'Ruby chocolate butter biscuit' : Cookie('Ruby chocolate butter biscuit',undecillion(100),1.1,everythingCondition(250)),
            'Lavender chocolate butter biscuit' : Cookie('Lavender chocolate butter biscuit',duodecillion(100),1.1,everythingCondition(300)),
            'Synthetic chocolate green honey butter biscuit' : Cookie('Synthetic chocolate green honey butter biscuit',tredecillion(100),1.1,everythingCondition(350)),
            'Royal raspberry chocolate butter biscuit' : Cookie('Royal raspberry chocolate butter biscuit',quattuordecillion(100),1.1,everythingCondition(400)),
            'Bingo center/Research facility' : DoubleUpgrade('Bingo center/Research facility',quadrillion(1),'Grandma',7,multiplier = 4),
            'Specialized chocolate chips' : Cookie('Specialized chocolate chips',quadrillion(1),1.01, Condition('Bingo center/Research facility')),
            'Designer coco beans' : Cookie('Designer coco beans',quadrillion(2),1.02,Condition('Specialized chocolate chips')),
            'Ritual rolling pins' : DoubleUpgrade('Ritual rolling pins',quadrillion(4),'Grandma', Condition('Designer coco beans')),
            'Underworld ovens' : Cookie('Underworld ovens',quadrillion(8),1.03, Condition('Ritual rolling pins')),
            'One mind' : Brainsweep('One mind',quadrillion(16),0.02,'Grandma','Grandma',Condition('Underworld ovens')),
            'Exotic nuts' : Cookie('Exotic nuts',quadrillion(32),1.04, Condition('One mind')),
            'Communal brainsweep' : Brainsweep('Communal brainsweep',quadrillion(64),0.02,'Grandma','Grandma',Condition('Exotic nuts')),
            'Arcane sugar' : Cookie('Arcane sugar',quadrillion(128),1.05,Condition('Communal brainsweep')),
            'Elder Pact' : Brainsweep('Elder Pact',quadrillion(256),0.05,'Grandma','Portal',Condition('Arcane sugar')),
            'Plastic mouse' : MouseUpgrade('Plastic mouse',50000),
            'Iron mouse' : MouseUpgrade('Iron mouse',million(5)),
            'Titanium mouse' : MouseUpgrade('Titanium mouse',million(500)),
            'Adamantium mouse' : MouseUpgrade('Adamantium mouse',billion(50)),
            'Unobtainium mouse' : MouseUpgrade('Unobtainium mouse',trillion(5)),
            'Eldium mouse' : MouseUpgrade('Eldium mouse',trillion(500)),
            'Wishalloy mouse' : MouseUpgrade('Wishalloy mouse',quadrillion(50)),
            'Fantasteel mouse' : MouseUpgrade('Fantasteel mouse',quintillion(5)),
            'Nevercrack mouse' : MouseUpgrade('Nevercrack mouse',quintillion(500)),
            'Armythril mouse' : MouseUpgrade('Armythril mouse',sextillion(50)),
            'Technobsidian mouse' : MouseUpgrade('Technobsidian mouse',septillion(5)),
            'Plasmarble mouse' : MouseUpgrade('Plasmarble mouse',septillion(500)),
            'Miraculite mouse' : MouseUpgrade('Miraculite mouse',octillion(50)),
            'Aetherice mouse' : MouseUpgrade('Aetherice mouse',nonillion(5)),
            'Heavenly chip secret' : HeavenlyChipUpgrade('Heavenly chip secret',11,0.05),
            'Heavenly cookie stand' : HeavenlyChipUpgrade('Heavenly cookie stand',1111,0.25),
            'Heavenly bakery' : HeavenlyChipUpgrade('Heavenly bakery',111111,0.5),
            'Heavenly confectionery' : HeavenlyChipUpgrade('Heavenly confectionery',million(11.111),0.75),
            'Heavenly key' : HeavenlyChipUpgrade('Heavenly key',billion(1.111),1.0),
            'Cookie crumbs' : Cookie('Cookie crumbs',100,1.01,Condition('Legacy',1)),
            'Chocolate chip cookie' : Cookie('Chocolate chip cookie',trillion(1),1.1,Condition('Legacy',1)),
            'British tea biscuits' : Cookie('British tea biscuits',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Chocolate british tea biscuits' : Cookie('Chocolate british tea biscuits',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Round british tea biscuits' : Cookie('Round british tea biscuits',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Round chocolate british tea biscuits' : Cookie('Round chocolate british tea biscuits',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Round british tea biscuits with heart motif' : Cookie('Round british tea biscuits with heart motif',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Round chocolate british tea biscuits with heart motif' : Cookie('Round chocolate british tea biscuits with heart motif',trillion(100),1.02,Condition('Tin of british tea biscuits')),
            'Caramoas' : Cookie('Caramoas',quadrillion(10),1.03,Condition('Box of brand biscuits')),
            'Sagalongs' : Cookie('Sagalongs',quadrillion(10),1.03,Condition('Box of brand biscuits')),
            'Shortfoils' : Cookie('Shortfoils',quadrillion(10),1.03,Condition('Box of brand biscuits')),
            'Win mints' : Cookie('Win mints',quadrillion(10),1.03,Condition('Box of brand biscuits')),
            'Fig gluttons' : Cookie('Fig gluttons',quadrillion(5),1.02,Condition('Box of brand biscuits')),
            'Loreols' : Cookie('Loreols',quadrillion(5),1.02,Condition('Box of brand biscuits')),
            'Jaffa cakes' : Cookie('Jaffa cakes',quadrillion(5),1.02,Condition('Box of brand biscuits')),
            "Grease's cups" : Cookie("Grease's cups",quadrillion(5),1.02,Condition('Box of brand biscuits')),
            'Digits' : Cookie('Digits',quadrillion(5),1.02,Condition('Box of brand biscuits')),
            'Lombardia cookies' : Cookie('Lombardia cookies',sextillion(5),1.03,Condition('Box of brand biscuits')),
            'Bastenaken cookies' : Cookie('Bastenaken cookies',sextillion(5),1.03,Condition('Box of brand biscuits')),
            'Festivity loops' : Cookie('Festivity loops',septillion(5),1.02,Condition('Box of brand biscuits')),
            'Havabreaks' : Cookie('Havabreaks',octillion(5),1.02,Condition('Box of brand biscuits')),
            'Zilla wafers' : Cookie('Zilla wafers',nonillion(5),1.02,Condition('Box of brand biscuits')),
            'Dim dams' : Cookie('Dim dams',decillion(5),1.02,Condition('Box of brand biscuits')),
            'Pokey' : Cookie('Pokey',decillion(5),1.02,Condition('Box of brand biscuits')),
            'Rose macarons' : Cookie('Rose macarons',9999,1.03,Condition('Box of macarons')),
            'Lemon macarons' : Cookie('Lemon macarons',million(10),1.03,Condition('Box of macarons')),
            'Chocolate macarons' : Cookie('Chocolate macarons',billion(10),1.03,Condition('Box of macarons')),
            'Pistachio macarons' : Cookie('Pistachio macarons',trillion(10),1.03,Condition('Box of macarons')),
            'Hazelnut macarons' : Cookie('Hazelnut macarons',quadrillion(10),1.03,Condition('Box of macarons')),
            'Violet macarons' : Cookie('Violet macarons',quintillion(10),1.03,Condition('Box of macarons')),
            'Caramel macarons' : Cookie('Caramel macarons',sextillion(10),1.03,Condition('Box of macarons')),
            'Licorice macarons' : Cookie('Licorice macarons',septillion(10),1.03,Condition('Box of macarons')),
            'Earl Grey macarons' : Cookie('Earl Grey macarons',octillion(10),1.03,Condition('Box of macarons')),
            'Butter horseshoes' : Cookie('Butter horseshoes',sextillion(100),1.04,Condition('Tin of butter cookies')),
            'Butter pucks' : Cookie('Butter pucks',sextillion(500),1.04,Condition('Tin of butter cookies')),
            'Butter knots' : Cookie('Butter knots',septillion(1),1.04,Condition('Tin of butter cookies')),
            'Butter slabs' : Cookie('Butter slabs',septillion(5),1.04,Condition('Tin of butter cookies')),
            'Butter swirls' : Cookie('Butter swirls',septillion(10),1.04,Condition('Tin of butter cookies'))
        }
        self.heavenlyUpgrades = {   
            'Legacy' : Upgrade('Legacy',Infinity()),
            'Heavenly cookies' : Cookie('Heavenly cookies',Infinity(),1.1),
            'Tin of british tea biscuits' : Upgrade('Tin of british tea biscuits',Infinity()),
            'Box of brand biscuits' : Upgrade('Box of brand biscuits',Infinity()),
            'Box of macarons' : Upgrade('Box of macarons',Infinity()),
            'Tin of butter cookies' : Upgrade('Tin of butter cookies',Infinity()),
            'Heralds' : Cookie('Heralds',Infinity(),heralds/100+1),
            'Starter kit' : Upgrade('Starter kit',Infinity()),
            'Starter kitchen' : Upgrade('Starter kitchen',Infinity()),
            'Synergies Vol. I' : Upgrade('Synergies Vol. I',Infinity()),
            'Synergies Vol. II' : Upgrade('Synergies Vol. II',Infinity())
        }
        self.diamond = None
        self.ruby = None
        self.jade = None
        self.spirits = {

        }

        for name in self.buildings:
            self.buildings[name].setup(self)
        for name in self.upgrades:
            self.upgrades[name].setup(self)
        for name in self.heavenlyUpgrades:
            self.heavenlyUpgrades[name].setup(self)

    def copy(self):
        newGame = Game()
        newGame.hardcore = self.hardcore
        newGame.showAll = self.showAll
        newGame.cpm = self.cpm
        newGame.clickMultiplier = self.clickMultiplier
        newGame.clickCpsMultiplier = self.clickCpsMultiplier
        newGame.clickAddMultiplier = self.clickAddMultiplier
        newGame.cookieMultiplier = self.cookieMultiplier
        newGame.achievements = self.achievements
        newGame.prestige = self.prestige
        newGame.prestigePercentMultiplier = self.prestigePercentMultiplier
        for i in self.kittenMultipliers:
            newGame.kittenMultipliers.append(i)
        for i in self.purchasedUpgrades:
            newGame.purchasedUpgrades.append(i)
        for i in self.buildings:
            newGame.buildings[i] = self.buildings[i].copy()
        for i in self.upgrades:
            newGame.upgrades[i] = self.upgrades[i].copy()
        for name in newGame.buildings:
            newGame.buildings[name].game = newGame
        for name in newGame.buildings:
            newGame.buildings[name].setup()
        for name in newGame.upgrades:
            newGame.upgrades[name].game = newGame
        for name in newGame.upgrades:
            newGame.upgrades[name].setup()
        for name in newGame.heavenlyUpgrades:
            newGame.heavenlyUpgrades[name].game = newGame
        for name in newGame.heavenlyUpgrades:
            newGame.heavenlyUpgrades[name].setup()
        return newGame

    def buy(self,name):
        if name in self.buildings:
            self.buildings[name].buy()
        elif name in self.upgrades:
            self.upgrades[name].buy()
        elif name in self.heavenlyUpgrades:
            self.heavenlyUpgrades[name].buy()
        else:
            print('error (1) name "{}" not a key in building, upgrade, or heavenly upgrade dict'.format(name))
    def sell(self,name):
        if name in self.buildings:
            self.buildings[name].sell()
        elif name in self.upgrades:
            self.upgrades[name].sell()
        elif name in self.heavenlyUpgrades:
            self.heavenlyUpgrades[name].sell()


    def cps(self):
        total = 0
        for i in self.buildings:
            total+=self.buildings[i].production()*self.buildings[i].owned
        return total*self.multiplier()
    
    def multiplier(self):
        kittens = 1
        for i in self.kittenMultipliers:
            kittens*=(i*self.achievements*0.04+1)
        return self.cookieMultiplier * kittens * (self.prestige*self.prestigePercentMultiplier[-1]/100+1)

    def cpsPlusClicks(self):
        return self.cookiesPerClick()*self.cpm/60+self.cps()

    def cookiesPerClick(self):
        totalBuildings = 0
        for i in self.buildings:
            if i!='Cursor':
                totalBuildings+=self.buildings[i].owned
        return 1.0*self.clickMultiplier+self.clickCpsMultiplier*self.cps()+self.clickAddMultiplier*totalBuildings

    def printStatus(self,showAll=False):
        print("cps:",self.cps())
        if self.cpm>0:
            print("cookies per click:",self.cookiesPerClick())
            print("cps+clicks:",self.cpsPlusClicks())
        print("achievements:",self.achievements)
        print("prestige:",self.prestige)
        #print("cps: {}\nachievements: {}/439\nprestige: {}".format(self.cps(),self.achievements,self.prestige))
        if self.cpm>0: print("cps + clicks: {}".format(self.cpsPlusClicks()))
        if showAll:
            print("Cookies per click: {}".format(self.cookiesPerClick()))
            print("building    owned        price        production      pay off time")
            for i in self.buildings:
                print("{}  {}  {}  {}  {}".format(self.buildings[i].name,self.buildings[i].owned,self.buildings[i].price(),self.buildings[i].production()*self.multiplier(),self.buildings[i].payOffTime()[0]))
            print("Purchased upgrades:\n{}".format(self.purchasedUpgrades))
        else:
            for i in self.buildings:
                print("{}[{}]: {}".format(self.buildings[i].name,self.buildings[i].level,self.buildings[i].owned))
        rank = []

    #sort the rankings for best payofftime
    def sortRank(self,rankInput):
        rank = rankInput
        length = len(rank)
        for index in range(length):
            lowest = index
            for x in range(index,length):
                if rank[x][1]<rank[lowest][1]:
                    lowest = x
            swap = rank[index]
            rank[index] = rank[lowest]
            rank[lowest] = swap
        return rank

    def run(self,**kwargs):
        if 'supressPrints' in kwargs:
            supressPrints = kwargs['supressPrints']
        else:
            supressPrints = False
        if not supressPrints:
            self.printStatus(self.showAll)
        rank = []
        for i in self.buildings:
            rank.append((self.buildings[i],self.buildings[i].payOffTime()[0]))
        if(not self.hardcore):
            for i in self.upgrades:
                if self.upgrades[i].avalable():
                    rank.append((self.upgrades[i],self.upgrades[i].payOffTime()[0]))
        rank = self.sortRank(rank)
        #if self.showAll: print(rank)
        rank = rank[:10]
        #options stored in tuple (building/upgrade object,payoff time in seconds)
        if self.showAll:
            for i in rank:
                print(i[0].name)
        best = rank[0]
        for i in range(1,len(rank)):
            if rank[i][1]==Infinity() or self.cpsPlusClicks()==0:
                continue
            if(self.showAll and not supressPrints):
                print("best: {}".format(best[0].name))
                print("time to upgrade: {}s".format(best[0].ttu()))
                print("option: {}".format(rank[i][0]))
                print("payoff time + ttu: {}s".format(rank[i][1]+rank[i][0].ttu()))
                print()
            if(rank[i][0].price()<best[0].price() and rank[i][0].ttu()+rank[i][1]<best[0].ttu()):
                best = rank[i]
        payOffTime,purchasedConditions = best[0].payOffTime()
        if purchasedConditions != []:
            if not supressPrints: print("{} + required {} has best efficency.".format(best[0],purchasedConditions))
            if purchasedConditions[0] in self.buildings:
                best = (self.buildings[purchasedConditions[0]],payOffTime)
            else:
                best = (self.upgrades[purchasedConditions[0]],payOffTime)
        if not supressPrints: print("\n Buy: {}".format(best[0].name))
        if 'inputOverride' in kwargs:
            text = kwargs['inputOverride']
        else:
            text = input()
        if text== "":
            self.buy(best[0].name)
        elif text == "showall":
            self.showAll = not self.showAll
        elif(text=="setall"):
            try:
                for i in self.buildings:
                    self.buildings[i].owned = int(input("{}: ".format(self.buildings[i])))
            except:
                print("error! (6)")
        elif(text[:13]=="achievements "):
            try:
                self.achievements = int(text[13:])
            except:
                print("error! (7)")
        elif(text=="achieve"):
            self.achievements+=1
        elif(text[:8]=="achieve "):
            try: self.achievements+=int(text[8:])
            except: print("error! (11)")
        elif(text[:4] == "cpm "):
            try:    
                self.cpm = int(text[4:])
            except:
                print("cpm change error")
        elif(text[:9]=='prestige '):
            try:
                self.prestige = int(text[9:])
            except:
                print("presitge change error")
        elif(text[:7] == "record "):
            #try:
            limit = int(text[7:])
            rGame = self.copy()
            rGame.record('cookie_buys.csv',limit)
            #except Exception as e:
            #    print("record error: {}".format(e))
        elif(text[:5] == "save "):
            self.save(text[5:])
        elif(text[:5] == "load "):
            self.load(text[5:])
        elif(text[8:] == "level "):
            self.buildings[text[:6]].level+=1
        elif(text=="setlevels"):
            try:
                for i in self.buildings:
                    self.buildings[i].level = int(input("{}: ".format(self.buildings[i])))
            except:
                print("error! (levels)")
        elif(text == 'ascend'):
            self.ascend()
        elif(text[:7] == "ascend "):
            self.ascend(int(text[7:]))
        elif(text[:4] == 'buy '):
            self.buy(text[4:])
        elif(text[:5] == 'sell '):
            self.sell(text[5:])
        elif(text[:8] == 'heralds '):
            global heralds
            heralds = text[8:]
        else:
            print("not a command")
        if not supressPrints: print('\n')
        return best[0].name,best[0].ttu(),self.cps()

    #records the best buys to a file for analysis
    def record(self,fileName,limit):
        with open(fileName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            print('[{}]'.format(' '*PROGRESS_BAR_LENGTH)),
            for i in range(limit):
                result = self.run(supressPrints = True,inputOverride = "")
                writer.writerow(list(result))
                progress = floor(i/limit*PROGRESS_BAR_LENGTH)
                progressString = ':'*progress+(' '*(PROGRESS_BAR_LENGTH-progress))
                print("{}[{}]".format('\b'*(PROGRESS_BAR_LENGTH+2),progressString)),
        print("done")

    def save(self,fileName:str):
        values = {}
        values['hardcore'] = self.hardcore
        values['cpm'] = self.cpm
        values['achievements'] = self.achievements
        values['prestige'] = self.prestige
        for i in self.buildings:
            values[self.buildings[i].name] = self.buildings[i].owned
        for i in self.buildings:
            values[self.buildings[i].name+' level'] = self.buildings[i].level
        for i in self.upgrades:
            values[self.upgrades[i].name] = self.upgrades[i].owned
        for i in self.heavenlyUpgrades:
            values[self.heavenlyUpgrades[i].name] = self.heavenlyUpgrades[i].owned
        lines = []
        for i in values:
                lines.append("{}:{}".format(i,values[i]))
        for i in range(1,len(lines)):
            lines[i] = '\n'+lines[i]
        with open('./'+fileName+'.sav','w') as file:
            file.writelines(lines)
        print("saved {}.sav".format(fileName))

    def load(self,fileName:str):
        self.__init__()
        try:
            values = {}
            with open(fileName+'.sav','r') as file:
                lines = file.readlines()
        except Exception as e:
            print('file read error: {}'.format(e))
        try:
            for line in lines:
                for i in range(len(line)):
                    if line[i] == ':':
                        values[line[:i]] = line[i+1:]
                        break
            self.hardcore = values['hardcore'] == 'True'
            self.cpm = int(values['cpm'])
            self.achievements = int(values['achievements'])
            self.prestige = int(values['prestige'])
            for i in self.buildings:
                self.buildings[i].owned = int(values[i])
            for i in self.buildings:
                self.buildings[i].level = int(values[i+' level'])
            unloaded = []
            for i in self.upgrades:
                if i not in values:
                    unloaded.append(i)
                    continue
                if int(values[i]) == 1:
                    self.upgrades[i].buy()
            for i in self.heavenlyUpgrades:
                if i not in values:
                    unloaded.append(i)
                    continue
                if int(values[i]) == 1:
                    self.heavenlyUpgrades[i].buy()
            for i in unloaded:
                print("value not found: {}".format(i))
            print("loaded {}.sav".format(fileName))
        except Exception as e:
            print("data load error: {}".format(e))

    def ascend(self,addPrestige=0):
        achievements = self.achievements
        prestige = self.prestige
        levels = {}
        for i in self.buildings:
            levels[i] = self.buildings[i].level
        heavenlyUpgrades = []
        for i in self.heavenlyUpgrades:
            if self.heavenlyUpgrades[i].owned == 1:
                heavenlyUpgrades.append(i)
        self.__init__()
        self.achievements = achievements
        self.prestige = prestige+addPrestige
        for i in self.buildings:
            self.buildings[i].level = levels[i]
        for upgrade in heavenlyUpgrades:
            self.heavenlyUpgrades[upgrade].buy()
        if self.heavenlyUpgrades['Starter kit'].owned == 1:
            self.buildings['Cursor'].owned = 10
        if self.heavenlyUpgrades['Starter kitchen'].owned == 1:
            self.buildings['Grandma'].owned = 5





class Buyable:
    def __init__(self,name:str,basePrice:int,conditions = []):
        self.name = name
        self.basePrice = basePrice
        self.owned = 0
        self.game = None
        self.conditions = []
        if type(conditions)==list:
            self.conditions = conditions
        else:
            self.conditions.append(conditions)

    def setup(self,game:Game):
        self.game = game
        for condition in self.conditions:
            if condition.targetName in self.game.buildings:
                condition.target = self.game.buildings[condition.targetName]
            elif condition.targetName in self.game.upgrades:
                condition.target = self.game.upgrades[condition.targetName]
            elif condition.targetName in self.game.heavenlyUpgrades:
                condition.target = self.game.heavenlyUpgrades[condition.targetName]

    def __str__(self):
        return self.name

    def price(self):
        return self.basePrice
    
    def ttu(self):
        if 0 == self.game.cpsPlusClicks():
            return Infinity()
        return self.price()/self.game.cpsPlusClicks()

    def efficency(self):
        return 1.0/self.payOffTime()[0]

    def payOffTime(self):
        conditionsPurchased = []
        totalPrice = 0
        for condition in self.conditions:
            if not condition.met():
                addPrice,newConditionsList=condition.buy()
                totalPrice = addPrice + totalPrice
                conditionsPurchased+=newConditionsList
        totalPrice+=self.price()
        self.game.buy(self.name)
        newCPS = self.game.cpsPlusClicks()
        self.game.sell(self.name)
        for condition in self.conditions:
            condition.sell()
        if newCPS==self.game.cpsPlusClicks() or totalPrice==Infinity():
            return Infinity(),conditionsPurchased
        return totalPrice/(newCPS-self.game.cpsPlusClicks()), conditionsPurchased
    
    def buy(self):
        self.owned+=1

    def sell(self):
        self.owned-=1

    def avalable(self):
        return True

    def copy(self,*args):
        if args == ():
            passArgs = (self.name,self.basePrice)
        else:
            passArgs = args
        newBuyable = type(self)(*passArgs)
        newBuyable.owned = self.owned
        newBuyable.game = self.game
        return newBuyable

class Building(Buyable):
    def __init__(self,name,basePrice,baseProduction):
        Buyable.__init__(self,name,basePrice)
        self.baseProduction = baseProduction
        self.grandmaBonus = 0
        self.multiplier = 1
        self.level = 0
        self.synergies = []

    def price(self):
        return int(ceil(self.basePrice * (1.15 ** (self.owned))))

    def production(self):
        total = self.baseProduction
        total*=self.grandmaBonus*self.game.buildings['Grandma'].owned+1
        total*=self.multiplier
        for synergy in self.synergies:
            total*= synergy.multiplier(self.game)
        total*=self.level/100+1
        return total

    def copy(self,new=None):
        if new == None:
            newBuilding = Building(self.name,self.basePrice,self.baseProduction)
        else:
            newBuilding = new
        newBuilding.owned = self.owned
        newBuilding.multiplier = self.multiplier
        newBuilding.grandmaBonus = self.grandmaBonus
        newBuilding.game = self.game
        return newBuilding
        

class Cursor(Building):
    def __init__(self,name,basePrice,baseProduction):
        Building.__init__(self,name,basePrice,baseProduction)
        self.addBonus = 0

    def production(self,throwAway=True,alsoThrowaway=True):
        totalBuildings = 0
        for i in self.game.buildings:
            if(i!='Cursor'):
                totalBuildings+=self.game.buildings[i].owned
        total = self.baseProduction
        total*=self.multiplier
        total+=self.addBonus*totalBuildings
        for synergy in self.synergies:
            total*= synergy.multiplier(self.game)
        total*=self.level/100+1
        return total


    def copy(self):
        newCursor = Cursor(self.name,self.basePrice,self.baseProduction)
        Building.copy(self,newCursor)
        newCursor.addBonus = self.addBonus
        return newCursor         
    
class Grandma(Building):
    def __init__(self,name,basePrice,baseProduction):
        Building.__init__(self,name,basePrice,baseProduction)
        self.brainSweeps = []

    def production(self):
        total = self.baseProduction
        for i in self.brainSweeps:
            total+=(i[0]*self.game.buildings[i[1]].owned)
        total*=self.grandmaBonus*self.game.buildings['Grandma'].owned+1
        total*=self.multiplier
        for synergy in self.synergies:
            total*= synergy.multiplier(self.game)
        total*=self.level/100+1
        return total

    def copy(self):
        newGrandma = Grandma(self.name,self.basePrice,self.baseProduction)
        Building.copy(self,newGrandma)
        newGrandma.brainSweeps = self.brainSweeps
        return newGrandma
       

class Upgrade(Buyable):
    def avalable(self):
        if(self.owned==0):
            return True
        return False

    def buy(self):
        Buyable.buy(self)
        self.game.purchasedUpgrades.append(self.name)

    def sell(self):
        Buyable.sell(self)
        self.game.purchasedUpgrades.remove(self.name)

    def copy(self):
        newUpgrade = Upgrade(self.name,self.basePrice)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game

class Condition:
    def __init__(self,targetName:str,required:int=1):
        self.targetName = targetName
        self.target = None
        self.required = required
        self.targetsToSell = 0
    
    def met(self):
        return self.target.owned>=self.required

    def buy(self):
        totalCost = 0
        conditionsList = []
        for condition in self.target.conditions:
            cost,newConditions = condition.buy()
            totalCost+=cost
            conditionsList+=newConditions
        if not self.met():
            conditionsList.append(self.targetName)
        while self.target.owned<self.required:
            totalCost=self.target.price()+totalCost
            self.target.buy()
            self.targetsToSell+=1
        return totalCost,conditionsList
    
    def sell(self):
        for condition in self.target.conditions:
            condition.sell()
        while(self.targetsToSell>0):
            self.target.sell()
            self.targetsToSell-=1

def everythingCondition(number:int):
    conditions = []
    for name in buildingsList:
        conditions.append(Condition(name,number))
    return conditions

class DoubleUpgrade(Upgrade):
    def __init__(self,name,price,target,unlockCondition=0,**kwargs):
        if type(unlockCondition) == int:
            Upgrade.__init__(self,name,price,Condition(target,unlockCondition))
        else:
            Upgrade.__init__(self,name,price,unlockCondition)
        self.multiplier = 2
        for kw in kwargs:
            if kw=='multiplier':
                self.multiplier = kwargs[kw]
            else:
                print("DoubleUpgrade kwarg error!")
        self.target = target

    def buy(self):
        Upgrade.buy(self)
        self.game.buildings[self.target].multiplier*=self.multiplier
    
    def sell(self):
        Upgrade.sell(self)
        self.game.buildings[self.target].multiplier/=self.multiplier

    def copy(self):
        newUpgrade = DoubleUpgrade(self.name,self.basePrice,self.target,self.unlockCondition,multiplier = self.multiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class Cookie(Upgrade):
    def __init__(self,name,price,multiplier,conditions = []):
        Upgrade.__init__(self,name,price,conditions)
        self.multiplier = multiplier

    def buy(self):
        Upgrade.buy(self)
        self.game.cookieMultiplier*=self.multiplier

    def sell(self):
        Upgrade.sell(self)
        self.game.cookieMultiplier/=self.multiplier

    def copy(self):
        newUpgrade = Cookie(self.name,self.basePrice,self.multiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class Kitten(Upgrade):
    def __init__(self,name,price,multiplier):
        Upgrade.__init__(self,name,price)
        self.multiplier = multiplier

    def buy(self):
        Upgrade.buy(self)
        self.game.kittenMultipliers.append(self.multiplier)

    #if teh kittens break later this might be why
    def sell(self):
        Upgrade.sell(self)
        self.game.kittenMultipliers.remove(self.multiplier)
    
    def copy(self):
        newUpgrade = Kitten(self.name,self.basePrice,self.multiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade



class GrandmaType(DoubleUpgrade):
    def __init__(self,name,price,enhancedBuilding,ratio,unlockCondition=0):
        DoubleUpgrade.__init__(self,name,price,"Grandma",unlockCondition)
        self.enhancedBuilding = enhancedBuilding
        self.bonusRatio = ratio

    def buy(self):
        DoubleUpgrade.buy(self)
        self.game.buildings[self.enhancedBuilding].grandmaBonus = self.bonusRatio

    def sell(self):
        DoubleUpgrade.sell(self)
        self.game.buildings[self.enhancedBuilding].grandmaBonus = 0

    def avalable(self):
        if(self.game.buildings['Grandma'].owned>0 and self.game.buildings[self.enhancedBuilding].owned>14 and DoubleUpgrade.avalable(self)):
            return True
        return False

    def copy(self):
        newUpgrade = GrandmaType(self.name,self.basePrice,self.enhancedBuilding,self.bonusRatio,self.unlockCondition)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class Brainsweep(Upgrade):
    def __init__(self,name,price,bonus,target,bonusBuilding,condition):
        Upgrade.__init__(self,name,price,condition)
        self.target = target
        self.bonusInsert = (bonus,bonusBuilding)

    def buy(self):
        Upgrade.buy(self)
        self.game.buildings[self.target].brainSweeps.append(self.bonusInsert)

    def sell(self):
        Upgrade.sell(self)
        self.game.buildings[self.target].brainSweeps.remove(self.bonusInsert)

    def copy(self):
        newUpgrade = Brainsweep(self.name,self.price,self.bonusInsert[0],self.target,self.bonusInsert[1])
        newUpgrade.game = self.game
        newUpgrade.owned = self.owned

class CursorDoubleUpgrade(DoubleUpgrade):
    def buy(self):
        DoubleUpgrade.buy(self)
        self.game.clickMultiplier*=2
    
    def sell(self):
        DoubleUpgrade.sell(self)
        self.game.clickMultiplier/=2

    def copy(self):
        newUpgrade = CursorDoubleUpgrade(self.name,self.basePrice,self.target,self.unlockCondition,multiplier = self.multiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class ThousandFingers(Upgrade):
    def buy(self):
        Upgrade.buy(self)
        self.game.buildings['Cursor'].addBonus+=0.1
        self.game.clickAddMultiplier+=0.1

    def sell(self):
        Upgrade.sell(self)
        self.game.buildings['Cursor'].addBonus-=0.1
        self.game.clickAddMultiplier-=0.1

    
    def copy(self):
        newUpgrade = ThousandFingers(self.name,self.basePrice,self.unlockCondition)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class CursorUpgrade(Upgrade):
    def __init__(self,name,basePrice,addBonus,unlockCondition=0):
        Upgrade.__init__(self,name,basePrice,Condition('Cursor',unlockCondition))
        self.addBonus = addBonus
        self.unlockCondition = unlockCondition

    def buy(self):
        Upgrade.buy(self)
        self.game.buildings['Cursor'].addBonus*=self.addBonus
        self.game.clickAddMultiplier*=self.addBonus

    def sell(self):
        Upgrade.sell(self)
        self.game.buildings['Cursor'].addBonus/=self.addBonus
        self.game.clickAddMultiplier/=self.addBonus

    def copy(self):
        newUpgrade = CursorUpgrade(self.name,self.basePrice,self.addBonus,self.unlockCondition)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class MouseUpgrade(Upgrade):
    def __init__(self,name,basePrice,multiplier = 0.01):
        Upgrade.__init__(self,name,basePrice)
        self.multiplier = multiplier

    def buy(self):
        self.game.clickCpsMultiplier+=self.multiplier

    def sell(self):
        self.game.clickCpsMultiplier-+self.multiplier

    def copy(self):
        newUpgrade = MouseUpgrade(self.name,self.basePrice,self.multiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class HeavenlyChipUpgrade(Upgrade):
    def __init__(self,name,basePrice,percentMultiplier):
        Upgrade.__init__(self,name,basePrice)
        self.percentMultiplier = percentMultiplier

    def buy(self):
        Upgrade.buy(self)
        self.game.prestigePercentMultiplier.append(self.percentMultiplier)

    def sell(self):
        Upgrade.sell(self)
        self.game.prestigePercentMultiplier.remove(self.percentMultiplier)
    
    def copy(self):
        newUpgrade = HeavenlyChipUpgrade(self.name,self.basePrice,self.percentMultiplier)
        newUpgrade.owned = self.owned
        newUpgrade.game = self.game
        return newUpgrade

class SynergyUpgrade(Upgrade):
    def __init__(self,name:str,price:float,target1:str,target2:str,bonus1:float,bonus2:float,conditions = []):
        Upgrade.__init__(self,name,price,conditions)
        self.target1 = target1
        self.target2 = target2
        self.synergy1 = Synergy(target2,bonus1)
        self.synergy2 = Synergy(target1,bonus2)

    def buy(self):
        Upgrade.buy(self)
        self.game.buildings[self.target1].synergies.append(self.synergy1)
        self.game.buildings[self.target2].synergies.append(self.synergy2)

    def sell(self):
        Upgrade.sell(self)
        self.game.buildings[self.target1].synergies.remove(self.synergy1)
        self.game.buildings[self.target2].synergies.remove(self.synergy2)


class Synergy:
    def __init__(self,target:str,bonus:int):

        self.target = target
        self.bonus = bonus

    def multiplier(self,game):
        return self.bonus**game.buildings[self.target].owned

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

#checkSynergies()
#testGame = Game()
#testGame.record('./cookie_buys.csv',3000)
mainGame = Game()
while True:
    mainGame.run()
