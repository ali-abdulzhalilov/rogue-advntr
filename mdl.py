from time import sleep
from stuff import *
		
class State(object):

	def __init__(self, level_filepath, entities,):
		self.map = self.load_map(level_filepath)
		self.entities = entities
		print('state init')
	
	def getXY(self, x, y):
		if y<0 or y>=len(self.map) or x<0 or x>=len(self.map[y]):
			return ' '
		else:
			return self.map[y][x]
			
	def display(self):
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				ch = self.map[y][x]
				for entity in [x for x in self.entities if isinstance(x, Person)]:
					if entity.x == x and entity.y == y and entity.health > 0:
						ch = entity.ch
				print(ch, end=' ')
			print()
		
	def load_map(self, filepath):
		file = open(filepath)
		
		tmp = []
		for line in file.read().split('\n'):
			tmp.append([x for x in line])
			
		return tmp
		
class Scene(object):

	def __init__(self):
		self.inp = ' '
	
	def loop(self): 
		self.update()
		self.display()
		self.inp = input(">: ")
		if self.inp == 'p':
			sleep(1)
			
	def update(self):
		pass
		
	def display(self):
		pass
		
	def clear(self):
		print('\n'*20)
		
class GameScene(Scene):

	def __init__(self, state):
		super(GameScene, self).__init__()
		self.state = state
	
	def update(self):
		for entity in self.state.entities:
			entity.update(self)
			
	def display(self):
		self.clear();
		
		self.state.display()
		
		for entity in self.state.entities:
			entity.display(self)
			
		print("nw n ne\n w + e \nsw s se")