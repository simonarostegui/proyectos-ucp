import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
#from prototipo_original_prueba import Combate_loop
#from menu import MenuPrincipal_Loop
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
FINAL_DIR = os.path.join(ASSETS_DIR, 'Victoria_Derrota')
MENU_DIR = os.path.join(ASSETS_DIR, 'menu')
MUSICA_DIR = os.path.join(ASSETS_DIR,'Musica')
fps,window=globales()

def final(todos_vivos):
	Volver_a_jugar=Boton("1_jugar.png","1_jugar_lit.png",MENU_DIR,640,200)
	Salir=Boton("1_salir.png","1_salir_lit.png",MENU_DIR,640,650)
	

	if not todos_vivos:
		"""
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		"""
		#window.fill((33, 33, 33))
		fondoPath = os.path.join(FINAL_DIR, "Derrota.png")
		fondo = Background(fondoPath)
		#window.blit(fondo.image, fondo.rect)

		musicaEstado = pygame.mixer.music.load(os.path.join(MUSICA_DIR, 'derrota.mp3'))
		pygame.mixer.music.play(0, 0.0)		

		while True:
			
			mouseX, mouseY = pygame.mouse.get_pos()
			mouse = pygame.Rect(mouseX, mouseY, 1, 1)
			click = pygame.mouse.get_pressed()

			window.fill((33, 33, 33))
			window.blit(fondo.image, fondo.rect)
			
			#Volver_a_jugar.IluminarMouse(mouse,click,window,MenuPrincipal_Loop)
			Salir.IluminarMouse(mouse,click,window,Goodbye)
			
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						quit()

			fps.tick(60)
			pygame.display.update()
	else:
		"""
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		"""
		#window.fill((33, 33, 33))
		fondoPath = os.path.join(FINAL_DIR, "Victoria.png")
		fondo = Background(fondoPath)
		#window.blit(fondo.image, fondo.rect)
		
		musicaEstado = pygame.mixer.music.load(os.path.join(MUSICA_DIR, 'victoria.mp3'))
		pygame.mixer.music.play(0, 0.0)		


		while True:
			window.fill((33, 33, 33))
			window.blit(fondo.image, fondo.rect)
			mouseX, mouseY = pygame.mouse.get_pos()
			mouse = pygame.Rect(mouseX, mouseY, 1, 1)
			click = pygame.mouse.get_pressed()
			#Volver_a_jugar.IluminarMouse(mouse,click,window,MenuPrincipal_Loop)
			Salir.IluminarMouse(mouse,click,window,Goodbye)
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						quit()

			fps.tick(60)
			pygame.display.update()