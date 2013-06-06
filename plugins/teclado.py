import base

class Teclado(base.Plugins):

	def __init__(self):
		self.binds = []
		self.startClock(-1000)
		
	def update(self, ator):
		self.testaAcoes(ator)
	
	def testaAcoes(self, ator):
		self.updateClock()
		pres = ator.engine.input.teclas
		for bind in self.binds:
			tem = 0
			for tecla in bind[0]:
				if pres.has_key(tecla):
					tem = tem + 1
			if tem == len(bind[0]):
				if bind[3]==False or (self.clock - bind[5]) >=  bind[4]:
					ator.funcoes[bind[2]](ator, True)
					bind[5] = self.clock
					bind[3] = True
			else:
				bind[3] = False
				ator.funcoes[bind[2]](ator, False)
				
		self.lastUpdate = self.clock
		
	def addBind(self, teclas, nome, acao, loop=0):
		self.binds.append([teclas, nome, acao, False, loop, -10000])