import datetime
import numpy as np
import json
import os
import shutil

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
best_loss = float('inf')

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


np.random.seed(0)
class layer_dense:
    def __init__(self, n_inputs, n_neurons, custom_weights=None, custom_biases=None):
        if custom_weights is None:
            self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
            self.biases = np.zeros((1, n_neurons))
        else:
            self.weights = custom_weights
            self.biases = custom_biases

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        self.inputs = inputs

    def backward(self, dvalues):
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs = np.dot(dvalues, self.weights.T)


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)
        self.inputs = inputs
    
    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities
        self.inputs = inputs
    
    def backward(self, dvalues):
        self.dinputs = np.empty_like(dvalues)
        for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
            single_output = single_output.reshape(-1, 1)
            jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
            self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)


class Loss:
    def calculate(self, output, y): # y is the target values
        sample_losses = self.forward(output, y) 
        data_loss = np.mean(sample_losses)
        return data_loss


class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7) # clip both sides to prevent division by 0
        
        if len(y_true.shape) == 1: # if targets are in a single dimension
            correct_confidences = y_pred_clipped[range(samples), y_true]
        
        elif len(y_true.shape) == 2: # if targets are in a one-hot encoded format
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

    def backward(self, dvalues, y_true):
        samples = len(dvalues)
        labels = len(dvalues[0])
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]
        self.dinputs = -y_true / dvalues
        self.dinputs = self.dinputs / samples


class Activation_Softmax_Loss_CategoricalCrossentropy():
    def __init__(self):
        self.activation = Activation_Softmax()
        self.loss = Loss_CategoricalCrossentropy()
    
    def forward(self, inputs, y_true):
        self.activation.forward(inputs)
        self.output = self.activation.output
        return self.loss.calculate(self.output, y_true)
    
    def backward(self, dvalues, y_true):
        samples = len(dvalues)
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)
        self.dinputs = dvalues.copy()
        self.dinputs[range(samples), y_true] -= 1
        self.dinputs = self.dinputs / samples


class Optimizer_SGD:
    global learning_rate
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases
    def update_learning_rate(self, new_learning_rate):
        self.learning_rate = new_learning_rate




# load_configurations is the function responsible for loading the configurations from the configuration file
#
#   How it works:
#   - Funtion opens the configuration file, loads the configurations to the respective global 
#     variables and closes the file
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Doesnt return anything
#
def load_configurarions():
    global number_of_inputs
    global number_of_outputs
    global number_of_hidden_layers
    global size_hidden_layers
    global learning_rate
    global number_of_epochs

    with open('Config\initial_config.json', 'r') as file:
        configurations = json.load(file)

    number_of_inputs = configurations['number_of_inputs']
    number_of_outputs = configurations['number_of_outputs']
    size_hidden_layers = configurations['size_hidden_layers']
    number_of_hidden_layers = configurations['number_of_hidden_layers']
    learning_rate = configurations['learning_rate']
    number_of_epochs = configurations['number_of_epochs']



# ask_user_weights is the function responsible for asking the user if he wants to load the weights or use random weights
#
#   How it works:
#   - Function prints the options to the user and waits for an input
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Returns the option chosen by the user
#
def ask_user_weights():
    print('Load weigths or use random weights?')
    print('1 - Load weights')
    print('2 - Random weights')
    print('3 - Exit')
    option = int(input())

    return option



# initialize_weights is the function responsible for initializing the weights and biases
#
#   How it works:
#   - If the user chooses to load weights, the function will first verify if there are any weights
#     for the specified configuration. If there are, it will load the most recent weights. If there
#     are no weights, the program will warn the user and exit. It will also load the learning rate
#     from the most recent folder.
#   - If the user chooses to use random weights, the function will initialize the weights and biases
#     with random values.
#   - If the user chooses to exit, the program will exit.
#
#   Parameters:
#   - weight_option: option chosen by the user
#
#   Returns:
#   - Doesnt return anything
#
def initialize_weights(weight_option):
    global weights_layer1
    global biases_layer1
    global weights_layer2
    global biases_layer2
    global weights_layer3
    global biases_layer3
    global learning_rate

    if weight_option == 1:
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
            biases_layer3 = biases_layer3.reshape(1, number_of_outputs)

            learning_rate = np.loadtxt(os.path.join(folder_path, 'learning_rate.txt'))

    elif weight_option == 2:
        weights_layer1 = None
        biases_layer1 = None
        weights_layer2 = None
        biases_layer2 = None
        weights_layer3 = None
        biases_layer3 = None
    elif weight_option == 3:
        exit()



# load_training_data is the function responsible for loading the training data from the database
#
#   How it works:
#   - Function opens the database file, loads the training data to the respective global
#     variables and closes the file
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Doesnt return anything
#
def load_training_data():
    global training_inputs
    global training_targets

    with open('Database\database.json', 'r') as file:
        training_data_list = json.load(file)

    # Extract inputs and targets from the list of objects
    training_inputs = [obj['inputs'] for obj in training_data_list]
    training_targets = [obj['targets'] for obj in training_data_list]

    training_inputs = np.array(training_inputs)
    training_targets = np.array(training_targets)



# initialize_objects is the function responsible for initializing the objects
#
#   How it works:
#   - Function initializes the objects with the respective parameters
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Doesnt return anything
#
def initialize_objects():
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global activation1
    global loss_activation
    global optimizer

    hidden_layer1 = layer_dense(number_of_inputs, size_hidden_layers, weights_layer1, biases_layer1) 
    hidden_layer2 = layer_dense(size_hidden_layers, size_hidden_layers, weights_layer2, biases_layer2) 
    hidden_layer3 = layer_dense(size_hidden_layers, number_of_outputs, weights_layer3, biases_layer3)

    activation1 = Activation_ReLU()
    loss_activation = Activation_Softmax_Loss_CategoricalCrossentropy()
    optimizer = Optimizer_SGD(learning_rate)



# train_data is the function responsible for training the data
#
#   How it works:
#   - Function trains the data loaded from the database, using the objects initialized
#     in the previous function. Uses the forward method to calculate the output and the
#     backward method to calculate the gradients and update the weights and biases. If 
#     the loss is greater than the last loss, the learning rate is decreased.
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Doesnt return anything
#
def train_data():
    global training_inputs
    global training_targets
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global activation1
    global loss_activation
    global optimizer
    global loss

    last_loss = float('inf')
    for epoch in range(number_of_epochs):
        # Forward pass
        hidden_layer1.forward(training_inputs)
        activation1.forward(hidden_layer1.output)

        hidden_layer2.forward(activation1.output)
        activation1.forward(hidden_layer2.output)

        hidden_layer3.forward(activation1.output)
        loss = loss_activation.forward(hidden_layer3.output, training_targets)

        if loss < best_loss:
            best_loss = loss

        if not epoch % 1000:
            print(f'loss: {loss}')
            print(f'learning_rate: {optimizer.learning_rate}')
            print(f'epoch: {epoch}')

            if optimizer.learning_rate < 0.00000000000000001:
                if loss > best_loss:
                    print('Not optimal: ', loss, ' > ', best_loss)
                    break
                return

        # Backward pass
        loss_activation.backward(loss_activation.output, training_targets)
        hidden_layer3.backward(loss_activation.dinputs)
        
        activation1.backward(hidden_layer3.dinputs)
        hidden_layer2.backward(activation1.dinputs)
        
        activation1.backward(hidden_layer2.dinputs)
        hidden_layer1.backward(activation1.dinputs)

        # Update weights and biases
        optimizer.update_params(hidden_layer1)
        optimizer.update_params(hidden_layer2)
        optimizer.update_params(hidden_layer3)

        if(epoch % 250 == 0):
            if loss > last_loss:
                optimizer.update_learning_rate(optimizer.learning_rate * 0.66)
            else:
                last_loss = loss



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
    np.savetxt(os.path.join(folder_path, 'hidden_layer1_weights.txt'), hidden_layer1.weights)
    np.savetxt(os.path.join(folder_path, 'hidden_layer1_biases.txt'), hidden_layer1.biases)
    np.savetxt(os.path.join(folder_path, 'hidden_layer2_weights.txt'), hidden_layer2.weights)
    np.savetxt(os.path.join(folder_path, 'hidden_layer2_biases.txt'), hidden_layer2.biases)
    np.savetxt(os.path.join(folder_path, 'hidden_layer3_weights.txt'), hidden_layer3.weights)
    np.savetxt(os.path.join(folder_path, 'hidden_layer3_biases.txt'), hidden_layer3.biases)
    np.savetxt(os.path.join(folder_path, 'learning_rate.txt'), np.array([optimizer.learning_rate]))
    np.savetxt(os.path.join(folder_path, 'loss.txt'), np.array([loss]))



# create_folder_for_weights is the function responsible for creating a folder to save the weights
#
#   How it works:
#   - Function creates a variable that holds the current timestamp. Verifies if a folder 
#   for this neural network configuration already exists. If it doesnt, it creates a folder 
#   for the current configuration with the name "Weights_number_of_hidden_layers_size_hidden_layers".
#   Then, it creates a folder inside the previous folder with the current timestamp as the name.
#
#   Parameters:
#   - Doesnt receive any parameters
#
#   Returns:
#   - Returns the path to the folder where the weights will be saved
#
def create_folder_for_weights():
    current_directory = os.getcwd()
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    string = "Weights_" + str(number_of_hidden_layers) + "_" + str(size_hidden_layers)

    weights_directory = os.path.join(current_directory, string)
    if not os.path.exists(os.path.join(current_directory, string)):
        os.makedirs(os.path.join(current_directory, string))

    folder_path = os.path.join(weights_directory, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path



# get_most_recent_folder is the function responsible for getting the most recent folder
#
#   How it works:
#   - Function saves the names of all the folders inside the specified folder to a list. Then,
#   it converts the names to datetime objects and gets the most recent folder.
#
#   Parameters:
#   - folder_path: path to the folder where the weights for a certain configuration are saved
#
#   Returns:
#   - Returns the name of the most recent folder
#
def get_most_recent_folder(folder_path):
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    if not folders:
        return None

    folders_dates = [datetime.datetime.strptime(f, "%Y-%m-%d_%H-%M-%S") for f in folders]

    most_recent_folder = max(folders_dates)

    most_recent_folder_name = most_recent_folder.strftime("%Y-%m-%d_%H-%M-%S")

    return most_recent_folder_name


def main():
    load_configurarions()
    weight_option = ask_user_weights()
    initialize_weights(weight_option)
    load_training_data()
    initialize_objects()
    train_data()
    folder_path = create_folder_for_weights()
    save_weights(folder_path)


main()

