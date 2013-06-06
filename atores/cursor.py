import plugins.cursor, plugins.colisao

def init(ator):
	ator.addPlugin(plugins.cursor.Cursor())
	ator.addPlugin(plugins.colisao.Colisao(20))

def update(ator):
	pass	
	
def colisao(self):
	for obj in self.colidindo:
		obj.remover(self)
	pass
	
ator = {
	"nome"  : "Cursor",
	"tipo"  : "cursor",
	"layer" : 5,
	"posicao"	: [10000,10000],
	"funcoes" : {},
	"estados" :[
			{
				"nome"		: "Normal",
				"arquivo" 	: "atores/sprites/cursor.png",
				"updatesec" : 30,
				"quadroswh" : [1, 1],
				"colorkey"	: [0,0,0]
			}
		]
}

ator["colisao"] = colisao
ator["init"] = init