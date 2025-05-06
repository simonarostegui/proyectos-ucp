import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
from desafios import Desafios_Loop
from itertools import islice
from prototipo_original_prueba import Combate_loop
from diccionarios import clases,cartas_mazo,recompensas,desafios
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
CHAR_DIR = os.path.join(ASSETS_DIR, 'personajes')

fps, window = globales()
charselect_1 = {
	0:{"Codigo":0,'Nombre': "Sagit", 'Imagen': 'sagit.png', 'ImagenLit': 'sagit_lit.png', 'CoordenadaX': 203 , 'CoordenadaY': 297,"Seleccionado":False},
	1:{"Codigo":1,'Nombre': "Mirmil", 'Imagen': 'mirmil.png', 'ImagenLit': 'mirmil_lit.png','CoordenadaX': 493 , 'CoordenadaY': 297,"Seleccionado":False},
	2:{"Codigo":2,'Nombre': "Thraex", 'Imagen': 'thraex.png', 'ImagenLit': 'thraex_lit.png', 'CoordenadaX': 784, 'CoordenadaY': 297,"Seleccionado":False},
	3:{"Codigo":3,'Nombre': "Provoc", 'Imagen': 'provoc.png', 'ImagenLit': 'provoc_lit.png',  'CoordenadaX': 1075, 'CoordenadaY': 297,"Seleccionado":False}}
charselect_2={
	0:{"Codigo":4,'Nombre': "Secutor", 'Imagen': 'secutor.png', 'ImagenLit': 'secutor_lit.png', 'CoordenadaX': 203 , 'CoordenadaY': 297,"Seleccionado":False},
	1:{"Codigo":5,'Nombre': "Retarius", 'Imagen': 'rhetarius.png', 'ImagenLit': 'rhetarius_lit.png','CoordenadaX': 493 , 'CoordenadaY': 297,"Seleccionado":False},
	2:{"Codigo":6,'Nombre': "Scissos", 'Imagen': 'scisoss.png', 'ImagenLit': 'scisoss_lit.png', 'CoordenadaX': 784, 'CoordenadaY': 297,"Seleccionado":False},
	3:{"Codigo":7,'Nombre': "Hoplo", 'Imagen': 'hoplo.png', 'ImagenLit': 'hoplo_lit.png', 'CoordenadaX': 1075, 'CoordenadaY': 297,"Seleccionado":False}}

def elegir_aliado(botones_jugadores_HP,jugadores_seleccionados,pestaña_nueva):
	jugador_elegido_bool=False
										

	while not jugador_elegido_bool:
		event =pygame.event.wait()

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		for ilu in range(len(botones_jugadores_HP)):
			pestaña_nueva.IluminarMouse(mouse,click,window)
			
			botones_jugadores_HP[ilu].IluminarMouse(mouse,click,window)

			if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(botones_jugadores_HP[ilu].rect):

				
				print("click")
				jugador_elegido=ilu
				jugador_elegido_bool=True
				print("Carta 1")
				#charselect_1[ilu]["Seleccionado"]=True
				#charselect_1.pop(ilu)
				pygame.display.update()
				
				return jugador_elegido
			elif event.type== MOUSEBUTTONDOWN and  mouse.colliderect(pestaña_nueva.rect):
				return -1
		pygame.display.update()
		
def elegir_aliado_2(botones_jugadores_HP,jugadores_seleccionados,pestaña_nueva):
	jugador_elegido_bool=False
										

	while not jugador_elegido_bool:
		event =pygame.event.wait()

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		for ilu in range(len(botones_jugadores_HP)):
			pestaña_nueva.IluminarMouse(mouse,click,window)
			
			botones_jugadores_HP[ilu].IluminarMouse(mouse,click,window)

			if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(botones_jugadores_HP[ilu].rect):
				

				print("click")
				jugador_elegido=ilu+4
				jugador_elegido_bool=True
				print("Carta 1")
				#charselect_2[ilu]["Seleccionado"]=True
				#charselect_2.pop(ilu)
				pygame.display.update()
				return jugador_elegido
			elif event.type== MOUSEBUTTONDOWN and  mouse.colliderect(pestaña_nueva.rect):
				return -1
		pygame.display.update()
		




def Personajes_Loop(cant_jugadores):
	contador_jugadores=cant_jugadores-1
	pestaña=1
	jugadores_seleccionados=[]
	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		#window.fill((33, 33, 33))
		#fondoPath = os.path.join(CHAR_DIR, "fondo1.png")
		#fondo = Background(fondoPath)
		#window.blit(fondo.image, fondo.rect)

		if pestaña==1:
			jugador_nuevo,contador_jugadores=pestaña_primera(mouse,click,contador_jugadores,jugadores_seleccionados)
			if jugador_nuevo>=0:
				jugadores_seleccionados.append(jugador_nuevo)
			else:
				pestaña=2
		else:
			jugador_nuevo,contador_jugadores=pestaña_segunda(mouse,click,contador_jugadores,jugadores_seleccionados)
			if jugador_nuevo>0:
				jugadores_seleccionados.append(jugador_nuevo)
			else:
				pestaña=1
		print(jugadores_seleccionados)
		#else:
		#	pestaña_segunda()
		print(str(contador_jugadores))
		if contador_jugadores==0:
			Combate_loop(jugadores_seleccionados)
		fps.tick(60)
		pygame.display.update()

def pestaña_primera(mouse,click,contador_jugadores,jugadores_seleccionados):

	window.fill((33, 33, 33))
	fondoPath = os.path.join(CHAR_DIR, "fondo1.png")
	fondo = Background(fondoPath)
	window.blit(fondo.image, fondo.rect)

	siguiente = Boton('next.png', 'next_lit.png', CHAR_DIR, 1230, 362)
	siguiente.IluminarMouse(mouse,click,window)
	botones_personajes_1=[]

	for i in range(len(charselect_1)):
		
		boton_personaje=Boton(charselect_1[i]['Imagen'], charselect_1[i]['ImagenLit'], CHAR_DIR, charselect_1[i]['CoordenadaX'], charselect_1[i]['CoordenadaY'])
		#window.blit(boton_personaje.image,boton_personaje.rect)
		botones_personajes_1.append(boton_personaje)
	print(botones_personajes_1)
	jugador=elegir_aliado(botones_personajes_1,jugadores_seleccionados,siguiente)
	
	if jugador>=0:
		contador_jugadores-=1
	
	return jugador,contador_jugadores
	print(jugadores_seleccionados)

def pestaña_segunda(mouse,click,contador_jugadores,jugadores_seleccionados):

	window.fill((33, 33, 33))
	fondoPath = os.path.join(CHAR_DIR, "fondo2.png")
	fondo = Background(fondoPath)
	window.blit(fondo.image, fondo.rect)
	
	back = Boton('back.png', 'back_lit.png', CHAR_DIR, 60, 180)
	back.IluminarMouse(mouse,click,window)
	botones_personajes_2=[]

	for i in range(len(charselect_2)):
		
		boton_personaje=Boton(charselect_2[i]['Imagen'], charselect_2[i]['ImagenLit'], CHAR_DIR, charselect_2[i]['CoordenadaX'], charselect_2[i]['CoordenadaY'])
		#window.blit(boton_personaje.image,boton_personaje.rect)
		botones_personajes_2.append(boton_personaje)
	print(botones_personajes_2)
	
	jugador=elegir_aliado_2(botones_personajes_2,jugadores_seleccionados,back)
		
	if jugador>=0:
		contador_jugadores-=1
	
	return jugador,contador_jugadores
	print(jugadores_seleccionados)


