class Cursor:

	def __init__(self, centro=False):
		self.centro = centro
		
	def update(self, ator):
		pos = ator.engine.input.mousepos
		if self.centro:
			tam = ator.estados[ator.estado_at].sprite.quadropx
			ator.posicao = [pos[0] - (tam[0]/2), pos[1] - (tam[1]/2)]
		else:
			ator.posicao = [pos[0] , pos[1]]