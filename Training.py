import numpy as np
import random

class train:
    def __init__(self, maxEpochs, tileArray):
        self.states = 100
        self.actions = 4
        self.goalState = 100
        self.QTable = np.zeros((self.states,self.actions))

        self.discount = 0.85
        self.learnRate = 0.85
        self.explorationProb = 0.27

        self.maxEpochs = maxEpochs
        self.epoch = 0

        self.tileArray = tileArray
    

    def chooseAction(self, playerPos):
        self.action = 0
        self.currentState = playerPos
        if random.uniform(0,1) < self.explorationProb:
            self.action = random.randint(1,self.actions)
        else:
            self.action = np.argmax(self.QTable[(self.currentState//12)+1])
        return self.action

    def updateQTable(self):
        pass
