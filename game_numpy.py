import random
import numpy as np
import classes
import os

# Neural network classes
hidden_layer1 = None
hidden_layer2 = None
hidden_layer3 = None
linear_activation = None
softmax_activation = None

weights_layer1_file = 'weights_layer1.txt'
biases_layer1_file = 'biases_layer1.txt'
weights_layer2_file = 'weights_layer2.txt'
biases_layer2_file = 'biases_layer2.txt'
weights_layer3_file = 'weights_layer3.txt'
biases_layer3_file = 'biases_layer3.txt'

weights_layer1 = []
biases_layer1 = []
weights_layer2 = []
biases_layer2 = []
weights_layer3 = []
biases_layer3 = []

with open(weights_layer1_file) as f:
    for line in f:
        weights_layer1.append([float(x) for x in line.split()])

with open(biases_layer1_file) as f:
    for line in f:
        biases_layer1.append([float(x) for x in line.split()])

with open(weights_layer2_file) as f:
    for line in f:
        weights_layer2.append([float(x) for x in line.split()])

with open(biases_layer2_file) as f:
    for line in f:
        biases_layer2.append([float(x) for x in line.split()])

with open(weights_layer3_file) as f:
    for line in f:
        weights_layer3.append([float(x) for x in line.split()])

with open(biases_layer3_file) as f:
    for line in f:
        biases_layer3.append([float(x) for x in line.split()])


guardar_inputs = []
guardar_melhor_move = []


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

# ----------------------------------------------------------------------------------------------------------

# Gerar fila random de simbolos
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
    global hidden_layer1
    global hidden_layer2
    global hidden_layer3
    global linear_activation
    global softmax_activation
    global guardar_inputs
    global guardar_melhor_move

    score = 0
    input_data = [0]
    while len(lista_simbolos) > 0:
        # Update input data based on the current game state
        input_data[0] = update_input_data()
        hidden_layer1.forward(input_data)
        linear_activation.forward(hidden_layer1.output)
        hidden_layer2.forward(linear_activation.output)
        linear_activation.forward(hidden_layer2.output)
        hidden_layer3.forward(linear_activation.output)
        softmax_activation.forward(hidden_layer3.output)

        # Get action from output layer probabilities
        sorted_actions = sorted(range(len(softmax_activation.output)), key=lambda k: softmax_activation.output[k], reverse=True)



        i = 0
        for action in sorted_actions:
            row, col = index_to_2d(action, 5)
            if tabuleiro[row][col] == " ":
                tabuleiro[row][col] = lista_simbolos[0]
                guardar_melhor_move.append(action)
                break
            i += 1

        if i == 25:
            # Game over
            return (score - 2**25) 


        # Verificar simbolo, update no score e retirar simbolo da lista
        score += verificar_macrofiguras(lista_simbolos[0], tabuleiro)
        score += verificar_microfiguras(lista_simbolos[0], tabuleiro)
        guardar_inputs.append(input_data[0])
        
        lista_simbolos.pop(0)

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

    hidden_layer1 = classes.layer_dense(weights_layer1, biases_layer1) 
    hidden_layer2 = classes.layer_dense(weights_layer2, biases_layer2) 
    hidden_layer3 = classes.layer_dense(weights_layer3, biases_layer3)

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


def main():
    global tabuleiro
    global lista_simbolos
    global guardar_inputs
    global guardar_melhor_move

    total_score = 0
    for i in range(11):
        tabuleiro = [[" " for _ in range(5)] for _ in range(5)]
        initialize_objects()
        gerar_fila_simbolos()
        score = simulate_game()
        total_score += score
    
    print("Score medio: ", total_score / 10)


    return 0

main()