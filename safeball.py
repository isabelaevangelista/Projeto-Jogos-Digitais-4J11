import math
import random
import time
import pygame
from pygame.locals import *

###
##
# INIT
##
###

pygame.init()
screen = pygame.display.set_mode((780,451))
clock = pygame.time.Clock()
screen.fill((255,255,255))
pygame.display.set_caption("Safeball")
icon = pygame.image.load("kai/cabeca-kai.png")
pygame.display.set_icon(icon)

###
##
# PLACARES
##
###

font = pygame.font.SysFont('forte',40)
placarTotal = 0

###
##
# TEMPO
##
###

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)

###
##
# VARIAVEIS DE MUSICA
##
###

musica = True # a desenvolver


###
##
# MAPAS
##
###

recorde = 0
mapaJaProTreino = pygame.image.load("telas/fundo-ja-pro-treino.png").convert_alpha()
mapaDribleSePuder = pygame.image.load("telas/fundo-drible-se-puder.png").convert_alpha()
telaInicial = pygame.image.load("telas/fundo-tela-inicial.jpg").convert_alpha()
telaInicialSom = pygame.image.load("telas/tela-som-ativado.png").convert_alpha()
telaInicialSemSom = pygame.image.load("telas/tela-som-desativado.png").convert_alpha()
telaJogos = pygame.image.load("telas/tela-jogos.png").convert_alpha()
telaPontuacao = pygame.image.load("telas/pontuacao.png").convert_alpha()

###
##
# SPIRITS
##
###




###
##
# Jogo 1 - Ja pro treino
##
###

bolaFutebol = pygame.image.load("img/bola.png").convert_alpha()
bolaVolei = pygame.image.load("img/bola_volei.png").convert_alpha()
camisa = pygame.image.load("img/camisa.png").convert_alpha()
caneleira = pygame.image.load("img/caneleira.png").convert_alpha()
faixaCapitao = pygame.image.load("img/capitao.png").convert_alpha()
chuteira = pygame.image.load("img/chuteira.png").convert_alpha()
raquete = pygame.image.load("img/raquete.png").convert_alpha()
sacolaTacos = pygame.image.load("img/tacos.png").convert_alpha()

itens = [bolaFutebol, bolaVolei, camisa, caneleira, faixaCapitao, chuteira, raquete, sacolaTacos]

itensCertos = [bolaFutebol, camisa, caneleira, faixaCapitao, chuteira]
itensErrados = [bolaVolei, raquete, sacolaTacos]

###
##
# Jogo 2 - Drible se puder
##
###






###
##
#   MENU
##
###

def menu():
    #boleanos p definir o andamento
    menu = True
    jogos = False
    sobre = False
    btn1 = False
    btn2 = False
    global recorde

    #bg
    global telaInicial
    global telaJogos
    telaSobre = pygame.image.load("telas/tela-sobre.png").convert_alpha()
    
    #img
    bolaFutebol = pygame.image.load("img/bola.png").convert_alpha()

    while menu:
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telaInicialSom, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270:
                    btn1 = True
                else:
                    btn1 = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370:
                    btn2 = True
                else:
                    btn2 = False
            if event.type == MOUSEBUTTONDOWN:
                #btn musica

                #btn menu
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 260 and mouse_position[1] <= 300 and menu == True:
                    menu = False
                    
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270 and jogos == False:
                    jogos = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and jogos == True:
                    jogos = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370 and sobre == False:
                    sobre = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and sobre == True:
                    sobre = False

            #hover mousemotion
            if btn1:
                screen.blit(bolaFutebol, (480, 235))
            if btn2:
                screen.blit(bolaFutebol, (480, 325))

            if jogos:
                menuJogos()
            if sobre:
                screen.blit(telaSobre, (0,0))
                #high = font.render("Recorde: "+str(recorde), True, (0,0,0))
                #screen.blit(high, (300,330))

            #printar tela
            pygame.display.update()
            clock.tick(30)

def menuJogos():
    #boleanos p definir o andamento
    menuJogos = True
    jogo1 = False
    jogo2 = False
    btnJ1 = False
    btnJ2 = False

    while menuJogos:
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telaJogos, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                if mouse_position[0] >= 260 and mouse_position[0] <= 560 and mouse_position[1] >= 215 and mouse_position[1] <= 300:
                    btnJ1 = True
                else:
                    btnJ1 = False
                if mouse_position[0] >= 260 and mouse_position[0] <= 560 and mouse_position[1] >= 310 and mouse_position[1] <= 380:
                    btnJ2 = True
                else:
                    btnJ2 = False
            if event.type == MOUSEBUTTONDOWN:
                #btn menu
                if mouse_position[0] >= 18 and mouse_position[0] <= 60 and mouse_position[1] >= 375 and mouse_position[1] <= 430 and menuJogos == True:
                    print("blabla")
                    menuJogos = False
                    menu()                    
                    
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270 and jogo1 == False:
                    jogo1 = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and jogo1 == True:
                    jogo1 = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370 and jogo2 == False:
                    jogo2 = True
                elif mouse_position[0] >= 0 and mouse_position[0] <= 785 and mouse_position[1] >= 0 and mouse_position[1] <= 550 and jogo2 == True:
                    jogo2 = False

            #hover mousemotion
            if btnJ1:
                screen.blit(bolaFutebol, (180, 225))
            if btnJ2:
                screen.blit(bolaFutebol, (180, 325))

            #if jogo1:
                #screen.blit(telaSobre, (0,0))
            #if jogo2:
                #screen.blit(telaSobre, (0,0))

            #printar tela
            pygame.display.update()
            clock.tick(30)

    

while True:
    menu()
    menuJogos()
