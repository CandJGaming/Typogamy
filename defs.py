
# Definitions for all map areas, map data #
class MapDefs:
	global areas
	
	areas = {
		"old town" : {
			"rooms" : [ 5, 7 ],
			"enemies" : [ "goblin", "slime", "rat" ],
			"loot" : [ "potion", "potion", "rope", "homestone", "old note one", "old note two", "old note three" ],
			"song" : 'Song0.wav',
			"boss" :  "troll",
			"levels" : [ 0 , 5 ]
		},
		"Cabin" : {
			"rooms" : [0, 0],
			"enemies" : None,
			"loot" : ["cabin note"],
			"song" : 'Song3.wav',
			"boss" : None,
			"levels" : [ 0 , 0 ]
		},
		"Crud town" : {
			"rooms" : [0, 0],
			"enemies" : None,
			"loot" : [ "junk", "junk", "potion", "potion", "rope", "rope", "town note one", "town note two" ],
			"song" : 'Song4.wav',
			"boss" : None,
			"levels" : [ 0, 0 ]
		},
		"abandoned lighthouse" : {
			"rooms" : [8, 10],
			"enemies" : [ "skeleton", "necromancer", "guard dog" ],
			"loot" : [ "junk", "junk", "rope", "junk", "junk", "potion", "potion", "homestone" ],
			"song" : 'Song5.wav',
			"boss" : "kraken eggs",
			"levels" : [ 5 , 10 ]
		},
		"junk town" : {
			"rooms" : [ 10, 14 ],
			"enemies" : [ "rogue", "fallen knight", "caster" ],
			"loot" : [ "junk", "junk", "junk", "junk", "junk", "potion", "potion" ],
			"song" : 'Song9.wav',
			"boss" : "lieutenant constantine",
			"levels" : [ 10 , 15 ]
		},
		"mausoleum" : {
			"rooms" : [ 5, 7 ],
			"enemies" : [ "vampire", "ork", "werewolf"],
			"loot" : [ "junk", "junk", "rope", "rope", "homestone", "potion", "potion" ],
			"song" : 'Song7.wav',
			"boss" : "captain bork",
			"levels" : [ 15 , 20 ]
		},
		"garrison" : {
			"rooms" : [ 12, 18 ],
			"enemies" : [ "spearman", "guard", "battle mage" ],
			"loot" : [ "junk", "junk", "junk", "junk", "junk", "junk", "junk", "junk", "crystal", "potion"  ],
			"song" : 'Song8.wav',
			"boss" : "commander zap",
			"levels" : [ 20 , 25 ]
		},
		"eerie cave" : {
			"rooms" : [ 20, 30 ],
			"enemies" : [ "baby dragon", "blind salamander", "giant bat" ],
			"loot" : [ "junk", "junk", "junk", "potion", "rope", "homestone", "junk", "junk", "onyx" ],
			"song" : 'Song6.wav',
			"boss" : "dragonkin soldier",
			"levels" : [ 25, 30 ]
		},
		"land of the dead" : {
			"rooms" : [ 40, 50 ],
			"enemies" : [ "imperfect lich", "skeleton warrior", "zombie" ],
			"loot" : [ "junk", "junk", "junk", "junk", "junk", "junk", "junk", "junk", "junk", "homestone", "potion", "diamond" ],
			"song" : 'Song11.wav',
			"boss" : "lich king",
			"levels" : [ 30, 35 ]
		},
		"lost swamp" : {
			"rooms" : [ 75, 100 ],
			"enemies" : ["zealot", "elite soldier", "shaman"],
			"loot" : [ "junk", "junk", "potion", "potion", "diamond", "homestone", "rope", "potion", "diamond", "potion", "potion", "rope" ],
			"song" : 'Song12.wav',
			"boss" : "ascended emperor",
			"levels" : [ 35, 40 ]
		}
	}
	
	def __init__(self):
		self.areas = areas

class npcAbilityDefs:
	global enemyAbility
	enemyAbility = {
		"attack" : {
			"dmgType" : "physical",
			"scale" : 0,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"bite" : {
			"dmgType" : "physical",
			"scale" : 0,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : True
		},
		"curse" : {
			"dmgType" : "magic",
			"scale" : 0,
			"crit" : 0,
			"status" : [2,2],
			"statChance" : 40,
			"life-steal" : 10,
			"omni" : True
		},
		"leech" : {
			"dmgType" : "physical",
			"scale" : 25,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 25,
			"omni" : True
		},
		"tentacle slap" : {
			"dmgType" : "physical",
			"scale" : 50,
			"crit" : 20,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 25,
			"omni" : False
		},
		"poison" : {
			"dmgType" : "physical",
			"scale" : 0,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : True
		},
		"throwing knife" : {
			"dmgType" : "physical",
			"scale" : 25,
			"crit" : 40,
			"status" : [2,0],
			"statChance" : 30,
			"life-steal" : 0,
			"omni" : False
		},
		"charge" : {
			"dmgType" : "physical",
			"scale" : 50,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"recover" : {
			"dmgType" : "heal",
			"scale" : 0,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : True
		},
		"darkness" : {
			"dmgType" : "magic",
			"scale" : 30,
			"crit" : 0,
			"status" : [3,0],
			"statChance" : 60,
			"life-steal" : 30,
			"omni" : True
		},
		"vampire claws" : {
			"dmgType" : "physical",
			"scale" : 30,
			"crit" : 0,
			"status" : [3,0],
			"statChance" : 60,
			"life-steal" : 30,
			"omni" : True
		},
		"rend" : {
			"dmgType" : "physical",
			"scale" : 40,
			"crit" : 30,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"poke" : {
			"dmgType" : "physical",
			"scale" : -25,
			"crit" : 100,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"lunge" : {
			"dmgType" : "physical",
			"scale" : 25,
			"crit" : 25,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"fireball" : {
			"dmgType" : "magic",
			"scale" : 25,
			"crit" : 0,
			"status" : [0,3],
			"statChance" : 50,
			"life-steal" : 0,
			"omni" : False
		},
		"rock throw" : {
			"dmgType" : "physical",
			"scale" : 25,
			"crit" : 10,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"ice spear" : {
			"dmgType" : "physical",
			"scale" : 10,
			"crit" : 25,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"lightning bolt" : {
			"dmgType" : "magic",
			"scale" : 35,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"dragon breath" : {
			"dmgType" : "magic",
			"scale" : 50,
			"crit" : 0,
			"status" : [3,3],
			"statChance" : 50,
			"life-steal" : 0,
			"omni" : True
		},
		"scorch" : {
			"dmgType" : "magic",
			"scale" : 25,
			"crit" : 25,
			"status" : [0,1],
			"statChance" : 100,
			"life-steal" : 0,
			"omni" : False
		},
		"soul drain" : {
			"dmgType" : "magic",
			"scale" : 25,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 75,
			"omni" : False
		},
		"dark blast" : {
			"dmgType" : "magic",
			"scale" : 25,
			"crit" : 25,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 25,
			"omni" : False
		},
		"kick" : {
			"dmgType" : "physical",
			"scale" : 100,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		},
		"shield bash" : {
			"dmgType" : "physical",
			"scale" : 50,
			"crit" : 10,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"omni" : False
		}
		
	}
	
	def __init__(self):
		self.enemyAbility = enemyAbility
class npcBuff:
	global npcBuffs
	npcBuffs = {
		"" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"xp" : 0,
			"scaling" : [0, 0, 0, 0, 0, 0],
			"abilities" : []
		},
		"berserk" : {
			"meleeAtk" : 5,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 1,
			"life" : 1,
			"xp" : 3,
			"scaling" : [2, 0, 1, 1, 1, 3],
			"abilities" : ["attack", "attack"]
		},
		"rabid" : {
			"meleeAtk" : 50,
			"mageAtk" : 50,
			"meleeDef" : 50,
			"mageDef" : 50,
			"life" : 25,
			"xp" : 25,
			"scaling" : [0, 0, 0, 0, 0, 2],
			"abilities" : ["attack", "attack"]
		},
		"divine" : {
			"meleeAtk" : 10,
			"mageAtk" : 10,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 4,
			"xp" : 5,
			"scaling" : [5, 5, 0, 0, 2, 3],
			"abilities" : ["attack", "recover"]
		},
		"profane" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 10,
			"life" : 15,
			"xp" : 5,
			"scaling" : [0, 0, 5, 5, 5, 3],
			"abilities" : ["dark blast"]
		},
		"corrupted" : {
			"meleeAtk" : 0,
			"mageAtk" : 3,
			"meleeDef" : 0,
			"mageDef" : 3,
			"life" : 1,
			"xp" : 2,
			"scaling" : [0, 3, 0, 3, 1, 2],
			"abilities" : ["poison", "darkness"]
		},
		"fiery" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 3,
			"life" : 1,
			"xp" : 2,
			"scaling" : [0, 4, 0, 3, 2, 2],
			"abilities" : ["fireball"]
		},
		"icy" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 3,
			"mageDef" : 0,
			"life" : 2,
			"xp" : 2,
			"scaling" : [0, 3, 3, 0, 3, 2],
			"abilities" : ["ice spear"]
		},
		"electric" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 1,
			"xp" : 1,
			"scaling" : [0, 3, 2, 2, 2, 2],
			"abilities" : ["lightning bolt"]
		},
		"dirty" : {
			"meleeAtk" : 3,
			"mageAtk" : 3,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 15,
			"xp" : 3,
			"scaling" : [3, 3, 3, 3, 3, 3],
			"abilities" : ["attack","poison"]
		},
		"educated" : {
			"meleeAtk" : 0,
			"mageAtk" : 10,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"xp" : 5,
			"scaling" : [0, 10, 0, 0, 0, 5],
			"abilities" : ["fireball", "lightning bolt", "rock throw", "ice spear"]
		},
		"poisonous" : {
			"meleeAtk" : 4,
			"mageAtk" : 4,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 5,
			"xp" : 2,
			"scaling" : [4, 4, 0, 0, 0, 1],
			"abilities" : ["poison", "poison"]
		},
		"spiteful" : {
			"meleeAtk" : 10,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"xp" : 5,
			"scaling" : [10, 0, 0, 0, 0, 5],
			"abilities" : ["charge"]
		},
		"juggernaut" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 15,
			"mageDef" : 15,
			"life" : 15,
			"xp" : 10,
			"scaling" : [0, 0, 15, 15, 15, 10],
			"abilities" : ["attack", "attack"]
		},
		"plagued" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 4,
			"mageDef" : 4,
			"life" : 15,
			"xp" : 3,
			"scaling" : [0, 0, 4, 4, 4, 3],
			"abilities" : ["attack", "poison"]
		},
		"treasure" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 100,
			"xp" : 50,
			"scaling" : [0, 0, 1, 1, 20, 15],
			"abilities" : ["attack", "attack"]
		},
		"mystical" : {
			"meleeAtk" : 0,
			"mageAtk" : 4,
			"meleeDef" : 4,
			"mageDef" : 4,
			"life" : 1,
			"xp" : 3,
			"scaling" : [0, 4, 4, 4, 1, 3],
			"abilities" : ["leech"]
		},
		"armored" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 50,
			"mageDef" : 0,
			"life" : 1,
			"xp" : 5,
			"scaling" : [0, 0, 10, 0, 2, 5],
			"abilities" : ["attack"]
		},
		"warded" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 50,
			"life" : 1,
			"xp" : 5,
			"scaling" : [0, 0, 0, 10, 2, 5],
			"abilities" : ["attack"]
		}
	}
	
	def __init__(self):
		self.npcBuffs = npcBuffs
## Definitions for all abilities
class AbilityDefs:
	global ability
	ability = {
		"accurate swing" : {
			"dmgType" : "physical",
			"scale" : 0,
			"manaCost" : 2,
			"crit" : 25,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0,
			"combatOnly" : True
		},
		"magic dart" : {
			"dmgType" : "magic",
			"scale" : 0,
			"manaCost" : 1,
			"crit" : 0,
			"status" : [2,2],
			"statChance" : 5,
			"life-steal" : 0, 
			"combatOnly" : True
		},
		"cure poison" : {#level 5
			"dmgType" : None,
			"scale" : 0,
			"manaCost" : 10,
			"crit" : 0,
			"status" : [-10,0],
			"statChance" : 100,
			"life-steal" : 0, 
			"combatOnly" : False
		},
		"drench" : {#level 5
			"dmgType" : None,
			"scale" : 0,
			"manaCost" : 10,
			"crit" : 0,
			"status" : [0,-5],
			"statChance" : 100,
			"life-steal" : 0,
			"combatOnly" : False 
		},
		"powerful swing" : {#level 10 with accurate swing
			"dmgType" : "physical",
			"scale" : 15,
			"manaCost" : 25,
			"crit" : 10,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0, 
			"combatOnly" : True
		},
		"fire ball" : {#level 10 with magic dart
			"dmgType" : "magic",
			"scale" : 20,
			"manaCost" : 30,
			"crit" : 5,
			"status" : [0,2],
			"statChance" : 40,
			"life-steal" : 0, 
			"combatOnly" : True
		},
		"troll skin" : {#troll
			"dmgType" : None,
			"scale" : 5,
			"manaCost" : 100,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0, 
			"combatOnly" : True
		},
		"minor heal" : {#level 20 with magic dart
			"dmgType" : "heal",
			"scale" : .25,
			"manaCost" : 35,
			"crit" : 0,
			"status" : [0,0],
			"statChance" : 0,
			"life-steal" : 0, 
			"combatOnly" : True
		},
		#every 10 levels do magic or melee spell, 5 do neutral spells, spell for each boss
	}
	
	def __init__(self):
		self.ability = ability
## Definitions for all enemies #
class EnemyDefs: 
	global enemy
	enemy = {
	
		"goblin" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 2,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 7,
			"xp" : 3,
			"drop" : "tier 1",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack"],
			"scaling" : [1,0,.5,.5,1,.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"slime" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 1,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 10,
			"xp" : 3,
			"drop" : "tier 1",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 10,
			"abilities" : ["attack"],
			"scaling" : [.5,0,.5,.5,1.5,.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"rat" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 1,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 1,
			"life" : 7,
			"xp" : 3,
			"drop" : "tier 1",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack"],
			"scaling" : [1,0,1,.5,.5,.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"troll" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 6,
			"mageAtk" : 0,
			"meleeDef" : 7,
			"mageDef" : 7,
			"life" : 20,
			"xp" : 15,
			"drop" : "tier 1",
			"crit" : 20,
			"status" : [4,0],
			"chance" : 20, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack"],
			"scaling" : [2,0,1,1,2,2] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"guard dog" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 4,
			"mageAtk" : 0,
			"meleeDef" : 4,
			"mageDef" : 4,
			"life" : 12,
			"xp" : 7,
			"drop" : "tier 2",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "bite"],
			"scaling" : [1.5,0,1.25,1.25,1,1] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"skeleton" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 8,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 15,
			"xp" : 7,
			"drop" : "tier 2",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "curse"],
			"scaling" : [2,0,1,1,1,1] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"necromancer" : { #tier 1 is 3 points of scaling
			"meleeAtk" : 2,
			"mageAtk" : 10,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 12,
			"xp" : 7,
			"drop" : "tier 2",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "leech", "leech", "leech"],
			"scaling" : [1,2,1,1,2,1] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"kraken eggs" : { #tier 2 is 6 points of scaling
			"meleeAtk" : 15,
			"mageAtk" : 15,
			"meleeDef" : 15,
			"mageDef" : 15,
			"life" : 40,
			"xp" : 35,
			"drop" : "tier 2",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "tentacle slap"],
			"scaling" : [2,2,2,2,2,3] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"rogue" : { #tier 3 is 9 points of scaling
			"meleeAtk" : 10,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 5,
			"life" : 20,
			"xp" : 10,
			"drop" : "tier 3",
			"crit" : 30,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "poison", "throwing knife"],
			"scaling" : [3,0,2,2,2,1.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"caster" : { #tier 3 is 9 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 10,
			"meleeDef" : 5,
			"mageDef" : 5,
			"life" : 20,
			"xp" : 10,
			"drop" : "tier 3",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 15,
			"abilities" : ["attack", "poison", "fireball"],
			"scaling" : [3,0,2,2,2,1.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"fallen knight" : { #tier 3 is 9 points of scaling
			"meleeAtk" : 7,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 10,
			"life" : 25,
			"xp" : 10,
			"drop" : "tier 3",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 5,
			"abilities" : ["attack", "poison", "throwing knife"],
			"scaling" : [1,0,2.5,2.5,3,1.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"lieutenant constantine" : { #tier 3 is 9 points of scaling
			"meleeAtk" : 15,
			"mageAtk" : 0,
			"meleeDef" : 20,
			"mageDef" : 20,
			"life" : 60,
			"xp" : 60,
			"drop" : "tier 3",
			"crit" : 15,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 25,
			"abilities" : ["attack", "charge", "recover"],
			"scaling" : [3,0,4,4,5,3] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"captain bork" : { #tier 4 is 12 points of scaling
			"meleeAtk" : 30,
			"mageAtk" : 0,
			"meleeDef" : 30,
			"mageDef" : 30,
			"life" : 75,
			"xp" : 100,
			"drop" : "tier 4",
			"crit" : 20,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 20,
			"abilities" : ["attack", "double hit"],
			"scaling" : [6,0,6,6,6,4] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"ork" : { #tier 4 is 12 points of scaling
			"meleeAtk" : 15,
			"mageAtk" : 0,
			"meleeDef" : 15,
			"mageDef" : 15,
			"life" : 35,
			"xp" : 20,
			"drop" : "tier 4",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 10,
			"abilities" : ["attack", "charge", "recover"],
			"scaling" : [3,0,3,3,3,2] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"vampire" : { #tier 4 is 12 points of scaling
			"meleeAtk" : 10,
			"mageAtk" : 10,
			"meleeDef" : 10,
			"mageDef" : 15,
			"life" : 25,
			"xp" : 20,
			"drop" : "tier 4",
			"crit" : 10,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 10,
			"abilities" : ["vampire claws", "vampire claws", "darkness"],
			"scaling" : [2,2,1,3,4,2] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"werewolf" : { #tier 4 is 12 points of scaling
			"meleeAtk" : 25,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 10,
			"life" : 25,
			"xp" : 20,
			"drop" : "tier 4",
			"crit" : 20,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 10,
			"abilities" : ["attack", "rend"],
			"scaling" : [6,0,2,2,2,2] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"spearman" : { #tier 5 is 15 points of scaling
			"meleeAtk" : 25,
			"mageAtk" : 0,
			"meleeDef" : 25,
			"mageDef" : 25,
			"life" : 50,
			"xp" : 40,
			"drop" : "tier 5",
			"crit" : 15,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 10,
			"abilities" : ["attack", "poke", "lunge"],
			"scaling" : [3,0,4,4,4,2.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"guard" : { #tier 5 is 15 points of scaling
			"meleeAtk" : 15,
			"mageAtk" : 0,
			"meleeDef" : 30,
			"mageDef" : 30,
			"life" : 60,
			"xp" : 40,
			"drop" : "tier 5",
			"crit" : 0,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 25,
			"abilities" : ["attack", "shield bash", "recover"],
			"scaling" : [1,0,4,4,6,2.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"battle mage" : { #tier 5 is 15 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 40,
			"meleeDef" : 15,
			"mageDef" : 20,
			"life" : 40,
			"xp" : 40,
			"drop" : "tier 5",
			"crit" : 25,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 10, #stun chance
			"block" : 0,
			"abilities" : ["fireball", "ice spear", "lightning bolt", "rock throw"],
			"scaling" : [0,9,2,2,2,2.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"commander zap" : { #tier 5 is 15 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 80,
			"meleeDef" : 30,
			"mageDef" : 40,
			"life" : 100,
			"xp" : 120,
			"drop" : "tier 5",
			"crit" : 50,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 20, #stun chance
			"block" : 0,
			"abilities" : ["lightning bolt", "lightning orb", "electrocute"],
			"scaling" : [0,18,4,4,4,5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"giant bat" : { #tier 6 is 18 points of scaling
			"meleeAtk" : 40,
			"mageAtk" : 40,
			"meleeDef" : 30,
			"mageDef" : 30,
			"life" : 60,
			"xp" : 60,
			"drop" : "tier 6",
			"crit" : 0,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 30,
			"abilities" : ["leech", "bite"],
			"scaling" : [5,5,2,2,4,3] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"baby dragon" : { #tier 6 is 18 points of scaling
			"meleeAtk" : 40,
			"mageAtk" : 0,
			"meleeDef" : 50,
			"mageDef" : 50,
			"life" : 90,
			"xp" : 60,
			"drop" : "tier 6",
			"crit" : 15,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 15,
			"abilities" : ["attack", "bite", "dragon breath"],
			"scaling" : [4,0,4,4,6,3] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"blind salamander" : { #tier 6 is 18 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 80,
			"meleeDef" : 30,
			"mageDef" : 30,
			"life" : 90,
			"xp" : 60,
			"drop" : "tier 6",
			"crit" : 0,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 0,
			"abilities" : ["scorch", "fireball"],
			"scaling" : [0,10,2,2,4,3] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"dragonkin soldier" : { #tier 6 is 18 points of scaling
			"meleeAtk" : 80,
			"mageAtk" : 80,
			"meleeDef" : 60,
			"mageDef" : 60,
			"life" : 200,
			"xp" : 240,
			"drop" : "tier 6",
			"crit" : 15,
			"status" : [0,5],
			"chance" : 30, #status chance
			"stun" : 15, #stun chance
			"block" : 30,
			"abilities" : ["dragon breath", "bite", "lunge", "poke"],
			"scaling" : [10,10,4,4,8,6] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"zombie" : { #tier 7 is 21 points of scaling
			"meleeAtk" : 40,
			"mageAtk" : 0,
			"meleeDef" : 80,
			"mageDef" : 80,
			"life" : 150,
			"xp" : 90,
			"drop" : "tier 7",
			"crit" : 10,
			"status" : [2,0],
			"chance" : 100, #status chance
			"stun" : 0, #stun chance
			"block" : 25,
			"abilities" : ["attack"],
			"scaling" : [5,0,5,5,6,3.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"skeleton warrior" : { #tier 7 is 21 points of scaling
			"meleeAtk" : 80,
			"mageAtk" : 0,
			"meleeDef" : 60,
			"mageDef" : 60,
			"life" : 110,
			"xp" : 90,
			"drop" : "tier 7",
			"crit" : 20,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 15,
			"abilities" : ["attack", "attack", "recover"],
			"scaling" : [9,0,4,4,4,3.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"imperfect lich" : { #tier 7 is 21 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 80,
			"meleeDef" : 80,
			"mageDef" : 80,
			"life" : 110,
			"xp" : 100,
			"drop" : "tier 7",
			"crit" : 35,
			"status" : [1,1],
			"chance" : 50, #status chance
			"stun" : 0, #stun chance
			"block" : 0,
			"abilities" : ["soul drain", "curse", "dark blast" ],
			"scaling" : [0,5,6,6,4,3.5] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"lich king" : { #tier 7 is 21 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 160,
			"meleeDef" : 160,
			"mageDef" : 160,
			"life" : 350,
			"xp" : 320,
			"drop" : "tier 7",
			"crit" : 0,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 40, #stun chance
			"block" : 40,
			"abilities" : ["attack", "bite", "dragon breath"],
			"scaling" : [10,0,10,10,12,7] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"zealot" : { #tier 8 is 24 points of scaling
			"meleeAtk" : 200,
			"mageAtk" : 0,
			"meleeDef" : 50,
			"mageDef" : 50,
			"life" : 150,
			"xp" : 150,
			"drop" : "tier 7",
			"crit" : 40,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 0,
			"abilities" : ["attack", "kick"],
			"scaling" : [12,0,4,4,4,4] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"elite soldier" : { #tier 8 is 24 points of scaling
			"meleeAtk" : 100,
			"mageAtk" : 0,
			"meleeDef" : 100,
			"mageDef" : 100,
			"life" : 200,
			"xp" : 150,
			"drop" : "tier 7",
			"crit" : 0,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 40,
			"abilities" : ["attack", "shield bash", "attack", "recover"],
			"scaling" : [6,0,6,6,6,4] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"shaman" : { #tier 8 is 24 points of scaling
			"meleeAtk" : 0,
			"mageAtk" : 200,
			"meleeDef" : 50,
			"mageDef" : 50,
			"life" : 150,
			"xp" : 150,
			"drop" : "tier 7",
			"crit" : 40,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 0,
			"abilities" : ["leech", "curse", "fireball", "recover"],
			"scaling" : [0,8,4,4,8,4] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		},
		
		"ascended emperor" : { #tier 8 is 24 points of scaling
			"meleeAtk" : 200,
			"mageAtk" : 200,
			"meleeDef" : 200,
			"mageDef" : 200,
			"life" : 500,
			"xp" : 500,
			"drop" : "tier 7",
			"crit" : 40,
			"status" : [0,0],
			"chance" : 0, #status chance
			"stun" : 0, #stun chance
			"block" : 40,
			"abilities" : ["attack", "kick", "dark blast", "soul drain"],
			"scaling" : [10,10,15,15,24,20] #[0] : "meleeAtk", [1] : "mage Atk", [2] : "meleeDef", [3] : "mageDef", [4] : "life", [5] : "xp"
		}
		
	}

	def __init__(self):
		self.enemy = enemy

class ItemBuffDefs:
	global prefix, suffix
	
	prefix = {
		"" : {
			"scaling" : [0,0,0,0,0],
			"material" : "all",
			"fragile" : False
		},
		
		"cotton" : {
			"scaling" : [.6,.6,.6,.6,.6],
			"material" : "cloth",
			"fragile" : False
		},
		
		"jute" : {
			"scaling" : [0,0,1,2,0],
			"material" : "cloth",
			"fragile" : False
		},
		
		"canvas" : {
			"scaling" : [0,0,2,0,1],
			"material" : "cloth",
			"fragile" : False
		},
		
		"linen" : {
			"scaling" : [1,0,0,1,1],
			"material" : "cloth",
			"fragile" : False
		},
		
		"tweed" : {
			"scaling" : [0,0,1,2,0],
			"material" : "cloth",
			"fragile" : False
		},
		
		"silk" : {
			"scaling" : [0,1,1,1,0],
			"material" : "cloth",
			"fragile" : False
		},
		
		"suede" : {
			"scaling" : [0,0,1,1,1],
			"material" : "leather",
			"fragile" : False
		},
		
		"cured" : {
			"scaling" : [1,0,1,1,0],
			"material" : "leather",
			"fragile" : False
		},
		
		"studded" : {
			"scaling" : [0,0,3,0,0],
			"material" : "leather",
			"fragile" : False
		},
		
		"boiled" : {
			"scaling" : [0,0,2,1,0],
			"material" : "leather",
			"fragile" : False
		},
		
		"snake" : {
			"scaling" : [0,1.5,.75,.75,0],
			"material" : "leather",
			"fragile" : False
		},
		
		"rawhide" : {
			"scaling" : [0,0,1.5,1.5,0],
			"material" : "leather",
			"fragile" : False
		},
		
		"rusty" : {
			"scaling" : [9,0,0,0,0],
			"material" : "metal",
			"fragile" : True
		},
		
		"iron" : {
			"scaling" : [1.5,0,1.5,0,0],
			"material" : "metal",
			"fragile" : False
		},
		
		"steel" : {
			"scaling" : [2,0,1,0,0],
			"material" : "metal",
			"fragile" : False
		},
		
		"mithril" : {
			"scaling" : [0,0,2,1,0],
			"material" : "metal",
			"fragile" : False
		},
		
		"silver" : {
			"scaling" : [0,2,0,1,0],
			"material" : "metal",
			"fragile" : False
		},
		
		"gold" : {
			"scaling" : [0,0,0,0,3],
			"material" : "metal",
			"fragile" : False
		},
		
		"diamond" : {
			"scaling" : [0,0,3,0,0],
			"material" : "gemstone",
			"fragile" : False
		},
		
		"onyx" : {
			"scaling" : [0,2,0,1,0],
			"material" : "gemstone",
			"fragile" : False
		},
		
		"sapphire" : {
			"scaling" : [0,3,0,0,0],
			"material" : "gemstone",
			"fragile" : False
		},
		
		"emerald" : {
			"scaling" : [0,0,.75,.75,1.5],
			"material" : "gemstone",
			"fragile" : False
		},
		
		"ruby" : {
			"scaling" : [3,0,0,0,0],
			"material" : "gemstone",
			"fragile" : False
		},
		
		"pearl" : {
			"scaling" : [3,3,0,0,3],
			"material" : "gemstone",
			"fragile" : True
		},
		
		"oak" : {
			"scaling" : [1,0,1,1,0],
			"material" : "wood",
			"fragile" : False
		},
		
		"mahogany" : {
			"scaling" : [.6,.6,.6,.6,.6],
			"material" : "wood",
			"fragile" : False
		},
		
		"hickory" : {
			"scaling" : [0,0,2,1,0],
			"material" : "wood",
			"fragile" : False
		},
		
		"elderwood" : {
			"scaling" : [0,3,0,0,0],
			"material" : "wood",
			"fragile" : False
		},
		
		"heartwood" : {
			"scaling" : [0,0,0,0,3],
			"material" : "wood",
			"fragile" : False
		},
		
		"ebony" : {
			"scaling" : [0,0,1.5,1.5,0],
			"material" : "wood",
			"fragile" : False
		},
		
		"wolf" : {
			"scaling" : [1,0,.5,.5,1],
			"material" : "depiction",
			"fragile" : False
		},
		
		"ram" : {
			"scaling" : [0,0,3,0,0],
			"material" : "depiction",
			"fragile" : False
		},
		
		"lion" : {
			"scaling" : [3,0,0,0,0],
			"material" : "depiction",
			"fragile" : False
		},
		
		"owl" : {
			"scaling" : [0,1.5,0,1.5,0],
			"material" : "depiction",
			"fragile" : False
		},
		
		"demon" : {
			"scaling" : [0,3,0,0,0],
			"material" : "depiction",
			"fragile" : False
		},
		
		"bear" : {
			"scaling" : [1.5,0,1.5,0,0],
			"material" : "depiction",
			"fragile" : False
		},
		
		"ivory" : {
			"scaling" : [0,2,.5,.5,0],
			"material" : "bone",
			"fragile" : False
		},
		
		"fossilized" : {
			"scaling" : [0,0,1.5,1.5,0],
			"material" : "bone",
			"fragile" : False
		},
		
		"ancient" : {
			"scaling" : [0,9,0,0,0],
			"material" : "bone",
			"fragile" : True
		},
		
		"consecrated" : {
			"scaling" : [0,0,1.5,1.5,0],
			"material" : "bone",
			"fragile" : False
		},
		
		"desecrated" : {
			"scaling" : [0,3,0,0,0],
			"material" : "bone",
			"fragile" : False
		},
		
		"monster" : {
			"scaling" : [1,0,1,1,0],
			"material" : "bone",
			"fragile" : False
		},
		
		"dragon" : {
			"scaling" : [0,0,0,0,3],
			"material" : "all",
			"fragile" : False
		},
		
		"magic" : {
			"scaling" : [1.5,1.5,0,0,0],
			"material" : "all",
			"fragile" : False
		},
		
		"enchanted" : {
			"scaling" : [.75,.75,.75,.75,0],
			"material" : "all",
			"fragile" : False
		},
		
		"elven" : {
			"scaling" : [1,1,0,0,1],
			"material" : "all",
			"fragile" : False
		},
		
		"holy" : {
			"scaling" : [0,1,1,1,0],
			"material" : "all",
			"fragile" : False
		},
		
		"mastercrafted" : {
			"scaling" : [.6,.6,.6,.6,.6],
			"material" : "all",
			"fragile" : False
		}
	}
	
	suffix = {
        "" : {
			"scaling" : [0,0,0,0,0]
        },
    
		"of the mountain" : {
			"scaling" : [0,0,3,0,0]
		},
		
		"of the swamp" : {
			"scaling" : [.75,0,.75,.75,.75]
		},
		
		"of storms" : {
			"scaling" : [0,1,0,2,0]
		},
		
		"of the sea" : {
			"scaling" : [1.5,1.5,0,0,0]
		},
		
		"of the forrest" : {
			"scaling" : [0,0,1,1,1]
		},
		
		"of strength" : {
			"scaling" : [3,0,0,0,0]
		},
		
		"of wisdom" : {
			"scaling" : [0,2,0,1,0]
		},
		
		"of courage" : {
			"scaling" : [1,0,0,0,2]
		},
		
		"of protection" : {
			"scaling" : [0,0,0,3,0]
		},
		
		"of destruction" : {
			"scaling" : [0,3,0,0,0]
		},
		
		"of adventuring" : {
			"scaling" : [.6,.6,.6,.6,.6]
		},
		
		"of medicine" : {
			"scaling" : [0,0,0,0,3]
		}
	}
	
	def __init__(self):
		self.prefix = prefix
		self.suffix = suffix

## Definitions of all items and their stats #
class ItemDefs:

	global gear, items

	gear = {
		"shirt" : { # 2 points of scaling, 10 base points
			"meleeAtk" : 3,
			"mageAtk" : 1,
			"meleeDef" : 1,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [.75, .25, .25, .25, .5],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"nothing" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"coat" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 6,
			"scaling" : [0, 0, .5, .5, 1],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"shoes" : {
			"meleeAtk" : 2,
			"mageAtk" : 2,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 2,
			"scaling" : [.4, .4, .4, .4, .4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"gloves" : {
			"meleeAtk" : 9,
			"mageAtk" : 2,
			"meleeDef" : 3,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [0, .5, .75, .25, .5],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"chain gloves" : {
			"meleeAtk" : 2,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [.5, 0, .75, .25, .5],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"capelet" : {
			"meleeAtk" : 0,
			"mageAtk" : 3,
			"meleeDef" : 1,
			"mageDef" : 3,
			"life" : 3,
			"scaling" : [0, 1, 0, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"ring" : {
			"meleeAtk" : 2,
			"mageAtk" : 2,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 2,
			"scaling" : [.4, .4, .4, .4, .4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"necklace" : {
			"meleeAtk" : 5,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1, 1, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"greaves" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 4,
			"mageDef" : 2,
			"life" : 4,
			"scaling" : [0, 0, 1, .25, .75],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"helm" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 4,
			"scaling" : [0, 0, .5, .5, 1],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"hood" : {
			"meleeAtk" : 0,
			"mageAtk" : 10,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 3,
			"scaling" : [0, 2, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"cuisse" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 6,
			"scaling" : [0, 0, .25, .25, 1.5],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"leather armor" : {
			"meleeAtk" : 1,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 4,
			"life" : 3,
			"scaling" : [.2, 0, .4, .8, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"robe" : {
			"meleeAtk" : 0,
			"mageAtk" : 8,
			"meleeDef" : 0,
			"mageDef" : 2,
			"life" : 0,
			"scaling" : [0, 1.6, 0, .4, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"hide armor" : {
			"meleeAtk" : 3,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 3,
			"life" : 3,
			"scaling" : [.6, 0, .2, .6, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"platemail" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 0, 0, 0, 2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"chainmail" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 3,
			"life" : 2,
			"scaling" : [0, 0, 1, .6, .4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"lamellar" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 5,
			"life" : 0,
			"scaling" : [0, 0, 1, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"scalemail" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 4,
			"scaling" : [0, 0, .6, .6, .8],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"kite shield" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 1,
			"life" : 4,
			"scaling" : [0, 0, .2, .2, .8],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 20,
			"double" : 0
		},
		
		"buckler" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 1,
			"life" : 7,
			"scaling" : [0, .0, .2, .2, 1.4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 5,
			"double" : 0
		},
		
		"square shield" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [0, 0, .4, .4, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 15,
			"double" : 0
		},

		"greatshield" : {
			"meleeAtk" : 3,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [.75, 0, .5, .5, .75],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 50,
			"double" : 0
		},
		
		"wood shield" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 10,
			"scaling" : [0, 0, 0, 0, 2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"bone shield" : {
			"meleeAtk" : 0,
			"mageAtk" : 4,
			"meleeDef" : 0,
			"mageDef" : 1,
			"life" : 1,
			"scaling" : [0, .8, 0, .2, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 20,
			"double" : 0
		},
		
		"sword" : {
			"meleeAtk" : 7,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1.5, 0, .5, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},

		"mace" : {
			"meleeAtk" : 7,
			"mageAtk" : 0,
			"meleeDef" : 1,
			"mageDef" : 1,
			"life" : 1,
			"scaling" : [1.4, 0, .2, .2, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"cane" : {
			"meleeAtk" : 1,
			"mageAtk" : 7,
			"meleeDef" : 0,
			"mageDef" : 1,
			"life" : 1,
			"scaling" : [.2, 1.4, 0, .2, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		
		"scimitar" : {
			"meleeAtk" : 10,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [2, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},

		"kris" : {
			"meleeAtk" : 9,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1.8, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 5
		},

		"katars" : {
			"meleeAtk" : 7,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1.4, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 15
		},

		"battle axe" : {
			"meleeAtk" : 15,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 5,
			"scaling" : [3, 0, 0, 0, 1],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},

		"halberd" : {
			"meleeAtk" : 10,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 4,
			"scaling" : [2, 0, .6, .6, .8],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 5,
			"double" : 0
		},
		
		"claws" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 100
		},

		"great spear" : {
			"meleeAtk" : 12,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 8,
			"scaling" : [2.4, 0, 0, 0, 1.6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 10
		},
        "katana" : {
            "meleeAtk" : 9,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1.8, 0, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 5,
			"double" : 0
        },
        "axe" : {
            "meleeAtk" : 7,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 3,
			"scaling" : [1.4, 0, 0, 0, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
        },
        
        "shiv" : {
            "meleeAtk" : 5,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [1, 1, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
        },
		
		"plank shield" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 10,
			"scaling" : [0, 0, 0, 0, 2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"wand" : {
			"meleeAtk" : 0,
			"mageAtk" : 10,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 2, 0, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"catalyst" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 1,
			"life" : 0,
			"scaling" : [0, 1, 0, .2, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 20,
			"double" : 0
		},
		
		"leather coat" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 5,
			"life" : 2,
			"scaling" : [0, 0, .6, 1, .4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"duster" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 5,
			"life" : 0,
			"scaling" : [0, 0, 1, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"boots" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 3,
			"life" : 4,
			"scaling" : [0, 0, .6, .6, .8],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"sandals" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 7,
			"mageDef" : 3,
			"life" : 0,
			"scaling" : [0, 0, 1.4, .6, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"leather boots" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 3,
			"mageDef" : 7,
			"life" : 0,
			"scaling" : [9, 0, .6, 1.4, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"sabatons" : {
			"meleeAtk" : 00,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 0, 2, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"leather gloves" : {
			"meleeAtk" : 3,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 4,
			"life" : 1,
			"scaling" : [.6, 0, .4, .8, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"gauntlets" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 10,
			"mageDef" : 0,
			"life" : 0,
			"scaling" : [0, 0, 2, 0, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"scale gloves" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 2,
			"life" : 3,
			"scaling" : [0, 0, 1, .4, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"cape" : {
			"meleeAtk" : 2,
			"mageAtk" : 2,
			"meleeDef" : 2,
			"mageDef" : 2,
			"life" : 2,
			"scaling" : [.4, .4, .4, .4, .4],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"mantle" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 5,
			"life" : 0,
			"scaling" : [0, 1, 0, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"amulet" : {
			"meleeAtk" : 0,
			"mageAtk" : 7,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 3,
			"scaling" : [0, 1.4, 0, 0, .6],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"leather pants" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 2,
			"mageDef" : 7,
			"life" : 1,
			"scaling" : [0, 0, .4, 1.4, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"skirt" : {
			"meleeAtk" : 0,
			"mageAtk" : 7,
			"meleeDef" : 0,
			"mageDef" : 2,
			"life" : 1,
			"scaling" : [0, 1.4, 0, .4, .2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"greathelm" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 5,
			"mageDef" : 5,
			"life" : 0,
			"scaling" : [0, 0, 1, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"mask" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 5,
			"life" : 0,
			"scaling" : [0, 1, 0, 1, 0],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"hat" : {
			"meleeAtk" : 0,
			"mageAtk" : 0,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 10,
			"scaling" : [0, 0, 0, 0, 2],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
		"crown" : {
			"meleeAtk" : 0,
			"mageAtk" : 5,
			"meleeDef" : 0,
			"mageDef" : 0,
			"life" : 5,
			"scaling" : [0, 1, 0, 0, 1],#[0] : "meleeAtk",[1] : "mageAtk", [2] : "meleeDef", [3] : "mageDef", [4] : "life"
			"block" : 0,
			"double" : 0
		},
		
	}

	items = {
		"nothing" : {
			"desc" : "It's certainly nothing.",
			"type" : "nothing",
			"key" : None,
			"material" : None
		},
		
		"small mana potion" : {
			"desc" : "A small potion for restoring mana.",
			"type" : "mana",
			"key" : 25,
			"material" : None
		},
		
		"town note two" : {
			"desc" : "A note I found in crud town.",
			"type" : "note",
			"key" : ["This is the last sanctuary for the living, it doesn't look like the dark forces can be stopped."],
			"material" : None
		},
	
		"town note one" : {
			"desc" : "A note I found in crud town.",
			"type" : "note",
			"key" : ["The merchants have tomes of power to make someone stronger, yet they only have them for sale. Worse than the monsters."],
			"material" : None
		},
	
		"cabin note" : {
			"desc" : "A note I found in old town.",
			"type" : "note",
			"key" : ["The ground here is hallowed, anyone who can enter these grounds is free to stay."],
			"material" : None
		},
		
		"old note three" : {
			"desc" : "A note I found in old town.",
			"type" : "note",
			"key" : ["The hermit from the woods always preached about how we needed warriors.\n Did he actually know what was coming?."],
			"material" : None
		},
		
		"old note one" : {
			"desc" : "A note I found in old town.",
			"type" : "note",
			"key" : ["They say its abandoned, but there are monsters there."],
			"material" : None
		},
		
		"old note two" : {
			"desc" : "A note I found in old town.",
			"type" : "note",
			"key" : ["The light is a warning, but ships aren't the only ones who should stay away"],
			"material" : None
		},
		
		"potion" : {
			"desc" : "A potion for self healing.",
			"type" : "healing",
			"key" : ["5"],
			"material" : None
		},
		
		"junk" : {
			"desc" : "Some useless junk.",
			"type" : "grabbable",
			"key" : False,
			"material" : None
		},
		
		"homestone" : {
			"desc" : "A stone that will take you directly to Crudtown",
			"type" : "travel",
			"key" : ["Crud town"],
			"material" : None
		},

		"tome of frost" : {
			"desc" : "This tome gives you an equal balance of stats.",
			"type" : "tome",
			"key" : ["1","1","1","1","1"],
			"material" : None
		},

		"tome of strength" : {
			"desc" : "This tome raises your strength greatly.",
			"type" : "tome",
			"key" : ["4","0","0","0","1"],
			"material" : None
		},

		"tome of magic" : {
			"desc" : "This tome raises your magic power greatly.",
			"type" : "tome",
			"key" : ["0","4","0","0","1"],
			"material" : None
		},

		"tome of resistance" : {
			"desc" : "This tome heightens your resiliance to your opponents",
			"type" : "tome",
			"key" : ["0","0","2","2","2"],
			"material" : None
		},

		"rope" : {
			"desc" : "A rope that will take you back to the cabin.",
			"type" : "travel",
			"key" : ["Cabin"],
			"material" : None
		},
		
		"jerky" : {
			"desc" : "Meat that has been dried and cured for preservation.",
			"type" : "food",
			"key" : ["25"],
			"material" : None
		},
		
		"ration" : {
			"desc" : "A typical knight's ration.",
			"type" : "food",
			"key" : ["10"],
			"material" : None
		},
		
		"steak" : {
			"desc" : "A beautiful steak.",
			"type" : "food",
			"key" : ["100"],
			"material" : None
		},

		"crystal" : {
			"desc" : "A bright crystal.",
			"type" : "gem",
			"key" : 1000,
			"material" : None
		},

		"onyx" : {
			"desc" : "A rare crystal",
			"type" : "gem",
			"key" : 5000,
			"material" : None
		},

		"diamond" : {
			"desc" : "A beautiful gem worth more than a rock should be.",
			"type" : "gem",
			"key" : 10000,
			"material" : None
		},
		
		"shirt" : {
			"desc" : "A cloth shirt.",
			"type" : "chest",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"coat" : {
			"desc" : "A basic coat.",
			"type" : "back",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"leather coat" : {
			"desc" : "A sturdy coat made of leather.",
			"type" : "back",
			"key" : False,
			"material" : ["leather"]
		},
		
		"duster" : {
			"desc" : "A large coat for traveling on horseback.",
			"type" : "back",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"shoes" : {
			"desc" : "Standard shoes.",
			"type" : "feet",
			"key" : False,
			"material" : ["leather"]
		},
		
		"boots" : {
			"desc" : "Standard boots that provide standard protection.",
			"type" : "feet",
			"key" : False,
			"material" : ["leather"]
		},
		
		"sandals" : {
			"desc" : "Protective leather sandals.",
			"type" : "feet",
			"key" : False,
			"material" : ["leather"]
		},
		
		"leather boots" : {
			"desc" : "Boots made of leather providing more defense and armor than your standard boots.",
			"type" : "feet",
			"key" : False,
			"material" : ["leather"]
		},
		
		"sabatons" : {
			"desc" : "Shoes made out of thin ribbons of metal called lame.",
			"type" : "feet",
			"key" : False,
			"material" : ["metal"]
		},
		
		"capelet" : {
			"desc" : "A plain capelet.",
			"type" : "back",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"cape" : {
			"desc" : "An average cape.",
			"type" : "back",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"mantle" : {
			"desc" : "A regular mantle",
			"type" : "back",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"chain gloves" : {
			"desc" : "Chainmail gloves.",
			"type" : "hands",
			"key" : False,
			"material" : ["metal"]
		},
		
		"leather gloves" : {
			"desc" : "Basic gloves made of leather.",
			"type" : "hands",
			"key" : False,
			"material" : ["leather"]
		},
		
		"gauntlets" : {
			"desc" : "Gauntlets made for a knight.",
			"type" : "hands",
			"key" : False,
			"material" : ["metal"]
		},
		
		"scale gloves" : {
			"desc" : "Gloves made from metal scales woven together.",
			"type" : "gloves",
			"key" : False,
			"material" : ["metal"]
		},
		
		"ring" : {
			"desc" : "A standard ring.",
			"type" : "accessory",
			"key" : False,
			"material" : ["metal", "gemstone"]
		},
		
		"necklace" : {
			"desc" : "A decorative accessory worn around the neck.",
			"type" : "accessory",
			"key" : False,
			"material" : ["metal", "gemstone"]
		},
		
		"amulet" : {
			"desc" : "A strange symbol tied on to some string.",
			"type" : "accessory",
			"key" : False,
			"material" : ["gemstone", "depiction"]
		},
		
		"greaves" : {
			"desc" : "Metal greaves.",
			"type" : "legs",
			"key" : False,
			"material" : ["metal"]
		},
		
		"leather pants" : {
			"desc" : "Leather pants.",
			"type" : "legs",
			"key" : False,
			"material" : ["leather"]
		},
		
		"Cuisse" : {
			"desc" : "Cuisse, thigh armor, also means legs in french",
			"type" : "legs",
			"key" : False,
			"material" : ["metal"]
		},
		
		"helm" : {
			"desc" : "A standard soldier's helm.",
			"type" : "head",
			"key" : False,
			"material" : ["metal"]
		},
		
		"greathelm" : {
			"desc" : "The classic bucket helmet",
			"type" : "head",
			"key" : False,
			"material" : ["metal"]
		},
		
		"mask" : {
			"desc" : "A wooden mask depicting some creature",
			"type" : "head",
			"key" : False,
			"material" : ["wood", "depiction"]
		},
		
		"hood" : {
			"desc" : "A plain hood.",
			"type" : "head",
			"key" : False,
			"material" : ["cloth", "leather"]
		},
		
		"Crown" : {
			"desc" : "A metal status symbol worn on one's head",
			"type" : "head",
			"key" : False,
			"material" : ["metal", "gemstone", "depiction"]
		},
		
		"hat" : {
			"desc" : "A common hat.",
			"type" : "head",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"claws" : {
			"desc" : "Short metal blades wielded in both hands",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"leather armor" : {
			"desc" : "Lightweight armor made of leather.",
			"type" : "chest",
			"key" : False,
			"material" : ["leather"]
		},
		
		"robe" : {
			"desc" : "Robes worn by lowly mages.",
			"type" : "chest",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"hide armor" : {
			"desc" : "Armor made out of cured animal hide.",
			"type" : "chest",
			"key" : False,
			"material" : ["leather"]
		},
		
		"platemail" : {
			"desc" : "Standard armor worn by knights.",
			"type" : "chest",
			"key" : False,
			"material" : ["metal"]
		},
		
		"chainmail" : {
			"desc" : "Armor made of interlinking rings of steel.",
			"type" : "chest",
			"key" : False,
			"material" : ["metal"]
		},
		
		"lamellar" : {
			"desc" : "Armor made of small rectangular plates.",
			"type" : "chest",
			"key" : False,
			"material" : ["metal"]
		},
		
		"scalemail" : {
			"desc" : "A cloth shirt covered in many small metal 'scales.'",
			"type" : "chest",
			"key" : False,
			"material" : ["metal"]
		},
		
		"kite shield" : {
			"desc" : "Tie a string to it and fly.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["metal"]
		},
		
		"square shield" : {
			"desc" : "A rectangular shield.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["metal"]
		},
		
		"buckler" : {
			"desc" : "A small round shield.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["metal"]
		},
		
		"greatshield" : {
			"desc" : "A sturdy and very large shield.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"bone shield" : {
			"desc" : "A buckler favored among mages.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["bone"]
		},
		
		"wood shield" : {
			"desc" : "A shield made of solid wood.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["wood"]
		},
		
		"catalyst" : {
			"desc" : "A magic artifact used by mages",
			"type" : "off-hand",
			"key" : False,
			"material" : None
		},
		
		"sword" : {
			"desc" : "A standard straight sword.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"wand" : {
			"desc" : "A magical stick for focusing spells",
			"type" : "weapon",
			"key" : False,
			"material" : ["wood"]
		},
		
		"mace" : {
			"desc" : "A basic mace.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"cane" : {
			"desc" : "Taken from a village elder I assume.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"scimitar" : {
			"desc" : "A scimitar.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		"katana" : {
			"desc" : "A katana.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"katars" : {
			"desc" : "A pair of katars.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"shiv" : {
			"desc" : "A homemade weapon, for stabbing.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal", "wood"]
		},
		
		"axe" : {
			"desc" : "An axe, you can have mine.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"battle axe" : {
			"desc" : "A battle axe.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"halberd" : {
			"desc" : "A spear with an axe attached to it.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"great spear" : {
			"desc" : "A spear, that is bigger and heavier than a typical sample.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},

		"plank shield" : {
			"desc" : "A shield made of tied together planks.",
			"type" : "off-hand",
			"key" : False,
			"material" : ["wood"]
		},
		
		"kris" : {
			"desc" : "A wavy dagger, maybe it wants to say hi.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"skirt" : {
			"desc" : "A skirt, popular with mages.",
			"type" : "legs",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"gloves" : {
			"desc" : "Standard cloth gloves.",
			"type" : "hands",
			"key" : False,
			"material" : ["cloth"]
		},
		
		"longsword" : {
			"desc" : "A long straight sword.",
			"type" : "weapon",
			"key" : False,
			"material" : ["metal"]
		},
		
		"stave" : {
			"desc" : "A large magical stick",
			"type" : "weapon",
			"key" : False,
			"material" : ["wood"]
		},
		
		"club" : {
			"desc" : "A large heavy branch smoothed out for ease of use.",
			"type" : "weapon",
			"key" : False,
			"material" : ["wood"]
		},
		
		"brooch" : {
			"desc" : "A decorative pin.",
			"type" : "accessory",
			"key" : False,
			"material" : ["metal", "gemstone"]
		},
		
		"earring" : {
			"desc" : "Jewelry worn through a hole in the ear.",
			"type" : "accessory",
			"key" : False,
			"material" : ["metal", "gemstone"]
		}
	}

	def __init__(self):
		self.items = items
		self.gear = gear
