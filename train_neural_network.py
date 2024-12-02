import datetime
import numpy as np
import json
import os
import classes
import logging

training_inputs = []
training_targets = []

# Variables
number_of_inputs = None
number_of_outputs = None
size_hidden_layers = None
number_of_hidden_layers = None
learning_rate = None
number_of_epochs = None
loss = None
rate_of_decrease = None

# Weights and biases variables
weights_layer1 = None
biases_layer1 = None
weights_layer2 = None
biases_layer2 = None
weights_layer3 = None
biases_layer3 = None

# Objects
hidden_layer1 = None
hidden_layer2 = None
hidden_layer3 = None
activation1 = None
loss_activation = None
optimizer = None

# Loggers
debug_logger = None
warning_logger = None
error_logger = None


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
    global debug_logger

    try:
        with open('Config\\initial_config.json', 'r') as file:
            configurations = json.load(file)
        debug_logger.debug('JSON file loaded successfully: Config\\initial_config.json')
    except FileNotFoundError:
        error_logger.error('File not found: Config\\initial_config.json')
    except json.JSONDecodeError as e:
        error_logger.error(f'Error decoding JSON: {e}')
    except Exception as e:
        error_logger.error(f'An unexpected error occurred: {e}')

    
    number_of_inputs = configurations['number_of_inputs']
    number_of_outputs = configurations['number_of_outputs']
    size_hidden_layers = configurations['size_hidden_layers']
    number_of_hidden_layers = configurations['number_of_hidden_layers']
    learning_rate = configurations['learning_rate']
    rate_of_decrease = configurations['rate_of_decrease']
    number_of_epochs = configurations['number_of_epochs']



def logging_config():
    """
        Funtion responsible for creating a folder for the logs, creating a logger for each level and file
        handlers for each log and tests the loggers at the end
    """
    global debug_logger
    global warning_logger
    global error_logger

    folder_path = create_folder_for_logs()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    debug_logger = logging.getLogger('debug_logger')
    warning_logger = logging.getLogger('warning_logger')
    error_logger = logging.getLogger('error_logger')

    debug_handler = logging.FileHandler(os.path.join(folder_path, 'debug.log'))
    warning_handler = logging.FileHandler(os.path.join(folder_path, 'warning.log'))
    error_handler = logging.FileHandler(os.path.join(folder_path, 'error.log'))

    debug_handler.setLevel(logging.DEBUG)
    warning_handler.setLevel(logging.WARNING)
    error_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    debug_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)

    debug_logger.addHandler(debug_handler)
    warning_logger.addHandler(warning_handler)
    error_logger.addHandler(error_handler)

    debug_logger.debug('Debug logger set up')
    warning_logger.warning('Warning logger set up')
    error_logger.error('Error logger set up')


def ask_user_weights():
    """
        Funtion responsible for asking the user how he wants to initialize the weights
    """
    global debug_logger

    print('Load weigths or use random weights?')
    print('1 - Load weights')
    print('2 - Random weights')
    print('3 - Exit')
    option = int(input())
    
    debug_logger.debug(f'User chose option {option}')

    return option


def initialize_weights(weight_option):
    """
        Given the option it will load existing weights, create random ones or exit the program 
        depending on the option choosen by the user

        Parameters
        ----------
        weight_option
            The option choosen by the user when asked how the weights should be initilized

        Returns
        -------
        count
            Number of occurances of that figure on the list

    """
    global weights_layer1
    global biases_layer1
    global weights_layer2
    global biases_layer2
    global weights_layer3
    global biases_layer3
    global learning_rate
    global debug_logger
    global warning_logger
    global error_logger

    if weight_option == 1:
        string = "Weights_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)
        folder_path = os.path.join(os.getcwd(), string)

        if not os.path.exists(folder_path):
            warning_logger.warning(f'No weights found for this configurarion! {folder_path}')
            print('No weights found for this configurarion!')
            exit()
        else:
            try:
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
                biases_layer3 = biases_layer3.reshape(1, number_of_outputs)

                learning_rate = np.loadtxt(os.path.join(folder_path, 'learning_rate.txt'))
            except FileNotFoundError:
                error_logger.error(f'File not found: {folder_path}')
            except Exception as e:
                error_logger.error(f'An unexpected error occurred: {e}')

    elif weight_option == 2:
        weights_layer1 = None
        biases_layer1 = None
        weights_layer2 = None
        biases_layer2 = None
        weights_layer3 = None
        biases_layer3 = None
    
    elif weight_option == 3:
        exit()


def load_training_data():
    """
        Funtion responsible for loading the training data from teh database, with which the neural network
        will be trained
    """
    global training_inputs
    global training_targets

    try:
        with open('Database\database.json', 'r') as file:
            training_data_list = json.load(file)
        debug_logger.debug('JSON file loaded successfully.')
    except FileNotFoundError:
        error_logger.error('File not found: Database\database.json')
    except json.JSONDecodeError as e:
        error_logger.error(f'Error decoding JSON: {e}')
    except Exception as e:
        error_logger.error(f'An unexpected error occurred: {e}')

    
    training_inputs = [obj['inputs'] for obj in training_data_list]
    training_targets = [obj['targets'] for obj in training_data_list]

    training_inputs = np.array(training_inputs)
    training_targets = np.array(training_targets)


def initialize_objects():
    """
        Funtion responsible for initializing the objects from the neural network
    """
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global activation1
    global loss_activation
    global optimizer

    hidden_layer1 = classes.Layer_Dense(number_of_inputs, size_hidden_layers, weights_layer1, biases_layer1) 
    hidden_layer2 = classes.Layer_Dense(size_hidden_layers, size_hidden_layers, weights_layer2, biases_layer2) 
    hidden_layer3 = classes.Layer_Dense(size_hidden_layers, number_of_outputs, weights_layer3, biases_layer3)

    activation1 = classes.Activation_ReLU()
    loss_activation = classes.Activation_Softmax_Loss_CategoricalCrossentropy()
    optimizer = classes.Optimizer_SGD(learning_rate)


def train_data():
    """
        Funtion responsible for using the training data loaded into the program and improve the neural network
        to obtain better results
    """
    global training_inputs
    global training_targets
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global activation1
    global loss_activation
    global optimizer
    global rate_of_decrease
    global debug_logger

    best_loss = float('inf')
    number_increases = 1

    for epoch in range(number_of_epochs):
        hidden_layer1.forward(training_inputs)
        activation1.forward(hidden_layer1.output)

        hidden_layer2.forward(activation1.output)
        activation1.forward(hidden_layer2.output)

        hidden_layer3.forward(activation1.output)
        loss = loss_activation.forward(hidden_layer3.output, training_targets)

        if epoch % 10000 == 0:
            print(f'loss: {loss}')
            print(f'learning_rate: {optimizer.learning_rate}')
            print(f'epoch: {epoch}')
        
        if optimizer.learning_rate < 0.00000000000000001:
            debug_logger.debug(f'Leaning rate too low. Epoch: {epoch}')
            return

        loss_activation.backward(loss_activation.output, training_targets)
        hidden_layer3.backward(loss_activation.dinputs)
        
        activation1.backward(hidden_layer3.dinputs)
        hidden_layer2.backward(activation1.dinputs)
        
        activation1.backward(hidden_layer2.dinputs)
        hidden_layer1.backward(activation1.dinputs)

        optimizer.update_params(hidden_layer1)
        optimizer.update_params(hidden_layer2)
        optimizer.update_params(hidden_layer3)

        if epoch % 10000 == 0:
            debug_logger.debug(f'Epoch: {epoch} - Loss: {loss} - Learning rate: {optimizer.learning_rate}')



        if loss < best_loss:
            best_loss = loss
            best_weights_layer1 = hidden_layer1.weights
            best_biases_layer1 = hidden_layer1.biases
            best_weights_layer2 = hidden_layer2.weights
            best_biases_layer2 = hidden_layer2.biases
            best_weights_layer3 = hidden_layer3.weights
            best_biases_layer3 = hidden_layer3.biases
        
        if (epoch + 1) % (number_increases * 50000) == 0:
            optimizer.update_learning_rate(optimizer.learning_rate * rate_of_decrease)	
            number_increases += 1	        	
            hidden_layer1.weights = best_weights_layer1
            hidden_layer1.biases = best_biases_layer1
            hidden_layer2.weights = best_weights_layer2
            hidden_layer2.biases = best_biases_layer2
            hidden_layer3.weights = best_weights_layer3
            hidden_layer3.biases = best_biases_layer3
            best_loss = float('inf')

    
    debug_logger.debug(f'Maximum number of epochs reached. Epoch: {epoch}')
            
        


# save_weights is the function responsible for saving the weights and biases to a file
#
#   How it works:
#   - Function saves the weights and biases to a file
#
#   Parameters:
#   - folder_path: path to the folder where the weights will be saved
#
#   Returns:
#   - Doesnt return anything
def save_weights(folder_path):
    """
        Funtion responsible for saving the new improved weights and biases

        Parameters
        ----------
        folder_path
            Path where the data will be saved

    """
    try:
        np.savetxt(os.path.join(folder_path, 'hidden_layer1_weights.txt'), hidden_layer1.weights)
        np.savetxt(os.path.join(folder_path, 'hidden_layer1_biases.txt'), hidden_layer1.biases)
        np.savetxt(os.path.join(folder_path, 'hidden_layer2_weights.txt'), hidden_layer2.weights)
        np.savetxt(os.path.join(folder_path, 'hidden_layer2_biases.txt'), hidden_layer2.biases)
        np.savetxt(os.path.join(folder_path, 'hidden_layer3_weights.txt'), hidden_layer3.weights)
        np.savetxt(os.path.join(folder_path, 'hidden_layer3_biases.txt'), hidden_layer3.biases)
        np.savetxt(os.path.join(folder_path, 'learning_rate.txt'), np.array([optimizer.learning_rate]))
        np.savetxt(os.path.join(folder_path, 'loss.txt'), np.array([loss]))
    except Exception as e:
        error_logger.error(f'An unexpected error occurred: {e}')


def create_folder_for_weights():
    """
        Creates a folder for the weigts according to the neural network architechure as well as the data and 
        time when the saving is happening
    """
    current_directory = os.getcwd()
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    string = "Weights_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)

    weights_directory = os.path.join(current_directory, string)
    if not os.path.exists(os.path.join(current_directory, string)):
        try:
            os.makedirs(os.path.join(current_directory, string))
        except PermissionError:
            error_logger.error(f'Permission denied: {os.path.join(current_directory, string)}')
        except OSError as e:
            error_logger.error(f'OS error: {e}')
        except Exception as e:
            error_logger.error(f'An unexpected error occurred: {e}')

    folder_path = os.path.join(weights_directory, folder_name)

    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except PermissionError:
            error_logger.error(f'Permission denied: {folder_path}')
        except OSError as e:
            error_logger.error(f'OS error: {e}')
        except Exception as e:
            error_logger.error(f'An unexpected error occurred: {e}')
    
    return folder_path


def create_folder_for_logs():
    """
        Funtion responsible for creating a folder to save the logs
    """
    current_directory = os.getcwd()
    string = "Train_Neural_Network_"
    string2 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = string + string2

    string = "Logs"

    logs_directory = os.path.join(current_directory, string)
    if not os.path.exists(os.path.join(current_directory, string)):
        os.makedirs(os.path.join(current_directory, string))

    folder_path = os.path.join(logs_directory, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path


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



def main():
    logging_config()
    load_configurarions()
    weight_option = ask_user_weights()
    initialize_weights(weight_option)
    load_training_data()
    initialize_objects()
    train_data()
    folder_path = create_folder_for_weights()
    save_weights(folder_path)


main()
