# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 03:58:43 2020

@author: Antiochian
"""
from board import Board
from random_player import Random_Player
from defensive_player import Defensive_Player
from aggressive_player import Aggressive_Player
from flexible_player import Flexible_Player
from suicidal_player import Suicidal_Player
from perfect_player import Perfect_Player


from manual_player import Manual_Player

import time

def display_outcome(ended):
    if ended == 1:
        print("Player 1 wins!")
    elif ended == 2:
        print("Player 2 wins!")
    elif ended == -1:
        print(" -- DRAW --")
    else:
        raise Exception("Invalid endstate")

        
def main(models,dim=3,verbose = False):
    players = (None, models[0], models[1])
    ended = False
    game = Board(dim,1)
    game.curr_turn = game.change_turn()
    while not ended:
        game.curr_turn = game.change_turn()
        current_player = game.curr_turn
        proposed_move = players[current_player].make_move(game)
        if verbose:
            print("Player ",current_player, "'s Turn:")
            game.print_state()
        game.make_move(proposed_move,current_player)
        ended = game.check_if_won()
    return ended
        

def round_robin(playerlist,runs,dim=3,points=False,verbose=False):
    print("Running...")
    t0 = time.time()
    num_of_players = len(playerlist)
    num_of_matchups = num_of_players**2
    if points:
        sq_length = 11
    else:
        sq_length = 16
    namelist = [pl.name[:sq_length-1].center(sq_length) for pl in playerlist]
    scoretable = [ [0]*num_of_players for _ in range(num_of_players)]
    count = 0
    for i in range(num_of_players):
        for j in range(num_of_players):
            players = (playerlist[i], playerlist[j])
            results = [None,0,0,0]
            score = 0
            for t in range(runs):
                trial = main( players,dim)
                results[trial] += 1
                #POINTS SYSTEM:
                if trial == 1: #if you win
                    score += 1
                elif trial == 2: #if you lose
                    score += -1
                elif trial == -1: #if you draw
                    score += 1
            if points:
                scoretable[i][j] = str(round(score / runs,2))[:sq_length-1].center(sq_length)
            else:
                scoretable[i][j] = (str(round(results[1] / runs,2))+"/"+str(round(results[2] / runs,2))+"/"+str(round(results[-1] / runs,2)) )[:sq_length-1].center(sq_length)
            count += 1
            print("\r",count,"/",num_of_matchups," matchups completed (",runs," games each )",end="")
    print("\nTotal time taken: ",round(time.time()-t0,3)," seconds\n")
    print(" "*sq_length,*namelist,"",sep="|") #print header
    print(("-"*sq_length+"|")*(1+num_of_players))
    for i in range(num_of_players): #print each result now
        print(namelist[i],*scoretable[i],"",sep="|")

    if points:
        return scoretable, namelist
    else:
        return 1,1

def sample_game(players,dim=3,verbose=True):
    ended = main( players,dim,verbose)
    print("------- GAME OVER ---------")
    display_outcome(ended)
    return


if __name__ == "__main__":
    all_players = []
    all_players.append(Suicidal_Player("Suicidal"))
    all_players.append(Random_Player("Random"))
    all_players.append(Defensive_Player("Defensive"))
    all_players.append(Aggressive_Player("Aggressive"))
    all_players.append(Flexible_Player("Flexible"))
    all_players.append(Perfect_Player("Perfect"))
    scoretable, namelist = round_robin(all_players,10,dim=3,points = False)


#sample_game((Perfect_Player("Henry"),Perfect_Player("Flexible")),dim=3,verbose=False)