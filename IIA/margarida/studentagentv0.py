from agent import *
from random import *
import collections
import math
from pickle import *
import time


class studentagentv0(Agent):
	def __init__(self, name, body, world):
		
		super().__init__(name, body, world)
				
		#Map Size
		self.mapsize=[60,40]
	
		#Save the last direction
		self.olddir = (0,0)
		
		#Save the last action
		self.lastAction = (0,0)
		
		#Save the last positions
		self.lastPositions = []

		self.path = []

		self.count = 0
		self.count2 = 0

		self.last_msg = b""

		#Pre-Processamento do mapa para tapar becos, retorna uma lista
		self.pp = Pre_Processing(self.world,list(self.world.size))
		self.iw = self.pp.imaginaryWalls()
		self.isLabyrinth = self.pp.labyrinth(self.iw, self)
		print(str(self.isLabyrinth))

	
	################################################## Responsavel pela acao que a snake toma ###############################################
	def chooseAction(self, vision, msg): 
		#start = time.time()
		####################### Inicialmente a ação da snake é aleatoria e a mensagem é vazia
		pesquisa = Pesquisa(self.world,vision,self.iw)
		head = self.body[0]        
		action = (0,0)
		recv_msg = msg
		
		if msg != b"":
			print("received message is: " + str(msg))
		#print("Dead Zones : ",self.iw)

		if self.isLabyrinth:
			action, msg = self.actionLabyrinth(vision, msg, pesquisa, head, action)
		else:
			action, msg = self.actionRegular(vision, msg, pesquisa, head, action)

		if msg == recv_msg or self.nutrients['S'] <= 400 or msg == self.last_msg:
			msg = b""

		self.last_msg = msg
		return action, msg

	def actionLabyrinth(self, vision, msg, pesquisa, head, action):
		#Listas separadas de comida movel e estatica
		S,M = self.pp.separateFoods(vision.food)

		if self.count2 > 3:
			validact = ACTIONS[:1]
			for act in ACTIONS[1:]:
				newpos = self.world.translate(head, act)
				if newpos not in self.world.walls and newpos not in vision.bodies and newpos not in self.iw:
					validact.append(act)

			action = validact[randint(0, len(validact)-1)]
			self.count2 = 0
		elif self.count > 8:
			self.count = 0
			newPos = pesquisa.randomPosition(head)
			while newPos == None:
				newPos = pesquisa.randomPosition(head)
			action, self.path = self.choice(head,newPos,pesquisa)
			self.count2 += 1
		elif self.path != []:
			action = pesquisa.calculateNextDirection(self.path[0],head)
			self.path = self.path[1:]
		elif vision.food != [] and M != [] and self.nutrients['M'] <= 200:
			shortestFood = pesquisa.foodCloser(head,M)
			action, self.path = self.choice(head,shortestFood,pesquisa)
		elif vision.food != [] and S != [] and self.nutrients['S'] <= 200:
			shortestFood = pesquisa.foodCloser(head,S)
			action, self.path = self.choice(head,shortestFood,pesquisa)
		elif vision.food != []:
			shortestFood = pesquisa.foodCloser(head,vision.food, msg)
			action, self.path = self.choice(head,shortestFood,pesquisa)
			msg=bytes(str(shortestFood), encoding='utf-8')
		else:
			action = (0,0)
			self.count +=1

		if len(self.lastPositions) > 4:
			self.lastPositions.pop()

		if self.checkLoop(head):
			newPos = pesquisa.randomPosition(head)
			while newPos == None:
				newPos = pesquisa.randomPosition(head)
			action, self.path = self.choice(head,newPos,pesquisa)


		self.lastAction = action
		self.lastPositions.append(head)				# Append actual position of snake
		self.olddir = head							# Actualizar a ultima posição
		
		if self.world.translate(head, action) in vision.bodies or pesquisa.validAction(action) == False or self.world.translate(head, action) in self.world.walls:
			action = (0,0)
			path = [] 
		
		
		
		#end = time.time() - start
		#print("time: ",end)
		return action, msg

	def actionRegular(self,vision, msg, pesquisa, head, action):
		S,M = self.pp.separateFoods(vision.food)
		
		if self.count > 4:
			validact = ACTIONS[:1]
			for act in ACTIONS[1:]:
				newpos = self.world.translate(head, act)
				if newpos not in self.world.walls and newpos not in vision.bodies and newpos not in self.iw:
					validact.append(act)

			action = validact[randint(0, len(validact)-1)]
			self.count = 0
		elif vision.food != [] and M != [] and self.nutrients['M'] <= 200:
			shortestFood = pesquisa.foodCloser(head,M)
			action, self.path = self.choice(head,shortestFood,pesquisa)
			msg = utils.pointToBytes(shortestFood)
		elif vision.food != [] and S != [] and self.nutrients['S'] <= 200:
			shortestFood = pesquisa.foodCloser(head,S)
			action, self.path = self.choice(head,shortestFood,pesquisa)
		elif vision.food != []:
			shortestFood = pesquisa.foodCloser(head,vision.food,msg)
			action, self.path = self.choice(head,shortestFood,pesquisa)
			msg = utils.pointToBytes(shortestFood)
		
		else:
			action = (0,0)
			self.count += 1

		if len(self.lastPositions) > 8:
			self.lastPositions.pop() 

		self.lastAction = action
		self.lastPositions.append(head)				# Append actual position of snake
		self.olddir = head							# Actualizar a ultima posição
		
		
		return action, msg 

	def choice(self,head,goal,pesquisa):
		path = []
		came_from = pesquisa.pesquisa(head,goal,self.olddir)	# Pesquisa do caminho mais curto para a comida	
		path = pesquisa.reconstruct_path(came_from,head,goal)	# Construção do caminho mais curto
		action = (0,0)
		
		if path != []:										# Caso tenha havido a construcao do caminho
			if len(path)>1 and path[1] != self.olddir:						# Verificar se a proxima posicao nao é igual à anterior para não colidir consigo mesmo
				path = path[1:]
				action = pesquisa.calculateNextDirection(path[0],head)

		if action == (0,0):	
			self.count += 1
		else:
			self.count = 0

		return action, path

	def checkLoop(self,head):
		if self.lastPositions.count(head) > 2:
			return True
		return False




################################################### Classe auxiliar à pesquisa ###############################################

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

##################################### Classe responsavel por descobrir e contruir o caminho mais curto ate o objectivo #################################

class Pesquisa:
	def __init__(self,world,vision,imaginaryWalls):
		self.world = world
		self.vision = vision
		self.IW = imaginaryWalls
	
	####################### Descobrir a comida mais proxima à snake ##################
	def foodCloser(self,head,food,msg=None):
		shortest = 99
		result = self.randomPosition(head)

		for f in food.keys():
			if self.world.dist(head,f) < shortest and f not in self.IW and utils.pointToBytes(f) != msg:
				shortest = self.world.dist(head,f)
				result = f

		return result 

	######################## Descobrir o caminho mais curto ##########################
	def pesquisa(self,head,end,oldpos):
		open = PriorityQueue()
		open.put(head,self.heuristic(head,end))

		cost_so_far = {}
		cost_so_far[head] = 0

		parent = {}
		parent[head] = None

		while not open.empty():
			current = open.get()
			
			if current == end:
				break

			for next in self.neighbors(current,oldpos):
				new_cost = cost_so_far[current] + self.costFromTo(current,next)
				if next not in cost_so_far\
				or new_cost < cost_so_far[next]:
					if self.vision==None or next not in self.vision.bodies:
						cost_so_far[next] = new_cost
						priority = new_cost + self.heuristic(end,next)
						open.put(next, priority)
						parent[next] = current

		return parent

	####################### Construcao do caminho mais curto ###########################
	def reconstruct_path(self,came_from, start, goal):
		current = goal
		path = [current]
		while current != start:
			if current in came_from:
				current = came_from[current]        
				path.append(current)
			else:
				return []
		path.reverse()
		return path

	############################ Calculo da heuristica #################################
	#distancia de manhatan
	def heuristic(self,pos, goal):
		p=1/(60+40+1)

		best_x_move = min(abs(pos[0]-goal[0]), pos[0]+60-goal[0], goal[0]+60-pos[0])
		best_y_move = min(abs(pos[1]-goal[1]), pos[1]+40-goal[1], goal[1]+40-pos[1])

		return best_x_move+best_y_move+p
		#return abs(x1-x2) + abs(y1-y2)
	
	########################## Verificacao das acoes validas ###########################
	def getAvailablesMoves(self,current,oldir):
		complement=[(0,1), (0,-1), (-1,0), (1,0)]
		invaliddir=[x for (x,y) in complement if y==oldir]
		validdir=[d for d in ACTIONS if not ( d in invaliddir )]
		return [val for val in complement 
			if not (self.world.translate(current, val) in self.world.walls 
			or self.world.translate(current,val) in self.world.bodies)] 

	
	########## Verificar se consegue ir a current nao e uma parede ou um bodie #########
	def passable(self, current):
		return current not in self.world.walls \
		and current not in self.world.bodies \
		and current not in self.IW

	
	################## Verificar o que esta à volta da head ############################
	def neighbors(self,current,oldpos):
		directions = self.getAvailablesMoves(current,oldpos)
		results = []
		for dirt in directions:
			results.append(self.world.translate(current,dirt))
			results = list(filter(self.passable,results))
		return results

	############ Funcao representativa do custo de ir de um nó para outro ##############
	def costFromTo(self,from_node,to_node):
		return 1

	########################## Calculo da proxima posicao #############################
	def calculateNextDirection(self, nextPos, currentPos):
		newDirX = nextPos[0]-currentPos[0]
		newDirY = nextPos[1]-currentPos[1]

		if newDirX > 1:	   # Direcao LEFT
			newDirX = -1
		elif newDirX < -1: # Direcao RIGHT
			newDirX = 1
		elif newDirY > 1:  # Direcao UP
			newDirY = -1
		elif newDirY < -1: # Direcao DOWN
			newDirY = 1

		newDirection = newDirX, newDirY
		return newDirection

	################### Escolher posicao random ###########################
	def randomPosition(self, head):
		p = self.world.randCoords()

		while p in self.world.walls or p in self.IW or self.world.dist(p, head)<15:
			p = self.world.randCoords()

		return p

	def validAction(self, action):
		if abs(action[0])+abs(action[1]) > 1:
			return False
		return True

		


##################################### Classe de Processamento do mapa antes do jogo começar ###########################	
class Pre_Processing:
	
	def __init__(self,world,mapsize):
		self.world = world
		self.walls = self.world.walls.keys()
		self.mapsize = mapsize
	
	def imaginaryWalls(self,globallist=[]):
		imaginaryWalls = []
		
		# Vai a todas as posicoes do mapa
		for x in range(0,self.mapsize[0]):
			for y in range(0,self.mapsize[1]):
				
				# se essa posicao nao pertencer ás walls ou às 
				if (x,y) not in self.walls:
					if ((x+1,y) in self.walls or (x+1,y) in globallist) and ((x-1,y) in self.walls or (x-1,y) in globallist) and ((x,y+1) in self.walls or (x,y+1) in globallist):
						if (x,y) not in globallist:
							imaginaryWalls.append((x,y))
					elif ((x+1,y) in self.walls or (x+1,y) in globallist) and ((x-1,y) in self.walls or (x-1,y) in globallist) and ((x,y-1) in self.walls or (x,y-1) in globallist):
						if (x,y) not in globallist:
							imaginaryWalls.append((x,y))
					elif ((x,y+1) in self.walls or (x,y+1) in globallist) and ((x,y-1) in self.walls or (x,y-1) in globallist) and ((x+1,y) in self.walls or (x+1,y) in globallist):	
						if (x,y) not in globallist:
							imaginaryWalls.append((x,y))
					elif ((x,y+1) in self.walls or (x,y+1) in globallist) and ((x,y-1) in self.walls or (x,y-1) in globallist) and ((x-1,y) in self.walls or (x-1,y) in globallist):	
						if (x,y) not in globallist:	
							imaginaryWalls.append((x,y))
		
		if imaginaryWalls == []:
			return globallist
		
		globallist += imaginaryWalls
		return self.imaginaryWalls(globallist)

	def separateFoods(self,food):
		foodS = {}
		foodM = {}

		for (coord,letter) in food.items():
			if letter == 'M':
				foodM[coord] = letter
			if letter == 'S':
				foodS[coord] = letter

		return foodS,foodM


	def labyrinth(self, iw, ag):
		try_count = 0
		far_count = 0


		for i in range(0,255):
			p1 = self.world.randCoords()
			while p1 in self.world.walls or p1 in iw:
				p1 = self.world.randCoords()

			for j in range(0,3):
				valid = True

				if j == 0:
					p2 = self.world.translate(p1, (2,0))
				if j == 1:
					p2 = self.world.translate(p1, (0,2))
				if j == 2:
					p2 = self.world.translate(p1, (-2,0))
				if j == 3:
					p2 = self.world.translate(p1, (0,-2))

				while p2 in self.world.walls or p2 in iw:
					if try_count > 2:
						valid = False
						break
					if j == 0:
						p2 = self.world.translate(p1, (1,0))
					if j == 1:
						p2 = self.world.translate(p1, (0,1))
					if j == 2:
						p2 = self.world.translate(p1, (-1,0))
					if j == 3:
						p2 = self.world.translate(p1, (0,-1))
					try_count += 1

				if valid:
					pesquisa = Pesquisa(self.world,None,iw)
					action, path = ag.choice(p1,p2,pesquisa)
					if len(path) >= 5*self.world.dist(p1,p2):
						far_count+=1
					#print("dist: " + str(len(path)))

			#p2 = self.world.randCoords()
			#while self.world.dist(p1,p2) < 2 or p2 in self.world.walls or p2 in iw:
			#	p2 = self.world.randCoords()

			
		#print("far count: " + str(far_count))
		if far_count > 28:
			return True
		return False

class utils:
	def pointToBytes(point):
		return bytes([point[0]])+bytes([point[1]])

	def bytesToPoint(msg):
		return msg[0],msg[1]

