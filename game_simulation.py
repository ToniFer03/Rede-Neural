import random
import numpy as np
import classes
import os
import datetime
from game_rules import verify_big_forms, verify_small_forms


# Neural network classes
linear_activation = None
softmax_activation = None

hidden_layers_array = []
weights_array = []
biasies_array = []

# Game variables
number_of_hidden_layers = 0
size_hidden_layers = 0

store_inputs = []
store_best_move = []

# Variables
figures_list = []
available_figures = ['X', 'O', '+', '-']
figures_translation_value = {'X': 1, 'O': 2, '+': 3, '-': 4}
board = []



def generate_figures_queue():
    """
        Funtion responsible for generating a queue of random figures to be played

    """
    global figures_list
    global available_figures

    num_iterations = random.randrange(10, 40)
    for i in range(num_iterations):
        figures_list.append(available_figures[random.randint(0, 3)])


def count_simbolos(figures_list_copy, figure):
    """
        Funtion responsible for many figures of a certain type are still left

        Parameters
        ----------
        figures_list_copy
            List that contains all the figures left to be played
        figure
            The symbol of which we want to know how many are left

        Returns
        -------
        count
            Number of occurances of that figure on the list

    """
    count = 0
    for i in figures_list_copy:
        if i == figure:
            count += 1
    return count


def update_input_data():
    """
        Funtion responsible for updating the input data
    """
    global board
    global figures_list
    global figures_translation_value

    input_data = []

    for i in range(5):
        for j in range(5):
            if board[i][j] == " ":
                input_data.append(0)
            else:
                input_data.append(figures_translation_value[board[i][j]])

    for i in range(12):
        if i < len(figures_list):
            input_data.append(figures_translation_value[figures_list[i]])
        else:
            input_data.append(0)
    
    input_data.append(count_simbolos(figures_list, available_figures[0]))
    input_data.append(count_simbolos(figures_list, available_figures[1]))
    input_data.append(count_simbolos(figures_list, available_figures[2]))
    input_data.append(count_simbolos(figures_list, available_figures[3]))
    input_data.append(len(figures_list))

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
    global board
    global figures_list
    global linear_activation
    global softmax_activation
    global store_inputs
    global store_best_move
    global hidden_layers_array
    global number_of_hidden_layers

    score = 0
    input_data = [0]
    while len(figures_list) > 0:
        input_data[0] = update_input_data()

        
        hidden_layers_array[0].forward(input_data)
        linear_activation.forward(hidden_layers_array[0].output)
        for num in range(1, number_of_hidden_layers+1):
            hidden_layers_array[num].forward(linear_activation.output)

            if num == number_of_hidden_layers:
                softmax_activation.forward(hidden_layers_array[num].output)
            else:
                linear_activation.forward(hidden_layers_array[num].output)

        flattened_output = softmax_activation.output.flatten()
        sorted_actions = sorted(range(len(flattened_output)), key=lambda k: flattened_output[k], reverse=True)

        i = 0
        for action in sorted_actions:
            row, col = index_to_2d(action, 5)
            if board[row][col] == " ":
                board[row][col] = figures_list[0]
                store_best_move.append(action)
                break
            i += 1

        show_board()

        if i == 25:
            return (score - 2**25) 


        score += verify_big_forms(figures_list[0], board)
        score += verify_small_forms(figures_list[0], board)
        store_inputs.append(input_data[0])
        
        figures_list.pop(0)

    cont = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != " ":
                cont += 1


    return (score - 2**cont)


def initialize_objects():
    """
        Funtion responsible for initializing the objects from the neural network
    """
    global linear_activation
    global softmax_activation

    global hidden_layers_array
    global weights_array
    global biasies_array
    global number_of_hidden_layers

    for num in range(number_of_hidden_layers+1):
        hidden_layers_array.append([])
        hidden_layers_array[num] = classes.Layer_Dense(None, None, weights_array[num], biasies_array[num])

    linear_activation = classes.Activation_ReLU()   
    softmax_activation = classes.Activation_Softmax()


def show_board():
    """
        Prints the board on the console line
    """
    global board

    print("-" * 24)
    count = 1
    for row in board:
        row_text = ""
        for cedule in row:
            row_text = row_text + "| "

            if(cedule == ' '):
                if(count < 10):
                    row_text = row_text + "0" + str(count) + " "
                else:
                    row_text = row_text + str(count) + " "
            else:
                row_text = row_text + cedule + "  "
            count += 1
        
        print(row_text)
        print("-" * 24)



def load_weights():
    """
        Funtion responsible for loading the weights and biasies to be used while 
        simulating the game
    """
    global weights_array
    global biasies_array
    global number_of_hidden_layers


    string = "Weights_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)
    current_directory = os.getcwd() + "\Weights"
    folder_path = os.path.join(current_directory, string)

    if not os.path.exists(folder_path):
        print('No weights found for this configurarion!')
        exit()
    else:
        most_recent_folder = get_most_recent_folder(folder_path)
        folder_path = os.path.join(folder_path, most_recent_folder)

        for layer_number in range(number_of_hidden_layers + 1):
            fileNameWeights = 'hidden_layer' + str(layer_number+1) + '_weights.txt'
            fileNameBiases = 'hidden_layer' + str(layer_number+1) + '_biases.txt'
            weights_array.append(None)
            biasies_array.append([])
            weights_array[layer_number] = np.loadtxt(os.path.join(folder_path, fileNameWeights))
            biasies_array[layer_number] = np.loadtxt(os.path.join(folder_path, fileNameBiases))

            if layer_number == number_of_hidden_layers:
                biasies_array[layer_number] = biasies_array[layer_number].reshape(1, 25)
            else:
                biasies_array[layer_number] = biasies_array[layer_number].reshape(1, size_hidden_layers)



def get_most_recent_folder(folder_path):
    """
        Function responsible for getting the most recent folder
    """
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    if not folders:
        return None

    folders_dates = [datetime.datetime.strptime(f, "%Y-%m-%d_%H-%M-%S") for f in folders]

    most_recent_folder = max(folders_dates)

    most_recent_folder_name = most_recent_folder.strftime("%Y-%m-%d_%H-%M-%S")

    return most_recent_folder_name



def ask_for_config():
    """
        Function responsible for asking the users for the neural network configuration
    """
    global number_of_hidden_layers
    global size_hidden_layers

    number_of_hidden_layers = int(input('Number of hidden layers: ')).__int__()
    size_hidden_layers = int(input('Size of hidden layers: ')).__int__()
    

def game_simulation_main():
    global board
    global figures_list
    global store_inputs
    global store_best_move


    ask_for_config()
    load_weights()
    board = [[" " for _ in range(5)] for _ in range(5)]
    initialize_objects()
    generate_figures_queue()
    score = simulate_game()

    print("Score: ", score)

    return 0