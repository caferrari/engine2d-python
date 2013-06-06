import engine
import atores.cursor, atores.faca, atores.bola, atores.carro

e = engine.nucleo.Engine(800, 600, "Joguinho")
e.loadAtor(atores.faca)
e.loadAtor(atores.cursor)
e.loadAtor(atores.carro)
#e.loadAtor(atores.bola)
#e.addGrupoColisao("cursor", "inimigo", "pq")
e.start()