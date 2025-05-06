import os
import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
RONDAS_DIR = os.path.join(ASSETS_DIR, 'rondas')

fps, window = globales()

def elegir_icono(botones_iconos):
	icono_elegido_bool=False
	while not icono_elegido_bool:

		event =pygame.event.wait()

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		
		for ilu in range(len(botones_iconos)):
			botones_iconos[ilu].IluminarMouse(mouse,click,window)
			if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(botones_iconos[ilu].rect):


				print("click")
				icono_elegido=0
				icono_elegido_bool=True
				print("Carta 1")
				#botones_iconos[0].IluminarMouse(mouse,click,window)
				pygame.display.update()
		pygame.display.update()
	return icono_elegido

def crear_imagen(direc,imagen,x,y,flecha,tamaño,scale_x=None,scale_y=None):
	img_dir=os.path.join(direc,imagen)
	img=pygame.image.load(img_dir).convert_alpha()
	img_rect=img.get_rect()
	img_rect.topleft=(x,y)
	if tamaño==True:
		imgX = img.get_width()
		imgY = img.get_height()
		img=pygame.transform.scale(img, (round(imgX*scale_x),round(imgY*scale_y)))
		img_rect=img.get_rect()
		img_rect.topleft=(x,y)
	window.blit(img,img_rect)
	if flecha==True:
		return img_rect

def Cambiar_Desafio_Loop(desafios_ronda,d):

	

	#for des in range(len(desafios_ronda)):
	#	xicon+=200
	#	if des==d:
	#		actual=crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon_lit"],xicon+100,200,True,False)
	#		crear_imagen(RONDAS_DIR,"flecha",actual.topleft[0]+180,160,False,False)
	#	elif des<d:
	#		crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon"],xicon+100,200,False,False)
	#	else:
	#		crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon_down"],xicon+100,200,False,False) 

	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		x=0
		window.fill((33, 33, 33))
		fondoPath = os.path.join(RONDAS_DIR, "fondo.png")
		fondo = Background(fondoPath)
		window.blit(fondo.image, fondo.rect)
		for des in range(len(desafios_ronda)):
			x+=200
			if des==d:
				actual=crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon_lit"],x+100,200,True,False)
				
			elif des<d:
				crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon"],x+100,200,False,False)
			else:
				crear_imagen(RONDAS_DIR,desafios_ronda[des]["Seleccion_icon_down"],x+100,200,False,False)
		boton_comenzar=Boton("comenzar.png","comenzar_lit.png",RONDAS_DIR,900,600)
		boton_comenzar_lista=[boton_comenzar]
		elegir_icono(boton_comenzar_lista)
		pygame.display.update()




