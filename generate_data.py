import random
import json
import os


# Variables
lista_figuras = []
figuras_disponiveis = ['X', 'O', '+', '-']
valor_figuras = {'X': 1, 'O': 2, '+': 3, '-': 4}
tabuleiro = []
data = []



# All possible coordinates to form an X in a 5x5 board
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

# All possible coordinates to form a Cross in a 5x5 board
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


# All possible coordinates to form a circle in a 5x5 board
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


# All possible coordinates to form a dash in a 5x5 board
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


def verifica_existencia_micro_x(tabuleiro_temp):
    """
        Verifies if there is an X formed by 5 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_x[1:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[0]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 5:
                return True

    return False


def verifica_existencia_micro_cruz(tabuleiro_temp):
    """
        Verifies if there is a Cross formed by 5 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_cruz[1:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[2]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 5:
                return True

    return False


def verifica_existencia_micro_bola(tabuleiro_temp):
    """
        Verifies if there is a circle formed by 4 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_bola[9:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 4:
                return True

    return False


def verifica_existencia_micro_traco(tabuleiro_temp):
    """
        Verifies if there is a Dash formed by 2 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_traco[15:]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 2:
                return True

    return False


def verifica_existencia_macro_x(tabuleiro_temp):
    """
        Verifies if there is an X formed by 9 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_x[:1]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[0]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 9:
                return True

    return False



def verifica_existencia_macro_cruz(tabuleiro_temp):
    """
        Verifies if there is a Cross formed by 9 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_cruz[:1]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[2]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 9:
                return True

    return False


def verifica_existencia_macro_bola(tabuleiro_temp):
    """
        Verifies if there is a Circle formed by 8 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_bola[:9]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            print(tabuleiro_temp[posicao[0]][posicao[1]])
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 8:
                return True

    return False


def verifica_existencia_macro_traco(tabuleiro_temp):
    """
        Verifies if there is a Dash formed by 3 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_traco[:15]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 3:
                return True

    return False


def verificar_microformas(figura, tabuleiro_temp):
    """
        Funtion responsible for calling the funtion to verify if the smaller form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figura
            String corresponding to the last figure that was played
        tabuleiro_temp
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns the score that that play originated to be added to the total score
    """
    temp_posicao = []
    temp_score = 0
    num_correspondecias = 0

    # X
    if figura == figuras_disponiveis[0]:
        if verifica_existencia_micro_x(tabuleiro_temp):
            temp_todas_posicoes = posicoes_x[1:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[0]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 5):
                    break           

            temp_score = 32


    # Cross
    elif figura == figuras_disponiveis[2]:
        if verifica_existencia_micro_cruz(tabuleiro_temp):
            temp_todas_posicoes = posicoes_cruz[1:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[2]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 5):
                    break
            
            temp_score = 32


    # Circle
    elif figura == figuras_disponiveis[1]:
        if verifica_existencia_micro_bola(tabuleiro_temp):
            temp_todas_posicoes = posicoes_bola[9:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                    
                if(num_correspondecias == 4):
                    break
            
            temp_score = 16  

    
    # Dash
    elif figura == figuras_disponiveis[3]:
        if verifica_existencia_micro_traco(tabuleiro_temp):
            temp_todas_posicoes = posicoes_traco[15:]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
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



def verificar_macroformas(figura, tabuleiro_temp):
    """
        Funtion responsible for calling the funtion to verify if the biggest form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figura
            String corresponding to the last figure that was played
        tabuleiro_temp
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = []
    temp_score = 0
    num_correspondecias = 0

    # X
    if figura == figuras_disponiveis[0]: 
        if verifica_existencia_macro_x(tabuleiro_temp):
            lista_posicoes = posicoes_x[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Cross
    elif figura == figuras_disponiveis[2]:
        if verifica_existencia_macro_cruz(tabuleiro_temp):
            lista_posicoes = posicoes_cruz[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Circle
    elif figura == figuras_disponiveis[1]:
        if verifica_existencia_macro_bola(tabuleiro_temp):
            temp_todas_posicoes = posicoes_bola[:9]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
                        temp_posicao.append(posicao)
                        num_correspondecias += 1
                    else:
                        num_correspondecias = 0
                        temp_posicao = []
                        break
                
                if(num_correspondecias == 8):
                    break
            
            temp_score = 256


    # Dash
    elif figura == figuras_disponiveis[3]:
        if verifica_existencia_macro_traco(tabuleiro_temp):
            temp_todas_posicoes = posicoes_traco[:15]
            for lista_posicoes in temp_todas_posicoes:
                for posicao in lista_posicoes:
                    if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
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


def gerar_fila_figuras():
    """
        Function responsible for generating a list of random predetermined symbols
    """
    global lista_figuras
    global figuras_disponiveis

    num_iterations = random.randrange(10, 40)
    for i in range(num_iterations):
        lista_figuras.append(figuras_disponiveis[random.randint(0, 3)])


def count_figuras(lista, simbolo):
    """
        Funtion responsible for counting how many of a certain symbols are still
        left on list

        Parameters
        ----------
        lista
            List that contains all the symbols left to be played
        simbolo
            The symbol of which we want to know how many are left

        Returns
        -------
        count
            Number of occurances of that symbol on the list

    """
    count = 0
    for i in lista:
        if i == simbolo:
            count += 1
    return count


def update_input_data():
    """
        Function responsible for storing the current state of the game after 
        each play, first 25 values are reserved for the board state and the next 
        12 to the next symbols in line, the last one is reserved to the numbers
        of symbols left

        Returns
        -------
        input_data
            Object containing the current state of the game to be stored
    """
    global tabuleiro
    global lista_figuras
    global valor_figuras

    input_data = []

    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] == " ":
                input_data.append(0)
            else:
                input_data.append(valor_figuras[tabuleiro[i][j]])

    for i in range(12):
        if i < len(lista_figuras):
            input_data.append(valor_figuras[lista_figuras[i]])
        else:
            input_data.append(0)
    
    input_data.append(count_figuras(lista_figuras, figuras_disponiveis[0]))
    input_data.append(count_figuras(lista_figuras, figuras_disponiveis[1]))
    input_data.append(count_figuras(lista_figuras, figuras_disponiveis[2]))
    input_data.append(count_figuras(lista_figuras, figuras_disponiveis[3]))

    input_data.append(len(lista_figuras))

    return input_data


def index_to_2d(index, num_columns):
    """
        Function responsible for turning and index into a coordinate in the board
    """
    row = index // num_columns
    col = index % num_columns
    return row, col


def simulate_game():
    """
        Function responsible for simulating the game and obtaining the final score

        Returns
        -------
        score
            Returns the final score of the game, already deducting the penalties for 
            the pieces left on the board

    """
    global tabuleiro
    global lista_figuras
    global data

    score = 0
    input_data = [0]
    while len(lista_figuras) > 0:
        input_data = []
        target_temp = []

        input_data = update_input_data()

        while True:
            exibir_tabuleiro()
            print("-------------------------------------")
            print("Simbolo atual: " + lista_figuras[0])
            print("-------------------------------------")
            result_string = "Simbolos: " + ', '.join(map(str, lista_figuras[1:12]))
            print(result_string)
            print("X na fila: " + str(count_figuras(lista_figuras, figuras_disponiveis[0])))
            print("O na fila: " + str(count_figuras(lista_figuras, figuras_disponiveis[1])))
            print("+ na fila: " + str(count_figuras(lista_figuras, figuras_disponiveis[2])))
            print("- na fila: " + str(count_figuras(lista_figuras, figuras_disponiveis[3])))
            print("-------------------------------------")
            print("Onde quer colocar o simbolo? (0-24)")
            posicao = int(input())
            row, col = index_to_2d(posicao, 5)
            if tabuleiro[row][col] == " ":
                tabuleiro[row][col] = lista_figuras[0]
                break
            else:
                print("Posicao invalida, selecione outra")


        for i in range(25):
            if i != posicao:
                target_temp.append(0)
            else:
                target_temp.append(1)


        score += verificar_macroformas(lista_figuras[0], tabuleiro)
        score += verificar_microformas(lista_figuras[0], tabuleiro)
        lista_figuras.pop(0)
        data.append([input_data, target_temp])
        clear_terminal()

    cont = 0
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] != " ":
                cont += 1


    return (score - 2**cont)


def exibir_tabuleiro():
    """
        Prints the board on the console line
    """
    global tabuleiro

    print("-" * 9)
    for linha in tabuleiro:
        print("|".join(celula for celula in linha))
        print("-" * 9)


def main():
    global tabuleiro
    global lista_figuras

    existing_data = None
    with open('Database/database.json', 'r') as file:
        existing_data = json.load(file)

    tabuleiro = [[" " for _ in range(5)] for _ in range(5)]

    gerar_fila_figuras()

    
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
