import random
import numpy as np
import classes
import os
import datetime
from game_rules import verificar_macroformas, verificar_microformas


# Neural network classes
hidden_layer1 = None
hidden_layer2 = None
hidden_layer3 = None
linear_activation = None
softmax_activation = None

weights_layer1 = []
biases_layer1 = []
weights_layer2 = []
biases_layer2 = []
weights_layer3 = []
biases_layer3 = []

# Game variables
number_of_hidden_layers = 0
size_hidden_layers = 0

guardar_inputs = []
guardar_melhor_move = []

# Variables
lista_figuras = []
figuras_disponiveis = ['X', 'O', '+', '-']
valor_figuras = {'X': 1, 'O': 2, '+': 3, '-': 4}
tabuleiro = []



# Gerar fila random de simbolos
def gerar_fila_simbolos():
    global lista_figuras
    global figuras_disponiveis

    num_iterations = random.randrange(10, 40)
    for i in range(num_iterations):
        lista_figuras.append(figuras_disponiveis[random.randint(0, 3)])


def count_simbolos(lista, simbolo):
    count = 0
    for i in lista:
        if i == simbolo:
            count += 1
    return count


# Função para dar update no input data (FALTA NUMERO DE CADA SIMBOLO NA FILA)
def update_input_data():
    global tabuleiro
    global lista_figuras
    global valor_figuras

    input_data = []

    # Update os primeiros 25 valores do input data com o tabuleiro
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] == " ":
                input_data.append(0)
            else:
                input_data.append(valor_figuras[tabuleiro[i][j]])

    # Update os 12 valores seguintes com os simbolos da lista
    for i in range(12):
        if i < len(lista_figuras):
            input_data.append(valor_figuras[lista_figuras[i]])
        else:
            input_data.append(0)
    
    input_data.append(count_simbolos(lista_figuras, figuras_disponiveis[0]))
    input_data.append(count_simbolos(lista_figuras, figuras_disponiveis[1]))
    input_data.append(count_simbolos(lista_figuras, figuras_disponiveis[2]))
    input_data.append(count_simbolos(lista_figuras, figuras_disponiveis[3]))
    input_data.append(len(lista_figuras))

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
    global lista_figuras
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global linear_activation
    global softmax_activation
    global guardar_inputs
    global guardar_melhor_move

    score = 0
    input_data = [0]
    while len(lista_figuras) > 0:
        # Update input data based on the current game state
        input_data[0] = update_input_data()
        hidden_layer1.forward(input_data)
        linear_activation.forward(hidden_layer1.output)
        hidden_layer2.forward(linear_activation.output)
        linear_activation.forward(hidden_layer2.output)
        hidden_layer3.forward(linear_activation.output)
        softmax_activation.forward(hidden_layer3.output)

        # Get action from output layer probabilities
        flattened_output = softmax_activation.output.flatten()
        sorted_actions = sorted(range(len(flattened_output)), key=lambda k: flattened_output[k], reverse=True)

        i = 0
        for action in sorted_actions:
            row, col = index_to_2d(action, 5)
            if tabuleiro[row][col] == " ":
                tabuleiro[row][col] = lista_figuras[0]
                guardar_melhor_move.append(action)
                break
            i += 1

        exibir_tabuleiro()

        if i == 25:
            # Game over
            return (score - 2**25) 


        # Verificar simbolo, update no score e retirar simbolo da lista
        score += verificar_macroformas(lista_figuras[0], tabuleiro)
        score += verificar_microformas(lista_figuras[0], tabuleiro)
        guardar_inputs.append(input_data[0])
        
        lista_figuras.pop(0)

    # Numero de peças no tabuleiro
    cont = 0
    for i in range(5):
        for j in range(5):
            if tabuleiro[i][j] != " ":
                cont += 1


    return (score - 2**cont)


def initialize_objects():
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global linear_activation
    global softmax_activation

    hidden_layer1 = classes.layer_dense(None, None, weights_layer1, biases_layer1) 
    hidden_layer2 = classes.layer_dense(None, None, weights_layer2, biases_layer2) 
    hidden_layer3 = classes.layer_dense(None, None, weights_layer3, biases_layer3)

    linear_activation = classes.Activation_ReLU()   
    softmax_activation = classes.Activation_Softmax()


# Função para exibir o tabuleiro
def exibir_tabuleiro():
    global tabuleiro

    print("-" * 9)
    for linha in tabuleiro:
        print("|".join(celula for celula in linha))
        print("-" * 9)



def load_weights():
    global weights_layer1
    global biases_layer1
    global weights_layer2
    global biases_layer2
    global weights_layer3
    global biases_layer3

    string = "Weights_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)
    folder_path = os.path.join(os.getcwd(), string)

    if not os.path.exists(folder_path):
        print('No weights found for this configurarion!')
        exit()
    else:
        most_recent_folder = get_most_recent_folder(folder_path)
        folder_path = os.path.join(folder_path, most_recent_folder)

        weights_layer1 = np.loadtxt(os.path.join(folder_path, 'hidden_layer1_weights.txt'))
        biases_layer1 = np.loadtxt(os.path.join(folder_path, 'hidden_layer1_biases.txt'))
        biases_layer1 = biases_layer1.reshape(1, size_hidden_layers)

        weights_layer2 = np.loadtxt(os.path.join(folder_path, 'hidden_layer2_weights.txt'))
        biases_layer2 = np.loadtxt(os.path.join(folder_path, 'hidden_layer2_biases.txt'))
        biases_layer2 = biases_layer2.reshape(1, size_hidden_layers)

        weights_layer3 = np.loadtxt(os.path.join(folder_path, 'hidden_layer3_weights.txt'))
        biases_layer3 = np.loadtxt(os.path.join(folder_path, 'hidden_layer3_biases.txt'))
        biases_layer3 = biases_layer3.reshape(1, 25)



def get_most_recent_folder(folder_path):
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    if not folders:
        return None

    folders_dates = [datetime.datetime.strptime(f, "%Y-%m-%d_%H-%M-%S") for f in folders]

    most_recent_folder = max(folders_dates)

    most_recent_folder_name = most_recent_folder.strftime("%Y-%m-%d_%H-%M-%S")

    return most_recent_folder_name



def ask_for_config():
    global number_of_hidden_layers
    global size_hidden_layers

    number_of_hidden_layers = int(input('Number of hidden layers: ')).__int__()
    size_hidden_layers = int(input('Size of hidden layers: ')).__int__()



def main():
    global tabuleiro
    global lista_figuras
    global guardar_inputs
    global guardar_melhor_move


    ask_for_config()
    load_weights()
    tabuleiro = [[" " for _ in range(5)] for _ in range(5)]
    initialize_objects()
    gerar_fila_simbolos()
    score = simulate_game()

    print("Score: ", score)

    return 0

main()