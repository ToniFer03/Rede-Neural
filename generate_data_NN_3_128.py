import random
import json
import os


data = []


# Variables
lista_simbolos = []
simbolos_disponiveis = ['X', 'O', '+', '-']
valor_simbolos = {'X': 1, 'O': 2, '+': 3, '-': 4}
tabuleiro = []


# Posicoes
# ----------------------------------------------------------------------------------------------------------
# Todos posições posiveis fazendo um x num tabuleiro 5x5
posicoes_x = [
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 4), (1, 3), (3, 1), (4, 0)],
    [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    [(0, 1), (0, 3), (1, 2), (2, 1), (2, 3)],
    [(0, 2), (0, 4), (1, 3), (2, 2), (2, 4)],
    [(1, 0), (1, 2), (2, 1), (3, 0), (3, 2)],
    [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)],
    [(1, 2), (1, 4), (2, 3), (3, 2), (3, 4)],
    [(2, 0), (2, 2), (3, 1), (4, 0), (4, 2)],
    [(2, 1), (2, 3), (3, 2), (4, 1), (4, 3)],
    [(2, 2), (2, 4), (3, 3), (4, 2), (4, 4)],
]

# Todos posições posiveis fazendo uma cruz num tabuleiro 5x5
posicoes_cruz = [
    [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2), (4, 2)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 2), (1, 1), (1, 2), (1, 3), (2, 2)],
    [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
    [(1, 1), (2, 0), (2, 1), (2, 2), (3, 1)],
    [(1, 2), (2, 1), (2, 2), (2, 3), (3, 2)],
    [(1, 3), (2, 2), (2, 3), (2, 4), (3, 3)],
    [(2, 1), (3, 0), (3, 1), (3, 2), (4, 1)],
    [(2, 2), (3, 1), (3, 2), (3, 3), (4, 2)],
    [(2, 3), (3, 2), (3, 3), (3, 4), (4, 3)],
]


# Todos posições posiveis fazendo uma bola num tabuleiro 5x5
posicoes_bola = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
    [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)],
    [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 2), (2, 3), (2, 4)],
    [(1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)],
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)],
    [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)],
    [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
    [(2, 1), (2, 2), (2, 3), (3, 1), (3, 3), (4, 1), (4, 2), (4, 3)],
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 1), (0, 2), (1, 1), (1, 2)],
    [(0, 2), (0, 3), (1, 2), (1, 3)],
    [(0, 3), (0, 4), (1, 3), (1, 4)],
    [(1, 0), (1, 1), (2, 0), (2, 1)],
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(1, 2), (1, 3), (2, 2), (2, 3)],
    [(1, 3), (1, 4), (2, 3), (2, 4)],
    [(2, 0), (2, 1), (3, 0), (3, 1)],
    [(2, 1), (2, 2), (3, 1), (3, 2)],
    [(2, 2), (2, 3), (3, 2), (3, 3)],
    [(2, 3), (2, 4), (3, 3), (3, 4)],
    [(3, 0), (3, 1), (4, 0), (4, 1)],
    [(3, 1), (3, 2), (4, 1), (4, 2)],
    [(3, 2), (3, 3), (4, 2), (4, 3)],
    [(3, 3), (3, 4), (4, 3), (4, 4)],
]


# Todas as posicoes para fazer um traco num tabuleiro 5x5
posicoes_traco = [
    [(0, 0), (1, 0), (2, 0)],
    [(1, 0), (2, 0), (3, 0)],
    [(2, 0), (3, 0), (4, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 1), (2, 1), (3, 1)],
    [(2, 1), (3, 1), (4, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(1, 2), (2, 2), (3, 2)],
    [(2, 2), (3, 2), (4, 2)],
    [(0, 3), (1, 3), (2, 3)],
    [(1, 3), (2, 3), (3, 3)],
    [(2, 3), (3, 3), (4, 3)],
    [(0, 4), (1, 4), (2, 4)],
    [(1, 4), (2, 4), (3, 4)],
    [(2, 4), (3, 4), (4, 4)],
    [(0, 0), (1, 0)],
    [(1, 0), (2, 0)],
    [(2, 0), (3, 0)],
    [(3, 0), (4, 0)],
    [(0, 1), (1, 1)],
    [(1, 1), (2, 1)],
    [(2, 1), (3, 1)],
    [(3, 1), (4, 1)],
    [(0, 2), (1, 2)],
    [(1, 2), (2, 2)],
    [(2, 2), (3, 2)],
    [(3, 2), (4, 2)],
    [(0, 3), (1, 3)],
    [(1, 3), (2, 3)],
    [(2, 3), (3, 3)],
    [(3, 3), (4, 3)],
    [(0, 4), (1, 4)],
    [(1, 4), (2, 4)],
    [(2, 4), (3, 4)],
    [(3, 4), (4, 4)],
]


# Função que verifica se existe uma microfigura x no tabuleiro
def verifica_existencia_micro_x(tabuleiro_temp):
    temp_posicao = posicoes_x[1:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[0]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 5:
                return True

    return False


# Função que verifica se existe uma microfigura cruz no tabuleiro
def verifica_existencia_micro_cruz(tabuleiro_temp):
    temp_posicao = posicoes_cruz[1:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[2]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 5:
                return True

    return False


# Função que verifica se existe uma microfigura bola no tabuleiro
def verifica_existencia_micro_bola(tabuleiro_temp):
    temp_posicao = posicoes_bola[9:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[1]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 4:
                return True

    return False


# Função que verifica se existe uma microfigura traco no tabuleiro
def verifica_existencia_micro_traco(tabuleiro_temp):
    temp_posicao = posicoes_traco[15:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[3]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 2:
                return True

    return False


# Função que verifica se existe uma macrofigura x no tabuleiro
def verifica_existencia_macro_x(tabuleiro_temp):
    temp_posicao = posicoes_x[:1]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[0]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 9:
                return True

    return False


# Função que verifica se existe uma macrofigura cruz no tabuleiro
def verifica_existencia_macro_cruz(tabuleiro_temp):
    temp_posicao = posicoes_cruz[:1]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[2]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 9:
                return True

    return False


# Função que verifica se existe uma macrofigura bola no tabuleiro
def verifica_existencia_macro_bola(tabuleiro_temp):
    temp_posicao = posicoes_bola[:9]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            print(tabuleiro_temp[posicao[0]][posicao[1]])
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[1]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 8:
                return True

    return False


# Função que verifica se existe uma macrofigura traco no tabuleiro
def verifica_existencia_macro_traco(tabuleiro_temp):
    temp_posicao = posicoes_traco[:15]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[3]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 3:
                return True

    return False


def verificar_microfiguras(figura, tabuleiro_temp):
    temp_posicao = []
    temp_score = 0
    num_correspondecias = 0

    # X
    if figura == simbolos_disponiveis[0]:
        if verifica_existencia_micro_x(tabuleiro_temp):
            temp_todas_posicoes = posicoes_x[1:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[0]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 5):
                    break           

            temp_score = 32


    # Cruz
    elif figura == simbolos_disponiveis[2]:
        if verifica_existencia_micro_cruz(tabuleiro_temp):
            temp_todas_posicoes = posicoes_cruz[1:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[2]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 5):
                    break
            
            temp_score = 32


    # Bola
    elif figura == simbolos_disponiveis[1]:
        if verifica_existencia_micro_bola(tabuleiro_temp):
            temp_todas_posicoes = posicoes_bola[9:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[1]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 4):
                    break
            
            temp_score = 16  

    

    elif figura == simbolos_disponiveis[3]:
        if verifica_existencia_micro_traco(tabuleiro_temp):
            temp_todas_posicoes = posicoes_traco[15:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[3]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 2):
                    break
            
            temp_score = 2
        
    for posicao in temp_posicao:
        tabuleiro_temp[posicao[0]][posicao[1]] = " "

    return temp_score


# Função que retorna se formou uma macrofigura
def verificar_macrofiguras(figura, tabuleiro_temp):
    temp_posicao = []
    temp_score = 0
    num_correspondecias = 0

    # X
    if figura == simbolos_disponiveis[0]: 
        if verifica_existencia_macro_x(tabuleiro_temp):
            lista_posicoes = posicoes_x[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Cruz
    elif figura == simbolos_disponiveis[2]:
        if verifica_existencia_macro_cruz(tabuleiro_temp):
            lista_posicoes = posicoes_cruz[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Bola
    elif figura == simbolos_disponiveis[1]:
        if verifica_existencia_macro_bola(tabuleiro_temp):
            temp_todas_posicoes = posicoes_bola[:9]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[1]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                
                if(num_correspondecias == 8):
                    break
            
            temp_score = 256


    # Traco
    elif figura == simbolos_disponiveis[3]:
        if verifica_existencia_macro_traco(tabuleiro_temp):
            temp_todas_posicoes = posicoes_traco[:15]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == simbolos_disponiveis[3]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                
                if(num_correspondecias == 3):
                    break
            temp_score = 8

    for posicao in temp_posicao:
        tabuleiro_temp[posicao[0]][posicao[1]] = " "

    return temp_score


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------------------------------------------------------------------
def gerar_fila_simbolos():
    global lista_simbolos
    global simbolos_disponiveis

    num_iterations = random.randrange(10, 40)
    for i in range(num_iterations):
        lista_simbolos.append(simbolos_disponiveis[random.randint(0, 3)])


def count_simbolos(lista, simbolo):
    count = 0
    for i in lista:
        if i == simbolo:
            count += 1
    return count


# Função para dar update no input data (FALTA NUMERO DE CADA SIMBOLO NA FILA)
def update_input_data():
    global tabuleiro
    global lista_simbolos
    global valor_simbolos

    input_data = []

    # Update os primeiros 25 valores do input data com o tabuleiro
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] == " ":
                input_data.append(0)
            else:
                input_data.append(valor_simbolos[tabuleiro[i][j]])

    # Update os 12 valores seguintes com os simbolos da lista
    for i in range(12):
        if i < len(lista_simbolos):
            input_data.append(valor_simbolos[lista_simbolos[i]])
        else:
            input_data.append(0)
    
    input_data.append(count_simbolos(lista_simbolos, simbolos_disponiveis[0]))
    input_data.append(count_simbolos(lista_simbolos, simbolos_disponiveis[1]))
    input_data.append(count_simbolos(lista_simbolos, simbolos_disponiveis[2]))
    input_data.append(count_simbolos(lista_simbolos, simbolos_disponiveis[3]))

    input_data.append(len(lista_simbolos))

    return input_data


# Turn an index into a the coordinate of the board
def index_to_2d(index, num_columns):
    row = index // num_columns
    col = index % num_columns
    return row, col


# Define a function to simulate the game and obtain the action (reward)
def simulate_game():
    # Replace this with your actual game logic to simulate the game and obtain the action (reward)
    # Choose an action based on the output layer probabilities
    global tabuleiro
    global lista_simbolos
    global data

    score = 0
    input_data = [0]
    while len(lista_simbolos) > 0:
        # Update input data based on the current game state
        input_data = []
        target_temp = []

        input_data = update_input_data()

        while True:
            exibir_tabuleiro()
            print("-------------------------------------")
            print("Simbolo atual: " + lista_simbolos[0])
            print("-------------------------------------")
            result_string = "Simbolos: " + ', '.join(map(str, lista_simbolos[1:12]))
            print(result_string)
            print("X na fila: " + str(count_simbolos(lista_simbolos, simbolos_disponiveis[0])))
            print("O na fila: " + str(count_simbolos(lista_simbolos, simbolos_disponiveis[1])))
            print("+ na fila: " + str(count_simbolos(lista_simbolos, simbolos_disponiveis[2])))
            print("- na fila: " + str(count_simbolos(lista_simbolos, simbolos_disponiveis[3])))
            print("-------------------------------------")
            print("Onde quer colocar o simbolo? (0-24)")
            posicao = int(input())
            row, col = index_to_2d(posicao, 5)
            if tabuleiro[row][col] == " ":
                tabuleiro[row][col] = lista_simbolos[0]
                break
            else:
                print("Posicao invalida, selecione outra")


        for i in range(25):
            if i != posicao:
                target_temp.append(0)
            else:
                target_temp.append(1)


        # Verificar simbolo, update no score e retirar simbolo da lista
        score += verificar_macrofiguras(lista_simbolos[0], tabuleiro)
        score += verificar_microfiguras(lista_simbolos[0], tabuleiro)
        lista_simbolos.pop(0)
        data.append([input_data, target_temp])
        clear_terminal()

    # Numero de peças no tabuleiro
    cont = 0
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] != " ":
                cont += 1


    return (score - 2**cont)


# Função para exibir o tabuleiro
def exibir_tabuleiro():
    global tabuleiro

    print("-" * 9)
    for linha in tabuleiro:
        print("|".join(celula for celula in linha))
        print("-" * 9)


def main():
    global tabuleiro
    global lista_simbolos

    existing_data = None
    with open('database.json', 'r') as file:
        existing_data = json.load(file)

    tabuleiro = [[" " for _ in range(5)] for _ in range(5)]

    gerar_fila_simbolos()

    
    score = simulate_game()
    print("Score: " + str(score))

    # Save pairs of input-output in a JSON file
    pairs_list = []

    for input_data, target_data in data:
        pairs_list.append({"inputs": input_data, "targets": target_data})

    existing_data.extend(pairs_list)

    with open('database.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    return 0


main()

