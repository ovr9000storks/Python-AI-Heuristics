# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import math

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #print("SCORES: " + str(scores))
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        #print("BEST NEXT MOVE SCORE: " + str(bestScore))
        #print("BEST INDICES: " + str(bestIndices))
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        #print("CHOSEN MOVE: " + str(chosenIndex) + "\n")
        

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]


    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        
        previousFood = currentGameState.getFood().asList()
        allFood = newFood.asList()
        nearestFoodScore = 0

        foodDistances = []
        for pos in allFood:
            foodDistances.append(manhattanDistance(newPos, pos))

        #print(action + " DISTANCES: " + str(foodDistances))
        stopPenalty = 0
        if(currentGameState.getPacmanPosition() == successorGameState.getPacmanPosition()):
            stopPenalty = -100
        
        if len(previousFood) - len(allFood) == 1:
            nearestFoodScore = 600
        elif len(foodDistances) > 1:
            minDistance = min(foodDistances)
            nearestFoodScore = 500 - minDistance
        
        ghostProxScore = 0
        nearestGhostPos = successorGameState.getGhostPositions()[0]
        nearestGhostDist = manhattanDistance(newPos, nearestGhostPos)
        
        
        if nearestGhostDist <= 2:
            #run from the ghost if nearby
            return -999999
        
        return ghostProxScore + successorGameState.getScore() + nearestFoodScore + stopPenalty

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

