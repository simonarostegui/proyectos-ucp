import random
import os
import pygame, sys, time
from pygame.locals import *
from ObjetosClases import *
from personajes import Personajes_Loop
from Recompensas import Recompensas_Loop
from Ganar_Perder import final
from fuentes_y_mas import font
from pantalla_desafios import Cambiar_Desafio_Loop
from seleccionar_desafios_lvl import Seleccion_lvl_desafios_Loop

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(CURRENT_DIR, 'assets')
COMBATE_DIR = os.path.join(ASSETS_DIR, 'combate')
CARTAS_DIR= os.path.join(COMBATE_DIR, 'Cartas')
HP_DIR=os.path.join(COMBATE_DIR, 'HP')
ICON_DIR=os.path.join(COMBATE_DIR, 'Iconos_estado')
PERSONAJES_DIR=os.path.join(COMBATE_DIR, 'Personajes')
ENEMIGOS_DIR=os.path.join(COMBATE_DIR, 'Enemigos')
fps, window = globales()
NEGRO=(0,0,0)
BLANCO=(255,255,255)

# == Musica ==
MUSICA_DIR= os.path.join(ASSETS_DIR, 'Musica')
musicaPeleaON = False
sonAtaque = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'ataque.wav'))
sonDefensa = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'defensa.wav'))
sonBuffeo = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'buffeo.wav'))
sonCuracion = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'curacion.wav'))
sonDebuffeo = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'debuffeo.wav'))
sonSangrado = pygame.mixer.Sound(os.path.join(MUSICA_DIR, 'sangrado.wav'))

def crear_imagen(direc,imagen,x,y,texto,tamaño,scale_x=None,scale_y=None):
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
	if texto==True:
		return img_rect


def agarrar_carta(carta,jug,j,jugadores,codigo_manos,manos):

	carta_agarrada=random.choices([0,1,2,3,4],jugadores[j]["Tipos_cartas"],k=1)

	actualizador={carta:cartas_mazo[carta_agarrada[0]][jugadores[j]["Posibles_cartas"][carta_agarrada[0]][random.randint(0,len(jugadores[j]["Posibles_cartas"][carta_agarrada[0]])-1)]]}

	while actualizador[carta]["Codigo_carta"] in codigo_manos[j]:
		carta_agarrada=random.choices([0,1,2,3,4],jugadores[j]["Tipos_cartas"],k=1)

		actualizador={carta:cartas_mazo[carta_agarrada[0]][jugadores[j]["Posibles_cartas"][carta_agarrada[0]][random.randint(0,len(jugadores[j]["Posibles_cartas"][carta_agarrada[0]])-1)]]}
	
	manos[j].update(actualizador)
	codigo_manos[j].append(actualizador[carta]["Codigo_carta"])

def elegir_aliado(botones_jugadores_HP,jugadores,personaje_img_lista):
	jugador_elegido_bool=False
										
	while not jugador_elegido_bool:
		event =pygame.event.wait()
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		cont_card_1=0
		x_primero=15
		y_primero=520
		x_segundo=15
		y_segundo=620
		flecha_imagen=Boton("flecha.png","flecha.png",COMBATE_DIR,380,600)
		window.blit(flecha_imagen.image,flecha_imagen.rect)
		for ilu in range(len(botones_jugadores_HP)):
			
			if jugadores[ilu]["Vida"]>0:
				botones_jugadores_HP[ilu].IluminarMouse(mouse,click,window)
				botones_jugadores_HP[ilu].Iluminar_Otro(mouse,window,personaje_img_lista[ilu])

			if ilu==0:
				x_primero+=80
				dibujarTexto(str(jugadores[ilu]["Vida"]),font,window,x_primero,y_primero,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero-20,y_primero+40,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero+20,y_primero+40,NEGRO)

			elif ilu==1:
				x_primero+=165
				dibujarTexto(str(jugadores[ilu]["Vida"]),font,window,x_primero,y_primero,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero-15,y_primero+40,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero+25,y_primero+40,NEGRO)
			elif ilu==2:
				x_segundo+=80
				dibujarTexto(str(jugadores[ilu]["Vida"]),font,window,x_segundo,y_segundo,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo-20,y_segundo+40,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo+20,y_segundo+40,NEGRO)
			else:
				x_segundo+=165
				dibujarTexto(str(jugadores[ilu]["Vida"]),font,window,x_segundo,y_segundo,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo-15,y_segundo+40,NEGRO)
				dibujarTexto(str(jugadores[ilu]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo+25,y_segundo+40,NEGRO)

			if jugadores[ilu]["Vida"]>0:
				if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(botones_jugadores_HP[ilu].rect):


					print("click")
					jugador_elegido=ilu
					jugador_elegido_bool=True
					print("Carta 1")
					
					pygame.display.update()
		pygame.display.update()
		
	return jugador_elegido

clases={0:{"Nombre":"Sagit","Tipos_cartas":[8,1,1,3,2],"Posibles_cartas":[[0,1,2,3,4,5,6,7],[0],[0],[3,4,5],[4,5]],"Vida":6,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"sagit_HP.png","ImagenLit":"sagit_HP_lit.png","ImagenDown":"sagit_HP_down.png","ImagenPer":"Sagit.png","ImagenPerLit":"Sagit_lit.png"},
		1:{"Nombre":"Mirmil","Tipos_cartas":[4,2,6,3,0],"Posibles_cartas":[[0,1,6,7],[0,1],[0,1,2,5,6,7],[0,1,7],[]],"Vida":10,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"mirmil_HP.png","ImagenLit":"mirmil_HP_lit.png","ImagenDown":"mirmil_HP_down.png","ImagenPer":"Mirmil.png","ImagenPerLit":"Mirmil_lit.png"},
		2:{"Nombre":"Rhetarius","Tipos_cartas":[4,2,1,2,6],"Posibles_cartas":[[0,1,6,7],[0,1],[0],[0,1],[0,1,2,3,4,5]],"Vida":8,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"rhetarius_HP.png","ImagenLit":"rhetarius_HP_lit.png","ImagenDown":"rhetarius_HP_down.png","ImagenPer":"Rhetarius.png","ImagenPerLit":"Rhetarius_lit.png"},
		3:{"Nombre":"Thraex","Tipos_cartas":[2,6,4,3,0],"Posibles_cartas":[[0,1],[1,2,3,4,6,7],[0,1,5,6],[0,1,7],[]],"Vida":12,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"thraex_HP.png","ImagenLit":"thraex_HP_lit.png","ImagenDown":"thraex_HP_down.png","ImagenPer":"Thraex.png","ImagenPerLit":"Thraex_lit.png"},
		4:{"Nombre":"Provocator","Tipos_cartas":[4,4,3,2,2],"Posibles_cartas":[[1,2,6,7],[0,1,2,],[0,1,2],[0,1],[1,2]],"Vida":7,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"provoc_HP.png","ImagenLit":"provoc_HP_lit.png","ImagenDown":"provoc_HP_down.png","ImagenPer":"Provocator.png","ImagenPerLit":"Provocator_lit.png"},
		5:{"Nombre":"Secutor","Tipos_cartas":[6,0,4,6,0],"Posibles_cartas":[[0,1,2,3],[],[0,1,5,6],[0,1,2,3,4,5,6],[]],"Vida":7,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"secutor_HP.png","ImagenLit":"secutor_HP_lit.png","ImagenDown":"secutor_HP_down.png","ImagenPer":"Secutor.png","ImagenPerLit":"Secutor_lit.png"},
		6:{"Nombre":"Scisoss","Tipos_cartas":[6,2,0,1,6],"Posibles_cartas":[[0,1,5,6,7],[0,1],[],[3,4],[0,2,3,6,7]],"Vida":6,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"scisoss_HP.png","ImagenLit":"scisoss_HP_lit.png","ImagenDown":"scisoss_HP_down.png","ImagenPer":"Scisoss.png","ImagenPerLit":"Scisoss_lit.png"},
		7:{"Nombre":"Hoplo","Tipos_cartas":[6,3,6,0,0],"Posibles_cartas":[[0,1,2,3,5,7],[0,1,2,3],[0,1,2,3,4],[],[]],"Vida":8,"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":"hoplo_HP.png","ImagenLit":"hoplo_HP_lit.png","ImagenDown":"hoplo_HP_down.png","ImagenPer":"Hoplo.png","ImagenPerLit":"Hoplo_lit.png"}}


cartas_mazo={0:{0:{"Codigo_carta":"00","Nombre":"Ataque rapido","Efecto_tipo":0,"Efecto_potencia":1,"Secundario_tipo":0,"Secundario_potencia":0,"Descripcion":"Inflijes 1 punto de daño al enemigo.","Imagen":"0_0_ataque_rapido.png","ImagenLit":"0_0_ataque_rapido_lit.png"},
				1:{"Codigo_carta":"01","Nombre":"Ataque fuerte","Efecto_tipo":0,"Efecto_potencia":2,"Secundario_tipo":0,"Secundario_potencia":0,"Descripcion":"Inflijes 2 puntos de daño al enemigo.","Imagen":"0_1_ataque_fuerte.png","ImagenLit":"0_1_ataque_fuerte_lit.png"},
				2:{"Codigo_carta":"02","Nombre":"Ataque completo","Efecto_tipo":0,"Efecto_potencia":3,"Secundario_tipo":0,"Secundario_potencia":0,"Descripcion":"Inflijes 3 puntos de daño al enemigo.","Imagen":"0_2_ataque_completo.png","ImagenLit":"0_2_ataque_completo_lit.png"},
				3:{"Codigo_carta":"03","Nombre":"Ataque de furia","Efecto_tipo":0,"Efecto_potencia":4,"Secundario_tipo":0,"Secundario_potencia":0,"Descripcion":"Inflijes 4 puntos de daño al enemigo.","Imagen":"0_3_ataque_de_furia.png","ImagenLit":"0_3_ataque_de_furia_lit.png"},
				4:{"Codigo_carta":"04","Nombre":"Golpe vital","Efecto_tipo":0,"Efecto_potencia":1,"Secundario_tipo":1,"Secundario_potencia":1,"Descripcion":"Inflijes 1 de daño y aplicas el efecto de sangrado por 1 turno.","Imagen":"0_4_golpe_vital.png","ImagenLit":"0_4_golpe_vital_lit.png"},
				5:{"Codigo_carta":"05","Nombre":"Robo de vida","Efecto_tipo":0,"Efecto_potencia":1,"Secundario_tipo":2,"Secundario_potencia":2,"Descripcion":"Inflijes 1 de daño y te curas 2 de vida.","Imagen":"0_5_robo_de_vida.png","ImagenLit":"0_5_robo_de_vida_lit.png"},
				6:{"Codigo_carta":"06","Nombre":"Regocijo","Efecto_tipo":0,"Efecto_potencia":2,"Secundario_tipo":2,"Secundario_potencia":3,"Descripcion":"Inflijes 2 de daño y te curas 3 de vida.","Imagen":"0_6_regocijo.png","ImagenLit":"0_6_regocijo_lit.png"},
				7:{"Codigo_carta":"07","Nombre":"Furia","Efecto_tipo":0,"Efecto_potencia":4,"Secundario_tipo":3,"Secundario_potencia":2,"Descripcion":"Inflijes 4 de daño pero recibes 2 de daño tambien.","Imagen":"0_7_furia.png","ImagenLit":"0_7_furia_lit.png"}},
			 
			 1:{0:{"Codigo_carta":"10","Nombre":"Cantaro","Efecto_tipo":1,"Efecto_potencia":1,"Tipo_cura":0,"Descripcion":"Te curas 1 punto de vida.","Imagen":"1_0_cantaro.png","ImagenLit":"1_0_cantaro_lit.png"},
			 	1:{"Codigo_carta":"11","Nombre":"Venda","Efecto_tipo":1,"Efecto_potencia":2,"Tipo_cura":0,"Descripcion":"Te curas 2 puntos de vida.","Imagen":"1_1_venda.png","ImagenLit":"1_1_venda_lit.png"},
			 	2:{"Codigo_carta":"12","Nombre":"Primeros auxilios","Efecto_tipo":1,"Efecto_potencia":3,"Tipo_cura":0,"Descripcion":"Te curas 3 puntos de vida.","Imagen":"1_2_primeros_auxilios.png","ImagenLit":"1_2_primeros_auxilios_lit.png"},
			 	3:{"Codigo_carta":"13","Nombre":"Ayuda","Efecto_tipo":1,"Efecto_potencia":1,"Tipo_cura":1,"Descripcion":"Curas 1 punto a todos tus aliados.","Imagen":"1_3_ayuda.png","ImagenLit":"1_3_ayuda_lit.png"},
			 	4:{"Codigo_carta":"14","Nombre":"Bendicion","Efecto_tipo":1,"Efecto_potencia":2,"Tipo_cura":1,"Descripcion":"Curas 2 puntos a todos tus aliados.","Imagen":"1_4_bendicion.png","ImagenLit":"1_4_bendicion_lit.png"},
			 	5:{"Codigo_carta":"15","Nombre":"Cura rapida","Efecto_tipo":1,"Efecto_potencia":1,"Tipo_cura":2,"Descripcion":"Curas 1 punto de vida a un aliado.","Imagen":"1_5_cura_rapida.png","ImagenLit":"1_5_cura_rapida_lit.png"},
			 	6:{"Codigo_carta":"16","Nombre":"Cura","Efecto_tipo":1,"Efecto_potencia":2,"Tipo_cura":2,"Descripcion":"Curas 2 puntos de vida a un aliado.","Imagen":"1_6_cura.png","ImagenLit":"1_6_cura_lit.png"},
			 	7:{"Codigo_carta":"17","Nombre":"Gran cura","Efecto_tipo":1,"Efecto_potencia":3,"Tipo_cura":2,"Descripcion":"Curas 3 puntos de vida a un aliado.","Imagen":"1_7_gran_cura.png","ImagenLit":"1_7_gran_cura_lit.png"}},
			 
			 2:{0:{"Codigo_carta":"20","Nombre":"Defensa rapida","Efecto_tipo":2,"Efecto_potencia":1,"Tipo_defensa":0,"Descripcion":"Recibes 1 punto de desefensa.","Imagen":"2_0_defensa_rapida.png","ImagenLit":"2_0_defensa_rapida_lit.png"},
			 	1:{"Codigo_carta":"21","Nombre":"Rodela","Efecto_tipo":2,"Efecto_potencia":2,"Tipo_defensa":0,"Descripcion":"Recibes 2 puntos de desefensa.","Imagen":"2_1_rodela.png","ImagenLit":"2_1_rodela_lit.png"},
			 	2:{"Codigo_carta":"22","Nombre":"Defensa completa","Efecto_tipo":2,"Efecto_potencia":3,"Tipo_defensa":0,"Descripcion":"Recibes 3 puntos de desefensa.","Imagen":"2_2_defensa_completa.png","ImagenLit":"2_2_defensa_completa_lit.png"},
			 	3:{"Codigo_carta":"23","Nombre":"Golpe defensivo","Efecto_tipo":2,"Efecto_potencia":1,"Tipo_defensa":1,"Descripcion":"Recibes 1 punto de defensa e inflijes 1 de daño al enemigo.","Imagen":"2_3_golpe_defensivo.png","ImagenLit":"2_3_golpe_defensivo_lit.png"},
			 	4:{"Codigo_carta":"24","Nombre":"Embestida","Efecto_tipo":2,"Efecto_potencia":2,"Tipo_defensa":1,"Descripcion":"Recibes 2 puntos de defensa e inflijes 2 de daño al enemigo.","Imagen":"2_4_embestida.png","ImagenLit":"2_4_embestida_lit.png"},
			 	5:{"Codigo_carta":"25","Nombre":"Escudar","Efecto_tipo":2,"Efecto_potencia":1,"Tipo_defensa":2,"Descripcion":"Das 1 punto de defensa a un aliado.","Imagen":"2_5_escudar.png","ImagenLit":"2_5_escudar_lit.png"},
			 	6:{"Codigo_carta":"26","Nombre":"Proteger","Efecto_tipo":2,"Efecto_potencia":2,"Tipo_defensa":2,"Descripcion":"Das 2 punto de defensa a un aliado.","Imagen":"2_6_proteger.png","ImagenLit":"2_6_proteger_lit.png"},
			 	7:{"Codigo_carta":"27","Nombre":"Tortuga","Efecto_tipo":2,"Efecto_potencia":3,"Tipo_defensa":2,"Descripcion":"Das 3 punto de defensa a un aliado.","Imagen":"2_7_tortuga.png","ImagenLit":"2_7_tortuga_lit.png"}},
			 
			 3:{0:{"Codigo_carta":"30","Nombre":"Grito de guerra","Efecto_tipo":3,"Efecto_potencia":1,"Tipo_buffo":0,"Descripcion":"Das 1 punto de ataque extra a todos los aliados en su siguiente ataque.","Imagen":"3_0_grito_de_guerra.png","ImagenLit":"3_0_grito_de_guerra_lit.png"},
			 	1:{"Codigo_carta":"31","Nombre":"Refuerzo","Efecto_tipo":3,"Efecto_potencia":2,"Tipo_buffo":0,"Descripcion":"Das 2 puntos de ataque extra a todos los aliados en su siguiente ataque.","Imagen":"3_1_refuezo.png","ImagenLit":"3_1_refuezo_lit.png"},
			 	2:{"Codigo_carta":"32","Nombre":"Subir la moral","Efecto_tipo":3,"Efecto_potencia":3,"Tipo_buffo":0,"Descripcion":"Das 3 puntos de ataque extra a todos los aliados en su siguiente ataque.","Imagen":"3_2_subir_moral.png","ImagenLit":"3_2_subir_moral_lit.png"},
			 	3:{"Codigo_carta":"33","Nombre":"Cuerno de batalla","Efecto_tipo":3,"Efecto_potencia":1,"Tipo_buffo":1,"Descripcion":"Das 1 punto de ataque extra a un aliado.","Imagen":"3_3_cuerno_de_batalla.png","ImagenLit":"3_3_cuerno_de_batalla_lit.png"},
			 	4:{"Codigo_carta":"34","Nombre":"Apoyo","Efecto_tipo":3,"Efecto_potencia":2,"Tipo_buffo":1,"Descripcion":"Das 2 puntos de ataque extra a un aliado.","Imagen":"3_4_apoyo.png","ImagenLit":"3_4_apoyo_lit.png"},
			 	5:{"Codigo_carta":"35","Nombre":"Distraccion","Efecto_tipo":3,"Efecto_potencia":3,"Tipo_buffo":1,"Descripcion":"Das 3 puntos de ataque extra a un aliado.","Imagen":"3_5_distraccion.png","ImagenLit":"3_5_distraccion_lit.png"},
			 	6:{"Codigo_carta":"36","Nombre":"Combinacion","Efecto_tipo":3,"Efecto_potencia":4,"Tipo_buffo":1,"Descripcion":"Das 4 puntos de ataque extra a un aliado.","Imagen":"3_6_combinacion.png","ImagenLit":"3_6_combinacion_lit.png"},
			 	7:{"Codigo_carta":"37","Nombre":"Ultimo aliento","Efecto_tipo":3,"Efecto_potencia":10,"Tipo_buffo":2,"Descripcion":"Evita que un aliado sea noqueado por el enemigo.","Imagen":"3_7_ultimo_aliento.png","ImagenLit":"3_7_ultimo_aliento_lit.png"}},
			 
			 4:{0:{"Codigo_carta":"40","Nombre":"Red","Efecto_tipo":4,"Efecto_potencia":1,"Tipo_nerffeo":0,"Descripcion":"Aturdes al enemigo por 1 turno.","Imagen":"4_0_red.png","ImagenLit":"4_0_red_lit.png"},
			 	1:{"Codigo_carta":"41","Nombre":"Confundir","Efecto_tipo":4,"Efecto_potencia":1,"Tipo_nerffeo":1,"Descripcion":"Reduces el ataque del enemigo en 1 punto.","Imagen":"4_1_confundir.png","ImagenLit":"4_1_confundir_lit.png"},
			 	2:{"Codigo_carta":"42","Nombre":"Repeler","Efecto_tipo":4,"Efecto_potencia":2,"Tipo_nerffeo":1,"Descripcion":"Reduces el ataque del enemigo en 2 puntos.","Imagen":"4_2_repeler.png","ImagenLit":"4_2_repeler_lit.png"},
			 	3:{"Codigo_carta":"43","Nombre":"Desarmar","Efecto_tipo":4,"Efecto_potencia":3,"Tipo_nerffeo":1,"Descripcion":"Reduces el ataque del enemigo en 3 puntos.","Imagen":"4_3_desarmar.png","ImagenLit":"4_3_desarmar_lit.png"},
			 	4:{"Codigo_carta":"44","Nombre":"Puñalada","Efecto_tipo":4,"Efecto_potencia":2,"Tipo_nerffeo":2,"Descripcion":"Aplicas el efecto de Sangrado al enemigo por +2 turnos.","Imagen":"4_4_puñalada.png","ImagenLit":"4_4_puñalada_lit.png"},
			 	5:{"Codigo_carta":"45","Nombre":"Corte profundo","Efecto_tipo":4,"Efecto_potencia":3,"Tipo_nerffeo":2,"Descripcion":"Aplicas el efecto de Sangrado al enemigo por +3 turnos.","Imagen":"4_5_corte_profundo.png","ImagenLit":"4_5_corte_profundo_lit.png"},
			 	6:{"Codigo_carta":"46","Nombre":"Espinas","Efecto_tipo":4,"Efecto_potencia":0,"Tipo_nerffeo":3,"Descripcion":"El enemigo recibe el mismo daño que inflije por 1 turno.","Imagen":"4_6_espinas.png","ImagenLit":"4_6_espinas_lit.png"},
			 	7:{"Codigo_carta":"47","Nombre":"Inversion","Efecto_tipo":4,"Efecto_potencia":0,"Tipo_nerffeo":4,"Descripcion":"El ataque del enemigo cura en vez de dañar por 1 turno.","Imagen":"4_7_inversion.png","ImagenLit":"4_7_inversion_lit.png"}}}

desafios={0:{0:{"Nombre":"Fiera I","Vida":1,"Ataque":1,"Nivel":0,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"fiera_icon.png","ImagenPer":"Fiera.png","Seleccion_icon":"fiera.png","Seleccion_icon_lit":"fiera_lit.png","Seleccion_icon_down":"fiera_down.png"},
			 1:{"Nombre":"Campeon I","Vida":1,"Ataque":2,"Nivel":0,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"campeon_icon.png","ImagenPer":"Campeon.png","Seleccion_icon":"campeon.png","Seleccion_icon_lit":"campeon_lit.png","Seleccion_icon_down":"campeon_down.png"},
			 2:{"Nombre":"Biga I","Vida":1,"Ataque":3,"Nivel":0,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"biga_icon.png","ImagenPer":"Biga.png","Seleccion_icon":"biga.png","Seleccion_icon_lit":"biga_lit.png","Seleccion_icon_down":"biga_down.png"}},
		  
		  1:{0:{"Nombre":"Fiera II","Vida":12,"Ataque":2,"Nivel":1,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"fiera_icon.png","ImagenPer":"Fiera.png","Seleccion_icon":"fiera.png","Seleccion_icon_lit":"fiera_lit.png","Seleccion_icon_down":"fiera_down.png"},
		  	 1:{"Nombre":"Campeon II","Vida":10,"Ataque":3,"Nivel":1,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"campeon_icon.png","ImagenPer":"Campeon.png","Seleccion_icon":"campeon.png","Seleccion_icon_lit":"campeon_lit.png","Seleccion_icon_down":"campeon_down.png"},
		  	 2:{"Nombre":"Biga II","Vida":8,"Ataque":4,"Nivel":1,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"biga_icon.png","ImagenPer":"Biga.png","Seleccion_icon":"biga.png","Seleccion_icon_lit":"biga_lit.png","Seleccion_icon_down":"biga_down.png"}},
		  
		  2:{0:{"Nombre":"Fiera III","Vida":14,"Ataque":3,"Nivel":2,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"fiera_icon.png","ImagenPer":"Fiera.png","Seleccion_icon":"fiera.png","Seleccion_icon_lit":"fiera_lit.png","Seleccion_icon_down":"fiera_down.png"},
		  	 1:{"Nombre":"Campeon III","Vida":12,"Ataque":4,"Nivel":2,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"campeon_icon.png","ImagenPer":"Campeon.png","Seleccion_icon":"campeon.png","Seleccion_icon_lit":"campeon_lit.png","Seleccion_icon_down":"campeon_down.png"},
		  	 2:{"Nombre":"Biga III","Vida":10,"Ataque":5,"Nivel":2,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"biga_icon.png","ImagenPer":"Biga.png","Seleccion_icon":"biga.png","Seleccion_icon_lit":"biga_lit.png","Seleccion_icon_down":"biga_down.png"}},
		  
		  3:{0:{"Nombre":"Fiera IV","Vida":1,"Ataque":40,"Nivel":3,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"fiera_icon.png","ImagenPer":"Fiera.png","Seleccion_icon":"fiera.png","Seleccion_icon_lit":"fiera_lit.png","Seleccion_icon_down":"fiera_down.png"},
		  	 1:{"Nombre":"Campeon IV","Vida":1,"Ataque":50,"Nivel":3,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"campeon_icon.png","ImagenPer":"Campeon.png","Seleccion_icon":"campeon.png","Seleccion_icon_lit":"campeon_lit.png","Seleccion_icon_down":"campeon_down.png"},
		  	 2:{"Nombre":"Biga IV","Vida":1,"Ataque":60,"Nivel":3,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"biga_icon.png","ImagenPer":"Biga.png","Seleccion_icon":"biga.png","Seleccion_icon_lit":"biga_lit.png","Seleccion_icon_down":"biga_down.png"}},
		  
		  4:{0:{"Nombre":"Fiera V","Vida":20,"Ataque":5,"Nivel":4,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"fiera_icon.png","ImagenPer":"Fiera.png","Seleccion_icon":"fiera.png","Seleccion_icon_lit":"fiera_lit.png","Seleccion_icon_down":"fiera_down.png"},
		  	 1:{"Nombre":"Campeon V","Vida":18,"Ataque":6,"Nivel":4,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"campeon_icon.png","ImagenPer":"Campeon.png","Seleccion_icon":"campeon.png","Seleccion_icon_lit":"campeon_lit.png","Seleccion_icon_down":"campeon_down.png"},
		  	 2:{"Nombre":"Biga V","Vida":16,"Ataque":7,"Nivel":4,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":"biga_icon.png","ImagenPer":"Biga.png","Seleccion_icon":"biga.png","Seleccion_icon_lit":"biga_lit.png","Seleccion_icon_down":"biga_down.png"}}}

especiales_efectos=["Daño","Heal","Defensa","Bufeo","Nerfeo"]

recompensas={0:{0:{"Nombre":"Cura I","Potencia":2,"Nivel":0,"Tipo":0},
				1:{"Nombre":"Espada I","Potencia":2,"Nivel":0,"Tipo":1},
				2:{"Nombre":"Armadura I","Potencia":2,"Nivel":0,"Tipo":2}},
			 
			 1:{0:{"Nombre":"Cura II","Potencia":2,"Nivel":1,"Tipo":0},
			 	1:{"Nombre":"Espada II","Potencia":2,"Nivel":1,"Tipo":1},
			 	2:{"Nombre":"Armadura II","Potencia":2,"Nivel":1,"Tipo":2}},
			 
			 2:{0:{"Nombre":"Cura III","Potencia":3,"Nivel":2,"Tipo":0},
			 	1:{"Nombre":"Espada III","Potencia":3,"Nivel":2,"Tipo":1},
			 	2:{"Nombre":"Armadura III","Potencia":3,"Nivel":2,"Tipo":2}},
			 
			 3:{0:{"Nombre":"Cura IV","Potencia":4,"Nivel":3,"Tipo":0},
			 	1:{"Nombre":"Espada IV","Potencia":4,"Nivel":3,"Tipo":1},
			 	2:{"Nombre":"Armadura IV","Potencia":4,"Nivel":3,"Tipo":2}},
			 
			 4:{0:{"Nombre":"Cura V","Potencia":5,"Nivel":4,"Tipo":0},
			 	1:{"Nombre":"Espada V","Potencia":5,"Nivel":4,"Tipo":1},
			 	2:{"Nombre":"Armadura V","Potencia":5,"Nivel":4,"Tipo":2}}}


def Combate_loop(clases_elegidas):
	todos_vivos=True
	cant_jugadores=len(clases_elegidas)
	jugadores=[]
	numeros_clases_jugadores=[]
	for j in range(cant_jugadores):

		clase_elegida_num=clases_elegidas[j]
		numeros_clases_jugadores.append(clase_elegida_num)
		print(clases[clase_elegida_num])
		clase_seleccionada={"Nombre":clases[clase_elegida_num]["Nombre"],"Tipos_cartas":clases[clase_elegida_num]["Tipos_cartas"],"Posibles_cartas":clases[clase_elegida_num]["Posibles_cartas"],"Vida":clases[clase_elegida_num]["Vida"],"Ataque":0,"Defensa":0,"Ataque_recompensa":0,"Defensa_recompensa":0,"Noqueado":False,"Ultimo_aliento":False,"ImagenHP":clases[clase_elegida_num]["ImagenHP"],"ImagenLit":clases[clase_elegida_num]["ImagenLit"],"ImagenDown":clases[clase_elegida_num]["ImagenDown"],"ImagenPer":clases[clase_elegida_num]["ImagenPer"],"ImagenPerLit":clases[clase_elegida_num]["ImagenPerLit"]}
		jugadores.append(clase_seleccionada)
	print(numeros_clases_jugadores)

	manos=[]
	print()

	musicaPeleaON = True

	if musicaPeleaON == True:
		musicaPelea = pygame.mixer.music.load(os.path.join(MUSICA_DIR, 'ingame.mp3'))
		pygame.mixer.music.play(-1, 0.0)

	codigo_manos=[]
	for j in range(cant_jugadores):

		manos.append({})
		codigo_manos.append([])
		for carta in range(4):
			
			agarrar_carta(carta,numeros_clases_jugadores,j,jugadores,codigo_manos,manos)

		

		print()

	multiplicador_desafios=[1,1.5,2,2.5]

	if cant_jugadores==1:
		cant_jugadores=0
	else:
		cant_jugadores-=1
	rondas=2

	fondoPath = os.path.join(COMBATE_DIR, "fondo.png")
	fondo = Background(fondoPath)
	

	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		mouse = pygame.Rect(mouseX, mouseY, 1, 1)
		click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					quit()
		botones_jugadores_HP=[]
		primer_boton_hp_x=-40
		primer_boton_hp_y=545
		segundo_boton_hp_x=-40
		segundo_boton_hp_y=645
		for bj in range(len(jugadores)):
			if bj==0:
				primer_boton_hp_x+=120
				print(jugadores[bj])
				boton_vida=Boton(jugadores[bj]["ImagenHP"],jugadores[bj]["ImagenLit"],HP_DIR,primer_boton_hp_x,primer_boton_hp_y)
				botones_jugadores_HP.append(boton_vida)
			elif bj==1:
				primer_boton_hp_x+=170
				print(jugadores[bj])
				boton_vida=Boton(jugadores[bj]["ImagenHP"],jugadores[bj]["ImagenLit"],HP_DIR,primer_boton_hp_x,primer_boton_hp_y)
				botones_jugadores_HP.append(boton_vida)
			elif bj==2:
				segundo_boton_hp_x+=120
				print(jugadores[bj])
				boton_vida=Boton(jugadores[bj]["ImagenHP"],jugadores[bj]["ImagenLit"],HP_DIR,segundo_boton_hp_x,segundo_boton_hp_y)
				botones_jugadores_HP.append(boton_vida)
			else:
				segundo_boton_hp_x+=170
				print(jugadores[bj])
				boton_vida=Boton(jugadores[bj]["ImagenHP"],jugadores[bj]["ImagenLit"],HP_DIR,segundo_boton_hp_x,segundo_boton_hp_y)
				botones_jugadores_HP.append(boton_vida)

		px=-50
		py=345
		personajes_lista_rect=[]
		personaje_img_lista=[]

		for pi in range(len(jugadores)):
			px+=130
			print("holas")
			print(jugadores[pi])
			personaje_img=Boton(jugadores[pi]["ImagenPer"],jugadores[pi]["ImagenPerLit"],PERSONAJES_DIR,px,py)
			personaje_img.cambiar_tamaño(round(personaje_img.imageX*0.85),round(personaje_img.imageY*0.85),px,py)
			personaje_img.rect.bottomleft=(px,py)
			personajes_lista_rect.append([personaje_img.image,personaje_img.rect])
			personaje_img_lista.append(personaje_img)

		terminador=0
		for ron in range(rondas):
			terminador+=1
			
			


			if todos_vivos==True:

				desafios_ronda=[]
				guardado_turnos_enemigo=[]
				vida_total=0
				niveles_desafios_ronda=Seleccion_lvl_desafios_Loop(clases_elegidas)
				for v in range(len(jugadores)):
					vida_total+=jugadores[v]["Vida"]


				for j in range(cant_jugadores+1):
					lvl_desafio_elegido=niveles_desafios_ronda[j]
					enemigo=desafios[lvl_desafio_elegido-1][random.randint(0,len(desafios[lvl_desafio_elegido-1])-1)]
					enemigo_elegido={"Nombre":enemigo["Nombre"],"Vida":enemigo["Vida"],"Ataque":enemigo["Ataque"],"Nivel":lvl_desafio_elegido-1,"Sangrado":0,"Aturdido":False,"Espinas":False,"Inversion":False,"Ataque_nerfeo":0,"Imagen":enemigo["Imagen"],"ImagenPer":enemigo["ImagenPer"],"Seleccion_icon":enemigo["Seleccion_icon"],"Seleccion_icon_lit":enemigo["Seleccion_icon_lit"],"Seleccion_icon_down":enemigo["Seleccion_icon_down"]}
					desafios_ronda.append(enemigo_elegido)
					print(enemigo_elegido)
				

				for des in range(len(desafios_ronda)):
					desafios_ronda[des]["Vida"]=round(desafios_ronda[des]["Vida"]*multiplicador_desafios[cant_jugadores])
					desafios_ronda[des]["Ataque"]=round(desafios_ronda[des]["Ataque"]*multiplicador_desafios[cant_jugadores])
				print(desafios_ronda)
				ataque_extra=0
				contador_turnos=0	
				
				for d in range(len(desafios_ronda)):
					Cambiar_Desafio_Loop(desafios_ronda,d,ron)
					if terminador==rondas and d==len(desafios_ronda)-1:
						terminar=True
					else:
						terminar=False
					if todos_vivos==True:
						while vida_total>0 and desafios_ronda[d]["Vida"]>0 and todos_vivos==True:

							pygame.mixer.music.set_volume(0.7)
							
							ataque_enemigo_turno=desafios_ronda[d]["Ataque"]
							print()
							for j in range(len(jugadores)):

								window.fill((33, 33, 33))
								window.blit(fondo.image, fondo.rect)
								dibujarTexto("RONDA "+str(ron+1),pygame.font.Font('TrajanPro-Regular.otf', 40),window,537,423,NEGRO)
								for pi in range(len(jugadores)):
									if jugadores[pi]["Vida"]>0:
										window.blit(personaje_img_lista[pi].image,personaje_img_lista[pi].rect)
								
								desafio_imagen=Boton(desafios_ronda[d]["ImagenPer"],desafios_ronda[d]["ImagenPer"],ENEMIGOS_DIR,960,215)
								desafio_imagen.cambiar_tamaño(round(desafio_imagen.imageX*0.85),round(desafio_imagen.imageY*0.85),1000,300)
								desafio_imagen.rect.bottomright=(1175,345)
								window.blit(desafio_imagen.image,desafio_imagen.rect)

								y=465
								desafio_icono=Boton(desafios_ronda[d]["Imagen"],desafios_ronda[d]["Imagen"],COMBATE_DIR,1175,600)
								desafio_icono.cambiar_tamaño(116,207,1165,600)
								window.blit(desafio_icono.image,desafio_icono.rect)
								dibujarTexto(str(desafios_ronda[d]["Vida"]),font,window,1170,663,NEGRO)
								dibujarTexto(str(desafios_ronda[d]["Ataque"]),font,window,1170,515,NEGRO)
								if desafios_ronda[d]["Sangrado"]>0:
									sangrado_img_rect=crear_imagen(ICON_DIR,"sangrado.png",900,75,True,True,0.7,0.7)
									dibujarTexto(str(desafios_ronda[d]["Sangrado"]),pygame.font.Font('TrajanPro-Regular.otf', 20),window,sangrado_img_rect.topleft[0]+8,sangrado_img_rect.topleft[1]+20,BLANCO)
								if desafios_ronda[d]["Aturdido"]==True:
									crear_imagen(ICON_DIR,"aturdir.png",950,75,False,True,0.7,0.7)
								if desafios_ronda[d]["Espinas"]==True:
									crear_imagen(ICON_DIR,"espinas.png",1000,75,False,True,0.7,0.7)
								if desafios_ronda[d]["Inversion"]==True:
									crear_imagen(ICON_DIR,"inversion.png",1050,75,False,True,0.7,0.7)
								if desafios_ronda[d]["Ataque_nerfeo"]>0:
									ataque_nerf_img_rect=crear_imagen(ICON_DIR,"menos_ataque.png",1100,75,True,True,0.7,0.7)
									dibujarTexto(str(desafios_ronda[d]["Ataque_nerfeo"]),pygame.font.Font('TrajanPro-Regular.otf', 20),window,ataque_nerf_img_rect.topleft[0]+12,ataque_nerf_img_rect.topleft[1]+18,BLANCO)
								for bj in range(len(jugadores)):
									if jugadores[bj]["Ataque"]>0 and jugadores[bj]["Vida"]>0 :
										ataque_buffo=crear_imagen(ICON_DIR,"mas_ataque.png",personaje_img_lista[bj].rect.topleft[0]+10,90,True,True,0.7,0.7)
										dibujarTexto(str(jugadores[bj]["Ataque"]),pygame.font.Font('TrajanPro-Regular.otf', 20),window,ataque_buffo.topleft[0]+15,ataque_buffo.topleft[1]+18,BLANCO)
									if jugadores[bj]["Ultimo_aliento"]==True:
										ultimo_aliento_icon=crear_imagen(HP_DIR,"no_puede_morir.png",personaje_img_lista[bj].rect.topleft[0]+50,90,True,True,0.7,0.7)
								x_primero=15
								y_primero=520
								x_segundo=15
								y_segundo=620
								for bj in range(len(botones_jugadores_HP)):
									
									if bj==0:
										x_primero+=80
										window.blit(botones_jugadores_HP[bj].image,botones_jugadores_HP[bj].rect)
										dibujarTexto(str(jugadores[bj]["Vida"]),font,window,x_primero,y_primero,NEGRO)
										dibujarTexto(str(jugadores[bj]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero-20,y_primero+40,NEGRO)
										dibujarTexto(str(jugadores[bj]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero+20,y_primero+40,NEGRO)

									elif bj==1:
										x_primero+=165
										window.blit(botones_jugadores_HP[bj].image,botones_jugadores_HP[bj].rect)
										dibujarTexto(str(jugadores[bj]["Vida"]),font,window,x_primero,y_primero,NEGRO)
										dibujarTexto(str(jugadores[bj]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero-15,y_primero+40,NEGRO)
										dibujarTexto(str(jugadores[bj]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_primero+25,y_primero+40,NEGRO)
									elif bj==2:
										x_segundo+=80
										window.blit(botones_jugadores_HP[bj].image,botones_jugadores_HP[bj].rect)
										dibujarTexto(str(jugadores[bj]["Vida"]),font,window,x_segundo,y_segundo,NEGRO)
										dibujarTexto(str(jugadores[bj]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo-20,y_segundo+40,NEGRO)
										dibujarTexto(str(jugadores[bj]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo+20,y_segundo+40,NEGRO)
									else:
										x_segundo+=165
										window.blit(botones_jugadores_HP[bj].image,botones_jugadores_HP[bj].rect)
										dibujarTexto(str(jugadores[bj]["Vida"]),font,window,x_segundo,y_segundo,NEGRO)
										dibujarTexto(str(jugadores[bj]["Ataque_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo-15,y_segundo+40,NEGRO)
										dibujarTexto(str(jugadores[bj]["Defensa_recompensa"]),pygame.font.Font('TrajanPro-Regular.otf', 17),window,x_segundo+25,y_segundo+40,NEGRO)

									if jugadores[bj]["Defensa"]>0:
										x_defensa=botones_jugadores_HP[bj].rect.topleft[0]+148
										y_defensa=botones_jugadores_HP[bj].rect.topleft[1]+22
										defensa=Boton("proteccion.png","proteccion.png",HP_DIR,x_defensa,y_defensa)
										defensa.cambiar_tamaño(30,30,x_defensa,y_defensa)
										window.blit(defensa.image,defensa.rect)
										dibujarTexto(str(jugadores[bj]["Defensa"]),pygame.font.Font('TrajanPro-Regular.otf', 15),window,botones_jugadores_HP[bj].rect.topleft[0]+145,botones_jugadores_HP[bj].rect.topleft[1]+16,BLANCO)
									
								if jugadores[j]["Vida"]>0:

									print(desafios_ronda[d]["Nombre"]+": Puntos de vida: "+str(desafios_ronda[d]["Vida"])+" Puntos de ataque: "+str(desafios_ronda[d]["Ataque"]))
									if desafios_ronda[d]["Vida"]>0:

										print("Tus Puntos de vida: "+str(jugadores[j]["Vida"]))
										print("\n")
										print("Mano de "+jugadores[j]["Nombre"]+" :")
										print()
										for i in range(len(manos[j])):
											print(str(i)+") "+manos[j][i]["Nombre"]+": "+manos[j][i]["Descripcion"])
										carta_1=Boton(manos[j][0]["Imagen"],manos[j][0]["ImagenLit"],CARTAS_DIR,515,600)
										window.blit(carta_1.image,carta_1.rect)
										carta_2=Boton(manos[j][1]["Imagen"],manos[j][1]["ImagenLit"],CARTAS_DIR,640,600)
										window.blit(carta_2.image,carta_2.rect)
										carta_3=Boton(manos[j][2]["Imagen"],manos[j][2]["ImagenLit"],CARTAS_DIR,765,600)
										window.blit(carta_3.image,carta_3.rect)
										carta_4=Boton(manos[j][3]["Imagen"],manos[j][3]["ImagenLit"],CARTAS_DIR,890,600)
										window.blit(carta_4.image,carta_4.rect)
										pygame.display.update()
										carta_usada=False
										
										while not carta_usada:
											event =pygame.event.wait()
											mouseX, mouseY = pygame.mouse.get_pos()
											mouse = pygame.Rect(mouseX, mouseY, 1, 1)
											click = pygame.mouse.get_pressed()
											carta_1.IluminarMouse(mouse,click,window)
											carta_2.IluminarMouse(mouse,click,window)
											carta_3.IluminarMouse(mouse,click,window)
											carta_4.IluminarMouse(mouse,click,window)
											if event.type== MOUSEBUTTONDOWN and  mouse.colliderect(carta_1.rect):

									
												print("click")
												carta_seleccionada=0
												carta_usada=True
												print("Carta 1")
												
												pygame.display.update()
											elif event.type== MOUSEBUTTONDOWN and mouse.colliderect(carta_2.rect):
												carta_seleccionada=1
												carta_usada=True
												print("Carta 2")
												
												pygame.display.update()
											elif event.type== MOUSEBUTTONDOWN and mouse.colliderect(carta_3.rect):
												carta_seleccionada=2
												carta_usada=True
												print("Carta 3")
												
												pygame.display.update()
											elif event.type== MOUSEBUTTONDOWN and mouse.colliderect(carta_4.rect):
												carta_seleccionada=3
												carta_usada=True
												print("Carta 4")
												
												pygame.display.update()

											pygame.display.update()

										carta_turno=manos[j][carta_seleccionada]

										agarrar_carta(carta_seleccionada,numeros_clases_jugadores,j,jugadores,codigo_manos,manos)
										codigo_manos[j].pop(codigo_manos[j].index(carta_turno["Codigo_carta"]))

										if carta_turno["Efecto_tipo"]==0:

											desafios_ronda[d]["Vida"]-=carta_turno["Efecto_potencia"]+jugadores[j]["Ataque"]+jugadores[j]["Ataque_recompensa"]
											sonAtaque.play()
											print("Le quitaste "+str(carta_turno["Efecto_potencia"])+" puntos de vida al enemigo.")
											if carta_turno["Secundario_tipo"]==1:
												desafios_ronda[d]["Sangrado"]+=1
												sonSangrado.play()
												print("Tu ataque aplico el efecto de Sangrado por 1 turno al enemigo."+"\n")
											elif carta_turno["Secundario_tipo"]==2:
												jugadores[j]["Vida"]+=carta_turno["Secundario_potencia"]
												sonCuracion.play()
												print("Tu ataque te curo "+str(carta_turno["Secundario_potencia"])+" puntos."+"\n")
											elif carta_turno["Secundario_tipo"]==3:
												jugadores[j]["Vida"]-=2
												sonSangrado.play()
												print("Tu ataque te quito 2 puntos de vida a ti tambien."+"\n")
											jugadores[j]["Ataque"]=0
										
										elif carta_turno["Efecto_tipo"]==1:

											if carta_turno["Tipo_cura"]==0:

												jugadores[j]["Vida"]+=carta_turno["Efecto_potencia"]
												sonCuracion.play()
												print("Te curaste "+str(carta_turno["Efecto_potencia"])+" puntos de vida.")
											elif carta_turno["Tipo_cura"]==1:
												for jug in range(len(jugadores)):
													if jugadores[jug]["Vida"]>0:
														jugadores[jug]["Vida"]+=carta_turno["Efecto_potencia"]
												sonCuracion.play()
												print("Curaste a todos "+str(carta_turno["Efecto_potencia"])+" puntos de vida.")
											else:
												jugador_elegido=elegir_aliado(botones_jugadores_HP,jugadores,personaje_img_lista)

												jugadores[jugador_elegido]["Vida"]+=carta_turno["Efecto_potencia"]
												sonCuracion.play()
												print("Curaste al "+jugadores[jugador_elegido]["Nombre"] +" "+str(carta_turno["Efecto_potencia"])+" puntos de vida.")
										elif carta_turno["Efecto_tipo"]==2:

											if carta_turno["Tipo_defensa"]==0 or carta_turno["Tipo_defensa"]==1:
												jugadores[j]["Defensa"]+=carta_turno["Efecto_potencia"]
												sonDefensa.play()
												print("Aumentaste tu defensa en "+ str(carta_turno["Efecto_potencia"])+" puntos.")
											if carta_turno["Tipo_defensa"]==1:
												desafios_ronda[d]["Vida"]-=carta_turno["Efecto_potencia"]
												sonAtaque.play()
												print("Tambien le sacaste "+ str(carta_turno["Efecto_potencia"])+" puntos de vida al enemigo.")
											elif carta_turno["Tipo_defensa"]==2:

												jugador_elegido=elegir_aliado(botones_jugadores_HP,jugadores,personaje_img_lista)
												jugadores[jugador_elegido]["Defensa"]+=carta_turno["Efecto_potencia"]
												sonDefensa.play()
												print("Aumentaste la defensa del "+jugadores[jugador_elegido]["Nombre"] +" en "+ str(carta_turno["Efecto_potencia"])+" puntos.")

										elif carta_turno["Efecto_tipo"]==3:

											if carta_turno["Tipo_buffo"]==0:
												for jug in range(len(jugadores)):
													if not jugadores[jug]["Noqueado"]:
														jugadores[jug]["Ataque"]+=carta_turno["Efecto_potencia"]
												sonBuffeo.play()
												print("Aumentaste el ataque a todos en "+str(carta_turno["Efecto_potencia"])+" puntos.")	
											elif carta_turno["Tipo_buffo"]==1:
												jugador_elegido=jugador_elegido=elegir_aliado(botones_jugadores_HP,jugadores,personaje_img_lista)
												jugadores[jugador_elegido]["Ataque"]+=carta_turno["Efecto_potencia"]
												sonBuffeo.play()
												print("Aumentaste el ataque del "+jugadores[jugador_elegido]["Nombre"]+" en "+ str(carta_turno["Efecto_potencia"])+" puntos.")

											else:
												jugador_elegido=elegir_aliado(botones_jugadores_HP,jugadores,personaje_img_lista)
												jugadores[jugador_elegido]["Ultimo_aliento"]=True
												sonDefensa.play()
												print("Ahora el "+jugadores[jugador_elegido]["Nombre"]+" puede evitar ser noqueado 1 vez.")

												

											
										else:
											if carta_turno["Tipo_nerffeo"]==0:
												desafios_ronda[d]["Aturdido"]=True
												sonDebuffeo.play()
												print("Aturdiste al enemigo.")
											
											elif carta_turno["Tipo_nerffeo"]==1:
												desafios_ronda[d]["Ataque_nerfeo"]+=carta_turno["Efecto_potencia"]
												sonDebuffeo.play()
												print("Reduciste el seguiente ataque del enemigo por "+str(carta_turno["Efecto_potencia"])+" puntos.")
											
											elif carta_turno["Tipo_nerffeo"]==2:
												desafios_ronda[d]["Sangrado"]+=carta_turno["Efecto_potencia"]
												sonSangrado.play()
												print("Aplicaste sangrado al enemigo por "+str(carta_turno["Efecto_potencia"])+" turnos.")

											elif carta_turno["Tipo_nerffeo"]==3:
												desafios_ronda[d]["Espinas"]=True
												sonSangrado.play()
												print("El enemigo se infligira el mismo daño que su ataque.")

											else:
												desafios_ronda[d]["Inversion"]=True
												sonCuracion.play()
												print("El siguiente ataque del enemigo curara al objetivo.")
										
										print()

							if desafios_ronda[d]["Vida"]>0 and todos_vivos==True:
								time.sleep(1)
								jugador_aleatorio=random.randint(0,len(jugadores)-1)
								vida_final=ataque_enemigo_turno-jugadores[jugador_aleatorio]["Defensa"]-jugadores[jugador_aleatorio]["Defensa_recompensa"]-desafios_ronda[d]["Ataque_nerfeo"]
								
								while jugadores[jugador_aleatorio]["Noqueado"]==True:
									jugador_aleatorio=random.randint(0,len(jugadores)-1)
								sonAtaque.play()
								print("El enemigo decide atacar al "+jugadores[jugador_aleatorio]["Nombre"])
										
								if not desafios_ronda[d]["Aturdido"]:
									if vida_final<=0:
										sonDefensa.play()
										print("La defensa fue tan grande que el ataque del enemigo no tuvo efecto.")
										if jugadores[jugador_aleatorio]["Defensa"]>ataque_enemigo_turno-desafios_ronda[d]["Ataque_nerfeo"]:
											jugadores[jugador_aleatorio]["Defensa"]-=ataque_enemigo_turno
											
										else:
											jugadores[jugador_aleatorio]["Defensa"]=0
										
									else:
										if not desafios_ronda[d]["Inversion"]:
											print("El enemigo te quito "+str(ataque_enemigo_turno)+" puntos de vida.")
											jugadores[jugador_aleatorio]["Vida"]-=vida_final
											jugadores[jugador_aleatorio]["Defensa"]=0
											if jugadores[jugador_aleatorio]["Vida"]<=0 and desafios_ronda[d]["Vida"]>0:
												jugadores[jugador_aleatorio]["Vida"]=0
												botones_jugadores_HP[jugador_aleatorio].dir_path = os.path.join(HP_DIR, jugadores[jugador_aleatorio]["ImagenDown"])
												botones_jugadores_HP[jugador_aleatorio].image=pygame.image.load(botones_jugadores_HP[jugador_aleatorio].dir_path).convert_alpha()
							
											if jugadores[jugador_aleatorio]["Vida"]<=0:
												print("El "+jugadores[jugador_aleatorio]["Nombre"]+" fue noqueado. No podra hacer nada hasta que se complete el desafio.")
											if desafios_ronda[d]["Espinas"]==True:
												desafios_ronda[d]["Vida"]-=ataque_enemigo_turno
												sonSangrado.play()
												print("El ataque del enemigo tambien lo daño a si mismo por la carta Espinas.")
										else:
											jugadores[jugador_aleatorio]["Vida"]+=desafios_ronda[d]["Ataque"]
											sonCuracion.play()
											print("El ataque del enemigo curo "+str(desafios_ronda[d]["Ataque"])+" puntos de vida gracias a la carta Inversion.")
									desafios_ronda[d]["Ataque_nerfeo"]=0
								else:
									sonDefensa.play()
									print("El enemigo no puede atacar porque esta Aturdido.")
									desafios_ronda[d]["Aturdido"]=False
								print(jugadores[jugador_aleatorio]["Nombre"])
								if jugadores[jugador_aleatorio]["Vida"]<0 and jugadores[jugador_aleatorio]["Ultimo_aliento"]==True:
									print("El "+jugadores[jugador_aleatorio]["Nombre"]+" evita caer noqueado gracias al Ultimo Aliento.")
									jugadores[jugador_aleatorio]["Ultimo_aliento"]=False
									jugadores[jugador_aleatorio]["Vida"]=4
								if desafios_ronda[d]["Sangrado"]>0:
									desafios_ronda[d]["Vida"]-=1
									sonSangrado.play()
									print("Debido al efecto de sangrado el enemigo perdio 1 punto de vida.")
									desafios_ronda[d]["Sangrado"]-=1
								if desafios_ronda[d]["Sangrado"]==0:
									print("El enemigo ya no sufre de Sangrado.")

							else:
								if not todos_vivos:
									print("Todos los jugadores murieron")
							print()
							vivos=0
							for v in range(len(jugadores)):
								if jugadores[v]["Vida"]>0:
									vivos+=1

							if vivos==0:
								todos_vivos=False
							contador_turnos+=1
					print(terminar)	
					if todos_vivos==True and desafios_ronda[d]["Vida"]<=0:
						Recompensas_Loop(jugadores,desafios_ronda,d,terminar,numeros_clases_jugadores)
						
			print(jugadores)
			if todos_vivos==True:
				for j in range(len(jugadores)):
					if jugadores[j]["Vida"]<=0:
						print(jugadores[j]["Nombre"])
						jugadores[j]["Vida"]+=4
						botones_jugadores_HP[j].dir_path = os.path.join(HP_DIR, jugadores[j]["ImagenHP"])
						botones_jugadores_HP[j].image=pygame.image.load(botones_jugadores_HP[j].dir_path).convert_alpha()
					else:
						jugadores[j]["Vida"]+=4


		final(todos_vivos)

globales()