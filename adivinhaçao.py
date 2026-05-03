import pygame
import random
import sys

pygame.init()


LARGURA, ALTURA = 700, 450
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Adivinhe o Número")


BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERDE = (0, 200, 0)


fonte = pygame.font.SysFont(None, 40)


def novo_jogo():
    return {
        "num": random.randint(1, 1023),
        "tentativas": 0,
        "valor": 512,
        "msg": ""
    }

estado = novo_jogo()


btn_mais1 = pygame.Rect(50, 250, 80, 50)
btn_mais10 = pygame.Rect(150, 250, 80, 50)
btn_mais100 = pygame.Rect(250, 250, 80, 50)

btn_menos1 = pygame.Rect(50, 320, 80, 50)
btn_menos10 = pygame.Rect(150, 320, 80, 50)
btn_menos100 = pygame.Rect(250, 320, 80, 50)

btn_ok = pygame.Rect(450, 280, 120, 60)

def desenhar():
    tela.fill(BRANCO)

    titulo = fonte.render("Adivinhe o Número (1 a 1023)", True, PRETO)
    tela.blit(titulo, (120, 20))

    numero = fonte.render(f"Seu número: {estado['valor']}", True, PRETO)
    tela.blit(numero, (200, 100))

    msg = fonte.render(estado["msg"], True, PRETO)
    tela.blit(msg, (180, 150))

   
    pygame.draw.rect(tela, CINZA, btn_mais1)
    pygame.draw.rect(tela, CINZA, btn_mais10)
    pygame.draw.rect(tela, CINZA, btn_mais100)

    tela.blit(fonte.render("+1", True, PRETO), (65, 260))
    tela.blit(fonte.render("+10", True, PRETO), (155, 260))
    tela.blit(fonte.render("+100", True, PRETO), (250, 260))

    
    pygame.draw.rect(tela, CINZA, btn_menos1)
    pygame.draw.rect(tela, CINZA, btn_menos10)
    pygame.draw.rect(tela, CINZA, btn_menos100)

    tela.blit(fonte.render("-1", True, PRETO), (65, 330))
    tela.blit(fonte.render("-10", True, PRETO), (155, 330))
    tela.blit(fonte.render("-100", True, PRETO), (245, 330))

    
    pygame.draw.rect(tela, VERDE, btn_ok)
    tela.blit(fonte.render("OK", True, PRETO), (485, 300))

    dica = pygame.font.SysFont(None, 25).render("Pressione R para reiniciar", True, PRETO)
    tela.blit(dica, (220, 400))

    pygame.display.update()


while True:
    desenhar()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

           
            if btn_mais1.collidepoint(x, y):
                estado["valor"] += 1
            elif btn_mais10.collidepoint(x, y):
                estado["valor"] += 10
            elif btn_mais100.collidepoint(x, y):
                estado["valor"] += 100

           
            elif btn_menos1.collidepoint(x, y):
                estado["valor"] -= 1
            elif btn_menos10.collidepoint(x, y):
                estado["valor"] -= 10
            elif btn_menos100.collidepoint(x, y):
                estado["valor"] -= 100

           
            elif btn_ok.collidepoint(x, y):
                estado["tentativas"] += 1

                if estado["valor"] > estado["num"]:
                    estado["msg"] = "-1 (Muito alto)"
                elif estado["valor"] < estado["num"]:
                    estado["msg"] = "1 (Muito baixo)"
                else:
                    estado["msg"] = f"Acertou em {estado['tentativas']}!"

        
            estado["valor"] = max(1, min(1023, estado["valor"]))

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                estado = novo_jogo()