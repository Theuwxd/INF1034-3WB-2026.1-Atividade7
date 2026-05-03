import pygame
import sys

pygame.init()


LARGURA, ALTURA = 300, 500
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Calculadora")


BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
PRETO = (0, 0, 0)
LARANJA = (255, 165, 0)


fonte = pygame.font.SysFont(None, 40)


valor_atual = ""
resultado = None
operador = None


botoes = [
    ("7", (0, 200)), ("8", (75, 200)), ("9", (150, 200)), ("/", (225, 200)),
    ("4", (0, 275)), ("5", (75, 275)), ("6", (150, 275)), ("*", (225, 275)),
    ("1", (0, 350)), ("2", (75, 350)), ("3", (150, 350)), ("-", (225, 350)),
    ("0", (0, 425)), ("C", (75, 425)), ("=", (150, 425)), ("+", (225, 425)),
]

def desenhar():
    tela.fill(BRANCO)

    
    pygame.draw.rect(tela, CINZA, (0, 0, 300, 150))
    texto = fonte.render(str(valor_atual if valor_atual else resultado if resultado else 0), True, PRETO)
    tela.blit(texto, (10, 50))

    
    for texto_btn, pos in botoes:
        rect = pygame.Rect(pos[0], pos[1], 75, 75)
        pygame.draw.rect(tela, LARANJA if texto_btn in "+-*/=" else CINZA, rect)
        txt = fonte.render(texto_btn, True, PRETO)
        tela.blit(txt, (pos[0] + 25, pos[1] + 20))

    pygame.display.update()

def calcular():
    global resultado, valor_atual, operador

    if resultado is None:
        resultado = float(valor_atual)
    else:
        num2 = float(valor_atual)

        if operador == "+":
            resultado += num2
        elif operador == "-":
            resultado -= num2
        elif operador == "*":
            resultado *= num2
        elif operador == "/":
            if num2 != 0:
                resultado /= num2
            else:
                resultado = 0

    valor_atual = ""


while True:
    desenhar()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            for texto_btn, pos in botoes:
                rect = pygame.Rect(pos[0], pos[1], 75, 75)

                if rect.collidepoint(x, y):

                    if texto_btn.isdigit():
                        valor_atual += texto_btn

                    elif texto_btn == "C":
                        valor_atual = ""
                        resultado = None
                        operador = None

                    elif texto_btn in "+-*/":
                        if valor_atual:
                            calcular()
                        operador = texto_btn

                    elif texto_btn == "=":
                        if valor_atual and operador:
                            calcular()