import plugins.cursor, plugins.misc, plugins.teclado, random

def init(ator):
	#ator.addPlugin(plugins.misc.AndaDiagonal(5))
	p = plugins.misc.ChamaFuncao()
	p.addFuncao("Escreve algo na tela", "teste", 1000)
	ator.addPlugin(p)
			

def selfclone(ator):
	t = ator.clone()
	t.posicao = [random.randint(0, ator.engine.dimensoes[0]), random.randint(0, ator.engine.dimensoes[1])]

def update(ator):
	pass
	
def colisao(self):
	pass
	
def teste(self):
	print "imprimindo teste"
	
ator = {
	"nome"  : "Faca",
	"tipo"  : "nada",
	"layer" : 1,
	"posicao"	: [150,200],
	"funcoes" : {},
	"estados" :[
			{
				"nome"		: "Normal",
				"arquivo" 	: "atores/sprites/bola.png",
				"updatesec" : 32,
				"quadroswh" : [8, 4],
				"colorkey"	: [255,0,255]
			}
		]
}

ator["init"] = init
ator["colisao"] = colisao
ator["funcoes"]["selfclone"] = selfclone
ator["funcoes"]["teste"] = teste