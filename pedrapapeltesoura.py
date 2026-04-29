import pygame
import random
import sys

pygame.init()

# tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# fonte
fonte = pygame.font.SysFont(None, 40)

# carregar imagens
pedra_img = pygame.image.load("pedra.png")
papel_img = pygame.image.load("papel.png")
tesoura_img = pygame.image.load("tesoura.png")

# redimensionar
pedra_img = pygame.transform.scale(pedra_img, (150, 150))
papel_img = pygame.transform.scale(papel_img, (150, 150))
tesoura_img = pygame.transform.scale(tesoura_img, (150, 150))

# posições
pedra_rect = pedra_img.get_rect(topleft=(100, 400))
papel_rect = papel_img.get_rect(topleft=(325, 400))
tesoura_rect = tesoura_img.get_rect(topleft=(550, 400))

opcoes = ["pedra", "papel", "tesoura"]

pontuacao = 0
resultado = ""
jogada_pc = ""

def desenhar():
    tela.fill(branco)

    # desenhar imagens
    tela.blit(pedra_img, pedra_rect)
    tela.blit(papel_img, papel_rect)
    tela.blit(tesoura_img, tesoura_rect)

    # textos
    texto = fonte.render("Escolha sua jogada:", True, preto)
    tela.blit(texto, (280, 50))

    res = fonte.render(resultado, True, preto)
    tela.blit(res, (300, 150))

    score = fonte.render(f"Pontuação: {pontuacao}", True, preto)
    tela.blit(score, (10, 10))

    if jogada_pc:
        pc_txt = fonte.render(f"PC: {jogada_pc}", True, preto)
        tela.blit(pc_txt, (320, 200))

    pygame.display.update()

def verificar_vencedor(jogador, pc):
    global pontuacao

    if jogador == pc:
        return "Empate!"
    elif (jogador == "pedra" and pc == "tesoura") or \
         (jogador == "tesoura" and pc == "papel") or \
         (jogador == "papel" and pc == "pedra"):
        pontuacao += 1
        return "Você venceu!"
    else:
        pontuacao -= 1
        return "Você perdeu!"

# loop principal
while True:
    desenhar()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if pedra_rect.collidepoint(mouse_pos):
                jogador = "pedra"
            elif papel_rect.collidepoint(mouse_pos):
                jogador = "papel"
            elif tesoura_rect.collidepoint(mouse_pos):
                jogador = "tesoura"
            else:
                jogador = None

            if jogador:
                jogada_pc = random.choice(opcoes)
                resultado = verificar_vencedor(jogador, jogada_pc)