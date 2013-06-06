import pygame, input, colisao
from pygame.locals import * 
from threading import Thread


class Engine:
	""" """
	def __init__ (self, w, h, titulo):
		pygame.init()
		window 			= pygame.display.set_mode((w, h), HWSURFACE|DOUBLEBUF) 
		pygame.mouse.set_visible(False)

		self.nome 		= titulo
		self.dimensoes 	= [w, h]
		self.tela 		= pygame.display.get_surface() 
		self.layers		= [[],[],[],[],[],[]]
		self.loop 		= 1
		self.sprites 	= {}
		self.clock		= 1
		self.input		= input.Input(self)
		self.clock 		= pygame.time.get_ticks()
		self.lastUpdate = self.clock
		self.conteiner	= {}
		self.grupocolisao = []
		self.colisao = colisao.Colisao(self)
		print "-- Engine Carregada"

	def flip (self):
		pygame.display.flip()
		self.tela.fill([255,255,255])
		self.clock = pygame.time.get_ticks()

	def addGrupoColisao(self, t1, t2, tipo="qq"):
		self.grupocolisao.append([t1, t2, tipo])
	
	def updateAll(self):
		#print self.layers[5][0].colidindo
		self.input.eventos()
		try:
			tmp = 1000 / (self.clock - self.lastUpdate)
		except:
			tmp = 0
		self.lastUpdate = self.clock		
		cont = 0
		for layer in self.layers:
			cont = cont + len(layer)
			for ator in layer:
				if ator.ativo:
					ator.update()
		pygame.display.set_caption( self.nome + " Atores: " + str(cont) + " FPS: " + str(tmp) )

	def desenhaAll(self):
		for layer in self.layers:
			for ator in layer:
				if ator.ativo:
					ator.desenhar()

	def criaEstado(self, arquivo, animado, fps=15, quadros=[1,1], colorkey=[255,0,255]):
		import estado
		return estado.Estado(self, arquivo, animado, fps, quadros, colorkey)
	
	def criaAtor(self, nome, tipo, layer, posicao):
		import ator
		return ator.Ator(self, nome, tipo, layer, posicao)
	
	def loadAtor(self, config):
		print "Carregando ator: ", config.ator["nome"]
		tmp = self.criaAtor(config.ator["nome"], config.ator["tipo"], config.ator["layer"], config.ator["posicao"])
		
		for dados in config.ator["estados"]:
			try:
				animado = dados["animado"]
			except:
				animado = True
			tmp.addEstado(dados["nome"], self.criaEstado(dados["arquivo"], animado, dados["updatesec"], dados["quadroswh"], dados["colorkey"]))

		config.ator["init"](tmp)
		tmp.colisao = config.ator["colisao"]
		tmp.funcoes = config.ator["funcoes"]

	def start(self):
		print "-- Inicializando o loop Principal"
		self.colisao.start()
		while (self.loop):
			self.updateAll()
			self.desenhaAll()
			self.flip()
		self.colisao.stop()
		print "-- Fim do jogo"