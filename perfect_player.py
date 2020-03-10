# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 06:00:59 2020

@author: Antiochian
"""
import random

class Perfect_Player:
    def __init__(self,name):
        self.name = name
        self.inf = 1024
        
    def make_move(self,board):
        if board.dim > 4:
            raise Exception("ERROR - ALG ONLY WORKS ON 3x3 GRID")
        self.dim = board.dim
        self.size = board.size
        self.me = board.curr_turn
        self.them = board.change_turn()
        board_state = board.state
        if self.dim == 3 and board_state[4] == 0:
            return 4
        else:
            best_choice = self.minimax(board_state,True,-self.inf,+self.inf)
            if best_choice[1] == None:
                test_order = list(range(board.size))
                random.shuffle(test_order)
                for i in test_order:
                    if board.state[i] == 0:
                        return i
                raise Exception ("No empty squares found!")
                return
        return best_choice[1]
            
    def minimax(self,board_state,isme,alpha,beta):
        if self.outcome(board_state) != None: #if game is over
            return (self.outcome(board_state),None)
        
        if isme:
            best_choice = (-self.inf,None)
            for choice in range(9):
                if self.shallow_legal_check(board_state,choice): #if space is available
                    board_state[choice] = self.me
                    curr_choice = self.minimax(board_state,False,alpha,beta)
                    if curr_choice[0] > best_choice[0]:
                        best_choice = (curr_choice[0],choice)
                    board_state[choice] = 0
                    alpha = max(alpha,best_choice[0])
                    if alpha >= beta:
                        break
            return best_choice
        else: #NOT ME
            worst_choice = (+self.inf,None)
            for choice in range(9):
                if self.shallow_legal_check(board_state,choice): #if space is available
                    board_state[choice] = self.them
                    curr_choice = self.minimax(board_state,True,alpha,beta)
                    if curr_choice[0] < worst_choice[0]:
                        worst_choice = (curr_choice[0],choice)
                    board_state[choice] = 0
                    beta = min(beta,worst_choice[0])
                    if alpha >= beta:
                        break
            return worst_choice
            
            
    def shallow_legal_check(self,board_state,pos):
        if pos >= 0 and pos < self.size:
            return not board_state[pos]
        else:
            return False
    
    def shallow_get_slices(self,board_state):
        vert = [[] for _ in range(self.dim)]
        horiz = [[] for _ in range(self.dim)]
        diag = [[] for _ in range(2)] #always 2 diags
        
        for i in range(0,self.size,self.dim):
            horiz[i//self.dim] =  board_state[i:i+self.dim]
            
            for col in range(self.dim):
                vert[col].append(board_state[i+col])
            
            diag[0].append(board_state[i + i//self.dim ])
            diag[1].append(board_state[i + self.dim - 1 - i//self.dim])
        return vert, horiz, diag

    def outcome(self, board_state):
        vert, horiz, diag = self.shallow_get_slices(board_state)
        win_target = [self.me] * self.dim
        lose_target = [self.them] * self.dim
        if win_target in vert+horiz+diag:
            return 1 #WIN
        elif lose_target in vert+horiz+diag:
            return -1 #LOSE
        elif not any([0 in col for col in vert]):
            return 0 #DRAW
        else:
            return None #game not ended

#test = Perfect_Player("tester")
#testboard = [2,0,1,1,0,0,1,2,2]
#print(test.make_move(testboard))