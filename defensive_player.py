# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 04:08:48 2020

@author: Antiochian
"""
import random

class Defensive_Player:
    """This player plays randomly unless it sees that it is about to lose, 
    in which case it takes a defensive action"""
    def __init__(self,name):
        self.name = name
        
    def check_imminent_threat(self,board):
        vert, horiz, diag = board.get_slices()
        opponent = board.change_turn()
        all_targs = []
        for i in range(board.dim):
            targ0 = [opponent for _ in range(board.dim)]
            targ0[i] = 0
            all_targs.append(targ0)
        
        threat = -1
        for i in range(board.dim):
            row = horiz[i]
            col = vert[i]
            if row in all_targs:
                threat = board.dim*i + row.index(0)
            elif col in all_targs:
                threat = i + board.dim*col.index(0)
        return threat
    
    def make_move(self,board):
        threat = self.check_imminent_threat(board)
        
        if threat != -1:
            #print("THREAT DETECTED")
            return threat
        else:
            test_order = list(range(board.size))
            random.shuffle(test_order)
            for i in test_order:
                if board.state[i] == 0:
                    return i
            raise Exception ("No empty squares found!")
            return