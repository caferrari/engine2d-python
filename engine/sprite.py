import pygame, os
from pygame.locals import * 

class Sprite:
	"""  """
	def __init__(self, engine, arquivo, quadros=[1,1], colorkey=[255,0,255]):
		self.engine = engine
		self.nome = arquivo
		self.quadros = quadros
		self.frames = {}
		self.tampx = [0,0]
		self.quadropx = [0,0]
		self.carregaSprite(arquivo, colorkey)
		self.criaFrames()
		self.rotacao = 0
		self.quadro = 0
		
		
	def carregaSprite(self, arquivo, colorkey):
		try:
			self.engine.sprites[arquivo]
		except:
			caminho = os.path.join(arquivo)
			sprite = pygame.image.load(caminho)
			sprite.set_colorkey(colorkey, RLEACCEL)	
			self.engine.sprites[arquivo] = sprite

		sprite.convert_alpha()
		rect = sprite.get_rect()
		self.tampx = [rect[2], rect[3]]

		self.quadropx = [self.tampx[0] / self.quadros[0], self.tampx[1] / self.quadros[1]]
		self.quadroat = 1

		print "-- Carregando Sprite:\t", arquivo;
	
	def criaFrames(self):
		x = 0
		for j in range(0, self.quadros[1]):
			for i in range(0, self.quadros[0]):
				rect = [i * self.quadropx[1], j * self.quadropx[0]]
				x=x+1				
				self.frames[x] = rect
		self.max_frames = x;
		self.frame_range = [1, x]

	def desenha(self, quadro, posicao):
		rect = [self.frames[quadro][0], self.frames[quadro][1], self.quadropx[0], self.quadropx[1]]
					
		if posicao == -1:
			posicao = [0,0]
		if rect == -1:
			rect = self.sprites[sprite].get_rect()
			
		self.engine.tela.blit(self.engine.sprites[self.nome], posicao, rect)
		