import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
DES_DIR = os.path.join(ASSETS_DIR, 'desafios')

fps, window = globales()

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
				#charselect_1[ilu]["Seleccionado"]=True
				#charselect_1.pop(ilu)
				pygame.display.update()
				
				return jugador_elegido

		pygame.display.update()
		
clases = {
	0:{"Codigo":0,'Nombre': "Sagit", 'Imagen': 'sagit.png'},
	1:{"Codigo":1,'Nombre': "Mirmil", 'Imagen': 'mirmil.png'},
	2:{"Codigo":2,'Nombre': "Thraex", 'Imagen': 'thraex.png'},
	3:{"Codigo":3,'Nombre': "Provoc", 'Imagen': 'provoc.png'},
	4:{"Codigo":4,'Nombre': "Secutor", 'Imagen': 'secutor.png'},
	5:{"Codigo":5,'Nombre': "Retarius", 'Imagen': 'rhetarius.png'},
	6:{"Codigo":6,'Nombre': "Scissos", 'Imagen': 'scisoss.png'},
	7:{"Codigo":7,'Nombre': "Hoplo", 'Imagen': 'hoplo.png'},}

desafios = {
	0:{'Nombre': "I", 'Imagen': 'nivel1.png', 'ImagenLit': 'nivel1_lit.png', 'CoordenadaX': 190 , 'CoordenadaY': 250},
	1:{'Nombre': "II", 'Imagen': 'nivel2.png', 'ImagenLit': 'nivel2_lit.png', 'CoordenadaX': 420 , 'CoordenadaY': 250},
	2:{'Nombre': "III", 'Imagen': 'nivel3.png', 'ImagenLit': 'nivel3_lit.png', 'CoordenadaX': 650 , 'CoordenadaY': 250},
	3:{'Nombre': "IV", 'Imagen': 'nivel4.png', 'ImagenLit': 'nivel4_lit.png', 'CoordenadaX': 880 , 'CoordenadaY': 250},
	4:{'Nombre': "V", 'Imagen': 'nivel5.png', 'ImagenLit': 'nivel5_lit.png', 'CoordenadaX': 1110 , 'CoordenadaY': 250}
}
def Seleccion_lvl_desafios_Loop(clases_elegidas):
	nivelelegido = []
	botonesDesafios=[]
	imagenes_clases_elegidas=[]
	desafios_ronda=[]
	for i in range(len(clases_elegidas)):
		imagenes_clases_elegidas.append(Boton(clases[clases_elegidas[i]]["Imagen"],clases[clases_elegidas[i]]["Imagen"],DES_DIR,640,600))

	for i in desafios:
		botonesDesafios.append(Boton(desafios[i]['Imagen'], desafios[i]['ImagenLit'], DES_DIR, desafios[i]['CoordenadaX'], desafios[i]['CoordenadaY']))


	#jugador = Boton(imagenJugador, imagenLitJugador, DES_DIR, 635, 615)

	while True:
		window.fill((33, 33, 33))
		fondoPath = os.path.join(DES_DIR, "fondo.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		for ju in range(len(clases_elegidas)):
			window.blit(imagenes_clases_elegidas[ju].image,imagenes_clases_elegidas[ju].rect)
			lvl_elegido=elegir_aliado(botonesDesafios)
			desafios_ronda.append(lvl_elegido)
		return desafios_ronda
		break
