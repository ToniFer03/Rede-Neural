# game_rules.py

# Variables
figuras_disponiveis = ['X', 'O', '+', '-']

# All possible coordinates to form an X in a 5x5 board
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


# All possible coordinates to form a Cross in a 5x5 board
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


# All possible coordinates to form a circle in a 5x5 board
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


# All possible coordinates to form a dash in a 5x5 board
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

def verifica_existencia_micro_x(tabuleiro_temp):
    """
        Verifies if there is an X formed by 5 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verifica_existencia_micro_cruz(tabuleiro_temp):
    """
        Verifies if there is a Cross formed by 5 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verifica_existencia_micro_bola(tabuleiro_temp):
    """
        Verifies if there is a circle formed by 4 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verifica_existencia_micro_traco(tabuleiro_temp):
    """
        Verifies if there is a Dash formed by 2 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verifica_existencia_macro_x(tabuleiro_temp):
    """
        Verifies if there is an X formed by 9 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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



def verifica_existencia_macro_cruz(tabuleiro_temp):
    """
        Verifies if there is a Cross formed by 9 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verifica_existencia_macro_bola(tabuleiro_temp):
    """
        Verifies if there is a Circle formed by 8 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_posicao = posicoes_bola[:9]

    for lista_posicao in temp_posicao:
        num_correspondecias = 0
        for posicao in lista_posicao:
            print(tabuleiro_temp[posicao[0]][posicao[1]])
            if tabuleiro_temp[posicao[0]][posicao[1]] == figuras_disponiveis[1]:
                num_correspondecias += 1
            else:
                break
        
            if num_correspondecias == 8:
                return True

    return False


def verifica_existencia_macro_traco(tabuleiro_temp):
    """
        Verifies if there is a Dash formed by 3 pieces

        Parameters
        ----------
        tabuleiro_temp
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


def verificar_microformas(figura, tabuleiro_temp):
    """
        Funtion responsible for calling the funtion to verify if the smaller form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figura
            String corresponding to the last figure that was played
        tabuleiro_temp
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns the score that that play originated to be added to the total score
    """
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


    # Cross
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


    # Circle
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

    
    # Dash
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



def verificar_macroformas(figura, tabuleiro_temp):
    """
        Funtion responsible for calling the funtion to verify if the biggest form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figura
            String corresponding to the last figure that was played
        tabuleiro_temp
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
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


    # Cross
    elif figura == figuras_disponiveis[2]:
        if verifica_existencia_macro_cruz(tabuleiro_temp):
            lista_posicoes = posicoes_cruz[0]
            for posicao in lista_posicoes:
                temp_posicao.append(posicao)
            temp_score = 512


    # Circle
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


    # Dash
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
