import os
import pygame, sys, time
from pygame.locals import *
from menu import MenuPrincipal_Loop
from ObjetosClases import globales

pygame.init()
#font = pygame.font.Font(None, 20)

globales()
pygame.display.set_caption('Arenas y Gladiadores')

MenuPrincipal_Loop()
