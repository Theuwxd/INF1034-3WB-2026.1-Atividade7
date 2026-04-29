import random 

while True:
    num = random.randint(1, 1023)
    tentativas = 0
    tentativascomp = 0
    escolha = input('Quem começara jogando(usuario/computador):')
    
    def jogar_usuario(num):
        tentativas = 0
        while True:
            usuario = int(input('Digite o número de 1 a 1023: '))
            tentativas += 1

            if usuario > num:
                print('-1')
            elif usuario < num:
                print("1")
            else:
                print('Parabéns, você acertou!!')
                print(f'Tentativas: {tentativas}')
                break
        return tentativas
            
    def jogar_computador(num):
        tentativascomp = 0
        print("Computador tentando...")
    
        while True:
            computador = random.randint(1, 1023)
            tentativascomp += 1
            print(f"Computador chutou: {computador}")

            if computador > num:
                print('-1')
            elif computador < num:
                print("1")
            else:
                print('Computador acertou!!')
                print(f'Tentativas: {tentativascomp}')
                break
        return tentativascomp

    if escolha == "usuario":
        tentativas = jogar_usuario(num)
        tentativascomp = jogar_computador(num)
    elif escolha == "computador":
        tentativascomp = jogar_computador(num)
        tentativas = jogar_usuario(num)
    else:
        print('Digite apenas "usuario" ou "computador"')
        continue 

    if tentativas < tentativascomp:
        print(f'Usuário ganhou! ({tentativas} vs {tentativascomp})')
    elif tentativas > tentativascomp:
        print(f'Computador ganhou! ({tentativascomp} vs {tentativas})')
    else:
        print(f'Empate! ({tentativas})')
 
    
    continuar = input('Quer jogar novamente? (s/n): ')
    if continuar != 's':
        print('Jogo encerrado')
        break
    

