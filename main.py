from mdl import *
from stuff import *

player = Player(1, 1)
state = State(
	"level0.txt",
	[
		player,
		Walker(3, 7),
		Rusher(2, 2, player)
	]
)

scene = GameScene(state)
	
def main():
	while scene.inp != 'q':
		scene.loop()
main()

'''
I want to:
	- fog of war
	- merchant
	- invertory
	- look, use, pick, talk, etc.
	- cell states (fire, water, etc.)
	- load/save
	- state onenter and onexit
	- logs and descriptions
	- controls
	- menu, game, options scenes
	- enemy ai
	- resourse manager
'''