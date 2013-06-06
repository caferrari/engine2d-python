def normalizaAngulo(angulo):
	while angulo < 0:
		angulo = angulo + 360
	
	while angulo > 360:
		angulo = angulo - 360
	
	return angulo

def moveDirecao(angulo, distancia=0, pAtual = [0,0]):
	import math
	
	if distancia < 0:
		distancia = 0
		
	angulo = angulo - 90
	normalizaAngulo(angulo)
	
	radiano = (angulo * math.pi) / 180
	
	mx = (math.cos(radiano) * distancia) + pAtual[0]
	my = (math.sin(radiano) * distancia) + pAtual[1]
	
	return [mx, my]