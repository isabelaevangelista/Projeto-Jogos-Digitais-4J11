# Isabela Maria Evangelista
# 31907891
# Jogos Digitais 4J

import math
import random
import time
import pygame
from pygame.locals import *

##
## VARIAVEIS DE INICIALIZACAO
##

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((750,451))
clock = pygame.time.Clock()
screen.fill((255,255,255))
pygame.display.set_caption("Safeball")
icon = pygame.image.load("img/kai/cabeca-kai.png")
pygame.display.set_icon(icon)

##
## FONTES
##

font = pygame.font.SysFont('Comic Sans', 36)
fontLittle = pygame.font.SysFont('Comic Sans', 30)
fontMini = pygame.font.SysFont('Comic Sans', 18)

##
## PLACARES
##

placarTotal = 0
placarJogo1 = 0
placarJogo2 = 0

##
## VARIAVEIS GERAIS
##

mouse_position = pygame.mouse.get_pos()
iconeDuvida = pygame.image.load("img/telas/icone-duvida.png").convert_alpha()
bolaIcone = pygame.image.load("img/bola-icone.png").convert_alpha()

##
## VARIAVEIS DE TEMPO
##

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)

##
## VARIAVEIS DE MUSICA
##

musica = True # a desenvolver
electrodoodle = pygame.mixer.music.load("sonoplastia/electrodoodle.mp3")
pygame.mixer.music.play()
somPorta = pygame.mixer.Sound("sonoplastia/porta.mp3")
somZiper = pygame.mixer.Sound("sonoplastia/ziper.mp3")

##
## MAPAS
##

mapaDribleSePuder = pygame.image.load("img/telas/fundo-drible-se-puder.png").convert_alpha()
telaInicialSom = pygame.image.load("img/telas/tela-som-ativado.png").convert_alpha()
telaInicialSemSom = pygame.image.load("img/telas/tela-som-desativado.png").convert_alpha()
telaSobre = pygame.image.load("img/telas/tela-sobre.png").convert_alpha()
telaJogos = pygame.image.load("img/telas/tela-jogos.png").convert_alpha()
telaJogo1 = pygame.image.load("img/telas/fundo-ja-pro-treino.png").convert_alpha()
telaInstJogo1 = pygame.image.load("img/telas/instrucoes-ja-pro-treino.png").convert_alpha()
telaPontuacao = pygame.image.load("img/telas/tela-pontuacao.png").convert_alpha()
telaJogo2 = pygame.image.load("img/telas/fundo-drible-se-puder.png").convert_alpha()
telaInstJogo2 = pygame.image.load("img/telas/instrucoes-drible-se-puder.png").convert_alpha()

##
## JOGO 1
##

btnJogar = pygame.image.load("img/telas/btnJogar.png").convert_alpha()
btnHome = pygame.image.load("img/telas/btn-home.png").convert_alpha()
vida = pygame.image.load("img/kai/icone-vida.png").convert_alpha()
mochila = pygame.image.load("img/mochila.png").convert_alpha()
caixa = pygame.image.load("img/caixa.png").convert_alpha()
kaiCimaPes = pygame.image.load("img/kai/kai-cima-pes-juntos.png").convert_alpha()
bolaFutebol = pygame.image.load("img/bola.png").convert_alpha()
bolaVolei = pygame.image.load("img/bola_volei.png").convert_alpha()
camisa = pygame.image.load("img/camisa.png").convert_alpha()
caneleira = pygame.image.load("img/caneleira2.png").convert_alpha()
faixaCapitao = pygame.image.load("img/capitao.png").convert_alpha()
chuteira = pygame.image.load("img/chuteira.png").convert_alpha()
capacete = pygame.image.load("img/capacete.png").convert_alpha()
luvas = pygame.image.load("img/luvas.png").convert_alpha()

itens = [bolaFutebol, camisa, caneleira, faixaCapitao, chuteira, capacete, luvas, bolaVolei]

itensCertos = [bolaFutebol, camisa, caneleira, faixaCapitao, chuteira]
itensErrados = [bolaVolei, capacete, luvas]

##
## JOGO 2 - DRIBLE SE PUDER
##

npc1 = pygame.image.load("img/npcs/npc1.png").convert_alpha()
npc2 = pygame.image.load("img/npcs/npc2.png").convert_alpha()
npc3 = pygame.image.load("img/npcs/npc3.png").convert_alpha()
colisao = pygame.USEREVENT+2


def menu():
    btn1 = False
    btn2 = False
    global recorde
    global bolaIcone
    global mouse_position
    global telaInicialSom
    global telaInicialSemSom
    global telaJogos
    global musica

    while True:
        mouse_position = pygame.mouse.get_pos()
        if musica:
            screen.blit(telaInicialSom, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                #hover da bola nos botões
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270:
                    btn1 = True
                else:
                    btn1 = False
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370:
                    btn2 = True
                else:
                    btn2 = False
                    
            if event.type == MOUSEBUTTONDOWN:
                #botão música
                if mouse_position[0] >= 670 and mouse_position[0] <= 735 and mouse_position[1] >= 375 and mouse_position[1] <= 440 and musica == True:
                    musica = False                    
                    pygame.mixer.music.stop()
                    screen.blit(telaInicialSemSom, (0,0))
                elif mouse_position[0] >= 670 and mouse_position[0] <= 735 and mouse_position[1] >= 375 and mouse_position[1] <= 440 and musica == False:
                    musica = True
                    pygame.mixer.music.play()
                    
                #botão para menu dos jogos
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270:
                    menuJogos()
                #botão para página de informações
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370:
                    sobre()

        #ativação do mousemotion hover
        if btn1:
            screen.blit(bolaIcone, (470, 230))
        if btn2:
            screen.blit(bolaIcone, (470, 320))

        #att da tela
        pygame.display.update()
        clock.tick(30)

def sobre():
    global telaSobre
    global mouse_position
    
    while True:
        
        screen.blit(telaSobre, (0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                #botão para voltar para o menu
                if mouse_position[0] >= 18 and mouse_position[0] <= 60 and mouse_position[1] >= 375 and mouse_position[1] <= 430:
                    menu()

        #att da tela
        pygame.display.update()
        clock.tick(30)        

def menuJogos():
    btnJ1 = False
    btnJ2 = False
    global bolaIcone
    global mouse_position

    while True:
        
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telaJogos, (0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEMOTION:
                #hover da bola nos botões
                if mouse_position[0] >= 260 and mouse_position[0] <= 560 and mouse_position[1] >= 215 and mouse_position[1] <= 300:
                    btnJ1 = True
                else:
                    btnJ1 = False
                if mouse_position[0] >= 260 and mouse_position[0] <= 560 and mouse_position[1] >= 310 and mouse_position[1] <= 380:
                    btnJ2 = True
                else:
                    btnJ2 = False
            if event.type == MOUSEBUTTONDOWN:
                #botão para voltar para o menu
                if mouse_position[0] >= 18 and mouse_position[0] <= 60 and mouse_position[1] >= 375 and mouse_position[1] <= 430:
                    menu()                    

                #botão para ir para o primeiro jogo
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 212 and mouse_position[1] <= 270:
                    jogo1()
                #botão para ir para o segundo jogo
                if mouse_position[0] >= 295 and mouse_position[0] <= 510 and mouse_position[1] >= 310 and mouse_position[1] <= 370:
                    jogo2()

        #hover mousemotion
        if btnJ1:
            screen.blit(bolaIcone, (165, 225))
        if btnJ2:
            screen.blit(bolaIcone, (165, 325))

        #att da tela
        pygame.display.update()
        clock.tick(30)

def jogo1():
    global telaInstJogo1
    global telaJogo1
    global kaiCimaPes
    global itens
    global caixa
    global mochila
    global placarJogo1
    global mouse_position
    px = 0
    py = 0
    x = 350
    y = 350
    angulo = 180
    maosVazias = True
    maosCtd = ""
    conteudo = ""    
    duvida = True
    timer = 40
    qtdVidas = 3

    while True:
        
        personagem = pygame.transform.rotate(kaiCimaPes, angulo)               

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                #tela inst
                if mouse_position[0] >= 640 and mouse_position[0] <= 670 and mouse_position[1] >= 80 and mouse_position[1] <= 110 and duvida == True:
                    duvida = False
                #tela jogo
                if mouse_position[0] >= 300 and mouse_position[0] <= 740 and mouse_position[1] >= 200 and mouse_position[1] <= 420 and duvida == False:
                    duvida = True
                else:
                    duvida = False

            if event.type == KEYDOWN and duvida == False:
                if event.key == K_RIGHT or event.key == K_d:
                    px += 6
                    angulo = 90
                if event.key == K_LEFT or event.key == K_a:
                    px -= 6
                    angulo = 270
                if event.key == K_UP or event.key == K_w:
                    py -= 6
                    angulo = 180
                if event.key == K_DOWN or event.key == K_s:
                    py += 6
                    angulo = 0

            if event.type == KEYUP and duvida == False:
                if event.key == K_RIGHT or event.key == K_d:
                    px = 0
                if event.key == K_LEFT or event.key == K_a:
                    px = 0
                if event.key == K_UP or event.key == K_w:
                    py = 0
                if event.key == K_DOWN or event.key == K_s:
                    py = 0

            if event.type == CLOCKTICK and duvida == False:
                timer = timer - 1
            
        if duvida:
            screen.blit(telaInstJogo1, (0,0)) 
        else:
            screen.blit(telaJogo1, (0,0))             
            screen.blit(caixa, (50, 110))
            screen.blit(bolaFutebol, (60, 160))
            screen.blit(chuteira, (60, 200))
            screen.blit(luvas, (60, 240))
            screen.blit(faixaCapitao, (60, 300))
            screen.blit(mochila, (665, 190))
            screen.blit(personagem, (x, y))
            screen.blit(iconeDuvida, (700, 380))
            
        #barreiras de fim do chão
        if x >= 710 - personagem.get_width():
            x = 710 - personagem.get_width()
        elif x < 100:
            x = 100
        if y >= 420 - personagem.get_width():
            y = 420 - personagem.get_width()
        elif y < 60:
            y = 60

        # barreira banco
        if x >= 200 and x <= 510 and y >= 115 and y <= 250:
            x = -x
            y = -y
            qtdVidas -= 1
            maosVazias = True
                
        #print(mouse_position)
        # pegando itens
        if x <= 100 and y >= 80 and y <=275 and maosVazias == True and angulo == 270:
            maosVazias = False
            conteudo = random.randint(0,7)
            if conteudo <= 4:
                maosCtd = "itensCertos"
            else:
                maosCtd = "itensErrados"            

        #toca mochila
        if x >= 570 and y >= 140 and y <= 210 and maosVazias == False and angulo == 90:
            conteudo = ""
            maosVazias = True
            if maosCtd == "itensCertos":
                placarJogo1 += 20
                pygame.mixer.Sound.play(somZiper)
            elif maosCtd == "itensErrados":
                placarJogo1 -= 10
        
        #toca armario
        if x >= 110 and x <= 510 and y <= 80 and maosVazias == False and angulo == 180:
            conteudo = ""
            maosVazias = True
            if maosCtd == "itensErrados":
                placarJogo1 += 5
                pygame.mixer.Sound.play(somPorta)
            elif maosCtd == "itensCertos":
                placarJogo1 -= 10            

        if qtdVidas == 3:
            screen.blit(vida, (135, 10))
        if qtdVidas >= 2:
            screen.blit(vida, (70, 10))
        if qtdVidas >= 1:
            screen.blit(vida, (10, 10))

        if timer == 0 or qtdVidas == 0:
            menuPontuacao()


        #att da posicao do personagem
        x += px
        y += py

        #down
        if maosVazias == False and angulo == 0:
            screen.blit(itens[conteudo], (x+40, y+90))
        #right
        elif maosVazias == False and angulo == 90:
            screen.blit(itens[conteudo], (x+90, y+50))
        #up
        elif maosVazias == False and angulo == 180:
            screen.blit(itens[conteudo], (x+50, y))
        #left
        elif maosVazias == False and angulo == 270:
            screen.blit(itens[conteudo], (x-5, y+40))

        tempo = fontLittle.render("Tempo: " + str(timer), True, (0,0,0))
        screen.blit(tempo, (600, 10))
        score = fontLittle.render("Pontos: " + str(placarJogo1), True, (0,0,0))
        screen.blit(score, (440, 10))

        #att da tela
        pygame.display.update()
        clock.tick(30)

def jogo2():
    global telaInstJogo2
    global telaJogo2
    global kaiCimaPes
    global placarJogo2
    global mouse_position
    duvida = True
    timer = 40
    qtdVidas = 3
    px = 0
    py = 0
    x = 0
    y = 150
    angulo = 90
    colidiu = True
    #npcs
    anguloNpc1 = 270
    anguloNpc2 = 270
    anguloNpc3 = 270
    #posições iniciais
    x_npc1 = 690 - npc1.get_width()
    y_npc1 = 430 - npc1.get_height()
    x_npc2 = 250 - npc2.get_width()
    y_npc2 = 150 - npc2.get_height()
    x_npc3 = 500 - npc3.get_width()
    y_npc3 = 220 - npc3.get_height()
    
    
        #personagem = pygame.transform.rotate(kaiCimaPes, angulo)
    while True:
        personagem = pygame.transform.rotate(kaiCimaPes, angulo)

        box1 = pygame.draw.rect(screen, (255,255,255), (x, y, 50, 65))
        box2 = pygame.draw.rect(screen, (0,0,0), (x_npc1, y_npc1, 70, 85))
        box3 = pygame.draw.rect(screen, (0,0,0), (x_npc2, y_npc2, 65, 50))
        box4 = pygame.draw.rect(screen, (0,0,0), (x_npc3, y_npc3, 60, 60))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                #tela inst
                if mouse_position[0] >= 640 and mouse_position[0] <= 670 and mouse_position[1] >= 80 and mouse_position[1] <= 110 and duvida == True:
                    duvida = False
                #tela jogo
                if mouse_position[0] >= 700 and mouse_position[0] <= 750 and mouse_position[1] >= 380 and mouse_position[1] <= 420 and duvida == False:
                    duvida = True
                else:
                    duvida = False

            if event.type == KEYDOWN and duvida == False:
                if event.key == K_RIGHT or event.key == K_d:
                    px += 6
                    angulo = 90
                if event.key == K_LEFT or event.key == K_a:
                    px -= 6
                    angulo = 270
                if event.key == K_UP or event.key == K_w:
                    py -= 6
                    angulo = 180
                if event.key == K_DOWN or event.key == K_s:
                    py += 6
                    angulo = 0

            if event.type == KEYUP and duvida == False:
                if event.key == K_RIGHT or event.key == K_d:
                    px = 0
                if event.key == K_LEFT or event.key == K_a:
                    px = 0
                if event.key == K_UP or event.key == K_w:
                    py = 0
                if event.key == K_DOWN or event.key == K_s:
                    py = 0
            if event.type == colisao:
                colidiu = True
            if event.type == CLOCKTICK and duvida == False:
                timer = timer - 1

        rotacao_npc1 = pygame.transform.rotate(npc1, anguloNpc1)
        rotacao_npc2 = pygame.transform.rotate(npc2, anguloNpc2)
        rotacao_npc3 = pygame.transform.rotate(npc3, anguloNpc3)


        #barreiras de fim do mapa
        if x >= 795 - personagem.get_width():
            x = 780 - personagem.get_width()
        elif x <= -40:
            x = -30
        if y >= 490 - personagem.get_height():
            y = 480 - personagem.get_height()
        elif y <= -40:
            y = -30
        
        if x >= 650 and y >= 130 and y <= 200:
            if timer >= 30:
                placarJogo2 += 30
            elif timer >= 20 and timer < 30:
                placarJogo2 += 20
            elif timer < 20:
                placarJogo2 += 10
            menuPontuacao()

        if colidiu:
            if box2.colliderect(box1):
                qtdVidas -= 1
                placarJogo2 -= 5
                colidiu = False
                pygame.time.set_timer(colisao, 1500)
            if box3.colliderect(box1):
                qtdVidas -= 1
                placarJogo2 -= 5
                colidiu = False
                pygame.time.set_timer(colisao, 1500)
            if box4.colliderect(box1):
                qtdVidas -= 1
                placarJogo2 -= 5
                colidiu = False
                pygame.time.set_timer(colisao, 1500)
                
        if duvida:
           screen.blit(telaInstJogo2, (0,0)) 
        else:
           screen.blit(telaJogo2, (0,0))
           screen.blit(personagem, (x, y))
           screen.blit(rotacao_npc1, (x_npc1, y_npc1))
           screen.blit(rotacao_npc2, (x_npc2, y_npc2))
           screen.blit(rotacao_npc3, (x_npc3, y_npc3))

        if qtdVidas == 3:
            screen.blit(vida, (135, 10))
        if qtdVidas >= 2:
            screen.blit(vida, (70, 10))
        if qtdVidas >= 1:
            screen.blit(vida, (10, 10))

        if timer == 0 or qtdVidas == 0:
            menuPontuacao()

        tempo = fontLittle.render("Tempo: " + str(timer), True, (0,0,0))
        screen.blit(tempo, (600, 10))
        score = fontLittle.render("Pontos: " + str(placarJogo2), True, (0,0,0))
        screen.blit(score, (440, 10))

        #att da posicao do personagem
        x += px
        y += py

        #att da tela
        pygame.display.update()
        clock.tick(30)
    

def menuPontuacao():
    global btnJogar
    global btnHome
    global mouse_position
    global telaPontuacao
    global placarJogo1
    global placarJogo2
    irJogos = False
    irMenu = False   

    while True:
        mouse_position = pygame.mouse.get_pos()
        screen.blit(telaPontuacao, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                #btn musica
                if mouse_position[0] >= 330 and mouse_position[0] <= 420 and mouse_position[1] >= 390 and mouse_position[1] <= 436 and irJogos == True:
                    menuJogos()
                if mouse_position[0] >= 330 and mouse_position[0] <= 420 and mouse_position[1] >= 390 and mouse_position[1] <= 436 and irMenu == True:
                    menu()

        pontosJogo1 = fontLittle.render("Já pro treino!:                   " + str(placarJogo1), True, (0,0,0))
        screen.blit(pontosJogo1, (180, 110))
        pontosJogo2 = fontLittle.render("Drible se puder:                " + str(placarJogo2), True, (0,0,0))
        screen.blit(pontosJogo2, (180, 170))
        placarTotal = placarJogo1 + placarJogo2
        pontosTotal = fontLittle.render("Pontos totais:                    " + str(placarTotal), True, (0,0,0))
        screen.blit(pontosTotal, (180, 230))

        if placarJogo1 == 0 or placarJogo2 == 0:
            screen.blit(btnJogar, (330, 390))
            irJogos = True
        else:
            screen.blit(btnHome, (360, 390))
            irMenu = True
        
        if placarTotal >= 50:
            resultado = fontMini.render("Parabéns Kai! Você se deu muito bem nos treinos e foi", True, (0,0,0))
            resultado1 = fontMini.render("escalado para o S.B.F.C.! Comemore e continue treinando", True, (0,0,0))
            resultado2 = fontMini.render("para sempre melhorar.", True, (0,0,0))
        elif placarTotal < 50:
            resultado = fontMini.render("Que pena, Kai, você não foi muito bem nos treinos, então", True, (0,0,0))
            resultado1 = fontMini.render("não foi escalado para o S.B.F.C.... Mas continue treinando", True, (0,0,0))
            resultado2 = fontMini.render("que esse dia logo chegará!", True, (0,0,0))
            
        screen.blit(resultado, (150, 280))
        screen.blit(resultado1, (150, 310))
        screen.blit(resultado2, (150, 340))
        
        #att da tela
        pygame.display.update()
        clock.tick(30)        

while True:
    menu()
    menuJogos()
