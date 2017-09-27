""" Michael Austin

    Given a 3x3 or 4x4 crossword partially filled with letters,
    this program will fill in the blanks with the most commonly-
    used words that fit. Dictionary of 3 and 4 letter words taken
    from the AIMA supplemental code, by Russell and Norvig.
"""    

import string
import copy
import gzip

""" A simple max heap implementation which will be used to
    store our dictionary words. """
import cross_heap as cw_heap                                  

# Builds a dictionary of 3 and 4 letter words, sorted by most used.
dict_file = "words34.txt.gz"
cross = cw_heap.Cross_heap()

for line in gzip.open(dict_file):
    word, n = line.strip().split('\t')
    pair = (word, float(n))
    cross.insert(pair)

class CW_solve():

    def __init__(self, initial):
        self.initial = initial

    def __repr__(self, state):
        """ Returns a visual representation of the crossword. """
        print ' ',
        for w in range(len(state)+2):
            print "___",
        print '\n'
        for x in state:
            print "|  ", x, "  |"
        print ' ',
        for y in range(len(state)+2):
            print "___",
        print '\n'
        return state

    def check_word(self, line, sp_ch='*'):
        """ Returns all words in the dictionary
            that will fit into the supplied line. """
        valid = []
        le = cross.get_length()
        for n in range(le):
            t1 = "".join(line)
            t2 = cross.get_word(n)
            if len(t1) == len(t2):
                z = zip(t1, t2)
                for x in z:
                    if (x[0] != x[1]) and (x[0] != sp_ch):
                        break
                else:
                    word_as_list = list(t2)
                    valid.append(word_as_list)
        return valid

    def cols(self, state):
        """ Returns a list containing the columns of the crossword,
            as opposed to the rows. """
        columns = []
        col_word = []
        g = state
        z = len(g)
        for x in range(z):
            for y in range(z):
                col_word.append(g[y][x])
            columns.append(col_word)
            col_word = []
                
        print "rows: "
        for i in range(len(g)):
            print g[i]
            
        print "cols: "
        for i in range(len(columns)):
            print columns[i]

        return columns

    def fill_words(self, state, i = 0, n = 0):
        """ Recursively fills in crossword with valid words. Replaces
            a word if no vertical word is possible. If no valid words
            can be found in the dictionary, replaces the previous word,
            and continues from there. Recursively returns either a solved
            crossword, or null. """
        current_state = copy.deepcopy(state)

        # Ensures that we stay in the crossword boundaries
        while (i < len(current_state)):
            action_list = self.check_word(current_state[i])

            # Return value if no solution can be found
            if (i < 0):
                return [['N', 'O', '*'],
                        ['A', 'N', 'S'],
                        ['W', 'E', 'R']]
            
            # Only iterates through dictionary
            while (n < len(action_list)):
                current_state[i] = action_list[n]

                # Checks if columns also form valid words
                if (self.valid_col_tester(current_state)):
                    vv = self.fill_words(current_state, i+1)
                    if vv:
                        return vv       # Success!
                    else:
                        n += 1          # Currently unsolveable, next dictionary entry
                else:
                    n += 1
            return
        
        return current_state

        
    def valid_col_tester(self, state):
        """ Tests the columns to ensure that they each are capable of forming
            at least one word found in the dictionary. Returns true or false. """
        vert_state = self.cols(state)
        for line in vert_state:
            line_index = vert_state.index(line)
            vert_word = self.check_word(vert_state[line_index])
            if  not(vert_word):
                return  False
        return True
