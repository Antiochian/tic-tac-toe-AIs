# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 03:59:25 2020

@author: Antiochian
"""
import random

class Random_Player:
    def __init__(self,name):
        self.name = name
    
    def make_move(self,board):
        test_order = list(range(board.size))
        random.shuffle(test_order)
        for i in test_order:
            if board.state[i] == 0:
                return i
        raise Exception ("No empty squares found!")
        return