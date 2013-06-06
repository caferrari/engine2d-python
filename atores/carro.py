import plugins.cursor, plugins.misc, plugins.teclado, random
import lib.func_math

def init(ator):
	p = plugins.misc.ChamaFuncao()
	p.addFuncao("Andar", "mover", 10)
	ator.addPlugin(p)
	
	p = plugins.teclado.Teclado()
	p.addBind([273], "Acelerador", "key_cima", 30);
	p.addBind([276], "Virar Esquerda", "key_esquerda", 5);
	p.addBind([275], "Virar Direita", "key_direita", 5);
	
	ator.addPlugin(p)
	
	ator.velocidade = 0
	ator.angulo = 0

	
def key_cima(ator, press):
	if press:
		if ator.velocidade <= 4:
			ator.velocidade = ator.velocidade + 0.02
	else:
		if ator.velocidade > 0:
			ator.velocidade = ator.velocidade - 0.005
		else: 
			ator.velocidade = 0

def key_esquerda(ator, press):
	if press and ator.estado_at == "Normal" and ator.velocidade > 0:
		ator.angulo = lib.func_math.normalizaAngulo(ator.angulo - 1)
		ator.estados["Normal"].quadroPorAngulo(ator.angulo)
	
def key_direita(ator, press):			
	if press and ator.estado_at == "Normal" and ator.velocidade > 0:
		ator.angulo = lib.func_math.normalizaAngulo(ator.angulo + 1)
		ator.estados["Normal"].quadroPorAngulo(ator.angulo)
	
def mover(ator):
	ator.posicao = lib.func_math.moveDirecao(ator.angulo, ator.velocidade, ator.posicao)
		
def colisao(self):
	pass
	
ator = {
	"nome"  : "Carro",
	"tipo"  : "player",
	"layer" : 1,
	"posicao"	: [400,300],
	"funcoes" : {},
	"estados" :[
			{
				"nome"		: "Normal",
				"arquivo" 	: "atores/sprites/carro.png",
				"updatesec" : 32,
				"quadroswh" : [8, 4],
				"colorkey"	: [255,0,255],
				"animado"	: False
			}
		]
}

ator["init"] = init
ator["colisao"] = colisao
ator["funcoes"]["mover"] = mover
ator["funcoes"]["key_cima"] = key_cima
ator["funcoes"]["key_esquerda"] = key_esquerda
ator["funcoes"]["key_direita"] = key_direita