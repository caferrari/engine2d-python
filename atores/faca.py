import plugins.cursor, plugins.misc, plugins.teclado, random

def init(ator):
	ator.addPlugin(plugins.misc.AndaDiagonal(5))
	p = plugins.teclado.Teclado()
	p.addBind([308, 97], "Duplicar", "selfclone", 100);
	ator.addPlugin(p)

def selfclone(ator, press):
	if press:
		t = ator.clone()
		t.posicao = [random.randint(0, ator.engine.dimensoes[0]), random.randint(0, ator.engine.dimensoes[1])]
	
def colisao(self):
	pass
	
ator = {
	"nome"  : "Faca",
	"tipo"  : "inimigo",
	"layer" : 1,
	"posicao"	: [0,0],
	"funcoes" : {},
	"estados" :[
			{
				"nome"		: "Normal",
				"arquivo" 	: "atores/sprites/knifes.png",
				"updatesec" : 30,
				"quadroswh" : [6, 6],
				"colorkey"	: [0,0,0]
			}
		]
}

ator["init"] = init
ator["colisao"] = colisao
ator["funcoes"]["selfclone"] = selfclone