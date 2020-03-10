# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 02:45:19 2020

@author: Antiochian
"""
import random

class Board:
    def __init__(self,dim,starting_player=1):
        self.dim = dim
        self.size = dim*dim
        self.state = [0]*self.size
        self.curr_turn = starting_player #initialise as p1's turn
        
    def coord_to_pos(self, coord):
        #takes (x,y) as input
        (x,y) = coord
        if x > self.dim or y > self.dim:
            print("coord: ",coord)
            raise ValueError("Invalid coord - x or y out of bounds")        
        pos = self.dim*y + x
        return pos
    
    def pos_to_coord(self,pos):
        x = pos % self.dim
        y = pos // self.dim
        return (x,y)
    
    def check_legal_pos(self,pos):
        if pos >= 0 and pos < self.size:
            return not self.state[pos]
        else:
            return False
        
    def make_move(self,movepos,player_ID=None):
        if player_ID == None:
            player_ID = self.curr_turn
            
        if player_ID == self.curr_turn:
            if self.check_legal_pos(movepos):
                self.state[movepos] = player_ID
            else:
                raise Exception("Invalid move!")
        else:
            print(player_ID)
            raise Exception("Wrong turn!")
    
    def change_turn(self,curr_turn=None):
        if curr_turn == None:
            curr_turn = self.curr_turn
        
        if curr_turn == 1:
            return 2
        elif curr_turn == 2:
            return 1
        else:
            raise Exception("Unknown player turn")
        return
    
    def get_slices(self):
        vert = [[] for _ in range(self.dim)]
        horiz = [[] for _ in range(self.dim)]
        diag = [[] for _ in range(2)] #always 2 diags
        
        for i in range(0,self.size,self.dim):
            horiz[i//self.dim] =  self.state[i:i+self.dim]
            
            for col in range(self.dim):
                vert[col].append(self.state[i+col])
            
            diag[0].append(self.state[i + i//self.dim ])
            diag[1].append(self.state[i + self.dim - 1 - i//self.dim])
        return vert, horiz, diag
    
    def check_if_won(self,target_player=None):
        if target_player not in [1,2]:
            target_player = self.curr_turn
        targ = [target_player]*self.dim
        
        vert, horiz, diag = self.get_slices()
            
        if targ in vert or targ in horiz or targ in diag:
            return target_player
        elif not any([0 in col for col in vert]):
            return -1 #DRAW
        else:
            return 0
        
    def print_state(self):
        print("Curr turn: ",self.curr_turn)
        print("\n\t ",end="")
        print(*self.state[0:self.dim], sep=" | ")
        
        for i in range(1,self.dim):
            print("\t"+"---"*(self.dim+1))
            print("\t ",end="")
            print(*self.state[i*self.dim:(i+1)*self.dim], sep=" | ")
        print("")
        return
    
    def get_first_empty_square(self):
        test_order = list(range(self.size))
        random.shuffle(test_order)
        for i in test_order:
            if self.state[i] == 0:
                return i
        raise Exception ("No empty squares found!")
        return
    


