import os
from generate_gameplay_data import generate_gameplay_data
from train_neural_network import train_neural_network
from game_simulation import game_simulation



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    clear_terminal()

    while True:
        print('Choose which action you want to perform:')
        print('----------------------------------------')
        print('[1] - Play and generate training data for the neural network')
        print('[2] - Train the neural network')
        print('[3] - Use the neural network to solve the game')
        print('[0] - Exit the program')
        ans = str(input())
        ans = ans.strip()

        if ans == '1':
            clear_terminal()
            generate_gameplay_data()
        elif ans == '2':
            clear_terminal()
            train_neural_network()
        elif ans == '3':
            clear_terminal()
            game_simulation()
        elif ans == '0':
            exit(0)
        else:
            clear_terminal()
            print("Invalid option, please choose one of the options shown below!")


main()