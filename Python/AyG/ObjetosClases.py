import os
import pygame, sys, time
from pygame.locals import *

class Background:
	def __init__(self, image_path):
		self.image = pygame.image.load(image_path).convert_alpha()
		self.rect = self.image.get_rect()


class Boton:
	def __init__(self, image_file, image_lit, image_dir, x, y):
		self.dir_path = os.path.join(image_dir, image_file)
		self.image = pygame.image.load(self.dir_path).convert_alpha()
		self.imageLit = pygame.image.load(os.path.join(image_dir, image_lit)).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.imageX = self.image.get_width()
		self.imageY = self.image.get_height()
		self.resguardo_image=pygame.image.load(self.dir_path).convert_alpha()
		self.resguardo_imageLit=pygame.image.load(os.path.join(image_dir, image_lit)).convert_alpha()
	def IluminarMouse(self, mouse, click, window, action=None, optional=None):
		if mouse.colliderect(self.rect):
			#self.image=self.resguardo_imageLit
			window.blit(self.imageLit,self.rect)

			if click[0] == 1 and action != None:
				if optional != None:
					action(optional)
				else:
					action()
		else:
			#self.image=self.resguardo_image
			window.blit(self.image,self.rect)
		
	def Iluminar_Otro(self,mouse,window,objetivo):
		if mouse.colliderect(self.rect):
			window.blit(objetivo.imageLit,objetivo.rect)
		else:
			window.blit(objetivo.image,objetivo.rect)
		#pygame.display.update()	
	def AsignarClase(self, mouse, click, window, action=None, optional=None, dictionary = None, clase = None):
		if mouse.colliderect(self.rect):
			window.blit(self.imageLit,self.rect)
			if click[0] == 1 and action != None:
				if optional != None:
					action(optional, dictionary, clase)
				else:
					action()
		else:
			window.blit(self.image,self.rect)

	def EsperarInput(self, mouse, window, dictionary, clase, event, action, personajes,diccionarios, backUp):
		if mouse.colliderect(self.rect):
			window.blit(self.imageLit,self.rect)
			if event.type == MOUSEBUTTONDOWN:
				dictionary.append(clase)
				print(dictionary)
				action(personajes, dictionary, diccionarios, backUp)
		else:
			window.blit(self.image,self.rect)

	def boton_empezar_combate(self, mouse, click, window, action,clases,cartas_mazo,recompensas,desafios,todos_vivos):
		if mouse.colliderect(self.rect):
			window.blit(self.imageLit,self.rect)
			if click[0] == 1:
				action(clases,cartas_mazo,recompensas,desafios,todos_vivos)

		else:
			window.blit(self.image,self.rect)

	def cambiar_tamaño(self,x_scale,y_scale,x,y):
		self.image=pygame.transform.scale(self.image, (x_scale,y_scale))
		self.imageLit =pygame.transform.scale(self.imageLit, (x_scale,y_scale))
		self.rect=self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.imageX = self.image.get_width()
		self.imageY = self.image.get_height()


#	def ARondas(self, mouse, click, window, action=None, optional=None, dictionary = None, clase = None)
#		pass

def crear_boton(window,x,y,ancho,alto,color):
	boton=pygame.Surface((ancho,alto))
	botonRect=pygame.Rect(x,y,ancho,alto)
	boton.fill(color)
	window.blit(boton, (x,y))
	return botonRect



def globales():

	fps = pygame.time.Clock()
	ANCHO_VENTANA = 1280
	ALTO_VENTANA = 720
	window = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

	return fps, window

def Goodbye():
	pygame.quit()
	quit()

def dibujarTexto(texto, fuente, superficie, x, y,color):
    objetoTexto = fuente.render(texto, True, color)
    rectanguloTexto = objetoTexto.get_rect()
    rectanguloTexto.topleft = (x, y)
    superficie.blit(objetoTexto, rectanguloTexto)