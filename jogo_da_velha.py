from functions import *

diagrama_velha = [
              [1,2,3],
              [4,'X',6],
              [7,8,9]
              ]

cabecalho("Jogo da Velha", 14)
resposta = False
mostrar_tabuleiro(diagrama_velha)
while resposta == False:
    jogada_user(diagrama_velha)
    sleep(1.5)
    resposta = game_over(diagrama_velha)
    if resposta == True:
        break
    else:
        jogada_maquina(diagrama_velha)
        sleep(1.5)
        resposta = game_over(diagrama_velha)
        if resposta == True:
            break
        else:
            continue
