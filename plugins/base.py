import pygame
from pygame.locals import * 

class Plugins:

	def __init__(self):
		pass
	
	def startClock(self, updateTime):
		self.clock = pygame.time.get_ticks()
		self.updateTime = updateTime
		self.lastUpdate = -10000
		
	def updateClock(self):
		self.clock = pygame.time.get_ticks()