import random
import json
import os
import game_rules
import itertools
from operator import itemgetter

# Variables
figures_list = []
figures_translation_value = {'X': 1, 'O': 2, '+': 3, '-': 4}
available_figures = ['X', 'O', '+', '-']
board = []
data = []
existing_data = []
database_dir = "Database/"
list_figure_counts = []

number_x_padrons = [] #List of lists, where every sublist represents a combination of padrons that can be formed with the total number of x's
number_circle_padrons = []
number_cross_padrons = []
number_dash_padrons = []
active_figures = [] #X, Cross, Circle, Dash

rank_best_figures = [] #List of lists, where the indexes on the inside list represent, score, index on the number_x_padrons list and index on the number_cross_padrons_list

all_X_Permutations = []
all_cross_permutations = []

index_x_position = 0
index_cross_position = 0

index_x_permutation = 0
index_cross_permutation = 0

index_x_padron = 0
index_cross_padron = 0

#Rules for making random figure queues
FigureXandCrossNumbers = [0, 5, 9, 10, 14, 15, 18, 19, 20, 23, 24, 25, 27, 28, 29, 30,
32, 33, 34, 35, 36, 37, 38, 39, 40]

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



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def generate_figures_queue():
    """
        Funtion responsible for generating a queue of random figures to be played

    """
    global figures_list
    global available_figures

    while True:
        num_iterations = random.randrange(20, 60)
        xCount = 0
        crossCount = 0
        circleCount = 0

        for i in range(num_iterations):
            next_figure = available_figures[random.randint(0, 3)]

            if next_figure == available_figures[0]:
                xCount += 1

            if next_figure == available_figures[1]:
                circleCount += 1
            
            if next_figure == available_figures[2]:
                crossCount += 1
            
            figures_list.append(next_figure)
        
        gamerulesCount = 0
        if xCount in FigureXandCrossNumbers:
            gamerulesCount += 1

        if crossCount in FigureXandCrossNumbers:
            gamerulesCount += 1

        if circleCount % 4 == 0:
            gamerulesCount += 1
        
        if gamerulesCount == 3:
            break
        else:
            figures_list = []



def count_figures(figures_list_copy, figure):
    """
        Funtion responsible for counting how many of a certain figures are still
        left on list

        Parameters
        ----------
        lista
            List that contains all the figures left to be played
        simbolo
            The symbol of which we want to know how many are left

        Returns
        -------
        count
            Number of occurances of that figures on the list

    """
    count = 0
    for i in figures_list_copy:
        if i == figure:
            count += 1
    return count



def generate_list_number_figures():
    #TODO: Comments
    global figures_list
    global list_figure_counts

    countX = 0
    countCircle = 0
    countCross = 0
    countDash = 0
    
    countX = count_figures(figures_list, available_figures[0])
    countCircle = count_figures(figures_list, available_figures[1])
    countCross = count_figures(figures_list, available_figures[2])
    countDash = count_figures(figures_list, available_figures[3])

    list_figure_counts.append(countX)
    list_figure_counts.append(countCircle)
    list_figure_counts.append(countCross)
    list_figure_counts.append(countDash)
    


def generate_lists_x_padrons():
    #TODO: Comments
    global list_figure_counts
    global number_x_padrons

    max_number_9 = list_figure_counts[0] // 9 #Max number of 9 figures that can be generated with the total
    max_number_5 = list_figure_counts[0] // 5 #Max number of 5 figures that can be generated with the total

    for x in range(max_number_9+1):
        temp_a = x #Holds the temporary number of figure 9
        temp_b = 0 #Holds the temporary number of figure 5
        temp_c = 0 #Holds the temporary number of the rest of the figures that cant be used
        check_number = temp_a*9 #counter to keep track of the total amount of figures

        
        for y in range(max_number_5+1):
            if(check_number >= list_figure_counts[0]):
                temp_c = list_figure_counts[0] - temp_a*9 - temp_b*5
                number_x_padrons.append([temp_a, temp_b, temp_c])
                break
            
            check_number += 5

            #Checks if by adding 5 it overflowed and in that case stop
            if(check_number > list_figure_counts[0]):
                temp_c = list_figure_counts[0] - temp_a*9 - temp_b*5
                number_x_padrons.append([temp_a, temp_b, temp_c])
                break

            temp_b += 1



def generate_lists_cross_padrons():
    #TODO: Comments
    global list_figure_counts
    global number_cross_padrons

    max_number_9 = list_figure_counts[2] // 9
    max_number_5 = list_figure_counts[2] // 5

    for x in range(max_number_9+1):
        temp_a = x
        temp_b = 0
        temp_c = 0
        check_number = temp_a*9 

        
        for y in range(max_number_5+1):
            if(check_number >= list_figure_counts[2]):
                temp_c = list_figure_counts[2] - temp_a*9 - temp_b*5
                number_cross_padrons.append([temp_a, temp_b, temp_c])
                break
            
            check_number += 5

            #Checks if by adding 5 it overflowed and in that case stop
            if(check_number > list_figure_counts[2]):
                temp_c = list_figure_counts[2] - temp_a*9 - temp_b*5
                number_cross_padrons.append([temp_a, temp_b, temp_c])
                break

            temp_b += 1


def generate_every_combination_list(positions_list):
    #TODO: Comments
    permutaions = list(itertools.permutations(positions_list))
    
    return permutaions


def update_input_data(next_figure):
    if next_figure == 'X':
        position_play = all_X_Permutations[index_x_permutation][index_x_position]
        index_x_position += 1
        return position_play

    if next_figure == 'Y':
        position_play = all_cross_permutations[index_cross_permutation][index_cross_position]
        index_cross_position += 1
        return position_play


def rank_best_figure_options():
    #TODO: Comments
    combinations_X = []
    combinations_cross = []
    best_overall_combination = []
    count = 0
    
    #Check all x combinations
    for i in number_x_padrons:
        score = pow(2, 9) * i[0] + pow(2, 5) * i[1] #Calculate the score
        combinations_X.append(['X', count, score, i[2]]) # Append the result of the score and the number of figures not used
        count += 1


    #Check all cross combinations
    count = 0
    for i in number_cross_padrons:
        score = pow(2, 9) * i[0] + pow(2, 5) * i[1] #Calculate the score
        combinations_cross.append(['+', count, score, i[2]]) # Append the result of the score and the number of figures not used
        count += 1
    

    #Calculate the best combinations together 
    count_i = 0
    count_j = 0
    for i in combinations_X:
        for j in combinations_cross:
            score = combinations_X[count_i][2] + combinations_cross[count_j][2] - pow(2, combinations_X[count_i][3] + combinations_cross[count_j][3])
            best_overall_combination.append([score, count_i, count_j]) #Stores the score as well as the index of the combinations that gives those scores
            count_j += 1
        
        count_j = 0
        count_i += 1
    
    print(best_overall_combination)

    #Rank combinations
    rank_best_figures = sorted(best_overall_combination, key=itemgetter(0), reverse=True)

    print(rank_best_figures)



def generate_every_permutation():
    #TODO: Comments

    return 0


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
    global data

    score = 0
    input_data = [0]
    while len(figures_list) > 0: #TODO: Needs to receive a copy of the figures_list so it can be restored to the original
        input_data = []
        target_temp = []

        input_data = update_input_data(figures_list[0]) #TODO: Make the input correspond to the next position based on the next figure

        while True:
            show_board()
            print("-------------------------------------")
            print("Simbolo atual: " + figures_list[0])
            print("-------------------------------------")
            result_string = "Simbolos: " + ', '.join(map(str, figures_list[1:12]))
            print(result_string)
            print("X na fila: " + str(count_figures(figures_list, available_figures[0])))
            print("O na fila: " + str(count_figures(figures_list, available_figures[1])))
            print("+ na fila: " + str(count_figures(figures_list, available_figures[2])))
            print("- na fila: " + str(count_figures(figures_list, available_figures[3])))
            print("-------------------------------------")
            print("Onde quer colocar o simbolo? (1-25)")
            position = int(input()) - 1 #TODO: This is no longer needed to calculate the position, since its already a tuple
            row, col = index_to_2d(position, 5)
            if board[row][col] == " ": #TODO: Stop this simulation and go to the next iteration if the space is not empty
                board[row][col] = figures_list[0]
                break
            else:
                print("position invalida, selecione outra")


        for i in range(25):
            if i != position:
                target_temp.append(0)
            else:
                target_temp.append(1)


        score += game_rules.verify_big_forms(figures_list[0], board)
        score += game_rules.verify_small_forms(figures_list[0], board)
        figures_list.pop(0)
        data.append([input_data, target_temp])
        clear_terminal()

        figures_in_board = 0
        for row in board:
            for col in row:
                if col != " ":
                    figures_in_board += 1
        
        if figures_in_board == 25:
            break

    cont = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != " ":
                cont += 1


    return (score - 2**cont)


def initialize_game():
    global figures_list

    figures_list = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '+', '+', '+', '+', '+', '+']
    
    generate_list_number_figures()
    generate_lists_x_padrons()
    generate_lists_cross_padrons()
    rank_best_figure_options()
    
    print(1)
    

initialize_game()
#generate_every_combination_list(game_rules.positions_x[0])
#generate_figures_queue()
#generate_list_number_figures()