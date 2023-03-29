#ok banda hoy hare un vaso, un recipiente en python
import pygame, sys
import numpy as np
import math
##from electre_class import *
from RIT_secondattempt  import *
import time
# Initialize the pygame
pygame.init()

### Problema 4
##dTperm = 20
##Te = np.array([260,160,50,20,50])
##Ts = np.array([60,30,100,200,100])
##FCP = np.array([1.48,4.42,3.02,2.98,5.98])
##Q = np.array([296,574.6,151,536.4,299])

### problema 5
##dTperm = 20
##Te = np.array([190,290,80,80,50])
##Ts = np.array([60,90,130,130,230])
##FCP = np.array([2.21,0.74,1.5,2.99,1.49])
##Q = np.array([50,80,140,140,240])

###problema 3
##dTperm = 20
##Te = np.array([280,230,50,170])
##Ts = np.array([70,110,210,260])
##FCP = np.array([4.5,7.5,6,9])
##Q = np.array([945,900,960,810])

### Problema 1 Lazos de calor
##dTperm = 10
##Te = np.array([170,150,20,80])
##Ts = np.array([60,30,35,140])
##FCP = np.array([3,1.5,2,4])


### Problema 6 Lazos de calor
##dTperm = 10
##Te = np.array([250,200,140,30])
##Ts = np.array([40,100,230,180])
##FCP = np.array([15,25,30,20])
##Q = np.array([3150,2500,2700,3000])

### Problema 1 Lazos de calor
##dTperm = 20
##Te = np.array([250,160,60,20])
##Ts = np.array([20,40,160,190])
##FCP = np.array([1.9,2.3,2.8,1.900001])

### Problema 1 Lazos de calor
##dTperm = 20
##Te = np.array([300,220,110,30,150])
##Ts = np.array([50,120,200,150,230])
##FCP = np.array([2,4,2,1,6])

# Problema 1 Lazos de calor
dTperm = 30
Te = np.array([300,220,110,30,150])
Ts = np.array([50,120,200,150,230])
FCP = np.array([2,4,2,1,6])




rit = RIT(Te,Ts,FCP,dTperm)
tabla1 =  rit.tabla1()
##print(rit.tabla1())
tabla1shape = np.shape(tabla1)
tabla2 =  rit.tabla2()
tabla2shape = np.shape(tabla2)
tabla3 =  rit.tabla3()
tabla3shape = np.shape(tabla3)
pinch = rit.pinch_point()
##print(pinch)
##print(f"{tabla1}  {tabla2}  {tabla3}  {tabla1shape}  {tabla2shape}  {tabla3shape}")
#Create the screen
HEIGHT, WIDTH = 400,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pygame project")
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)

#Create the clock
clock = pygame.time.Clock()

arriba_pinch_tabla = rit.up_pinch()
arriba_pinch_forma = np.shape(arriba_pinch_tabla)


abajo_pinch_tabla = rit.down_pinch()
abajo_pinch_forma = np.shape(abajo_pinch_tabla)

#Codeline for the image background
#background = pygame.image.load('')


scale = 60

# variables
segundero = 0
cur_vel_x = 0
cur_vel_y = 0
cur_x = 100
cur_y = 100
# programare visualmente el arriba_pinch_tabla de





# Funciones de dibujo
def creartabla(title,matriz,tamanio,scale,posx,posy,color):
    text(title,posx,posy,color)
    titlespace = 40
    offspace = 5
    if len(tamanio) == 1 :
        for i in range(tamanio[0]):
            rect(posx,scale*i+posy+titlespace,scale-offspace,scale-offspace)
            text(str(matriz[i]),posx,scale*i+posy+titlespace,color)
    else:
        for i in range(tamanio[0]):
            for j in range(tamanio[1]):
                #coordinates.append(np.array([scale*i,scale*j]))
                rect(scale*j+posx,scale*i+posy+titlespace,scale-offspace,scale-offspace)
                text(str(matriz[i,j]),scale*j+posx,scale*i+posy+titlespace,color)
def dot(xi,yi,r):
    pygame.draw.circle(screen,(255,255,0),(xi,yi),r)
def line(xi,yi,xf,yf):
    pygame.draw.line(screen,(255,255,255),(xi,yi),(xf,yf),1)
def rect(xi,yi,w,h):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
def text(string,xi,yi,color):
    textsurface = font.render(string,False,color,(198,233,92))
    screen.blit(textsurface,(xi,yi))
def panel(xi,yi,string):
    w,h = 250,40
    pygame.draw.rect(screen,(25,25,255),(xi,yi,w,h))
    textsurface = font.render(string,False,(255,255,255))
    screen.blit(textsurface,(xi,yi))
def cursor(xi,yi):
    ri,re = 10,12
    pygame.draw.circle(screen,(0,0,0),(xi,yi),re)
    pygame.draw.circle(screen,(255,255,255),(xi,yi),ri)
def vaso(xi,yi,w,h,e):
    pygame.draw.rect(screen,(255,255,255),(xi,yi,w,h))
    pygame.draw.rect(screen,(0,0,0),(xi+e,yi,w-2*e,h-e))
    
aux = 1
while True:
    clock.get_time()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = -10
            if event.key == pygame.K_a:
                cur_vel_x = -10
            if event.key == pygame.K_x:
                pass
            if event.key == pygame.K_d:
                cur_vel_x = 10
            if event.key == pygame.K_s:
                cur_vel_y = 10
            if event.key == pygame.K_n:
                pass
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_q:
                pass
            if event.key == pygame.K_w:
                cur_vel_y = 0
            if event.key == pygame.K_e:
                pass
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                cur_vel_x = 0
            if event.key == pygame.K_s:
                cur_vel_y = 0
            if event.key == pygame.K_d:
                cur_vel_x = 0
            if event.key == pygame.K_f:
                pass
    screen.fill((0,0,0))
    # A partir de aqui dibujas
    #print(segundero)
    
    creartabla('RIT',tabla1,tabla1shape,scale,cur_x,cur_y,(203,10,29))
    creartabla('Punto Pinch',tabla2,tabla2shape,scale,cur_x,cur_y+scale*7,(203,10,29))
    creartabla('Cascada de calor',tabla3,tabla3shape,scale,cur_x,cur_y+scale*(16),(203,10,29))
    creartabla('Arriba del Pinch',arriba_pinch_tabla,arriba_pinch_forma,scale,cur_x,cur_y+scale*(25),(203,10,29))
    creartabla('Abajo del Pinch',abajo_pinch_tabla,abajo_pinch_forma,scale,cur_x,cur_y+scale*(31),(203,10,29))
    #cursor
    cur_x += cur_vel_x
    cur_y += cur_vel_y

    #Aqui termina el loop
    segundero = segundero + 1
    pygame.display.update()
    clock.tick(30)
