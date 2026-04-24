import pygame
import os

pygame.mixer.init()

def carregar_sfx(nome_arquivo):
    caminho = os.path.join("assets", nome_arquivo)
    if os.path.exists(caminho):
        return pygame.mixer.Sound(caminho)
    return None

SOM_ACERTO = carregar_sfx("level_up.wav")
SOM_ERRO = carregar_sfx("acesso_negado.wav")
SOM_PORTA = carregar_sfx("porta_abrindo.wav")

def tocar_sfx(tipo):
    if tipo == "acerto" and SOM_ACERTO:
        SOM_ACERTO.play()
    elif tipo == "erro" and SOM_ERRO:
        SOM_ERRO.play()
    elif tipo == "porta" and SOM_PORTA:
        SOM_PORTA.play()

def iniciar_musica():
    try:
        caminho = os.path.join("assets", "music.mp3")
        if os.path.exists(caminho):
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.6)
    except:
        pass