import base

class AndaDiagonal(base.Plugins):

	def __init__(self, updateTime=0):
		self.dx = 1
		self.dy = 1
		self.startClock(updateTime)
		
	def update(self, ator):
		self.updateClock()
		if (self.clock - self.lastUpdate) >= self.updateTime:
			self.lastUpdate = self.clock
			if ator.posicao[0]+ator.dimensoes[0] >= ator.engine.dimensoes[0]:
				self.dx = -1
			if ator.posicao[1]+ator.dimensoes[1] >= ator.engine.dimensoes[1]:
				self.dy = -1
			if ator.posicao[0] <=0:
				self.dx = 1
			if ator.posicao[1] <=0:
				self.dy = 1

			ator.posicao = [ator.posicao[0] + self.dx, ator.posicao[1] + self.dy]
			
class ChamaFuncao(base.Plugins):

	def __init__(self):
		self.binds = []
		self.startClock(-1000)
	
	def addFuncao(self, nome, acao, intervalo=10):
		self.binds.append([nome, acao, intervalo, -10000])
	
	def update(self, ator):
		self.updateClock()
		for bind in self.binds:
			if (self.clock - bind[3]) >=  bind[2]:
				ator.funcoes[bind[1]](ator)
				bind[3] = self.clock
				
		self.lastUpdate = self.clock