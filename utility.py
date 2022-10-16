import os
import sys
import socket
import random
import time
import math

from defs import AbilityDefs
from defs import npcAbilityDefs
from defs import ItemBuffDefs
from defs import ItemDefs

from colorama import Fore, init
from termcolor import colored, cprint

from objects import Item
from objects import Enemy

from map import Area

class Text:

	def __init__(self, player): # constructor / on-call code for Text class
		# init colorama for termcolor handling on windomows
		init()
		self.player = player

	def player(self, value=None):
		if(value == None):
			return self._player
		self._player = value

	def header(self): # display the logo + ternary-based compass; pass in room to identify exits
		cardinal = [
			self.color('N', 'green' if self.player.room.checkExit("north") else 'red'),
			self.color('S', 'green' if self.player.room.checkExit("south") else 'red'),
			self.color('W', 'green' if self.player.room.checkExit("west") else 'red'),
			self.color('E', 'green' if self.player.room.checkExit("east") else 'red'),
		]
	# all white and cyan strings are colored red if player is under 25 percent hp
		# print ascii header formatted with our compass
		#self.player.hp > (self.player.stats["MaxHP"]
		print colored('\n	 ____  _  _  ____  _____  ___    __    __  __  _  _ '+'         ^', 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')
		print colored('	(_  _)( \/ )(  _ \(  _  )/ __)  /__\  (  \/  )( \/ )'+'         '+cardinal[0], 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')
		print colored('	  )(   \  /  )___/ )(_)(( (_-. /(__)\  )    (  \  / '+'     < '+cardinal[2]+colored(' + ', 'white' if self.player.hp > self.player.stats["MaxHP"] else 'red')+cardinal[3]+colored(' > ', 'white' if self.player.hp > self.player.stats["MaxHP"] else 'red'), 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')
		print colored('	 (__)  (__) (__)  (_____)\___/(__)(__)(_/\/\_) (__) '+'         '+cardinal[1], 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')
		print colored("        =====================================================        v", 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')
		
	# print out for player-related gui data	
	def playerData(self):
		items, gear, gears = "", "", [ self.player.weapon[0], self.player.chest[0] ]
		out = ("  "+t.color("Level: ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color(self.player.level, 'blue') + "\n")
		out += "  You currently have {} lives.\n".format(self.player.life)
		out += colored("  Insanity: ", 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+t.color(self.player.insanity, 'magenta')+"\n"
		for i in range(len(self.player.inventory)):
			if((len(self.player.inventory) == i+1) or (i == len(self.player.inventory))):
				items += self.color(Item(*self.player.inventory[i]).fullName, 'green')
			else:
				items += self.color(Item(*self.player.inventory[i]).fullName + ", ", 'green')
		out += (colored("  Your backpack contains [ {} ", 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+self.color("]", 'white' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+"\n").format(self.color(items, 'green') if (items != "") else self.color("nothing", 'red'))
		for i in range(len(gears)):
			if((len(gears) == i+1) or (i == len(gears))):
				gear += self.color(gears[i], 'green')
			else:
				gear += self.color(gears[i]+", ", 'green')
		hp = 20.0 * self.player.hp
		hp = hp / self.player.stats["MaxHP"]
		hp = int(hp)
		xp = 20.0 * self.player.xp
		xp = xp / self.player.levelxp
		xp = int(xp)
		stam0 = float(self.player.stamina * 20.0)
		stam0 = stam0 / 100.0
		stam0 = int(stam0)
		
		if(stam0 > 40):
			stam0 = 40
		if(stam0 > 20):
			stam1 = 20
			stam2 = stam0 - 20
		else:
			stam1 = stam0
			stam2 = 0
		mana = float(self.player.mana * 20.0)
		mana = mana / self.player.maxMana
		mana = int(mana)
		if(mana > 20):
			mana = 20
		out += ("  "+t.color("You are currently wielding: [", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+","+t.color(" {}", 'green')+t.color("]", 'cyan')+"\n").format(str(Item(*self.player.weapon).fullName), str(Item(*self.player.chest).fullName), str(Item(*self.player.offhand).fullName), str(Item(*self.player.back).fullName), str(Item(*self.player.feet).fullName), str(Item(*self.player.hands).fullName), str(Item(*self.player.accessory).fullName), str(Item(*self.player.head).fullName), str(Item(*self.player.legs).fullName) )
		out += ("  "+t.color("Health: ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("[", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("#" * hp, 'red') + t.color("~" * (20 - hp), 'red') + t.color("] \n", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red'))
		out += ("  "+t.color("Experience: ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("[", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("#" * xp, 'white') + t.color("~" * (20 - xp), 'white') + t.color("] \n", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red'))
		out += ("  "+t.color("You currently have ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + "{}" + t.color(" gold pieces.", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+"\n").format(self.color(self.player.gold, 'yellow'))
		out += ("  "+t.color("You currently have ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + "{}" + t.color(" souls", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red')+"\n").format(self.color(self.player.souls, 'red'))
		out += ("  "+t.color("Mana: ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("[", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("#" * mana, 'blue') + t.color("~" * (20 - mana), 'blue') + t.color("] \n", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red'))
		out += ("  "+t.color("Stamina: ", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("[", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red') + t.color("#" * stam1, 'green') + t.color("~" * (20 - stam1), 'blue') + t.color("#" * stam2, 'yellow') + t.color("] \n", 'cyan' if self.player.hp > self.player.stats["MaxHP"] * .25 else 'red'))
		if(self.player.target != None):
			out += ("  " + t.color("Combatants:", 'red'))
			for i in range(len(self.player.target)):
				out += " level " +str(self.player.target[i].level)+ " " + str(self.player.target[i].buff) + " " + t.color(str(self.player.target[i].name), 'red')
		return out

	def roomData(self, room):
		out = " Room data: \n"
		out += "  Items: \n"
		for item in room.items:
			out += "   - "+item
		print out

	def send(self, message, color=None): # for sending just a message + color
		print colored(message, color)

	def color(self, message, color=None,effect=None):
		if(color == None):
			color = 'grey'
		if(effect == None):
			return colored(message, color)
		else:
			return colored(message, color, attrs=[effect])

	def info(self, head, message, color):
		print head.format(colored(message, color))

class Engine:

	global verbs, verblist, neednouns, combatVerbs
	global rtitle, t

	def __init__(self, player): # constructor for engine
		global rtitle, t
		# set the player instance, we will use this to pull data for the whole runtime
		self.player = player
		self.room = self.player.room
		self.items = self.room.items
		self.enemies = self.room.enemies
		t = Text(self.player)
		rtitle = t.color(' Response:', 'yellow')
	
	def player(self, value=None):
		if(value == None):
			return self._player
		self._player = value

	def response(self, value=None):
		if(value == None):
			return self._response
		self._response = value
	
	def status(self):
		if (self.player.status[0] > 0):
			self.poison()
		if (self.player.status[1] > 0):
			self.burning()
		if (self.player.status[2] > 0):
			self.regen()
		if(self.player.combat == True):
			for i in range(len(self.player.target)):
				if (self.player.target[i].status[0] > 0):
					self.player.target[i].life -= self.player.target.life * .1
					self.player.target[i].status[0] -= 1
					if(self.player.target[i].life <= 0):
						self.deadEnemy(i)
					print "enemy poisoned"
					time.sleep(.2)
				if (self.player.target[i].status[1] > 0):
					self.player.target[i].life -= self.player.target.life * .2
					self.player.target[i].status[1] -= 1
					if(self.player.target[i].life <= 0):
						self.deadEnemy(i)
					print "enemy burning"
					time.sleep(.2)
	
	def poison(self):
		self.player.hp -= int(self.player.stats["MaxHP"] * .05)
		self.player.status[0] -= 1
	
	def burning(self):
		self.player.hp -= int(self.player.stats["MaxHP"] * .1)
		self.player.status[1] -= 1
		
	def regen(self):
		self.player.hp += int(self.player.stats["MaxHP"] * .05)
		self.player.status[2] -= 1
		if(self.player.hp > self.player.stats["MaxHP"]):
			self.player.hp = self.player.stats["MaxHP"]
	
	def go(self, noun):
		self.response = " Invalid exit.\n"
		# check for valid exits in the current room
		for i in range(len(self.room.exits)): # a valid exit is found
			if (noun == self.room.exits[i]): # change the current room to the one that is associated with the specified exit
				self.room, self.player.room = self.room.locations[i], self.room.locations[i]
				self.response = t.color(" You go {} into the next room!\n".format(noun), 'green')
				if (len(self.room.enemies) > 0):
					self.player.target =[]
					for i in range(len(self.room.enemies)):
						self.player.target.append(Enemy(self.room.enemies[i][0], self.room.enemies[i][1], self.room.enemies[i][2]))
						self.player.combat = True
						self.response += "\n You have entered combat with a level " + str(self.player.target[i].level) + " "+ str(self.player.target[i].buff)+ " " + str(self.player.target[i].name) + "!\n"
					break
		return self.response

	def look (self):
		self.response = " Here is what's in the current room:"
		# check for valid items in the current room
		self.response += t.color("\n  Items:", 'cyan')
		for i in range(len(self.room.items)): # a valid item is found
			item = Item( self.room.items[i][0], self.room.items[i][1],self.room.items[i][2],self.room.items[i][3] )
			self.response += t.color("\n    * "+item.fullName, 'green')
		self.response += t.color("\n  Enemies:", 'cyan')
		for i in range(len(self.room.enemies)): # a valid enemy is found
			enemy = Enemy( str(self.room.enemies[i][0]), int(self.room.enemies[i][1]), str(self.room.enemies[i][2]))
			if(self.room.enemies[i][2] == ""):
				self.response += t.color("\n    * level "+ str(enemy.level) + " "+ str(enemy.name), 'green')
			else:
				self.response += t.color("\n    * level "+ str(enemy.level) + " "+ str(enemy.buff) + " " + str(enemy.name), 'green')
		return self.response

	def stats(self):
		self.response = " Here are your current stats:"
		for stat, value in self.player.stats.iteritems():
			self.response += t.color("\n   * "+stat+": "+str(value), 'green')
		return self.response

	def take(self, noun):
		if (self.room.enemies == []):
			self.response = " I don't see that item.\n"
			# check for valid grabbable items in the current room
			for i in range(len(self.room.items)): # a valid grabbable item is found
				if(i >= len(self.room.items)):
					break
				if (len(self.player.inventory) >= 25):
					self.response = " Your backpack is currently full."
					break
				if (noun == Item(self.room.items[i][0],self.room.items[i][1],self.room.items[i][2],self.room.items[i][3]).fullName): # add the grabbable item to the player's inventory and remove it from the room
					self.player.inventory.append([self.room.items[i][0],self.room.items[i][1],self.room.items[i][2],self.room.items[i][3]])
					self.room.doItem(self.room.items[i][0],self.room.items[i][1],self.room.items[i][2],self.room.items[i][3], True)
					self.response = " Item grabbed.\n"
					break
		else:
			self.response = " You can't take this item while a monster is guarding it."
		return self.response
		
	def error(self):
		self.response = " I didn't catch that, please use the {} syntax for actions!\n".format(t.color('verb noun', 'yellow'))
		return self.response
		
	def fight(self, noun):
		self.response = " I don't see that enemy.\n"
		# check for valid enemies in the room
		for i in range(len(self.room.enemies)):
			if (noun == self.room.enemies[i][0]):	# if a valid enemy is found combat starts
				self.player.combat = True
				self.response = ""
				self.player.target = []
				for j in range(len(self.room.enemies)):
					self.player.target.append(Enemy(self.room.enemies[j][0], self.room.enemies[j][1], self.room.enemies[j][2]))
					self.response += " You have entered a fight with a level " + str(self.player.target.level)+ " " + t.color(noun, 'green') + "!"
		return self.response
	
	# removes item from inventory and adds it to room
	def drop(self, noun):
		self.response = " I do not have that item."
		# checks if player has the item
		for i in self.player.inventory:
			if(Item(i[0],i[1],i[2],i[3]).fullName == noun):
				self.player.inventory.remove([i[0],i[1],i[2],i[3]])
				self.room.doItem(i[0],i[1],i[2],i[3])
				self.response = (" You drop "+"{}"+".").format(t.color(noun, 'green'))
				break
		return self.response
	
	# allows the player to use an item
	def use(self, noun):
		self.response = " I do not have that item."
		# checks if the player has an item
		for i in range (len(self.player.inventory)):
			if (noun == self.player.inventory[i][0]):
				self.response = " {} is not a usable item.".format(t.color(noun, 'green'))
				#this creates a string using the arguments from the item's key
				argList = "self,noun"
				for i in range (len(Item(noun,0).key)):
					argList += ","
					argList += Item(noun,0).key[i]
				#eval uses a string to run code so the string thats evaluated is method(arglist), healing(3)
				try:
					eval("Engine." + Item(noun,0).type + "(" + argList + ")")
				except:
					try:
						eval("Engine." + Item(noun,0).type + "(self,noun,1)")
					except:
						self.response = " {} is not a usable item.".format(t.color(noun, 'green'))
				return self.response
		return self.response
	#if item type is a note
	def note(self,noun,text):
		if(Item(noun,0).key[0] in self.player.journal["quest"]):
			self.response =str(Item(noun,0).key[0]) + "\n This note is already in your journal."
		else:
			self.player.journal["quest"].append(Item(noun,0).key[0])
			self.response = str(Item(noun,0).key[0]) + "\n The note has been added to your journal."
		self.player.inventory.remove([noun,0,"",""])
		return self.response
	#if item type is tome then it add stats based on the Item(noun).key[]
	def tome(self,noun,melee,mage,defence,mdefence,health):
		self.player.stats["meleeAtk"] += melee
		self.player.stats["mageAtk"] += mage
		self.player.stats["meleeDef"] += defence
		self.player.stats["mageDef"] += mdefence
		self.player.stats["MaxHP"] += health
		self.player.inventory.remove([noun,0,"",""])
		self.response = " You used the {}.".format(t.color(noun, 'green'))
		return self.response
	#if item is healing then player is healed for a portion of their max health, for example a potion heals for 1/3rd max health
	#therefore the healFractal is 3
	def healing(self,noun,healFractal):
		heal = int(self.player.stats["MaxHP"]/healFractal)
		self.player.hp += heal
		if (self.player.hp > self.player.stats["MaxHP"]):
			self.player.hp = self.player.stats["MaxHP"]
		self.player.inventory.remove([noun,0,"",""])
		self.response = " You used the {}.".format(t.color(noun, 'green'))
		return self.response
	#if item type is food it restores stamina
	def food(self,noun,stam):
		if(self.player.stamina < 95):
			self.player.stamina += stam
			if(self.player.stamina > 100):
				self.player.stamina = 100
		elif (self.player.stamina > 95):
			self.player.stamina += int(stam/2)
			if(self.player.stamina > 200):
				self.player.stamina = 200
		self.player.inventory.remove([noun,0,"",""])
		self.response = " You used the {}.".format(t.color(noun, 'green'))
		return self.response
	#if item type is travel relocates player to fresh map
	def travel(self,noun,location):
		area = Area(Item(noun,0).key[0])
		self.room = area.rooms[0]
		self.player.room = area.rooms[0]
		self.player.location = Item(noun,0).key[0]
		self.player.boss = False
		self.player.inventory.remove([noun,0,"",""])
		self.response = " You used the {}".format(t.color(noun, 'green'))
		self.response += " and travel to {}.".format(t.color(Item(noun,0).key[0],'blue'))
		return self.response
	
	# player equips item
	def equip(self, noun):
		self.response = " I don't have that item."
		itemArray = ""
		valid = False
		# checks if player has item
		for i in self.player.inventory:
			if(Item(i[0],i[1],i[2],i[3]).fullName == noun):
				itemArray = [i[0],i[1],i[2],i[3]]
				valid = True
		# checks if player is high enough level to equip item
		if (itemArray[1] > self.player.level):
			self.response = " You need to be level " + t.color(itemArray[1], 'blue') + " to equip " + t.color(noun, 'green') + "."
			return self.response
		# checks if player has item
		if (valid):
			self.response = " {} is not an equippable item.".format(t.color(noun, 'green'))
			# checks for item type and then swaps the item out with the currently equipped one
			# adds stats for new item and removes stats added by old item
			try:
				x = getattr(self.player, Item(*itemArray).type)
				x = True
			except:
				x = False
			if(x == True):
				#increasing stats based on the item being equipped
				self.player.stats["MaxHP"] += (Item(*itemArray).stats[4])
				self.player.stats["meleeAtk"] += Item(*itemArray).stats[0]
				self.player.stats["mageAtk"] += Item(*itemArray).stats[1]
				self.player.stats["meleeDef"] += Item(*itemArray).stats[2]
				self.player.stats["mageDef"] += Item(*itemArray).stats[3]
				#a temp variable to store the stats of the player item of the same type
				#this gets the object stored under the same name as the item type
				#so if the item being equipped is armor then it grabs self.player.armor
				g = getattr(self.player, Item(*itemArray).type)
				#subtracting the stats of the item being removed from the player
				if (g[0] != "nothing"):
					self.player.stats["MaxHP"] -= Item(*g).stats[4]
					self.player.stats["meleeAtk"] -= Item(*g).stats[0] 
					self.player.stats["mageAtk"] -= Item(*g).stats[1]
					self.player.stats["meleeDef"] -= Item(*g).stats[2]
					self.player.stats["mageDef"] -= Item(*g).stats[3]
				#if the item has less max health, the players hp drops to the new max
				if (self.player.hp > self.player.stats["MaxHP"]):
					self.player.hp = self.player.stats["MaxHP"]
				self.player.inventory.remove(itemArray)
				#adds the players item to the inventory array
				if (g[0] != "nothing"):
					self.player.inventory.append(g)
				#changes the player equipped item based on type
				setattr(self.player, Item(*itemArray).type, itemArray)
				self.response += "\n weapon assignment failed"
				self.response = " You equipped {}.".format(t.color(Item(*itemArray).fullName, 'green'))
		return self.response
	
	# allows the player to go to new dungeons
	def explore(self, noun):
		self.response = " You can't go exploring from here."
		locations = [ "old town", "abandoned lighthouse", "junk town", "mausoleum", "garrison", "eerie cave", "cave of elementals", "land of the dead", "lost swamp" ]
		# player cant explore unless in the cabin or crud town areas
		if (self.player.location == "Cabin" or self.player.location == "Crud town"):
			self.response = " That is not an explorable location. Explorable locations are: " + t.color(locations, 'green')
			for i in range(len(locations)):
				# if player chooses a valid area it generates a fresh map
				if (noun == locations[i]):
					area = Area(noun)
					self.room = area.rooms[0]
					self.player.room = area.rooms[0]
					self.player.location = noun
					self.player.boss = False
					self.response = " You are now exploring {}.".format(t.color(noun, 'green'))
					break
		return self.response

	# allows player to buy certain items
	def buy(self, noun):
		self.response = " You can only buy items in "+t.color("Crud town", 'green')+"."
		buyables = [ "potion", "leather armor", "robe", "hide armor", "platemail", "chainmail", "lamellar", "scalemail", 
"buckler", "square shield", "kite shield", "coat", "greatshield", "sword",
"tome of frost", "tome of magic", "tome of resistance", "tome of strength", "jerky", "ration", "steak", "small mana potion", "mana potion", "large mana potion" ]
		# checks if player is in crud town
		if (self.player.location == "Crud town"):
			self.response = " Items in stock: "+t.color(buyables, 'green')
			for i in range(len(buyables)):
				# checks if player picked a valid item
				if (noun == buyables[i]):
					# checks if player's inventory is full
					if (len(self.player.inventory) >= 30):
						self.response = " Your backpack is currently full."
						break
					# adds item to player's inventory if player has enough gold
					elif (noun == "potion"):
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= 200):
							self.player.gold -= 200
							self.player.inventory.append(["potion",0,"",""])
							self.response = " You purchase a "+t.color("potion", 'green') + " for "+t.color("200", 'yellow')+" gold."
					elif (noun == "tome of frost" or noun == "tome of magic" or noun == "tome of resistance" or noun == "tome of strength"):
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= 5000):
							self.player.gold -= 5000
							self.player.inventory.append([noun,0,"",""])
							self.response = " You purchase {} for {} gold.".format(t.color(noun, 'green'),t.color("5000", 'yellow'))
					elif (noun == "jerky"):
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= 50):
							self.player.gold -= 50
							self.player.inventory.append([noun,0,"",""])
							self.response = " You purchase {} for {} gold.".format(t.color(noun, 'green'),t.color(50, 'yellow'))
					elif (noun == "ration"):
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= 25):
							self.player.gold -= 25
							self.player.inventory.append([noun,0,"",""])
							self.response = " You purchase {} for {} gold.".format(t.color(noun, 'green'),t.color("25", 'yellow'))
					elif (noun == "steak"):
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= 100):
							self.player.gold -= 100
							self.player.inventory.append([noun,0,"",""])
							self.response = " You purchase {} for {} gold.".format(t.color(noun, 'green'),t.color("100", 'yellow'))
					else:
						self.response = " You lack the funds for this purchase."
						if (self.player.gold >= (Item(noun,self.player.level,"","").level * 25)):
							self.player.gold -= (Item(noun,self.player.level,"","").level * 25)
							self.player.inventory.append([noun,self.player.level,"",""])
							self.response = " You purchase {} for {} gold.".format(t.color(Item(noun,self.player.level,"","").fullName, 'green'),t.color((Item(noun,self.player.level,"","").level * 25), 'yellow'))
		return self.response
	
	# allows player to sell items
	def sell(self, noun):
		self.response = " You can only sell items in "+t.color("Crud town", 'green')+"."
		# checks if player is in crud town
		if (self.player.location == "Crud town"):
			self.response = " That item is not in your backpack."
			# checks if player has the item
			for i in range(len(self.player.inventory)):
				if (noun == Item(*self.player.inventory[i]).fullName):
					# depending on item sold player gets an amount of gold back
					if (Item(*self.player.inventory[i]).type != "grabbable" and Item(*self.player.inventory[i]).type != "food" and Item(*self.player.inventory[i]).type != "travel" and Item(*self.player.inventory[i]).type != "healing" and Item(*self.player.inventory[i]).type != "tome" and Item(*self.player.inventory[i]).type != "gem"):
						sellGold = (Item(*self.player.inventory[i]).stats[0] + Item(*self.player.inventory[i]).stats[1] + Item(*self.player.inventory[i]).stats[2] + Item(*self.player.inventory[i]).stats[3] + Item(*self.player.inventory[i]).stats[4])
						self.player.gold += sellGold
						self.response = " You sold "+t.color(noun, 'green')+" for "+t.color(sellGold, 'yellow')+" gold."
						self.player.inventory.remove(self.player.inventory[i])
						break
					elif (noun == "junk"):
						self.player.inventory.remove(self.player.inventory[i])
						self.player.gold += 1
						self.response = " You sold "+t.color(noun, 'green')+" for "+t.color("1", 'yellow')+" gold."
						break
					elif (Item(noun).type == "gem"):
						self.player.gold += Item(*self.player.inventory[i]).key
						self.response = " You sold "+t.color(noun, 'green')+" for "+t.color(str(Item(*self.player.inventory[i]).key), 'yellow')+" gold."
						self.player.inventory.remove(self.player.inventory[i])
					else:
						self.player.gold += 25
						self.response = " You sold "+t.color(noun, 'green')+" for "+t.color("25", 'yellow')+" gold."
						self.player.inventory.remove(self.player.inventory[i])
						break
		return self.response

	# allows the player to look at an item's description
	def examine(self, noun):
		self.response = " You don't have that item."
		for i in range(len(self.player.inventory)):
			if (noun == Item(self.player.inventory[i]).fullName):
				self.response = " "+Item(self.player.inventory[i]).desc
		return self.response
	
	# allows the player to return to the cabin area without using a rope
	def recall(self):
		area = Area("Cabin")
		self.room = area.rooms[0]
		self.player.room = area.rooms[0]
		self.player.location = "Cabin"
		# resets boss spawn
		self.player.boss = True
		spentXp = self.player.xp
		# heals player based on how much xp they have
		self.player.hp += self.player.xp * 5
		if (self.player.hp > self.player.stats["MaxHP"]):
			self.player.hp = self.player.stats["MaxHP"]
		# sets player xp back to zero
		self.player.xp = 0
		self.response = " You expend "+t.color(spentXp, 'blue')+" xp to return to your cabin and "+t.color("heal", 'red')+"."
		return self.response

	# shows player the possible commands and which ones need a noun as well as other tips 
	def help(self):
		self.response = " Commands: "
		for i in range(len(verblist)):
			self.response += verblist[i] + " "
		self.response += "\n Needs a noun: "
		for i in range(len(neednouns)):
			self.response += neednouns[i] + " "
		self.response += "\n Combat only: "
		for i in range(len(combatVerbs)):
			self.response += combatVerbs[i] + " "
		self.response += "\n Use a rope and return to the cabin and try to explore new places."
		self.response += "\n Shortcut commands are 'l' for look and 'a', 's', 'd', 'w' for changing rooms."
		self.response += "\n Stamina affects your damage and at 0% actions will cost " + t.color("hp", 'red') + "."
		return self.response
	
	# allows the player to turn voice commands on and off 
	def voice(self):
		# checks if player has internet access as its required 
		def internet(host='8.8.8.8', port=53, timeout=3):
			try:
				socket.setdefaulttimeout(timeout)
				socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
				return True
			except Exception as ex:
				print ex.message
				return False
		# keeps voice commands off if there is no internet connection
		if (internet() == False):
			self.player.voice = False
			self.response = " Voice commands require an internet connection."
		else:
			if (self.player.voice == True):
				self.player.voice = False
				self.response = " You have deactivated voice commands."
			else:
				self.player.voice = True
				self.response = " You have activated voice commands."
		return self.response
	
	# allows the player to recover stamina to full without an item and requires player to be in the cabin area
	def sleep(self):
		if (self.player.location == "Cabin"):
			self.response = " You sleep and recover your stamina."
			self.player.stamina = 100
		else:
			self.response = " You can't sleep here."
		return self.response

	def flee(self):
		if (self.player.combat == True):
			self.player.stamina -= 2
			escape = False
			if (random.randint(1, 1001)+(self.player.insanity * 5) < 500):
				self.player.combat = False
				self.player.target = None
				for i in range(len(self.room.exits)):
					if(len(self.room.locations[i].enemies) == 0):
						self.room, self.player.room = self.room.locations[i], self.room.locations[i]
						break
				self.response =  " You flee the fight and escape into a safe area."
			else:
				self.response = " You failed to flee the fight."
				self.enemyDmg()
				self.response += "\n While attempting to escape, the " + t.color(self.player.enemy.name, 'green') + " attacked you. \n You received " + t.color(int(edealt), 'red') + " points of health damage."
				if (self.player.hp <= 0): # checks if player is dead
					self.response += "\n You have died."
					self.deadPlayer()
		else:
			self.response = " You can only flee from a fight."
		return self.response
	
	def enemyDmg(self):
		for i in range(len(self.player.target)):
			ability = random.choice(self.player.target[i].abilities)
			self.response += "\n " + str(self.player.target[i].name) + " used " + str(ability) + "."
			if (npcAbilityDefs().enemyAbility[ability]["dmgType"] != "heal"):
				if (npcAbilityDefs().enemyAbility[ability]["dmgType"] == "physical"): #checks damage type
					damage = self.player.target[i].stats[0]
					if (npcAbilityDefs().enemyAbility[ability]["omni"] == True): #if omni is true combines enemy's physical and magical attack
						damage += self.player.target[i].stats[1]
					damage = int(damage * (1 + (npcAbilityDefs().enemyAbility[ability]["scale"] / 100))) # increases damage based on the ability's scale stat
					damage = damage * (1 / (2 ** (self.player.stats["meleeDef"] / 100))) # reduces damage based on the player corresponding defensive stat
				elif (npcAbilityDefs().enemyAbility[ability]["dmgType"] == "magic"):
					damage = self.player.target[i].stats[1]
					if (npcAbilityDefs().enemyAbility[ability]["omni"] == True):
						damage += self.player.target[i].stats[0]
					damage = int(damage * (1 + (npcAbilityDefs().enemyAbility[ability]["scale"] / 100)))
					damage = damage * (1 / (2 ** (self.player.stats["mageDef"] / 100))) # reduces damage based on the player corresponding defensive stat
				crit = random.randint(0,100)
				if ( crit <= (self.player.target[i].crit + npcAbilityDefs().enemyAbility[ability]["crit"])): #doubles damage if critical hit
					damage *= 2
					self.response += "\n" + str(self.player.target[i].name) + " landed a critical hit."
				self.player.hp -= int(damage)
				if (self.player.hp <= 0):
					self.deadPlayer()
				self.response += "\n You took " + t.color(str(int(damage)), 'yellow') + " points of physical damage."
				lifestolen = int(damage * (npcAbilityDefs().enemyAbility[ability]["life-steal"] / 100))
				if (lifestolen > 0):
					self.player.target[i].life += lifestolen
					self.response += "\n " + str(self.player.target[i].name) + "has stolen " + t.color(str(lifestolen), 'red') + " hp from you."
				if (random.randint(0,100) <= (self.player.target[i].statusChance + npcAbilityDefs().enemyAbility[ability]["statChance"])):
					poison = self.player.target[i].atkStatus[0] + npcAbilityDefs().enemyAbility[ability]["status"][0]
					if (poison > 0):
						self.player.status[0] += poison
						self.response += "\n You have been poisoned!"
					fire = self.player.target[i].atkStatus[1] + npcAbilityDefs().enemyAbility[ability]["status"][1]
					if (fire > 0):
						self.player.status[1] += fire
						self.response += "\n You are on fire!"
			else:
				heal = self.player.target[i].stats[0] + self.player.target[i].stats[1]
				self.player.target[i].life += heal
				self.response += "\n" + str(self.player.target[i].name) + " recovered " + str(int(heal)) + " hitpoints!"
	
	def playerLevel(self):
		self.player.xp -= self.player.levelxp # removes xp for level leaving the player with extra xp
		self.player.levelxp += 5 + self.player.level
		self.player.level += 1
		if (self.player.level < 150):
			if (self.player.level % 10 == 0): # every 10 levels grants an extra life
				self.player.life += 1
		# uses the player.growth array to increase players stats with each level
		self.player.stats["MaxHP"] += self.player.growth[4]
		self.player.stats["meleeAtk"] += self.player.growth[0]
		self.player.stats["mageAtk"] += self.player.growth[1]
		self.player.stats["meleeDef"] += self.player.growth[2]
		self.player.stats["mageDef"] += self.player.growth[3]
		self.player.maxMana += self.player.growth[5]
		if(self.player.stamina < 100):
			self.player.stamina = 100
		self.player.hp = self.player.stats["MaxHP"]
	
	def ItemDrop(self,quality):
		if (quality == "gold"):
			temp = ItemDefs().gear.keys()
			temp1 = ItemBuffDefs().prefix.keys()
			temp2 = ItemBuffDefs().suffix.keys()
			temp3 = (random.choice(temp),random.randint(Area(self.player.location).levels[0],Area(self.player.location).levels[1]),random.choice(temp1),random.choice(temp2))
			self.room.doItem(temp3[0],temp3[1],temp3[2],temp3[3])
			return "level " + str(temp3[1]) + " " + temp3[2] + " " + temp3[0] + " " + temp3[3]
		elif (quality == "silver"):
			temp = ItemDefs().gear.keys()
			temp1 = ItemBuffDefs().prefix.keys()
			temp2 = ItemBuffDefs().suffix.keys()
			if (random.randint(0,1) == 0):
				temp3 = (random.choice(temp),random.randint(Area(self.player.location).levels[0],Area(self.player.location).levels[1]),random.choice(temp1))
				self.room.doItem(temp3[0],temp3[1],temp3[2],"")
				return "level " + str(temp3[1]) + " " + temp3[2] + " " + temp3[0]
			else:
				temp3 = (random.choice(temp),random.randint(Area(self.player.location).levels[0],Area(self.player.location).levels[1]),"",random.choice(temp2))
				self.room.doItem(temp3[0],temp3[1],temp3[2],temp3[3])
				return "level " + str(temp3[1]) + " " + temp3[0] + " " + temp3[3]
		elif (quality == "bronze"):
			temp = list(ItemDefs().gear.keys())
			temp.extend(["potion","rope","homestone"])
			temp1 = random.choice(temp)
			temp2 = random.randint(Area(self.player.location).levels[0],Area(self.player.location).levels[1])
			if (temp1 in ItemDefs().gear):
				self.room.doItem(temp1,temp2,"","")
				return "level " + str(temp2) + " " + temp1
			else:
				self.room.doItem(temp1,0,"","")
				return temp1
	
	def deadEnemy(self, selection):
		gold = (self.player.target[selection].stats[0] + self.player.target[selection].stats[1] + self.player.target[selection].stats[2] + self.player.target[selection].stats[3] + (3 * self.player.target[selection].level)) # adds gold based on enemy stats
		self.player.gold += gold
		itemdrop = False
		if(self.player.target[selection].name in self.player.journal["kills"]):
			self.player.journal["kc"][self.player.journal["kills"].index(self.player.target[selection].name)] += 1
		else:
			self.player.journal["kills"].append(self.player.target[selection].name)
			self.player.journal["kc"].append(1)
		quality = "consumable"
		dropAdd = int(self.player.target[selection].drop[-1]) * 5
		dropChance = random.randint(1, 1001) + dropAdd + (self.player.insanity * 10)
		if (dropChance > 900): # 10 percent item drop chance (random.randint(1, 1001) > 400): chance increases with insanity
			itemdrop = True
			quality = "gold"
		elif (dropChance >= 650): # 10 percent item drop chance (random.randint(1, 1001) > 400): chance increases with insanity
			itemdrop = True
			quality = "silver"
		elif (dropChance >= 350):
			itemdrop = True
			quality = "bronze"
		if (itemdrop == True):
			item = self.ItemDrop(quality)
			self.response += "\n The level {} {} has been killed, and dropped {}.".format(self.player.target[selection].level, t.color(self.player.target[selection].name, 'green'),t.color(item, 'green'))
		else:
			self.response += "\n The level {} {} has been killed.".format(self.player.target[selection].level, t.color(self.player.target[selection].name, 'green'))
		self.room.enemies.remove([self.player.target[selection].name, self.player.target[selection].level, self.player.target[selection].buff]) # removes enemy from room
		self.response += "\n You got {} gold pieces.".format(t.color(gold, 'yellow'))
		self.player.xp += self.player.target[selection].xp
		while (self.player.xp >= self.player.levelxp): # checks if the player has enough xp to level up
			self.playerLevel()
			#if (self.player.stamina < 100): # refills stamina upon level up if it is not at 100
			#	self.player.stamina = 100
		spawn = True
		# checks if the rooms are empty (spawns boss at random points(usually when cleared from beginning to a dead end, but guaranteed to spawn if all rooms are cleared)
		for i in range(len(self.room.locations)):
			temp = self.room.locations[i]
			if (temp.enemies != []):
				spawn = False
		if (spawn == True):
			if (self.player.boss == False):
				self.response += "\n The area boss has spawned."
				self.player.boss = True #prevents boss from spawning again
				x = int(Area(self.player.location).levels[0])
				y = int(Area(self.player.location).levels[1])
				z = random.randint(x,y)
				x1 = random.randint(0,100)
				y1 = ["berserk", "rabid", "divine", "profane", "corrupted", "fiery", "icy", "electric", "dirty", "educated", "poisonous", "spiteful", "juggernaut", "plagued", "treasure", "mystical", "armored", "warded"]
				if(x1 <= 90):
					self.room.doEnemy(str(Area(self.player.location).boss), int(z),"")
				else:
					self.room.doEnemy(str(Area(self.player.location).boss), int(z), random.choice(y1))
		souls = self.player.target[selection].drop.split()
		souls = int(souls[1])
		souls = souls * self.player.target[selection].level
		self.player.souls += souls
		self.response += "\n You've been awarded " + t.color(str(souls), 'red') + " souls."
		del self.player.target[selection]
		if(len(self.player.target) <= 0):
			self.player.combat = False
			self.player.target = None
	
	def deadPlayer(self):
		self.response += "\n You have died."
		self.player.insanity += 1
		self.player.life -= 1
		self.player.target = None
		self.player.combat = False
		self.player.hp = self.player.stats["MaxHP"]
		self.player.stamina = 100
		self.player.mana = self.player.maxMana
	
	def attack(self):
		selection = raw_input("pick an enemy to attack!")
		selection = int(selection) - 1
		if (self.player.combat == False): 
			self.response = " You can only use weapon attacks in combat."
		if (self.player.combat == True):
			self.response = " Invalid selection."
			self.response = " You attack level "+ str(self.player.target[selection].level) + " " + t.color(self.player.target[selection].name, 'green') + " with your weapon."
			pDealt = self.player.stats["meleeAtk"]
			pDealt = pDealt * pDealt
			pDealt = pDealt / self.player.target[selection].stats[2]
			pDealt = pDealt * ((self.player.stamina) + 300)
			pDealt = pDealt / 400.0
			self.player.target[selection].life -= pDealt
			self.response += "\n You dealt " + t.color(int(pDealt), 'yellow') + " physical damage."
			self.enemyDmg()
			if (self.player.target[selection].life <= 0): # checks if the npc has died
				self.deadEnemy(selection)
			if (self.player.hp <= 0): # checks if player is dead
				self.deadPlayer()
		return self.response

	def spell(self):
		self.response = ""
		print "Your available spells are: " + str(self.player.abilities) + "\n"
		pAbility = raw_input("What spell will you cast? ")
		if (pAbility in self.player.abilities):
			if(AbilityDefs().ability[pAbility]["manaCost"] <= self.player.mana):
				if(self.player.combat == True):
					if(AbilityDefs().ability[pAbility]["dmgType"] == "heal"):
						self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
						heal = int(self.player.stats["mageAtk"] * AbilityDefs().ability[pAbility]["scale"])
						self.player.hp += heal
						self.player.status[0] += AbilityDefs().ability[pAbility]["status"][0]
						self.player.status[1] += AbilityDefs().ability[pAbility]["status"][1]
						self.response = "You healed yourself for " + t.color(str(heal), 'red') + " hitpoints."
						if(self.player.hp > self.player.stats["MaxHP"]):
							self.player.hp = self.player.stats["MaxHP"]
						self.enemyDmg()
					if(AbilityDefs().ability[pAbility]["dmgType"] == None):
						self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
						self.player.status[2] = AbilityDefs().ability[pAbility]["scale"]
						self.player.status[0] += AbilityDefs().ability[pAbility]["status"][0]
						self.player.status[1] += AbilityDefs().ability[pAbility]["status"][1]
					if(AbilityDefs().ability[pAbility]["dmgType"] == "physical"):
						selection = raw_input("choose a target!")
						selection = int(selection)
						self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
						self.enemyDmg()
						pDealt = self.player.stats["meleeAtk"]
						pDealt = pDealt * pDealt
						pDealt = pDealt / self.player.target[selection].stats[2]
						pDealt = pDealt * ((100 + AbilityDefs().ability[pAbility]["scale"])/100)
						self.player.hp += pDealt * (((100 + AbilityDefs().ability[pAbility]["life-steal"])/100)-1)
						if(random.randint(1,100) > (100 - AbilityDefs().ability[pAbility]["crit"])):
							pDealt = int(pDealt * 2)
							self.response += "\nCritical Hit!"
						if(AbilityDefs().ability[pAbility]["status"][0] > 0 or AbilityDefs().ability[pAbility]["status"][1] > 0):
							if(random.randint(1,100) < AbilityDefs().ability[pAbility]["statChance"] + 1):
								self.player.target[selection].status = AbilityDefs().ability[pAbility]["status"]
								self.response += "\nThe " + t.color(str(self.player.target.name),'green') + " has been afflicted with an ailment."
						self.player.target.life -= pDealt
						if(self.player.target.life <= 0):
							self.deadEnemy(0)
						self.response += "\nYour spell dealt " + str(int(pDealt)) + " physical damage."
					if(AbilityDefs().ability[pAbility]["dmgType"] == "magic"):
						selection = raw_input("choose a target!")
						selection = int(selection)
						self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
						self.enemyDmg()
						pDealt = self.player.stats["mageAtk"]
						pDealt = pDealt * pDealt
						pDealt = pDealt / self.player.target[selection].stats[3]
						pDealt = pDealt * ((100 + AbilityDefs().ability[pAbility]["scale"])/100)
						self.player.hp += pDealt * (((100 + AbilityDefs().ability[pAbility]["life-steal"])/100)-1)
						if(random.randint(1,100) > (100 - AbilityDefs().ability[pAbility]["crit"])):
							pDealt = int(pDealt * 2)
							self.response += "\nCritical Hit!"
						if(AbilityDefs().ability[pAbility]["status"][0] > 0 or AbilityDefs().ability[pAbility]["status"][1] > 0):
							if(random.randint(1,100) < AbilityDefs().ability[pAbility]["statChance"] + 1):
								self.player.target[selection].status = AbilityDefs().ability[pAbility]["status"]
								self.response += "\nThe " + t.color(str(self.player.target.name), 'green') + " has been afflicted with an ailment."
						self.player.target[selection].life -= pDealt
						if(self.player.target[selection].life <= 0):
							self.deadEnemy()
						self.response += "\nYour spell dealt " + str(int(pDealt)) + " magic damage."
				else:
					if(AbilityDefs().ability[pAbility]["combatOnly"] == True):
						self.response = "You can only use this spell in combat."
					else:
						if(AbilityDefs().ability[pAbility]["dmgType"] == None):
							self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
							self.player.status[2] = AbilityDefs().ability[pAbility]["scale"]
							self.player.status[0] += AbilityDefs().ability[pAbility]["status"][0]
							self.player.status[1] += AbilityDefs().ability[pAbility]["status"][1]
						elif(AbilityDefs().ability[pAbility]["dmgType"] == "heal"):
							self.player.mana -= AbilityDefs().ability[pAbility]["manaCost"]
							heal = int(self.player.stats["mageAtk"] * AbilityDefs().ability[pAbility]["scale"])
							self.player.hp += heal
							self.response = "You healed yourself for " + t.color(str(heal), 'red') + " hitpoints."
							if(self.player.hp > self.player.stats["MaxHP"]):
								self.player.hp = self.player.stats["MaxHP"]
			else:
				self.response = "You do not have enough " + t.color("mana", 'blue') + "."
		else:
			self.response = "You don't have that spell."
		#self.response = AbilityDefs().ability["magic dart"]["dmgType"]
		return self.response

	def heal(self):
		if (self.player.combat == True):
			self.player.stamina -= 2
			self.response = " You use a potion and heal yourself."
			Engine.use(self,"potion")
		if (self.player.combat == False):
			self.response = " You cannot do this outside of combat."
		return self.response

	#lets the player recover stamina by expending xp
	def rest(self):
		self.response = " You take a break and rest."
		while(self.player.stamina <= 100 & self.player.xp > 0):
			self.player.stamina += 10
			self.player.xp -= 1
		if (self.player.stamina >= 100):
			self.player.stamina = 100
		return self.response
	
	def check(self, noun):
		self.response = " Here is(are) the noun(s): " + str(noun)
		return self.response
	#prints the player's journal(story notes/monster kills/player notes)
	def journal(self):
		self.response = ""
		#if player has 10 or more insanity a string is added
		insanity2 = ["It itches, even my blood itches.\n", "There are fairies everywhere, I see their little lights everywhere. They just won't let me catch them.\n", "Buzzing, buzzing, thats all the bees do. Buzz. Buzz. Buzz.\n", "AAAAh! The smell, everywhere stinks, the world is polluted with the smell of rotted corpses.\n", "Blood, nothing but blood in my mouth. The taste is unbearable.\n"] # 5 senses
		if(self.player.insanity >= 3):
			self.response += insanity2[random.randint(0,4)]
		#if the player has used any notes they will appear here
		for i in range(len(self.player.journal["quest"])):
			self.response += " " + str(self.player.journal["quest"][i]) + "\n"
		#displays the players number of actions performed
		self.response += "Actions performed: " + str(self.player.actions) + "\n"
		#displayers the monster kills
		self.response += " Monster kills: \n"
		if (self.player.journal["kills"] != []):
			i = 0
			for i in range(len(self.player.journal["kills"])):
				self.response += (" " + str(self.player.journal["kills"][i]) + " | " + str(self.player.journal["kc"][i]) + "\n")
		#displays the players previously added notes to self
		self.response += " Notes to self: \n"
		if (self.player.journal["notes"] != []):
			for i in range(len(self.player.journal["notes"])):
				self.response += (" " + str(self.player.journal["notes"][i]) + "\n")
		x = raw_input("Add a note: ")
		if (x != ""):
			self.player.journal["notes"].append(x)
		#changes the characters to be displayed in the response with a frequency relevant to the players insanity
		if(self.player.insanity>0):
			rateOfChange = (100/(self.player.insanity*5))
			if (rateOfChange < 1):
				rateOfChange = 1
			for i in range(len(self.response)):
				if(i%rateOfChange == 0):
					charVal = ord(self.response[i])
					charVal = charVal/2 + 26
					self.response = self.response[:i] + chr(charVal) + self.response[i+1:]
		return self.response
	
	combatVerbs = [ "flee", "spell", "attack", "heal" ]
	neednouns = [ "go", "take", "fight", "drop", "use", "equip", "explore", "buy", "sell", "examine" ]
	verblist = [ "journal", "go", "look", "take", "stats", "fight", "drop", "use", "equip", "explore", "buy", "recall", "sell", "examine", "help", "sleep", "voice", "rest", "flee", "heal", "attack", "spell", ""]
	verbs = {
		"journal" : journal,
		"go" : go,
		"look" : look,
		"take" : take,
		"stats" : stats,
		"fight" : fight,
		"check" : check,
		"drop" : drop,
		"use" : use,
		"equip" : equip,
		"explore" : explore,
		"recall" : recall,
		"buy" : buy,
		"sell" : sell,
		"examine" : examine,
		"help" : help,
		"voice" : voice,
		"sleep" : sleep,
		"rest" : rest,
		"attack" : attack,
		"spell" : spell,
		"flee" : flee,
		"heal" : heal,
		"" : error
	}

	def requiresNoun(self, verb):
		for i in range(len(neednouns)):
			if(verb == neednouns[i]):
				return True
		return False

	def query(self, verb, noun=None, insanity=False):
		for i in range(len(verblist)): # iterate through all of our recognized verbs
			if(verb == verblist[i]): # check if our verb matches one of the indexs
				if(self.player.combat == True):
					for i in range(len(combatVerbs)):
						if(verb == combatVerbs[i]):
							self.response = verbs[verb](self) if (noun == None) else verbs[verb](self, noun)
							break
						elif(verb != combatVerbs[i]):
							self.response = " You cannot " + t.color(verb, 'red') + " while in combat."
				elif (self.player.combat == False):
					self.response = verbs[verb](self) if (noun == None) else verbs[verb](self, noun)
				if (insanity == True):
					self.response += "\n The voices stop and your vision clears."
				return self.response
		return self.error()