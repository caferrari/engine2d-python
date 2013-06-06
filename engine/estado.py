import pygame, math
from pygame.locals import * 

import sprite

class Estado:
	""" """
	def __init__(self, engine, arquivo, animado, fps=15, quadros=[1,1], colorkey=[255,0,255]):
		self.engine = engine
		self.updatetime = 0
		self.fps = fps
		self.sprite = sprite.Sprite(engine, arquivo, quadros, colorkey)
		self.anim_range = self.sprite.frame_range
		self.quadroat = 1
		self.animado = animado
				
	def setAnimacao(self, ini, fim):
		self.animrange = [ini, fim]
		self.quadroat = ini

	def update(self):
		if (self.updatetime==0):
			self.updatetime = self.engine.clock

		tmp1 = self.engine.clock - self.updatetime
		tmp2 = (1000 / self.fps)
		
		if (self.engine.clock - self.updatetime) >= (1000 / self.fps):
			self.animar()
			self.updatetime = self.engine.clock

	def quadroPorAngulo(self, angulo):
		q = ((self.sprite.max_frames * angulo) / 360) + 1
		
		if (q > self.sprite.max_frames): q = self.sprite.max_frames
		
		self.quadroat = q
			
	def animar(self):
		if self.animado:
			self.quadroat = self.quadroat + 1
			if self.quadroat > self.anim_range[1]:
				self.quadroat = self.anim_range[0]

	def desenha(self, posicao, quadro=-1):
		if quadro==-1:
			quadro = self.quadroat
		
		self.sprite.desenha(quadro, posicao)

	def clone(self):
		return copy.copy(self)
