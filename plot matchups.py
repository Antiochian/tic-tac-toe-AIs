# -*- coding: utf-8 -*- python3
"""
Created on Tue Mar 10 07:07:51 2020

@author: Antiochian
"""

import matplotlib.pyplot as plt
import numpy as np
from driver import *

if __name__=="__main__":
    all_players = []
    all_players.append(Suicidal_Player("Suicidal"))
    all_players.append(Random_Player("Random"))
    all_players.append(Defensive_Player("Defensive"))
    all_players.append(Aggressive_Player("Aggressive"))
    all_players.append(Flexible_Player("Flexible"))
    all_players.append(Perfect_Player("Perfect"))
    strscoretable, namelist = round_robin(all_players,100,dim=3,points = True)
else:
    namelist = [' Suicidal', '  Random ', ' Defensive', ' Aggressive', ' Flexible', ' Perfect ']
    strscoretable = [['   0.68  ', '   0.02  ', '   0.34  ', '  -0.26  ', '  -0.44  ', '  -0.88  '], ['   0.84  ', '   0.4   ', '   0.36  ', '   0.02  ', '   0.0   ', '  -0.76  '], ['   0.94  ', '   0.7   ', '   0.46  ', '   0.68  ', '   0.3   ', '  -0.22  '], ['   0.86  ', '   0.64  ', '   0.4   ', '   0.56  ', '  -0.02  ', '  -0.84  '], ['   0.92  ', '   0.82  ', '   0.54  ', '   0.92  ', '   0.3   ', '  -0.08  '], ['   1.0   ', '   1.0   ', '   1.0   ', '   1.0   ', '   1.0   ', '   1.0   ']]
scoretable = [list(map(float,sublist)) for sublist in strscoretable]
#[sub.reverse() for sub in scoretable]
scoretable = np.array(scoretable)
#scoretable = scoretable.transpose()
xlab = namelist.copy()
ylab = namelist.copy()

# We want to show all ticks...
fig, ax = plt.subplots()
im = plt.imshow(scoretable, cmap='RdYlGn')
ax.set_xticks(np.arange(len(namelist)))
ax.set_yticks(np.arange(len(namelist)))
# ... and label them with the respective list entries
ax.set_xticklabels(xlab)
ax.set_yticklabels(ylab)

# Rotate the tick labels and set their alignment.

ax.xaxis.tick_top()
plt.setp(ax.get_xticklabels(), rotation=335, ha="right",
         rotation_mode="anchor")
# Loop over data dimensions and create text annotations.
for i in range(len(namelist)):
    for j in range(len(namelist)):
        text = ax.text(j, i, scoretable[i][j],
                       ha="center", va="center", color="black")

ax.set_title('Performance of competing Tic Tac Toe algorithms', fontsize=14, fontweight='bold')
ax.set_xlabel("(Value is the lefthand player's ratio of wins OR draws against losses)")
fig.tight_layout()
plt.show()