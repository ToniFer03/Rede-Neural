import random
import math

hidden_layer1_weights_file = 'hidden_layer1_weights.txt'
hidden_layer1_biases_file = 'hidden_layer1_biases.txt'
hidden_layer2_weights_file = 'hidden_layer2_weights.txt'
hidden_layer2_biases_file = 'hidden_layer2_biases.txt'
hidden_layer3_weights_file = 'hidden_layer3_weights.txt'
hidden_layer3_biases_file = 'hidden_layer3_biases.txt'
hidden_layer4_weights_file = 'hidden_layer4_weights.txt'
hidden_layer4_biases_file = 'hidden_layer4_biases.txt'

hidden_layer1_weights = []
hidden_layer1_biases = []
hidden_layer2_weights = []
hidden_layer2_biases = []
hidden_layer3_weights = []
hidden_layer3_biases = []
hidden_layer4_weights = []
hidden_layer4_biases = []

with open(hidden_layer1_weights_file) as f:
    for line in f:
        hidden_layer1_weights.append([float(x) for x in line.split()])

with open(hidden_layer1_biases_file) as f:
    for line in f:
        hidden_layer1_biases.append([float(x) for x in line.split()])

with open(hidden_layer2_weights_file) as f:
    for line in f:
        hidden_layer2_weights.append([float(x) for x in line.split()])

with open(hidden_layer2_biases_file) as f:
    for line in f:
        hidden_layer2_biases.append([float(x) for x in line.split()])

with open(hidden_layer3_weights_file) as f:
    for line in f:
        hidden_layer3_weights.append([float(x) for x in line.split()])

with open(hidden_layer3_biases_file) as f:
    for line in f:
        hidden_layer3_biases.append([float(x) for x in line.split()])

with open(hidden_layer4_weights_file) as f:
    for line in f:
        hidden_layer4_weights.append([float(x) for x in line.split()])

with open(hidden_layer4_biases_file) as f:
    for line in f:
        hidden_layer4_biases.append([float(x) for x in line.split()])


guardar_inputs = []
guardar_melhor_move = []


# Variables
lista_figuras = []
figuras_disponiveis = ['X', 'O', '+', '-']
valor_figuras = {'X': 1, 'O': 2, '+': 3, '-': 4}
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[0]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[2]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[0]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[2]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
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
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[3]:
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


    # Cruz
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


    # Bola
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


# Função que retorna se formou uma macrofigura
def verificar_macrofiguras(figura, tabuleiro_temp):
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


    # Cruz
    elif figura == figuras_disponiveis[2]:
        if verifica_existencia_macro_cruz(tabuleiro_temp):
            lista_posicoes = posicoes_cruz[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Bola
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


    # Traco
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

# ----------------------------------------------------------------------------------------------------------

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


# Função que activa a função de activação ReLU
def Activation_ReLU(input):
    return max(0, input)


# Função que activa a função de activação Softmax
def softmax(z):
    exp_values = [math.exp(i) for i in z]
    sum_exp_values = sum(exp_values)
    softmax_values = [i / sum_exp_values for i in exp_values]
    return softmax_values


def forward_propagation_input_hidden1(input_data):
    global hidden_layer1_weights
    global hidden_layer1_biases

    hidden_layer1_output = [0] * len(hidden_layer1_weights[0])
    for i in range(len(hidden_layer1_weights)):
        for j in range(len(hidden_layer1_weights[i])):
            hidden_layer1_output[j] += hidden_layer1_weights[i][j] * input_data[0][i]
    
    for i in range(len(hidden_layer1_output)):
        hidden_layer1_output[i] += hidden_layer1_biases[0][i]
    
    for i in range(len(hidden_layer1_output)):
        hidden_layer1_output[i] = Activation_ReLU(hidden_layer1_output[i])
        
    return hidden_layer1_output


def forward_propagation_hidden1_hidden2(hidden_layer1_output):
    global hidden_layer2_weights
    global hidden_layer2_biases

    hidden_layer2_output = [0] * len(hidden_layer2_weights[0])
    for i in range(len(hidden_layer2_weights)):
        for j in range(len(hidden_layer2_weights[i])):
            hidden_layer2_output[j] += hidden_layer2_weights[i][j] * hidden_layer1_output[i]
    
    for i in range(len(hidden_layer2_output)):
        hidden_layer2_output[i] += hidden_layer2_biases[0][i]

    for i in range(len(hidden_layer2_output)):
        hidden_layer2_output[i] = Activation_ReLU(hidden_layer2_output[i])

    return hidden_layer2_output


def forward_propagation_hidden2_hidden3(hidden_layer2_output):
    global hidden_layer3_weights
    global hidden_layer3_biases

    hidden_layer3_output = [0] * len(hidden_layer3_weights[0])
    for i in range(len(hidden_layer3_weights)):
        for j in range(len(hidden_layer3_weights[i])):
            hidden_layer3_output[j] += hidden_layer3_weights[i][j] * hidden_layer2_output[i]
    
    for i in range(len(hidden_layer3_output)):
        hidden_layer3_output[i] += hidden_layer3_biases[0][i]

    for i in range(len(hidden_layer3_output)):
        hidden_layer3_output[i] = Activation_ReLU(hidden_layer3_output[i])

    return hidden_layer3_output


def forward_propagation_hidden3_hidden4(hidden_layer3_output):
    global hidden_layer4_weights
    global hidden_layer4_biases

    hidden_layer4_output = [0] * len(hidden_layer4_weights[0])
    for i in range(len(hidden_layer4_weights)):
        for j in range(len(hidden_layer4_weights[i])):
            hidden_layer4_output[j] += hidden_layer4_weights[i][j] * hidden_layer3_output[i]
    
    for i in range(len(hidden_layer4_output)):
        hidden_layer4_output[i] += hidden_layer4_biases[0][i]

    for i in range(len(hidden_layer4_output)):
        hidden_layer4_output[i] = Activation_ReLU(hidden_layer4_output[i])

    return hidden_layer4_output


def forward_propagation_hidden4_output(hidden_layer4_output):
    output_layer_output = softmax(hidden_layer4_output)

    return output_layer_output


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
    global hidden_layer1_weights
    global hidden_layer1_biases
    global hidden_layer2_weights
    global hidden_layer2_biases
    global hidden_layer3_weights
    global hidden_layer3_biases
    global hidden_layer4_weights
    global hidden_layer4_biases
    global guardar_inputs
    global guardar_melhor_move

    score = 0
    input_data = [0]
    while len(lista_figuras) > 0:
        # Update input data based on the current game state
        input_data[0] = update_input_data()


        # Forward propagation
        hidden1_output = forward_propagation_input_hidden1(input_data)
        hidden2_output = forward_propagation_hidden1_hidden2(hidden1_output)
        hidden3_output = forward_propagation_hidden2_hidden3(hidden2_output)
        hidden4_output = forward_propagation_hidden3_hidden4(hidden3_output)
        output_layer = forward_propagation_hidden4_output(hidden4_output)
        sorted_actions = sorted(range(len(output_layer)), key=lambda k: output_layer[k], reverse=True)


        i = 0
        for action in sorted_actions:
            row, col = index_to_2d(action, 5)
            if tabuleiro[row][col] == " ":
                tabuleiro[row][col] = lista_figuras[0]
                guardar_melhor_move.append(action)
                break
            i += 1

        if i == 25:
            # Game over
            return (score - 2**25) 


        # Verificar simbolo, update no score e retirar simbolo da lista
        score += verificar_macrofiguras(lista_figuras[0], tabuleiro)
        score += verificar_microfiguras(lista_figuras[0], tabuleiro)
        guardar_inputs.append(input_data[0])
        
        lista_figuras.pop(0)

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
    global lista_figuras
    global guardar_inputs
    global guardar_melhor_move

    total_score = 0
    for i in range(11):
        tabuleiro = [[" " for _ in range(5)] for _ in range(5)]
        gerar_fila_simbolos()
        score = simulate_game()
        total_score += score
    
    print("Score medio: ", total_score / 10)


    return 0

main()