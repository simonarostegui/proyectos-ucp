import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
from desafios import Desafios_Loop
from itertools import islice

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
CHAR_DIR = os.path.join(ASSETS_DIR, 'personajes')

fps, window = globales()

charselect = {
	0:{'Nombre': "Sagit", 'Imagen': 'sagit.png', 'ImagenLit': 'sagit_lit.png', 'CoordenadaX': 203 , 'CoordenadaY': 297},
	1:{'Nombre': "Murmil", 'Imagen': 'mirmil.png', 'ImagenLit': 'mirmil_lit.png','CoordenadaX': 493 , 'CoordenadaY': 297},
	2:{'Nombre': "Thraex", 'Imagen': 'thraex.png', 'ImagenLit': 'thraex_lit.png', 'CoordenadaX': 784, 'CoordenadaY': 297},
	3:{'Nombre': "Hoplo", 'Imagen': 'hoplo.png', 'ImagenLit': 'hoplo_lit.png', 'CoordenadaX': 1075, 'CoordenadaY': 297},
	4:{'Nombre': "Provoc", 'Imagen': 'provoc.png', 'ImagenLit': 'provoc_lit.png', 'CoordenadaX': 202, 'CoordenadaY': 297},
	5:{'Nombre': "Secutor", 'Imagen': 'secutor.png', 'ImagenLit': 'secutor_lit.png', 'CoordenadaX': 493, 'CoordenadaY': 297},
	6:{'Nombre': "Retarius", 'Imagen': 'rhetarius.png', 'ImagenLit': 'rhetarius_lit.png', 'CoordenadaX': 784, 'CoordenadaY': 297},
	7:{'Nombre': "Scissos", 'Imagen': 'scisoss.png', 'ImagenLit': 'scisoss_lit.png', 'CoordenadaX': 1077, 'CoordenadaY': 298}}

botonesCartas = {}
botonesCartas2 = {}

def Personajes_Loop(backUp):

	back = Boton('back.png', 'back_lit.png', CHAR_DIR, 60, 180)
	siguiente = Boton('next.png', 'next_lit.png', CHAR_DIR, 1230, 362)

	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		window.fill((33, 33, 33))
		fondoPath = os.path.join(CHAR_DIR, "fondo1.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)

		for i in islice(charselect, 4):
			botonesCartas[charselect[i]['Nombre']] = Boton(charselect[i]['Imagen'], charselect[i]['ImagenLit'], CHAR_DIR, charselect[i]['CoordenadaX'], charselect[i]['CoordenadaY'])

		for i in botonesCartas:
				botonesCartas[i].AsignarClase(mouse, click, window, Desafios_Loop, Personajes_Loop, charselect, i)

		back.IluminarMouse(mouse, click, window, backUp)
		siguiente.IluminarMouse(mouse, click, window, Personajes_Loop2, backUp)

		for event in pygame.event.get():
			if event.type == QUIT:
				Goodbye()
			elif event.type == MOUSEBUTTONDOWN:
				for i in botonesCartas:
					if mouse.colliderect(botonesCartas[i]):
						pygame.display.set_caption('Arenas y Gladiadores - '+i)
						claseElegida = i
						# Desafios_Loop(mouse, claseElegida)
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Goodbye()
				elif event.key == K_SPACE: #BOTON DEBUG
					print("Clase Elegida:",claseElegida)

		fps.tick(60)
		pygame.display.update()

def Personajes_Loop2(backUp):
	atras = Boton('atras.png', 'atras_lit.png', CHAR_DIR, 50, 362)
	back = Boton('back.png', 'back_lit.png', CHAR_DIR, 60, 180)

	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		for i in islice(charselect, 4, None):
			botonesCartas2[charselect[i]['Nombre']] = Boton(charselect[i]['Imagen'], charselect[i]['ImagenLit'], CHAR_DIR, charselect[i]['CoordenadaX'], charselect[i]['CoordenadaY'])

		window.fill((33, 33, 33))
		fondoPath = os.path.join(CHAR_DIR, "fondo2.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)

		for i in botonesCartas2:
			botonesCartas2[i].AsignarClase(mouse, click, window, Desafios_Loop, Personajes_Loop, charselect, i)

		back.IluminarMouse(mouse, click, window, backUp)
		atras.IluminarMouse(mouse, click, window, Personajes_Loop, backUp)

		for event in pygame.event.get():
			if event.type == QUIT:
				Goodbye()
			elif event.type == MOUSEBUTTONDOWN:
				for i in botonesCartas2:
					if mouse.colliderect(botonesCartas2[i]):
						pygame.display.set_caption('Arenas y Gladiadores - '+i)
						claseElegida = i
						# Desafios_Loop(mouse, claseElegida)
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Goodbye()
				elif event.key == K_SPACE: #BOTON DEBUG
					print("Clase Elegida:",claseElegida)

		fps.tick(60)
		pygame.display.update()