import threading
import sys
import time
import ctypes

from defs import ItemDefs
from defs import EnemyDefs
from defs import npcBuff

from map import Room

class Music(threading.Thread):
	def __init__(self,name): 
		threading.Thread.__init__(self) 
		self.name = name
		
	def __init__(self, *args, **keywords): 
		threading.Thread.__init__(self, *args, **keywords) 
		self.killed = False

	def start(self): 
		self.__run_backup = self.run 
		self.run = self.__run       
		threading.Thread.start(self) 

	def __run(self): 
		sys.settrace(self.globaltrace) 
		self.__run_backup() 
		self.run = self.__run_backup 

	def globaltrace(self, frame, event, arg): 
		if event == 'call': 
			return self.localtrace 
		else: 
			return None

	def localtrace(self, frame, event, arg): 
		if self.killed: 
			if event == 'line': 
				raise SystemExit() 
		return self.localtrace 
  
	def kill(self): 
		self.killed = True

class Player(object):

	def __init__(self, life, insanity, room):
		self.level = 1
		self.life = life
		self.insanity = insanity
		self.room = room
		self.voice = False
		self.combat = False
		self.target = None
		self.hp = 3
		self.xp = 0
		self.growth = [0, 0, 0, 1, 1, 1] #0:meleeAtk,1:mageAtk,2:meleeDef,3:mageDef,4:hp,5:mana
		self.levelxp = 8
		self.inventory = [ ["rope",0,"",""], ["small mana potion",0,"",""], ["potion",0,"",""], ["potion",0,"",""], ["jerky",0,"",""], ["jerky",0,"",""] ]
		self.abilities = []
		self.location = "old town"
		self.boss = False
		self.name = ""
		self.gold = 0
		self.status = [0,0,0]
		self.stamina = 100
		self.mana = 5
		self.souls = 0
		self.maxMana = 5
		self.actions = 0
		self.journal = {
			"quest" : [],
			"kills" : [],
			"kc" : [],
			"notes" : []
		}
		self.weapon, self.chest, self.offhand, self.back, self.feet, self.hands, self.accessory, self.legs, self.head = ["sword", 1,"",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""], ["nothing","","",""]
		self.stats = {
			"meleeAtk" : Item(self.weapon[0],self.weapon[1]).stats[0],
			"mageAtk" : Item(self.weapon[0],self.weapon[1]).stats[1],
			"meleeDef" : Item(self.weapon[0],self.weapon[1]).stats[2],
			"mageDef" : Item(self.weapon[0],self.weapon[1]).stats[3],
			"MaxHP" : Item(self.weapon[0],self.weapon[1]).stats[4] + 3,
		}

#equipment slots: weapon, offhand, feet, hands, chest, back, accessory, legs, head
	def souls(self,value=None):
		if(value == None):
			return self._souls
		self._souls = value
	
	def abilities(self,value=None):
		if(value == None):
			return self._abilities
		self._abilities = value
	
	def maxMana(self,value=None):
		if(value == None):
			return self._maxMana
		self._maxMana = value
	
	def status(self, value=None):
		if(value == None):
			return self._status
		self._status = value
	
	def actions(self, value=None):
		if(value == None):
			return self._actions
		self._actions = value
	
	def target(self, value=None):
		if(value == None):
			return self._target
		self._target = value
	
	def combat(self, value=None):
		if(value == None):
			return self._combat
		self._combat = value
	
	def stamina(self, value=None):
		if(value == None):
			return self._stamina
		self._stamina = value
	
	def mana(self, value=None):
		if(value == None):
			return self._adrenaline
		self._adrenaline = value
	
	def name(self, value=None):
		if(value == None):
			return self._name
		self._name = value
	
	def growth(self, value=None):
		if(value == None):
			return self._growth
		self._growth = value
	
	def back(self, value=None):
		if(value == None):
			return self._back
		self._back = value
	
	def feet(self, value=None):
		if(value == None):
			return self._feet
		self._feet = value
	
	def hands(self, value=None):
		if(value == None):
			return self._hands
		self._hands = value
	
	def accessory(self, value=None):
		if(value == None):
			return self._accessory
		self._accessory = value
	
	def legs(self, value=None):
		if(value == None):
			return self._legs
		self._legs = value
	
	def head(self, value=None):
		if(value == None):
			return self._head
		self._head = value
	
	def voice(self, value=None):
		if(value == None):
			return self._voice
		self._voice = value
	
	def gold(self, value=None):
		if(value == None):
			return self._gold
		self._gold = value
	
	def boss(self, value=None):
		if(value == None):
			return self._boss
		self_boss = value
	
	def location(self, value=None):
		if(value == None):
			return self._location
		self._location = value
	
	def xp(self, vlaue=None):
		if(value == None):
			return self._xp
		self._xp = value
		
	def levelxp(self, value=None):
		if(value == None):
			return self._levelxp
		self._levelxp = value
	
	def level(self, value=None):
		if(value == None):
			return self._level
		self._level = value

	def hp(self, value = None):
		if (value == None):
			return self._hp
		self._level = value
	
	def life(self, value=None):
		if(value == None):
			return self._life
		self._life = value

	def insanity(self, value=None):
		if(value == None):
			return self._insanity
		self._insanity = value

	def name(self, value=None):
		if(value == None):
			return self._name
		self._name = value

	def inventory(self, value=None):
		if(value == None):
			return self._inventory
		self._inventory = value
		
	def weapon(self, value=None):
		if(value == None):
			return self._weapon
		self._weapon = value
	
	def chest(self, value=None):
		if(value == None):
			return self._chest
		self._chest = value

	def offhand(self, value=None):
		if(value == None):
			return self._offhand
		self._offhand = value
		
	def stats(self, value=None):
		if(value == None):
			return self._stats
		self._stats = value
	
	def room(self, value=None):
		if(value == None):
			return self._room
		self._room = value

## Enemy object-type definitions and functions #	
class Enemy(object):

	def __init__(self, name,level,buff):
		info = EnemyDefs()
		self.enemy = info.enemy
		info1 = npcBuff()
		self.buffInfo = info1.npcBuffs
		self.name = name
		self.abilities = self.enemy[name]["abilities"] + self.buffInfo[buff]["abilities"]
		self.level = level
		self.life = self.enemy[name]["life"] + (level * (self.enemy[name]["scaling"][4] + npcBuff().npcBuffs[buff]["scaling"][4])) + npcBuff().npcBuffs[buff]["life"]
		self.drop = self.enemy[name]["drop"]
		self.atkStatus = self.enemy[name]["status"]
		self.crit = self.enemy[name]["crit"]
		self.statusChance = self.enemy[name]["chance"]
		self.xp = self.enemy[name]["xp"] + (level * (self.enemy[name]["scaling"][5] + npcBuff().npcBuffs[buff]["scaling"][5])) + npcBuff().npcBuffs[buff]["xp"]
		self.stats = [ self.enemy[name]["meleeAtk"]  + (level * (self.enemy[name]["scaling"][0] + npcBuff().npcBuffs[buff]["scaling"][0])) + npcBuff().npcBuffs[buff]["meleeAtk"], self.enemy[name]["mageAtk"] + (level * (self.enemy[name]["scaling"][1] + npcBuff().npcBuffs[buff]["scaling"][1])) + npcBuff().npcBuffs[buff]["mageAtk"], self.enemy[name]["meleeDef"] + (level * (self.enemy[name]["scaling"][2] + npcBuff().npcBuffs[buff]["scaling"][2])) + npcBuff().npcBuffs[buff]["meleeDef"], self.enemy[name]["mageDef"] + (level * (self.enemy[name]["scaling"][3] + npcBuff().npcBuffs[buff]["scaling"][3])) + npcBuff().npcBuffs[buff]["mageDef"] ]
		self.status = [0,0]
		self.stun = self.enemy[name]["stun"]
		self.block = self.enemy[name]["block"]
		self.buff = buff
	
	def buffInfo(self, value=None):
		if(value == None):
			return self._buffInfo
		self._buffInfo = value
	
	def buff(self, value=None):
		if(value == None):
			return self._buff
		self._buff = value
	
	def abilities(self, value=None):
		if(value == None):
			return self._abilities
		self._abilities = value
	
	def level(self,value=None):
		if(value == None):
			return self._level
		self._level = value
	
	def block(self,value=None):
		if(value == None):
			return self._block
		self._block = value
	
	def stun(self,value=None):
		if(value == None):
			return self._stun
		self._stun = value
	
	def statusChance(self,value=None):
		if(value == None):
			return self._statusChance
		self._statusChance = value
	
	def crit(self, value=None):
		if(value == None):
			return self._crit
		self._crit = value
	
	def atkSatus(self, value=None):
		if(value == None):
			return self._atkStatus
		self._atkStatus = value
	
	def status(self, value=None):
		if(value == None):
			return self._status
		self._status = value

	def enemy(self, value=None):
		if(value == None):
			return self._enemy
		self._enemy = value
		
	def name(self, value=None):
		if(value == None):
			return self._name
		self._name = value
		
	def level(self, value=None):
		if(value == None):
			return self._level
		self._level = value
		
	def life(self, value):
		if(value == None):
			return self._life
		self._life = value

	def drop(self, value=None):
		if(value == None):
			return self._drop	
		self._drop = value
		
	def boss(self, value=None):
		if(value == None):
			return self._boss
		self._boss = value
		
	def stats(self, value=None):
		if(value == None):
			return self._stats
		self._stats = value
	
	def xp(self, value=None):
		if(value == None):
			return self._xp
		self._xp = value
	
## Item object-type definitions and functions #
class Item(object):
	def __init__(self, name="nothing", level=None, prefix="",suffix=""):
		self.name = name
		self.info = ItemDefs()
		self.desc = self.info.items[name]["desc"]
		self.type = self.info.items[name]["type"]
		self.key = self.info.items[name]["key"]
		if(self.type == "weapon") or (self.type == "chest") or (self.type == "off-hand") or (self.type == "back") or (self.type == "feet") or (self.type == "hands") or (self.type == "two-hand") or (self.type == "accessory") or (self.type == "dual-wield") or (self.type == "legs") or (self.type == "head"):
			self.stats = [ self.info.gear[name]["meleeAtk"] + (self.info.gear[name]["scaling"][0] * level), self.info.gear[name]["mageAtk"] + (self.info.gear[name]["scaling"][1] * level), self.info.gear[name]["meleeDef"] + (self.info.gear[name]["scaling"][2] * level), self.info.gear[name]["mageDef"] + (self.info.gear[name]["scaling"][3] * level), self.info.gear[name]["life"] + (self.info.gear[name]["scaling"][4] * level) ]
			self.block = self.info.gear[name]["block"]
			self.stun = 0
			self.double = self.info.gear[name]["double"]
			if(prefix != "" and suffix != ""):
				self.fullName = "level " + str(level) + " " + str(prefix) + " " + str(name) + " " + str(suffix)
			elif(prefix != "" and suffix == ""):
				self.fullName = "level " + str(level) + " " + str(prefix) + " " + str(name)
			elif(prefix == "" and suffix != ""):
				self.fullName = "level " + str(level) + " " + str(name) + " " + str(suffix)
			else:
				self.fullName = "level " + str(level) + " " + str(name)
		else:
			self.stats = False
			self.block = False
			self.stun = False
			self.double = False
			self.fullName = name

#equipment slots: weapon, offhand, feet, hands, chest, back, accessory, legs, head
	def fullName(self, value=None):
		if(value == None):
			return self._fullName
		self._fullName = value
	
	def double(self, value=None):
		if(value == None):
			return self._double
		self._double = value
	
	def block(self, value=None):
		if(value == None):
			return self._block
		self._block = value

	def stun(self, value=None):
		if(value == None):
			return self._stun
		self._stun = value

	def name(self, value=None):
		if(value == None):
			return self._name
		self._name = value
		
	def desc(self, value=None):
		if(value == None):
			return self._desc
		self._desc = value
		
	def type(self, value=None):
		if(value == None):
			return self._type
		self._type = value
		
	def key(self, value=None):
		if(value == None):
			return self._key
		self._key = value
	
	def stats(self, value=None):
		if(value == None):
			return self._stats
		self._stats = value
