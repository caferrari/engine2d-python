import base

class Colisao(base.Plugins):

	def __init__(self, updateTime=10):
		self.dx = 1
		self.dy = 1
		self.startClock(updateTime)

	def update(self, ator):
		if len(ator.colidindo) > 0:
			self.updateClock()
			if (self.clock - self.lastUpdate) >= self.updateTime:
				self.lastUpdate = self.clock
				ator.colisao(ator)