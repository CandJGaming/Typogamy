import os
import sys
import pickle
import random
import threading
import time
import multiprocessing

from objects import Player
from objects import Enemy
from objects import Item
from objects import Music

from map import Room
from map import Area

from utility import Text
from utility import Engine

from termcolor import colored

import pkgutil

from playsound import playsound

from multiprocessing import Process

import speech_recognition as sr
import socket
import sys

global p, t, rtitle # instances of Player class and Text class
p = "first"

def music():
	while (True):
		if(p == "first"):
			time.sleep(.1)
			playsound("Song2.wav")
		elif(p.hp <= p.stats["MaxHP"]/5):
			playsound('Song1.wav')
		else:
			time.sleep(.1)
			playsound(Area(p.location).song)
area = Area("old town")
## START THE GAME!!! #
# a line return for beauty
print "\n"
m = Music(target=music)
m.start()
# instances for voice recognition
playerVoice = sr.Recognizer()
mic = sr.Microphone()
playerList = {}
name = raw_input("  What is your name? ").title()
#global p, t, rtitle # instances of Player class and Text class
def createGame(name):
	global p, e, t, rtitle
	try: # attempts to load the player's save file
		with open(name + ".txt", 'r') as filehandler:
			print " Loading Game."
			p = pickle.load(filehandler)
			e, t = Engine(p), Text(p)
			rtitle = t.color(' Reponse:', 'yellow')
			p.voice = False
			print " returning variables"
			return p, e, t, rtitle
	except: # if loading the save file didn't work or doesn't exist a new file/game is started
		print " New Game."
		p = Player(2, 0, area.rooms[0]) # create an instance of Player
		e, t = Engine(p), Text(p) # create an instance of Text and Engine
		rtitle = t.color(' Response:', 'yellow')
		p.name = name
		print " Starting new game."
		x = ""
		# allows the player to have some control over stat growth
		while (True):
			x = raw_input("  Sword or Shield? ").title()
			if (x == "Shield"):
				print "  Your Defence Scaling has increased."
				p.growth[2] += 1
				p.stats["meleeDef"] += 2
				p.growth[3] += 1
				p.stats["mageDef"] += 2
				p.growth[4] += 4
				p.hp += 8
				p.stats["MaxHP"] += 8
				break
			if (x == "Sword"):
				print "  Your Offense scaling has increased."
				p.growth[0] += 2
				p.stats["meleeAtk"] += 4
				p.growth[1] += 2
				p.stats["mageAtk"] += 4
				p.growth[4] += 1
				p.hp += 2
				p.stats["MaxHP"] += 2
				break
		while (True):
			x = raw_input("  Staff or Greatsword? ").title()
			if (x == "Staff"):
				print "  Your Magic scaling has increased."
				p.growth[4] += 1
				p.stats["MaxHP"] += 2
				p.hp += 2
				p.growth[1] += 3
				p.stats["mageAtk"] += 4
				p.growth[3] += 2
				p.stats["mageDef"] += 4
				p.growth[5] += 2
				p.mana += 4
				p.maxMana += 4
				p.abilities.append("magic dart")
				return p, e, t, rtitle
				break
			if (x == "Greatsword"):
				print "  Your Physical scaling has increased."
				p.growth[4] += 3
				p.stats["MaxHP"] += 6
				p.hp += 6
				p.growth[0] += 4
				p.growth[1] -= 2
				p.stats["meleeAtk"] += 4
				p.growth[2] += 2
				p.stats["meleeDef"] += 4
				p.abilities.append("accurate swing")
				return p, e, t, rtitle
				break

createGame(name)
no_use = os.system("cls")
print "QUICK GUIDE:\n 'look' to see what is in the room. 'go' followed by a cardinal direction to change rooms(available rooms indicated by compass.\n \
'stats' to view your stats. 'take' followed by an item in the room to pick up the item.\n 'fight' followed by an enemy in the room to enter combat with the enemy.\n \
'drop' followed by an item in your inventory drops the item in the room. 'use' followed by a usable item in your inventory will use the item.\n \
'equip' followed by an equippable item in your inventory to equip the item.\n 'explore' followed by an explorable location while in town or your cabin to go to a new area.\n \
'buy' while in town followed by a buyable item will let you buy that item if you have the gold.\n 'sell' followed by an inventory item will sell that item.\n \
'examine' followed by an inventory item will give you a description of that item. 'recall' expends your xp for hp and returns you to your cabin.\n \
'help' will give you a list of commands. 'voice' toggles voice commands(requires internet connection).\n 'sleep' restores stamina, but can only be done in the cabin.\n \
'flee' will allow you to escape combat if you think you may die. 'attack' deals dmg based on physical stats.\n 'spell' deals magic damage based on mage stats.\n \
After choosing to attack or a spell to cast you will be required to select a target. Choose the enemy to attack by their position, with 1 being the first enemy. \n \
'heal' in combat will consume a potion and heal you.\n 'rest' unlike sleep can be done anywhere but wont give you full stamina(unless you have enough xp).\n \
'journal' allows you to read your journal and leave notes to yourself.\n Dying with too few lives will delete your save.\n \
'w','a','s','d' can be used to more quickly navigate dungeons."
x = raw_input(" Press Enter to Continue")
# saves the character file
with open(p.name + ".txt", 'w+') as filehandler:
	pickle.dump(p, filehandler)

#variables for temp data
global first, verb, noun
first = True
# play forever (well, at least until the player dies or asks to quit) 
while (True): # set the status so the player has situational awareness 
	# save game after every command
	e.status()
	if(p.hp <= 0):
		if(p.combat == True):
			p.combat = False
		p.hp = p.stats["MaxHP"]
		p.status = [0,0,0]
		p.life -= 1
		p.insanity += 1
		p.mana = p.maxMana
	if(p.life > -1):
		with open(p.name + ".txt", 'w+') as filehandler:
			pickle.dump(p, filehandler)
			
	else:
		no_use = os.system("cls")
		print t.color("You Have Died, Permanently!", 'red')
		m.kill()
		os.remove(p.name + ".txt")
		time.sleep(5)
		m.join()
		sys.exit(0)
	# clear the display - preferred version for windows
	no_use = os.system("cls")
	
	if(p.name == "Arithmancer"):
		p.insanity = 0
		p.stamina = 200
		p.mana = p.maxMana
		p.life = 99
	
	if(not first):
		e.response = "\n{}{}".format(rtitle, e.response) 
	# print ascii header, with inline if / ternary to emulate the current compass for navigation
	t.header() # pass currentRoom into the header to format compass
	print colored("\n Player Status - {}\n{}".format(p.name, t.color(t.playerData(), 'cyan' if p.hp > p.stats["MaxHP"] * .25 else 'red')), 'white' if p.hp > p.stats["MaxHP"] * .25 else 'red')
	if(p.status[0]>0):
		print t.color("\n You are poisoned.", 'magenta', 'blink')
	if(p.status[1]>0):
		print t.color("\n You are burning.", 'red', 'concealed')
	if(p.status[2]>0):
		print t.color("\n Your health is recovering.", 'blue', 'blink')
	# check if there is any additional text in the response, if so, display response
	if(not first):
		print e.response
	# prompt for player input: the game supports a simple language of <verb> <noun>
	# valid verbs are go, look, and take; valid nouns depend on the verb
	# we use raw_input here to treat the input as a string instead of a int
	if (p.voice == True):
		print " What will you do? "
		with mic as source:
			playerVoice.adjust_for_ambient_noise(source)
			audio = playerVoice.listen(source)
		try:
			action = playerVoice.recognize_google(audio)
		except sr.RequestError:
			action = " "
		except sr.UnknownValueError:
			action = " "
	else:
		if(p.combat == False):
			action = raw_input(" What will you do? ")
			p.stamina -= 1
			if(p.stamina < 0):
				p.stamina = 0
			p.actions += 1
		if(p.combat == True):
			p.stamina -= 1
			if(p.stamina < 0):
				p.stamina = 0
			p.actions += 1
			action = raw_input(" You are in combat. What will you do? ")
	# set the user's input to lowercase, which is parsed more easily
	action = action.lower()

    # exit the game if the player wants to leave (supports quit, # exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		m.kill()
		print "Goodbye! \n [*] Closing Game [*]"
		m.join()
		sys.exit(0)

	# split the user input into words (words are separated by spaces)
	words = action.split()

	# the game only understands verb noun word inputs
	if (len(words) > 1): # isolate the verb and noun
		verb = words[0]
		if(e.requiresNoun(verb)):
			words.pop(0)
			iNoun = ""
			if(len(words) > 1):
				for i in range(len(words)):
					iNoun += words[i] + " "
				combineWord = 0
				iNoun = iNoun.split()
				noun = ""
				for i in range(len(iNoun)):
					if (combineWord == 1):
						comineWord = 0
					else:
						if (iNoun[i] == "plate" or iNoun[i] == "scale" or iNoun[i] == "chain" or iNoun[i] == "star" or iNoun[i] == "home" or iNoun[i] == "great"):
							try:
								if(iNoun[i+1] == "mail" or iNoun[i+1] == "sword" or iNoun[i+1] == "burst" or iNoun[i+1] == "stone"):
									noun += str(iNoun[i] + iNoun[i + 1] + " ")
									combineWord = 1
							except:
								noun += str(iNoun[i] + " ")
						else:
							noun += str(iNoun[i] + " ")
							
				noun = noun[:-1]
			else:
				noun = words[0]
		else:
			noun = None
	elif(len(words) == 1):
		verb, noun = words[0], None
		if (e.requiresNoun(verb)):
			noun = ""
		if (verb == "l"):
			verb = "look"
		elif (verb == "w"):
			verb = "go"
			noun = "north"
		elif (verb == "a"):
			verb = "go"
			noun = "west"
		elif (verb == "s"):
			verb = "go"
			noun = "south"
		elif (verb == "d"):
			verb = "go"
			noun = "east"
	
	if(first):
		first = not first
	#if player has 0 stamina they lose 5% hp per action
	if (p.stamina == 0):
		p.hp -= p.stats["MaxHP"]/20
		if(p.hp <= 0):
			p.insanity += 1
			p.life -= 1
			p.hp = p.stats["MaxHP"]
			p.stamina = 100
			p.mana = p.maxMana
	
	try:
		# % chance to commit "random" action if check passes
		if (random.randint(0, 300) < p.insanity):
			iActions = ["look", "stats", "drop", "drop", "drop", "discard"]
			if (p.inventory == []):
				iActions = ["look", "rest", "stats"]
				finalAction = iActions[random.randint(0,2)]
			elif(p.combat == True):
				iActions = ["attack", "spell", "heal", "flee","heal", "heal"]
				finalAction = iActions[random.randint(0,5)]
			else:
				finalAction = iActions[random.randint(0,5)]
			if (finalAction == "drop" or finalAction == "discard"):
				e.query(finalAction, p.inventory[0], True)
			else:
				e.query(finalAction, None, True)
		else:
			# run a query based on whether or not we have a noun
			e.query(verb) if(noun == None) else e.query(verb, noun)
	except:
		response = "Ooops! Something went wrong."