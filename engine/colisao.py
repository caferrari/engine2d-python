from threading import Thread


def testColisaoPQ(engine, g1, g2):
	l1 = engine.conteiner[g1]
	l2 = engine.conteiner[g2]
	for obj1 in range(0, len(l1)):
		for obj2 in range(obj1, len(l2)):
			try:
				if l1[obj1].ativo and l2[obj2].ativo and l1[obj1].posicao[0] >= l2[obj2].posicao[0] and l1[obj1].posicao[1] >= l2[obj2].posicao[1] and l1[obj1].posicao[0] <= l2[obj2].posicao[0] + l2[obj2].dimensoes[0] and l1[obj1].posicao[1] <= l2[obj2].posicao[1] + l2[obj2].dimensoes[1]:
					if l1[obj1].existeColisao(l2[obj2])==False:
						l1[obj1].addColisao(l2[obj2])
						l2[obj2].addColisao(l1[obj1])
				else:
					if l1[obj1].existeColisao(l2[obj2]):
						l1[obj1].removeColisao(l2[obj2])
						l2[obj2].removeColisao(l1[obj1])
			except:
				pass

class Colisao(Thread):

	def __init__(self, engine):
		Thread.__init__(self)
		self.engine = engine
		self.ativo = True
		

	def testColisao(self):
		import colisao
		for grupo in self.engine.grupocolisao:
			if grupo[2] == "qq":
				pass
			if grupo[2] == "pq":
				colisao.testColisaoPQ(self.engine, grupo[0], grupo[1])
			if grupo[2] == "qp":
				pass
			
	def run(self):
		print "Ligando thread de colisao"
		import time
		while self.ativo:
			time.sleep(.03)
			self.testColisao()
			
	def stop(self):
		self.ativo = False