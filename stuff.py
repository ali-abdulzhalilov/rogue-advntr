import random

class Entity(object):
	
	def __init__(self, ch, name, x, y):
		self.ch = ch
		self.name = name
		self.x = x
		self.y = y
		self.directions = {
			'n' :( 0,-1),
			's' :( 0, 1),
			'w' :(-1, 0),
			'e' :( 1, 0),
			'nw':(-1,-1),
			'ne':( 1,-1),
			'sw':(-1, 1),
			'se':( 1, 1)
		}
		
	def update(self, scene):
		pass
		
	def display(self, scene):
		pass
		
	def is_collide(self, scene):
		return scene.state.getXY(self.x+self.dx, self.y+self.dy) == "#"
		
	def is_touch(self, entities):
		for entity in entities:
			if entity != self and \
			   entity.x == self.x+self.dx and \
			   entity.y == self.y+self.dy:
				return entity
		return None
	
	def set_dir(self, dir):
		dx, dy = dir
		self.dx = dx
		self.dy = dy
	
	def move(self):
		self.x += self.dx
		self.y += self.dy

class Person(Entity):
	
	def __init__(self, ch, name, x, y):
		super(Person, self).__init__(ch, name, x, y)
		self.inventory = []
		self.health = 3
		self.max_health = 5
		self.dx = 0
		self.dy = 0
		
	def update(self, scene):
		if not self.is_collide(scene):
			thing = self.is_touch(scene.state.entities)
			if thing:
				if isinstance(thing, Person):
					thing.health -= 1;
			else:
				self.move()
	
	def display(self, scene):
		print(self.ch, end=' ')
		print(self.name+(10-len(self.name))*" ", end=' ')
		print("HP: ["+'|'*self.health+'-'*(self.max_health-self.health), end='] ') #str(self.health), end=' ')
		print(" on: "+scene.state.getXY(self.x, self.y))
		
	def print_inventory(self):
		print(self.inventory)
	
class Player(Person):
	
	def __init__(self, x, y):
		super(Player, self).__init__('@', 'Player', x, y)
		
	def update(self, scene):
		if scene.inp in self.directions:
			self.set_dir(self.directions[scene.inp])
			super(Player, self).update(scene)
				
class Walker(Person):
	
	def __init__(self, x, y):
		super(Walker, self).__init__('w', 'Walker', x, y)
		
	def update(self, scene):
		dir_name = random.choice(list(self.directions.keys()))
		self.set_dir(self.directions[dir_name])
		super(Walker, self).update(scene)
		
class Rusher(Person):
	
	def __init__(self, x, y, target):
		super(Rusher, self).__init__('r', 'Rusher', x, y)
		self.target = target
		
	def update(self, scene):
		dirs = {}
		for dir_name in self.directions:
			dx, dy = self.directions[dir_name]
			dirs[dir_name] = self.dist_to_target(dir_name)
			
		dir_name = min(dirs, key=dirs.get)
		self.set_dir(self.directions[dir_name])
		super(Rusher, self).update(scene)
		
	def dist_to_target(self, dir_name):
		STR_COST = 10
		DIAG_COST = 14
	
		dx, dy = self.directions[dir_name]
		mi = min(abs(self.x-self.target.x+dx), abs(self.y-self.target.y-dy))
		ma = max(abs(self.x-self.target.x+dx), abs(self.y-self.target.y-dy))
		
		return mi*STR_COST + (ma-mi)*DIAG_COST