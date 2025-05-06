import random
import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
#from prototipo_original_prueba import jugadores
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
RECOMPENSAS_DIR = os.path.join(ASSETS_DIR, 'Recompensas')
PERSONAJES_RECOMPENSAS_DIR = os.path.join(RECOMPENSAS_DIR, 'personajes_iconos')
COMENZAR_DIR= os.path.join(ASSETS_DIR, 'rondas')
MUSICA_DIR = os.path.join(ASSETS_DIR,'Musica')

recompensas={0:{0:{"Nombre":"Cura I","Potencia":2,"Nivel":0,"Tipo":0,"Imagen":"nivel_1_cura.png"},
				1:{"Nombre":"Arma I","Potencia":2,"Nivel":0,"Tipo":1,"Imagen":"nivel_1_arma.png"},
				2:{"Nombre":"Armadura I","Potencia":2,"Nivel":0,"Tipo":2,"Imagen":"nivel_1_armadura.png"}},
			 
			 1:{0:{"Nombre":"Cura II","Potencia":2,"Nivel":1,"Tipo":0,"Imagen":"nivel_2_cura.png"},
			 	1:{"Nombre":"Arma II","Potencia":2,"Nivel":1,"Tipo":1,"Imagen":"nivel_2_arma.png"},
			 	2:{"Nombre":"Armadura II","Potencia":2,"Nivel":1,"Tipo":2,"Imagen":"nivel_2_armadura.png"}},
			 
			 2:{0:{"Nombre":"Cura III","Potencia":3,"Nivel":2,"Tipo":0,"Imagen":"nivel_3_cura.png"},
			 	1:{"Nombre":"Arma III","Potencia":3,"Nivel":2,"Tipo":1,"Imagen":"nivel_3_arma.png"},
			 	2:{"Nombre":"Armadura III","Potencia":3,"Nivel":2,"Tipo":2,"Imagen":"nivel_3_armadura.png"}},
			 
			 3:{0:{"Nombre":"Cura IV","Potencia":1,"Nivel":3,"Tipo":0,"Imagen":"nivel_4_cura.png"},
			 	1:{"Nombre":"Arma IV","Potencia":1,"Nivel":3,"Tipo":1,"Imagen":"nivel_4_arma.png"},
			 	2:{"Nombre":"Armadura IV","Potencia":1,"Nivel":3,"Tipo":2,"Imagen":"nivel_4_armadura.png"}},
			 
			 4:{0:{"Nombre":"Cura V","Potencia":2,"Nivel":4,"Tipo":0,"Imagen":"nivel_5_cura.png"},
			 	1:{"Nombre":"Arma V","Potencia":2,"Nivel":4,"Tipo":1,"Imagen":"nivel_5_arma.png"},
			 	2:{"Nombre":"Armadura V","Potencia":2,"Nivel":4,"Tipo":2,"Imagen":"nivel_5_armadura.png"}}}

clases={0:{"Nombre":"Sagit","ImagenIcon":"sagit_icon.png","ImagenIconLit":"sagit_icon_lit.png"},
		1:{"Nombre":"Mirmil","ImagenIcon":"mirmil_icon.png","ImagenIconLit":"mirmil_icon_lit.png"},
		2:{"Nombre":"Rhetarius","ImagenIcon":"rhetarius_icon.png","ImagenIconLit":"rhetarius_icon_lit.png"},
		3:{"Nombre":"Thraex","ImagenIcon":"thraex_icon.png","ImagenIconLit":"thraex_icon_lit.png"},
		4:{"Nombre":"Provocator","ImagenIcon":"provoc_icon.png","ImagenIconLit":"provoc_icon_lit.png"},
		5:{"Nombre":"Secutor","ImagenIcon":"secutor_icon.png","ImagenIconLit":"secutor_icon_lit.png"},
		6:{"Nombre":"Scisoss","ImagenIcon":"scisoss_icon.png","ImagenIconLit":"scisoss_icon_lit.png"},
		7:{"Nombre":"Hoplo","ImagenIcon":"hoplo_icon.png","ImagenIconLit":"hoplo_icon_lit.png"}}

fps,window=globales()

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



def Recompensas_Loop(jugadores,desafios_ronda,d,final,numeros_clases):
	botones_icon_jugadores=[]
	x=205
	for juga in range(len(jugadores)):
		x+=175
		cla=numeros_clases[juga]

		boton_icon=Boton(clases[cla]["ImagenIcon"],clases[cla]["ImagenIconLit"],PERSONAJES_RECOMPENSAS_DIR,x,500)
		boton_icon.cambiar_tamaño(154,193,x,575)
		botones_icon_jugadores.append(boton_icon)


	SonidoRecom = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'recompensasWAV.wav'))

	while True:

		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()

		window.fill((33, 33, 33))
		#fondoPath = os.path.join(RECOMPENSAS_DIR, "recompensas_fondo.png")
		#fondo = Background(fondoPath)
		#window.blit(fondo.image, fondo.rect)

		recompensas_ronda=recompensas[desafios_ronda[d]["Nivel"]][random.randint(0,len(recompensas[desafios_ronda[d]["Nivel"]])-1)]
		print(recompensas_ronda)
		print("Obtuviste una carta: "+recompensas_ronda["Nombre"]+" de nivel "+str(recompensas_ronda["Nivel"])+"."+"\n")
		
		pygame.mixer.music.set_volume(0.2)
		SonidoRecom.play()
		
		recompensa_obtenida=Boton(recompensas_ronda["Imagen"],recompensas_ronda["Imagen"],RECOMPENSAS_DIR,640,360)
		recompensa_obtenida.cambiar_tamaño(300,300,640,250)
		
		if final==False:
			if recompensas_ronda["Nivel"]<3:
				fondoPath = os.path.join(RECOMPENSAS_DIR, "recompensas_fondo_lvl_1_3.png")
				fondo = Background(fondoPath)
				window.blit(fondo.image, fondo.rect)
				window.blit(recompensa_obtenida.image,recompensa_obtenida.rect)
				for bot in range(len(botones_icon_jugadores)):
					window.blit(botones_icon_jugadores[bot].image,botones_icon_jugadores[bot].rect)
				objetivo_recompensa=elegir_icono(botones_icon_jugadores)

				#objetivo_recompensa=int(input("Ingrese el numero del jugador al que desea otorgar esta recompensa: "))
				if recompensas_ronda["Tipo"]==0:
					jugadores[objetivo_recompensa]["Vida"]+=recompensas_ronda["Potencia"]
					print("El jugador nr"+str(objetivo_recompensa)+" se curo "+str(recompensas_ronda["Potencia"])+" puntos de vida.")
				elif recompensas_ronda["Tipo"]==1:
					jugadores[objetivo_recompensa]["Ataque_recompensa"]+=recompensas_ronda["Potencia"]
					print("El jugador nr"+str(objetivo_recompensa)+" obtuvo una "+recompensas_ronda["Nombre"]+" que le otroga +"+str(recompensas_ronda["Potencia"])+" de daño durante el resto de la partida.")
				else:
					jugadores[objetivo_recompensa]["Defensa_recompensa"]+=recompensas_ronda["Potencia"]
					print("El jugador nr"+str(objetivo_recompensa)+" obtuvo una "+recompensas_ronda["Nombre"]+" que le otroga +"+str(recompensas_ronda["Potencia"])+" de defensa durante el resto de la partida.")
				pygame.display.update()
				break
			
			else:
				fondoPath = os.path.join(RECOMPENSAS_DIR, "recompensas_fondo_lvl_4_5.png")
				fondo = Background(fondoPath)
				window.blit(fondo.image, fondo.rect)
				window.blit(recompensa_obtenida.image,recompensa_obtenida.rect)
				if recompensas_ronda["Tipo"]==0:
					for j in range(len(jugadores)):

						if jugadores[j]["Vida"]>0:
							jugadores[j]["Vida"]+=recompensas_ronda["Potencia"]
					
					#print("Todos los jugadores se curaron "+str(recompensas_ronda["Potencia"])+" puntos de vida.")
				elif recompensas_ronda["Tipo"]==1:
					for j in range(len(jugadores)):
						jugadores[j]["Ataque_recompensa"]+=recompensas_ronda["Potencia"]
					
					#print("Todos los jugadores obtuvieron una "+recompensas_ronda["Nombre"]+" que les otroga +"+str(recompensas_ronda[r]["Potencia"])+" de daño durante el resto de la partida.")
				else:
					for j in range(len(jugadores)):
						jugadores[j]["Defensa_recompensa"]+=recompensas_ronda["Potencia"]
					
					#print("Todos los jugadores obtuvieron una "+recompensas_ronda["Nombre"]+" que les otroga +"+str(recompensas_ronda[r]["Potencia"])+" de defensa durante el resto de la partida.")
				boton_comenzar=Boton("comenzar.png","comenzar_lit.png",COMENZAR_DIR,900,600)
				boton_comenzar_lista=[boton_comenzar]
				elegir_icono(boton_comenzar_lista)
				pygame.display.update()

				break
		break
		fps.tick(60)
		pygame.display.update()