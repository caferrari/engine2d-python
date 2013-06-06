import pygame
from pygame.locals import * 

class Input:
	"""  """
	def __init__(self, engine):
		self.engine = engine
		self.teclas = {}
		self.mousepos = [0, 0]
		
	def eventos(self):
		ev = pygame.event.get()
		
		for e in ev:
			if e.type == QUIT:
				self.engine.loop = 0
			if e.type == KEYDOWN:
				self.teclas[e.key] = True
			if e.type == KEYUP:
				if self.teclas.has_key(e.key):
					del self.teclas[e.key]
			if e.type == MOUSEMOTION:
				self.mousepos = e.pos
	
	def tecla(self, tecla):
		if self.teclas.has_key(tecla):
			return True
		return False