# tic-tac-toe-AIs
Implementation and comparison of six AI strategies for the game of tic-tac-toe.

A simple wrapper for the game of Tic-Tac-Toe, with 6 basic algorithms already included. I hope to use this program as a test metric for a later machine learning project.

At the moment, the AI strategies are:
 - Suicidal: Actively avoids winning the game as much as it can
 - Random: Makes random (legal) moves
 - Defensive: Makes random moves unless it is directly threatened with a loss in the next turn from 2-in-a-row
 - Aggressive: Makes random moves unless it can see an opportunity to win in the next turn with a 2-in-a-row
 - Flexible: Switches between the previous "Defensive" and "Aggressive" modes based on the situation
 - Perfect: A minimax algorithm with alpha-beta pruning that should in theory never lose a game
 
 A round-robin tournament gives the following matchup results:
 |Results|(36000 total games)|
 |:---:|:---:|
 | ![Greedy](greedy_matchups.png)|![Safe](safe_matchups.png)   |
 |"Greedy" tournament (draws count as a loss)| "Safe" tournament (draws count as a win)|
