# game_rules.py

# Variables
available_figures = ['X', 'O', '+', '-']

# All possible coordinates to form an X in a 5x5 board
positions_x = [
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
positions_cross = [
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
positions_circle = [
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
positions_dash = [
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

def verify_five_figure_x(board):
    """
        Verifies if there is an X formed by 5 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_x[1:]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[0]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 5:
                return True

    return False


def verify_five_figure_cross(board):
    """
        Verifies if there is a Cross formed by 5 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_cross[1:]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[2]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 5:
                return True

    return False


def verify_four_figure_circle(board):
    """
        Verifies if there is a circle formed by 4 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_circle[9:]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[1]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 4:
                return True

    return False


def verify_two_figure_dash(board):
    """
        Verifies if there is a Dash formed by 2 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_dash[15:]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[3]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 2:
                return True

    return False


def verify_nine_figure_x(board):
    """
        Verifies if there is an X formed by 9 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_x[:1]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[0]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 9:
                return True

    return False



def verify_nine_figure_cross(board):
    """
        Verifies if there is a Cross formed by 9 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_cross[:1]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[2]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 9:
                return True

    return False


def verify_eight_figure_circle(board):
    """
        Verifies if there is a Circle formed by 8 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_circle[:9]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            print(board[position[0]][position[1]])
            if board[position[0]][position[1]] == available_figures[1]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 8:
                return True

    return False


def verify_three_figure_dash(board):
    """
        Verifies if there is a Dash formed by 3 pieces

        Parameters
        ----------
        board
            Object that contains a copy of the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = positions_dash[:15]

    for position_list in temp_position:
        num_correspondances = 0
        for position in position_list:
            if board[position[0]][position[1]] == available_figures[3]:
                num_correspondances += 1
            else:
                break
        
            if num_correspondances == 3:
                return True

    return False


def verify_small_forms(figure, board):
    """
        Funtion responsible for calling the funtion to verify if the smaller form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figure
            String corresponding to the last figure that was played
        board
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns the score that that play originated to be added to the total score
    """
    temp_position = []
    temp_score = 0
    num_correspondances = 0

    if figure == available_figures[0]:
        if verify_five_figure_x(board):
            temp_all_positions = positions_x[1:]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[0]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                    
                if(num_correspondances == 5):
                    break           

            temp_score = 32


    elif figure == available_figures[2]:
        if verify_five_figure_cross(board):
            temp_all_positions = positions_cross[1:]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[2]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                    
                if(num_correspondances == 5):
                    break
            
            temp_score = 32


    elif figure == available_figures[1]:
        if verify_four_figure_circle(board):
            temp_all_positions = positions_circle[9:]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[1]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                    
                if(num_correspondances == 4):
                    break
            
            temp_score = 16  

    
    elif figure == available_figures[3]:
        if verify_two_figure_dash(board):
            temp_all_positions = positions_dash[15:]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[3]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                    
                if(num_correspondances == 2):
                    break
            
            temp_score = 2
        
    for position in temp_position:
        board[position[0]][position[1]] = " "

    return temp_score



def verify_big_forms(figure, board):
    """
        Funtion responsible for calling the funtion to verify if the biggest form of the
        last figure played has been completed.
        If they have been completed, it will clear the board of the form and increase the 
        score.

        Parameters
        ----------
        figure
            String corresponding to the last figure that was played
        board
            Object that contains the current state of the board

        Returns
        -------
        boolean
            Returns a boolean indicating if a certain figure was formed or not

    """
    temp_position = []
    temp_score = 0
    num_correspondances = 0

    if figure == available_figures[0]: 
        if verify_nine_figure_x(board):
            positions_list = positions_x[0]
            for position in positions_list:
                temp_position.append(position)
            temp_score = 512


    elif figure == available_figures[2]:
        if verify_nine_figure_cross(board):
            positions_list = positions_cross[0]
            for position in positions_list:
                temp_position.append(position)
            temp_score = 512


    elif figure == available_figures[1]:
        if verify_eight_figure_circle(board):
            temp_all_positions = positions_circle[:9]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[1]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                
                if(num_correspondances == 8):
                    break
            
            temp_score = 256


    elif figure == available_figures[3]:
        if verify_three_figure_dash(board):
            temp_all_positions = positions_dash[:15]
            for positions_list in temp_all_positions:
                for position in positions_list:
                    if board[position[0]][position[1]] == available_figures[3]:
                        temp_position.append(position)
                        num_correspondances += 1
                    else:
                        num_correspondances = 0
                        temp_position = []
                        break
                
                if(num_correspondances == 3):
                    break
            temp_score = 8

    for position in temp_position:
        board[position[0]][position[1]] = " "

    return temp_score
