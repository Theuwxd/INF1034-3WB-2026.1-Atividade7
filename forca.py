import pygame
import random
import sys

pygame.init()


LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


fonte = pygame.font.SysFont(None, 50)
fonte_peq = pygame.font.SysFont(None, 30)


palavras = ["banana", "manga", "abacaxi", "morango", "laranja"]

def novo_jogo():
    palavra = random.choice(palavras)
    return {
        "palavra": palavra,
        "letras_descobertas": ["_"] * len(palavra),
        "usadas": [],
        "vidas": 6,
        "fim": False,
        "msg": ""
    }

estado = novo_jogo()

def desenhar():
    tela.fill(BRANCO)

    
    texto = fonte.render(" ".join(estado["letras_descobertas"]), True, PRETO)
    tela.blit(texto, (200, 200))

   
    vidas = fonte_peq.render(f"Vidas: {estado['vidas']}", True, PRETO)
    tela.blit(vidas, (10, 10))

    usadas = fonte_peq.render(f"Usadas: {', '.join(estado['usadas'])}", True, PRETO)
    tela.blit(usadas, (10, 50))

    msg = fonte_peq.render(estado["msg"], True, PRETO)
    tela.blit(msg, (200, 300))

    pygame.display.update()

def verificar_letra(letra):
    if letra in estado["usadas"]:
        estado["msg"] = "Letra já usada!"
        return

    estado["usadas"].append(letra)

    if letra in estado["palavra"]:
        for i in range(len(estado["palavra"])):
            if estado["palavra"][i] == letra:
                estado["letras_descobertas"][i] = letra
        estado["msg"] = "Acertou!"
    else:
        estado["vidas"] -= 1
        estado["msg"] = "Errou!"

def verificar_fim():
    if "_" not in estado["letras_descobertas"]:
        estado["msg"] = "Você venceu! Pressione R"
        estado["fim"] = True

    elif estado["vidas"] <= 0:
        estado["msg"] = f"Perdeu! Palavra: {estado['palavra']} (R para reiniciar)"
        estado["fim"] = True


while True:
    desenhar()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            
            if estado["fim"]:
                if evento.key == pygame.K_r:
                    estado = novo_jogo()

            else:
                tecla = evento.unicode.lower()

                
                if tecla.isalpha() and len(tecla) == 1:
                    verificar_letra(tecla)
                    verificar_fim()

                
                elif tecla == "\r":  
                    chute = input("Digite a palavra no terminal: ")

                    if chute.isalpha():
                        if chute == estado["palavra"]:
                            estado["letras_descobertas"] = list(estado["palavra"])
                        else:
                            estado["vidas"] -= 1

                        verificar_fim()