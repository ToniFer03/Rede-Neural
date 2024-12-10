import random
import json
import os
from game_rules import verify_big_forms, verify_small_forms


# Variables
figures_list = []
figures_translation_value = {'X': 1, 'O': 2, '+': 3, '-': 4}
available_figures = ['X', 'O', '+', '-']
board = []
data = []
existing_data = []
database_dir = "Database/"

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
        Function responsible for generating a list of random predetermined figures
    """
    global figures_list
    global available_figures

    num_iterations = random.randrange(10, 40)
    for i in range(num_iterations):
        figures_list.append(available_figures[random.randint(0, 3)])



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



def update_input_data():
    """
        Function responsible for storing the current state of the game after 
        each play, first 25 values are reserved for the board state and the next 
        12 to the next figures in line, the last one is reserved to the numbers
        of figures left

        Returns
        -------
        input_data
            Object containing the current state of the game to be stored
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
    
    input_data.append(count_figures(figures_list, available_figures[0]))
    input_data.append(count_figures(figures_list, available_figures[1]))
    input_data.append(count_figures(figures_list, available_figures[2]))
    input_data.append(count_figures(figures_list, available_figures[3]))

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
    global data

    score = 0
    input_data = [0]
    while len(figures_list) > 0:
        input_data = []
        target_temp = []

        input_data = update_input_data()

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
            position = int(input()) - 1
            row, col = index_to_2d(position, 5)
            if board[row][col] == " ":
                board[row][col] = figures_list[0]
                break
            else:
                print("position invalida, selecione outra")


        for i in range(25):
            if i != position:
                target_temp.append(0)
            else:
                target_temp.append(1)


        score += verify_big_forms(figures_list[0], board)
        score += verify_small_forms(figures_list[0], board)
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



def select_existing_database():
    """
        Function responsible for asking the user what file he wants to use as a database, and
        load the data inside it to program memory

        Returns
        -------
        return_file
            Returns name of the file choosen to be used as the database

    """
    global existing_data
    files = []
    for (dirpath, dirnames, filenames) in os.walk('Database'):
        files.extend(filenames)
    
    while True:
        count = 1
        print("Choose the database file: ")
        print("--------------------------")
        for file in files:
            print("[{}] - {}".format(count, file))
            count += 1
        
        print("[0] - Sair")
        ans = int(input())

        if ans == 0:
            exit()
        else:
            try:
                return_file = files[ans-1]
                database_file_path = database_dir + return_file
                with open(database_file_path, 'r') as file:
                    existing_data = json.load(file)
                return(return_file)
            except IndexError:
                clear_terminal()
                print("Invalid option \n")
                continue
            except:
                print("An error occured")
                exit()



def create_new_database():
    """
        Function responsible for asking the user the name of the database file that he 
        wants to create and adding the file to the directory

        Returns
        -------
        ans_with_file_extension
            Returns the name of the file choosen already with the extension

    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk('Database'):
        files.extend(filenames)
    
    while True:
        print("Choose the name for the file: ")
        print("------------------------------")
        ans = str(input()).strip()
        ans_with_file_extension = ans + ".json"
        matches = 0

        for file in files:
            if file == ans_with_file_extension:
                matches = 1
        
        if matches == 0:
            return ans_with_file_extension
        else:
            clear_terminal()
            print("A file with that name already exists! \n")
        


def display_database_options():
    """
        Function responsible for asking the user if he wants to select a database file that 
        already exists or to create a new file to be used

        Returns
        -------
        select_existing_database()
            Returns the name of the file that was selected by the user
        
        create_new_database()
            Returns the name of the file created by the user

    """
    while True:
        print('Select an exising database or create a new one: ')
        print('------------------------------------------------')
        print('[1] - Select an existing database')
        print('[2] - Create a new one')
        print('[0] - Exit')
        ans = int(input())

        if ans == 1:
            clear_terminal()
            return select_existing_database()
        if ans == 2:
            clear_terminal()
            return create_new_database()
        if ans == 0:
            exit()
        else:
            print('Not a valid answer!')



#TODO: Be able to revert a move
def generate_gameplay_data():
    global board
    global figures_list
    global existing_data

    clear_terminal()
    database_file_path = database_dir + display_database_options()
    board = [[" " for _ in range(5)] for _ in range(5)]
    generate_figures_queue()
    score = simulate_game()
    print("Score: " + str(score))
    pairs_list = []
    for input_data, target_data in data:
        pairs_list.append({"inputs": input_data, "targets": target_data})
    existing_data.extend(pairs_list)
    with open(database_file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)