from game_simulation import game_simulation_main
from train_neural_network import train_neural_network_main
from generate_gameplay_data import generate_gameplay_data_main
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_terminal()

    while True:
        print('Choose an option: ')
        print('------------------')
        print('[1] - Generate training data by playing')
        print('[2] - Train the neural network')
        print('[3] - Simulate the game')
        print('[0] - Exit')
        ans = int(input())

        if ans == 1:
            generate_gameplay_data_main()
            #TODO: Clear the terminal after selecting a database
            continue
        
        if ans == 2:
            train_neural_network_main()
            continue

        if ans == 3:
            game_simulation_main()
            #TODO: Dont load by most recent folder ask the user what folder he wants to use, leave the most recent function it can be usefull
            #TODO: Dont ask the user for a configuration, obtain it by the folder name
            #TODO: Dont have the layers, weights and biasies be written into the code create them following the folder names
            #TODO: At the end ask if the user wants to play again
            #TODO: Ask the user if he wants a random generated queue or a specific one to be created by him
            continue

        if ans == 0:
            exit()
        
        else:
            clear_terminal
            print("Invalid option, please choose one of the optins shown below \n")


main()