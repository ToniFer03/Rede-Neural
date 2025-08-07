# Neural network written in python to solve a Figuma game

## Table of contents
- [Function of the code](#a-function-code-that-immitates-a-ticket-machine-in-a-metro-system-done-in-the-context-of-a-university-project)
- [Commit Rules](#rules-to-follow-before-a-commit)
- [Branches](#rules-for-branches)
- [Requirements](#requirements)
- [Setup](#how-to-setup-the-tools)
- [User Manual](#how-to-use-the-code)
- [Video Demo](#video-demonstration-of-the-repository)
- [Resume of the code](#Resume-of-the-code)


## Neural network project made to solve a Figuma game  
To understand the Game please check out the Gamerules PDF on the Help folder in this repository. This project allows you to tweek the parameters
of the neural network, create and select what database you want to use to train the neural network, play to expand the database and test the effectiveness
of the Neural network in game.
It is made primarly to showcase how an implementation of this type could work to solve a complex game with a lot of variables.  

## Rules to follow before a commit

The commits must follow this rules:

    type [scope optional]: description

The commits must be atomic, only one objective

### Types

The available types with their respective emojis:  
🏗️build - Changes to the project build  
🔄️ci - Changes to the continuous integration cycle  
📄docs - Changes to project documentation  
🎨style - Changes related to the styling of the code  
✨feat - Changes that add new features  
🐛fix - Changes to fix errors (bugs) in the code  
🏎️perf - Changes to improve performance of the project  
🧹refactor - Refactoring of the code  
🔙revert - Reverting a previous commit  
🧮test - Changes to the unit tests of the code  
💡chore - Changes that do not alter the project code

### Scope:

The name of the component affected by the changes, example:
Compiler, readme, forms

### Description:

Brief description of the changes made, must be in english, present verb form of the imperative and without a full stop, example:
feat(validations): implement messageServer-side validations


## Rules for Branches

Must be used when implementing a new feature, working on a new release or fixing a bug in the code, when finished the development on that branch it can be merged with the main branch.
There are two types of branches always present on the repository:

    main/master
    dev/name-of-developer

There can also exist temporary branches like:

    feat/<nome-da-funcionalidade>
    bug/<descrição-do-erro>
    release/<ID da release>
    <ID do issue>/<descrição-do-issue>

The branch names must be short and explain its purpose, can't contain special characters of white spaces;


## Requirements

Python 3.12 or superior


##  How to use the code

1. Open the Config file and choose what configuration you want your neural network to have
2. Run the main.py file 
3. Choose one of the options

1. Selecting option one you need to select a database file to store the new game data

1. Selecting option 2 you can select either:
2. Load the most recent weights of the configuration you have choosen and improve it
3. Create new weights with that same configuration

1. Selecting option 3:
2. Select a random queue of figures for the Neural network to solve
3. Select a custom queue of figures for the Neural network to solve

## Video demonstration of the repository   

## Resume of the code  
