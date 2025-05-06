import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
DES_DIR = os.path.join(ASSETS_DIR, 'desafios')
BOSS_DIR = os.path.join(ASSETS_DIR, 'rondas')

fps, window = globales()

enemigos = {
	0:{'Nombre': "Campeon", 'Imagen': 'campeon.png', 'ImagenLit': 'campeon_lit.png', 'CoordenadaX': 300 , 'CoordenadaY': 250},
	1:{'Nombre': "Fiera", 'Imagen': 'fiera.png', 'ImagenLit': 'fiera_lit.png', 'CoordenadaX': 650 , 'CoordenadaY': 250},
	2:{'Nombre': "Biga", 'Imagen': 'biga.png', 'ImagenLit': 'biga_lit.png', 'CoordenadaX': 1000 , 'CoordenadaY': 250},
}

desafios = {
	0:{'Nombre': "I", 'Imagen': 'nivel1.png', 'ImagenLit': 'nivel1_lit.png', 'CoordenadaX': 190 , 'CoordenadaY': 250},
	1:{'Nombre': "II", 'Imagen': 'nivel2.png', 'ImagenLit': 'nivel2_lit.png', 'CoordenadaX': 420 , 'CoordenadaY': 250},
	2:{'Nombre': "III", 'Imagen': 'nivel3.png', 'ImagenLit': 'nivel3_lit.png', 'CoordenadaX': 650 , 'CoordenadaY': 250},
	3:{'Nombre': "IV", 'Imagen': 'nivel4.png', 'ImagenLit': 'nivel4_lit.png', 'CoordenadaX': 880 , 'CoordenadaY': 250},
	4:{'Nombre': "V", 'Imagen': 'nivel5.png', 'ImagenLit': 'nivel5_lit.png', 'CoordenadaX': 1110 , 'CoordenadaY': 250}
}

botonesDesafios = {}
botonesEnemigos = {}

def Desafios_Loop(backUp, diccionarios, claseElegida):
	
	nivelelegido = []

	for i in diccionarios:
		if diccionarios[i]['Nombre'] == claseElegida:
			imagenJugador = diccionarios[i]['Imagen']
			imagenLitJugador = diccionarios[i]['ImagenLit']

	for i in desafios:
		botonesDesafios[desafios[i]['Nombre']] = Boton(desafios[i]['Imagen'], desafios[i]['ImagenLit'], DES_DIR, desafios[i]['CoordenadaX'], desafios[i]['CoordenadaY'])


	jugador = Boton(imagenJugador, imagenLitJugador, DES_DIR, 635, 615)

	while True:
		window.fill((33, 33, 33))
		fondoPath = os.path.join(DES_DIR, "fondo.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		jugador.IluminarMouse(mouse, click, window)

		event2 = pygame.event.wait()

		for i in botonesDesafios:
			botonesDesafios[i].EsperarInput(mouse, window, nivelelegido, i, event2, EPIC_Loop, claseElegida,diccionarios, Desafios_Loop)

		for event in pygame.event.get():
			if event.type == QUIT:
				Goodbye()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Goodbye()

		fps.tick(60)
		pygame.display.update()

def EPIC_Loop(claseElegida, nivelElegido,diccionarios, backUp):

	for i in diccionarios:
		if diccionarios[i]['Nombre'] == claseElegida:
			imagenJugador = diccionarios[i]['Imagen']
			imagenLitJugador = diccionarios[i]['ImagenLit']

	for i in enemigos:
		botonesEnemigos[enemigos[i]['Nombre']] = Boton(enemigos[i]['Imagen'], enemigos[i]['ImagenLit'], BOSS_DIR, enemigos[i]['CoordenadaX'], enemigos[i]['CoordenadaY'])

	while True:
		window.fill((33, 33, 33))
		fondoPath = os.path.join(BOSS_DIR, "fondo.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		for i in botonesEnemigos:
			botonesEnemigos[i].IluminarMouse(mouse, click, window)

		jugador = Boton(imagenJugador, imagenLitJugador, DES_DIR, 635, 615)

		jugador.IluminarMouse(mouse, click, window)

		for event in pygame.event.get():
			if event.type == QUIT:
				Goodbye()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Goodbye()
				elif event.key == K_SPACE: #BOTON DEBUG
					print("Clase Elegida:",claseElegida)


		fps.tick(60)
		pygame.display.update()