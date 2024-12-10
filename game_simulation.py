import random
import numpy as np
import classes
import os
import datetime
import json
from game_rules import verify_big_forms, verify_small_forms


#Config Variables
number_of_inputs = None
number_of_outputs = None
size_hidden_layers = None
number_of_hidden_layers = None
learning_rate = None
number_of_epochs = None
rate_of_decrease = None

# Game Simulation Results
store_inputs = []
store_best_move = []

# Variables
figures_list = []
available_figures = ['X', 'O', '+', '-']
figures_translation_value = {'X': 1, 'O': 2, '+': 3, '-': 4}
board = []

# Neural Network variables
weights_array = []
biases_array = []
layers_array = []
linear_activation = None
softmax_activation = None

# Colours
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'


def load_configurarions():
    """
        Funtion responsible for loading the configurations to be used on this program from a specific file
    """
    global number_of_inputs
    global number_of_outputs
    global number_of_hidden_layers
    global size_hidden_layers
    global learning_rate
    global number_of_epochs
    global rate_of_decrease

    try:
        with open('Config\\initial_config.json', 'r') as file:
            configurations = json.load(file)
    except Exception as e:
        exit()

    
    number_of_inputs = configurations['number_of_inputs']
    number_of_outputs = configurations['number_of_outputs']
    size_hidden_layers = configurations['size_hidden_layers']
    number_of_hidden_layers = configurations['number_of_hidden_layers']
    learning_rate = configurations['learning_rate']
    rate_of_decrease = configurations['rate_of_decrease']
    number_of_epochs = configurations['number_of_epochs']



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
    global layers_array
    global linear_activation
    global softmax_activation
    global store_inputs
    global store_best_move

    score = 0
    input_data = [0]
    while len(figures_list) > 0:
        input_data[0] = update_input_data()
        
        layers_array[0].forward(input_data)
        linear_activation.forward(layers_array[0].output)
        for i in range(1, number_of_hidden_layers):
            layers_array[i].forward(linear_activation.output)
            linear_activation.forward(layers_array[i].output)
        layers_array[number_of_hidden_layers].forward(linear_activation.output)
        softmax_activation.forward(layers_array[number_of_hidden_layers].output)

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
    global weights_array
    global biases_array
    global layers_array
    global linear_activation
    global softmax_activation

    for i in range(0, number_of_hidden_layers+1):
        tempLayer = classes.Layer_Dense(None, None, weights_array[i], biases_array[i])
        layers_array.append(tempLayer)

    linear_activation = classes.Activation_ReLU()   
    softmax_activation = classes.Activation_Softmax()



def show_board():
    """
        Prints the board on the console line
    """
    global board

    print("-" * 24)
    count = 1
    colour = None
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
                if cedule == available_figures[0]:
                    colour = RED
                elif cedule == available_figures[1]:
                    colour = GREEN 
                elif cedule == available_figures[2]:
                    colour = BLUE   
                else:
                    colour = YELLOW
                    
                row_text = row_text + colour + cedule + WHITE + "  "
            count += 1
        
        print(row_text)
        print("-" * 24)



def load_weights():
    """
        Funtion responsible for loading the weights and biasies to be used while 
        simulating the game
    """
    global weights_array
    global biases_array
    global number_of_outputs

    string = "Layers_Information\\Layers_Size_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)
    folder_path = os.path.join(os.getcwd(), string)

    if not os.path.exists(folder_path):
        print('No weights found for this configurarion!')
        exit()
    else:
        most_recent_folder = get_most_recent_folder(folder_path)
        folder_path = os.path.join(folder_path, most_recent_folder)

        for i in range(number_of_hidden_layers+1):
            weightFile = 'hidden_layer' + str(i+1) + '_weights.txt'
            tempWeight = np.loadtxt(os.path.join(folder_path, weightFile))
            weights_array.append(tempWeight)
            biasesFile = 'hidden_layer' + str(i+1) + '_biases.txt'
            tempBiases = np.loadtxt(os.path.join(folder_path, biasesFile))
            if i < number_of_hidden_layers:
                tempBiases = tempBiases.reshape(1, size_hidden_layers)
            else:
                tempBiases = tempBiases.reshape(1, number_of_outputs)
            biases_array.append(tempBiases)



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


#TODO: Dont load by most recent folder ask the user what folder he wants to use, leave the most recent function it can be usefull
#TODO: Ask the user if he wants a random generated queue or a specific one to be created by him
#TODO: Change the colour of the figures in relation to the board to make them more visible

def game_simulation():
    global board
    global figures_list
    global store_inputs
    global store_best_move

    load_configurarions()
    load_weights()
    board = [[" " for _ in range(5)] for _ in range(5)]
    initialize_objects()
    generate_figures_queue()
    score = simulate_game()

    print("Score: ", score)