import random
import json
import os
from game_rules import verificar_macroformas, verificar_microformas


# Variables
lista_figuras = []
valor_figuras = {'X': 1, 'O': 2, '+': 3, '-': 4}
tabuleiro = []
data = []

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
