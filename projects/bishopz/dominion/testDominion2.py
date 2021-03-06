# -*- coding: utf-8 -*-
"""
Created on  Oct 16 20:16:00 2020

@author: bishopz
"""

import Dominion
import random
import testUtility
from collections import defaultdict

# Get player names
player_names = ["Annie","*Ben","*Carla"]

# Set number of Victory and Curse cards
(nV, nC) = testUtility.setVictoryCurse(len(player_names))

# Initialize the box
box = testUtility.boxInit(nV)


supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

# Define what cards will be in the supply for this game
supply = testUtility.supplyInit(box, nV, nC, len(player_names))

# Initialize the trash
trash = []

# Set up test data
supply["Thief"] += [Dominion.Thief()] * 10

# Construct the player objects
players = testUtility.playerInit(player_names)

# Play the game
testUtility.play(supply, supply_order, players, trash)

# Print winners
testUtility.finalize(players)
