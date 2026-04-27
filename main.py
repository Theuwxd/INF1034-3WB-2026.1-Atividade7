#from pygame import *
#lista_palavras = ["arroz", "banana", "queijo" , "alface", "frango"]
#print(random.choices(lista_palavras))
import random
def pedrapapeltesoura(pedra, papel, tesoura):
    condiçao_vitoria1 = pedra > tesoura 
    condiçao_vitoria2 = tesoura > papel
    condiçao_vitoria3 = papel > pedra
    
def escolhabot(pedra, papel, tesoura):
    lista_palavra = ["pedra", "papel", "tesoura"]
    return lista_palavra

while True:
    jogador = input("escolha entre pedra, papel ou tesoura: ")
    jogador2 = escolhabot
    print(f"Jogador 1 esocolheu {jogador}")
    print(f"jogador 2 escolheu {random.choices(jogador2)}")
    if jogador > jogador2:
        print("jogador ganhou")
    elif jogador2 > jogador:
        print("computador ganhou")
    else:
        print("empate")
    
   