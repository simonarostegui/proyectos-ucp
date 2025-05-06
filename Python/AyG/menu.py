import os
import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
from personajes_seleccion import Personajes_Loop
#from prototipo_original_prueba import Combate_loop,clases,cartas_mazo,recompensas,desafios,todos_vivos
def elegir_aliado(botones_jugadores_HP):
	jugador_elegido_bool=False
										

	while not jugador_elegido_bool:
		event =pygame.event.wait()

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		for ilu in range(len(botones_jugadores_HP)):

			botones_jugadores_HP[ilu].IluminarMouse(mouse,click,window)

			if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(botones_jugadores_HP[ilu].rect):


				print("click")
				jugador_elegido=ilu+1
				jugador_elegido_bool=True
				print("Carta 1")
				pygame.display.update()
		pygame.display.update()
		
	return jugador_elegido
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
MENU_DIR = os.path.join(ASSETS_DIR, 'menu')
MULTI_DIR = os.path.join(ASSETS_DIR,'multijugador')
CREDITOS_DIR = os.path.join(ASSETS_DIR, 'creditos')
MUSICA_DIR = os.path.join(ASSETS_DIR, 'Musica')

fps, window = globales()

def MultiPersonajes(cantidadJugadores, backUp, extraBack):
	for i in range(cantidadJugadores):
		Personajes_Loop(backUp, extraBack)


def MenuPrincipal_Loop():
	fondoPath = os.path.join(MENU_DIR, "1_fondo.png")
	fondo = Background(fondoPath)

	play = Boton('1_jugar.png', '1_jugar_lit.png', MENU_DIR, 645, 450)
	opciones = Boton('1_opciones.png', '1_opciones_lit.png', MENU_DIR, 645, 530)
	salir = Boton('1_salir.png', '1_salir_lit.png', MENU_DIR, 645, 610)

	pygame.mixer.music.load(os.path.join(MUSICA_DIR, 'Menu.mp3'))
	pygame.mixer.music.play(-1, 0.0)
	
	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		window.fill((33, 33, 33))
		window.blit(fondo.image, fondo.rect)

		play.IluminarMouse(mouse, click, window, SelectJugadores_Loop, MenuPrincipal_Loop)
		opciones.IluminarMouse(mouse, click, window, Creditos_Loop, MenuPrincipal_Loop)
		salir.IluminarMouse(mouse, click, window, Goodbye)

		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					quit()

		fps.tick(60)
		pygame.display.update()


def SelectJugadores_Loop(backUp):
	fondoPath = os.path.join(MULTI_DIR, "fondo.png")
	fondo = Background(fondoPath)
	botones_cantidad=[]
	unjugador = Boton('1jug.png', '1jug_lit.png', MULTI_DIR, 800, 245)
	botones_cantidad.append(unjugador)
	dosjugador = Boton('2jug.png', '2jug_lit.png', MULTI_DIR, 800, 325)
	botones_cantidad.append(dosjugador)
	tresjugador = Boton('3jug.png', '3jug_lit.png', MULTI_DIR, 800, 405)
	botones_cantidad.append(tresjugador)
	cuatrojugador = Boton('4jug.png', '4jug_lit.png', MULTI_DIR, 800, 485)
	botones_cantidad.append(cuatrojugador)
	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		window.fill((33, 33, 33))
		window.blit(fondo.image, fondo.rect)

		cantidades=elegir_aliado(botones_cantidad)
		Personajes_Loop(cantidades+1)
			


		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					quit()
		Personajes_Loop(cantidades)
		fps.tick(60)
		pygame.display.update()

def Creditos_Loop(backUp):
	fondoPath = os.path.join(CREDITOS_DIR, "fondo.png")
	fondo = Background(fondoPath)

	volveratras = Boton('back.png', 'back_lit.png', CREDITOS_DIR, 640, 655)

	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		window.fill((33, 33, 33))
		window.blit(fondo.image, fondo.rect)

		volveratras.IluminarMouse(mouse, click, window, MenuPrincipal_Loop)

		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					quit()

		fps.tick(60)
		pygame.display.update()