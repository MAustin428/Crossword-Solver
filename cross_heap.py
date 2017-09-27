""" Michael Austin

    A basic implementation of a max heap. This is designed to be used
    in conjunction with the dictionary found in the AIMA supplemental
    code, written by Russell & Norvig. Since the frequencies attached
    to each word are static, this heap implementation only has the
    functionality needed for it to be run once!
"""

import string
import gzip

class Cross_heap():

    def __init__(self):
        self.word_array = []

    def contains(self, word):
        wa = self.word_array
        if word in [x[0] for x in wa]:
            return True
        else:
            return False

    def insert(self, pair):
        wa = self.word_array
        n = len(wa)
        
        wa.append(pair)
        self.percolate_up(n)

    def percolate_up(self, final_position):
        wa = self.word_array
        n = final_position
        temp_pair = wa[n]

        while (n>1 and self.swap(wa[n], wa[n/2])):
            wa[n] = wa[n/2]
            n = n/2
        
        wa[n] = temp_pair

    def swap(self, pair, pairent):
        if pair[1] < pairent[1]:
            return True
        else:
            return False
    def get_word(self, int):
        pair = self.word_array[int]
        return pair[0]
    
    def get_length(self):
        wa = self.word_array
        return len(wa)
