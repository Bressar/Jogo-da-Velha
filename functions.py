from random import randint
from time import sleep

def linha(numero):
    # Escreve uma linha tracejada
    return '-' * numero


def cabecalho(titulo='txt', valor=20):
    # Exibe um cabeçalho centralizado entre 2 linhas tracejadas
    print(f"{linha(valor)}\n{titulo.center(valor)}\n{linha(valor)}")


def mostrar_tabuleiro(tabela):
    # A função exibe a  tabela formatada
    # exibe no console.
    for row in tabela:
        linha(9)
        print(' | '.join(map(str, row)))  # transforma em string para visualizar formatado
        print(linha(9))


def leiaInt(msg):
    # Função para ler somente números inteiros entre 1 e 9
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except Exception as e:
            print(f'\033[31mErro inesperado: {e}\033[m')
            continue
        else:
            if numero < 1 or numero > 9:
                print("\033[31mNúmero inválido! Digite um número entre 1 e 9.\033[m")
                continue
            return numero


def jogada_user(tabuleiro):
    # Função para ler somente números inteiros entre 1 e 9
    # Gravar os lances do user na tabela e exibir a tabela com o resultado da jogada
    print(linha(36))
    while True:
        try:
            numero = int(input("digite o número da casa desejada: "))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except Exception as e:
            print(f'\033[31mErro inesperado: {e}\033[m')
            continue
        else:
            if numero < 1 or numero > 9:
                print("\033[31mNúmero inválido! Digite um número entre 1 e 9.\033[m")
                continue
        # Essa parte do código não está feita com um loop for para ficar mais didática....
        if numero == 1:
            if tabuleiro[0][0] != 0 and tabuleiro[0][0] != 'X':
                tabuleiro[0][0] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 2:
            if tabuleiro[0][1] != 0 and tabuleiro[0][1] != 'X':
                tabuleiro[0][1] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 3:
            if tabuleiro[0][2] != 0 and tabuleiro[0][2] != 'X':
                tabuleiro[0][2] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 4:
            if tabuleiro[1][0] != 0 and tabuleiro[1][0] != 'X':
                tabuleiro[1][0] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 6:
            if tabuleiro[1][2] != 0 and tabuleiro[0][2] != 'X':
                tabuleiro[1][2] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 7:
            if tabuleiro[2][0] != 0 and tabuleiro[2][0] != 'X':
                tabuleiro[2][0] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 8:
            if tabuleiro[2][1] != 0 and tabuleiro[2][1] != 'X':
                tabuleiro[2][1] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif numero == 9:
            if tabuleiro[2][2] != 0 and tabuleiro[2][2] != 'X':
                tabuleiro[2][2] = 0
                break
            else:
                print('\033[31mCasa ocupada! Digite novamente!\033[m')
                continue
        elif all(cell != 0 and cell != 'X' for row in tabuleiro for cell in row):
            return
    print(linha(36))
    print('Seu lance!')
    print(linha(36))
    return mostrar_tabuleiro(tabuleiro)


def jogada_maquina(tabuleiro):
    # Cria uma lista com todas as posições disponíveis no tabuleiro
    # Registra as jogadas aleatórias da máquina e exibe a jogada do computador
    posicoes_disponiveis = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != 0 and tabuleiro[i][j] != 'X':
                posicoes_disponiveis.append((i, j))
    if not posicoes_disponiveis:  # Se não houver posições disponíveis, sai do loop
        print("Não há mais posições disponíveis. O jogo terminou.")
        return
    # Escolhe aleatoriamente uma posição disponível
    i, j = posicoes_disponiveis[randint(0, len(posicoes_disponiveis) - 1)]
    tabuleiro[i][j] = 'X'  # Marca a posição escolhida no tabuleiro
    print(linha(36))
    print("Lance da máquina...")
    print(linha(36))
    mostrar_tabuleiro(tabuleiro)


def sair_ou_nao():
    # Função para sair de uma aplicação, está sem controle de execessões...
    print(linha(36))
    resposta = str(input('Quer continuar [S] ou [N]? ')).strip().upper()
    if resposta == 'S':
        return False
    else:
        print(linha(36))
        print('Encerrando o programa...')
        return True


def game_over(Tabela):
    # Verifica se o jogo terminou, quem foi o vencedor ou se houve empate
    # Verifica se uma das linhas contém uma vitória
    for row in Tabela:
        if row.count('X') == 3:  # Vitória do computador
            print(linha(36))
            print('Game Over! O Computador Venceu! ')
            return True
        elif row.count(0) == 3:  # Vitória do jogador
            print(linha(36))
            print('Game Over! Você Venceu!')
            return True
    # Verifica se uma das colunas contém uma vitória
    for coluna in range(3):
        if Tabela[0][coluna] == Tabela[1][coluna] == Tabela[2][coluna] == 'X':  # Vitória do computador
            print(linha(36))
            print('Game Over! O Computador Venceu! ')
            return True
        elif Tabela[0][coluna] == Tabela[1][coluna] == Tabela[2][coluna] == 0:  # Vitória do jogador
            print(linha(36))
            print('Game Over! Você Venceu!')
            return True
    # Verifica as diagonais
    if Tabela[0][0] == Tabela[1][1] == Tabela[2][2] == 'X' or Tabela[0][2] == Tabela[1][1] == Tabela[2][0] == 'X':
        print(linha(36))
        print('Game Over! O Computador Venceu! ')
        return True
    elif Tabela[0][0] == Tabela[1][1] == Tabela[2][2] == 0 or Tabela[0][2] == Tabela[1][1] == Tabela[2][0] == 0:
        print(linha(36))
        print('Game Over! Você Venceu!')
        return True
    # verifica se o tabuleiro está cheio
    if all(cell == 0 or cell == 'X' for row in Tabela for cell in row):
        print('Game Over! Empate!')
        return
    # Se nenhum dos casos acima for atendido, o jogo continua
    return False

