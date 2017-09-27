""" Michael Austin

    Driver program for a crossword solver. Requires a
    double-list (matrix) input from the user, with missing
    letters marked with either a star, or a user-specified
    character that must be passed as an argument into the
    crossword solver
"""    


import cw_solver_class

"""treble = [['*', 'a', '*'],
            ['o', '*', 'e'],
            ['*', 'e', '*']]
"""
quad = [['*', '*', '*', '*'],
         ['*', 'e', 'r', '*'],
         ['*', '*', '*', '*'],
         ['e', '*', '*', '*']]


def cwsolver(initial):
    crw = cw_solver_class.CW_solve(initial)
    solved = crw.fill_words(initial)    
    crw.__repr__(solved)
    
cwsolver(quad)
