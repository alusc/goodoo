class Globals:

	RATIO = 20 # ratio écran / grille
	FPS = 60 # images/boucles par seconde
	counter = 0 # compteur de boucle
	resolution = (1280,720)

	# COULEURS
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	GRAY = (76, 76, 76)
	RED = (255,0,0)
	YELLOW = (255,255,0)
	GREEN = (0,255,0)
	CYAN = (0,255,255)
	BLUE = (0,0,255)
	PURPLE = (255,0,255)

	# NIVEAU
	level = 0
	blocks = [] # liste qui stock des blocs de l'environnement

	# ENNEMIES
	enemies1 = [] # liste des ennemies de type 1
	enemies2 = [] # liste des ennemies de type 2
	enemies3 = [] # liste des ennemies de type 3
	enemies = [] # liste de tout les ennemies

	#PROJECTILES
	projectiles = [] # liste de tous les projectiles