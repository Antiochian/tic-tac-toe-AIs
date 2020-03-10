# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 05:17:05 2020

@author: Antiochian
"""

class Manual_Player:
    def __init__(self,name):
        self.name = name
        
    def make_move(self,board):
        board.print_state()
        accepted = False
        while not accepted:
            print("YOUR TURN (Player ",board.curr_turn,")")
            choice = int(input("\t>Enter choice: "))
            if board.check_legal_pos(choice):
                accepted = True
            else:
                print("Invalid move! Try again.")
                
        return choice
#        while not accepted:
#            print("YOUR TURN (Player ",board.curr_turn,")")
#            choice = int(input("\tEnter choice: "))
#            if 0 <= choice < board.size:
#                coords = board.pos_to_coord(choice)
#                print("Selection coords: ",coords)
#                conf = input("Confirm? (Y/N) ")
#                if conf.lower == "y":
#                    if board.check_legal_pos(choice):
#                        accepted = True
#                    else:
#                        print("Invalid choice, try again")
#            else:
#                print("Selection out of range. Try again.")
#        board.print_state()
#        return choice