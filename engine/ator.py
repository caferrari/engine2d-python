import pygame, copy
from pygame.locals import * 

class Ator:
	""" sdf """
	def __init__(self, engine, nome, tipo, layer, posicao=[0,0]):
		self.engine 		= engine
		self.nome 			= nome
		self.estados 		= {}
		self.estado_at 		= None
		self.posicao 		= posicao
		self.dimensoes 		= [0,0]
		self.destruir 		= False
		self.plugins		= []
		self.ativo			= True
		self.tipo			= tipo
		self.layer			= layer
		self.colidindo		= []
				
		self.add()
	
	def add(self):
		if self.engine.conteiner.has_key(self.tipo) == False:
			self.engine.conteiner[self.tipo] = []
		self.engine.conteiner[self.tipo].append(self)
		self.engine.layers[self.layer].append(self)
		
	def addEstado(self, nome, estado):
		self.estados[nome] = estado
		if self.estado_at == None:
			self.play(nome)

	def existeColisao(self, obj):
		c = self.colidindo.count(obj)
		
		if c > 0:
			return True
		else:
			return False
			
	def addColisao(self, obj):
		self.colidindo.append(obj)
		
	def removeColisao(self, obj):
		self.colidindo.remove(obj)
			
	def remover(self, origem=0):
		self.destruir = True
		try:
			self.engine.conteiner[self.tipo].remove(self)
		except:
			pass
			
		try:
			self.engine.layers[self.layer].remove(self)
		except:
			pass

	def play(self, estado):
		self.estado_at = estado
		self.dimensoes = self.estados[estado].sprite.quadropx
		
	def update(self):
		for x in self.colidindo:
			if x.destruir:
				i = self.colidindo.index(x)
				del self.colidindo[i]
	
		for plugin in self.plugins:
			plugin.update(self)		
		self.estados[self.estado_at].update()

	def desenhar(self):
		self.estados[self.estado_at].desenha(self.posicao)

	def setPosicao(self, x, y):
		self.posicao = [x, y]

	def addPlugin(self, plugin):
		self.plugins.append(plugin)
	
	def clone(self):
		copia = copy.copy(self)
		copia.plugins = []
		for plugin in self.plugins:
			copia.plugins.append(copy.copy(plugin))
		copia.add()
		return copia