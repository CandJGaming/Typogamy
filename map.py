import time

from defs import MapDefs
from defs import npcBuffs
from random import randint, choice

global directions, inverse
directions = [ "north", "south", "west", "east" ]
inverse = {
		"south" : "north",
		"north" : "south",
		"west" : "east",
		"east" : "west"
}
class Area(object): # an area object, holds many rooms and area-specific variables

	global info

	def __init__(self, name):
		# set your definition getters
		info = MapDefs()
		self.area = info.areas[name]
		self.buffs = ["berserk", "rabid", "divine", "profane", "corrupted", "fiery", "icy", "electric", "dirty", "educated", "poisonous", "spiteful", "juggernaut", "plagued", "treasure", "mystical", "armored", "warded"]
		# set all of these to a default list value
		self.name = name
		self.boss = self.area["boss"]
		self.song = self.area["song"]
		self.rooms, self.enemies, self.items = [], [], []
		self.max = randint(self.area["rooms"][0], self.area["rooms"][1]) # set the max amount of rooms, for us to index
		self.enemies = self.area["enemies"]
		self.levels = self.area["levels"]
		self.items = self.area["loot"]
		# add all the rooms, by spawning Room()s
		self.setupRooms()
	
	
	def buffs(self, value=None):
		if(value == None):
			return self._buffs
		self._buffs = value
	
	def levels(self, value=None):
		if(value == None):
			return self_levels
		self._levels = value
	
	def song(self, value=None):
		if(value == None):
			return self._song
		self._song = value
	
	def area(self, value=None):
		if(value == None):
			return self._area
		self._area = value
		
	def name(self, value=None):
		if(value == None):
			return self._name
		self._name = value
		
	def rooms(self, value=None):
		if(value == None):
			return self._rooms
		self._rooms = value
		
	def max(self, value=None):
		if(value == None):
			return self._max
		self._max = value
		
	def enemies(self, value=None):
		if(value == None):
			return self._enemies
		self._enemies = value
		
	def items(self, value=None):
		if(value == None):
			return self._items
		self._items = value
		
	def addRoom(self, room):
		self.rooms.append(room)
		
	# dynamic room setup, hard to write, op as hell
	def setupRooms(self):
		first, golden, original, limit = False, False, None, 0
		room = None
		# add all rooms to the list
		for i in range(self.max+1):
			golden = (first == False) & ((randint(0, 4) == 0) or i == (self.max+1))
			if(golden == True):
				first = True
			room = Room(golden)
			self.addRoom(room)
			if (self.items != None):
				room.doItem(choice(self.items),0)
			if (self.enemies != None):
				numEnemies = randint(1,3)
				for i in range(0,numEnemies):
					buffness = randint(0,100)
					if(buffness <= 90):
						room.doEnemy(choice(self.enemies), randint(self.levels[0],self.levels[1]),"")
					else:
						room.doEnemy(choice(self.enemies), randint(self.levels[0],self.levels[1]), choice(self.buffs))
		# setup each room with exits, use index to track first room
		for i in range(self.max+1):
			if(i < limit):
				i = limit
			if(limit < self.max+1): # we can decrement the amount of rooms to get an accurate number
				room = self.rooms[i] # easily accessible room object 
				direction = directions[randint(0, 3)] # our current direction for the default new room
				while room.checkExit(direction): # makes sure we get a good direction
					original = direction # this gets set to re-add it later
					directions.remove(original)
					direction = directions[randint(0, 2)]
					directions.remove(direction)
				limit = i+1 # set new limit
				if(limit < self.max+1): # new default extra room
					room.addExit(direction, self.rooms[limit])
				if(randint(0, 2) == 0): # random added room 
					if(limit < self.max):
						limit += 1 # increment by one
						room.addExit(directions[len(directions)-1], self.rooms[limit])
				directions.append(direction)
				if(original != None):
					directions.append(original)
			else:
				self.rooms[0].enemies = []
				break
				
class Room(object): # room object, can generate any number of these in an area

	def __init__(self, golden):
		self.golden = golden
		self.exits = []
		self.locations = []
		self.items = []
		self.enemies = []
		
	def golden(self, value=None):
		if(value == None):
			return self._golden
		self._golden = value

	def exits(self, value=None):
		if(value == None):
			return self._exits
		self._exits = value

	def locations(self, value=None):
		if(value == None):
			return self._locations
		self._locations = value

	def items(self, value=None):
		if(value == None):
			return self._items
		self._items = value
	
	def enemies(self, value=None):
		if(value == None):
			return self._enemies
		self._enemies = value
		
	# adds an exit to the room, the exit is a string (e.g., north), the room is an instance of a room
	def addExit(self, exit, room): # append the exit and room to the appropriate lists
		self.exits.append(exit)
		self.locations.append(room)
		# add room exits on the opposite side
		room.exits.append(inverse[exit])
		room.locations.append(self)
	
	# boolean, used to check if there is an exit in a direction
	def checkExit(self, direction):
		# check for valid exits in the current room
		for i in range(len(self.exits)): # this exits index exists in the array
			if (direction == self.exits[i]): # check if it matches our direction
				return True
				break
		return False
	
	def doItem(self, item, level=0, prefix="", suffix="",remove=False):
		if(remove == False):
			self.items.append([item, level,prefix,suffix])
		else:
			self.items.remove([item, level,prefix,suffix])
	
	def doEnemy(self, enemy, level,buff="", dead=False):
		if(dead == False):
			self.enemies.append([enemy, level, buff])
		else:
			self.enemies.remove([enemy, level, buff])
