# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 04:33:55 2020

@author: Antiochian
"""
import random

class Aggressive_Player:
    """This player plays randomly unless it sees that it is about to win, 
    in which case it takes an agressive action"""
    def __init__(self,name):
        self.name = name
        
    def check_imminent_opportunity(self,board):
        vert, horiz, diag = board.get_slices()
        me = board.curr_turn
        all_targs = []
        for i in range(board.dim):
            targ0 = [me for _ in range(board.dim)]
            targ0[i] = 0
            all_targs.append(targ0)
        
        opportunity = -1
        for i in range(board.dim):
            row = horiz[i]
            col = vert[i]
            if row in all_targs:
                opportunity = board.dim*i + row.index(0)
            elif col in all_targs:
                opportunity = i + board.dim*col.index(0)
        return opportunity
    
    def make_move(self,board):
        opportunity = self.check_imminent_opportunity(board)
        
        if opportunity != -1:
            #print("THREAT DETECTED")
            return opportunity
        else:
            test_order = list(range(board.size))
            random.shuffle(test_order)
            for i in test_order:
                if board.state[i] == 0:
                    return i
            raise Exception ("No empty squares found!")
            return