import numpy as np
import random

class train:
    def __init__(self, maxEpochs, tileArray):
        self.states = 100
        self.actions = 4
        self.goalState = 100
        self.QTable = np.zeros((self.states,self.actions))

        self.discount = 0.95
        self.learnRate = 0.85

        self.maxExplorationProb = 1
        self.minExplorationProb = 0.00
        self.decayFactor = 0.01

        self.maxEpochs = maxEpochs
        self.epoch = 0
        self.episode = 0
        self.steps = 0

        self.tileArray = tileArray
    

    def printQTable(self):
        print(self.QTable)

    def nextEpisode(self):
        self.episode +=1
        
        print(self.episode,"-",self.steps)
        self.steps=0

    def chooseAction(self, playerPos):
        self.action = 0
        self.prevPlayerPos = playerPos
        self.gridPos = []
        self.gridPos.append(playerPos%12)
        self.gridPos.append(playerPos//12)
        self.currentState = self.gridPos[0]-1 + (self.gridPos[1]-1) * 10
        explorationProb = self.minExplorationProb + (self.maxExplorationProb - self.minExplorationProb)* np.exp(-self.decayFactor*self.episode)
        self.steps += 1
        if random.uniform(0,1) < explorationProb:
            self.action = random.randint(1,self.actions)
        else:
            self.action = np.argmax(self.QTable[self.currentState])+1
        if self.steps > 132:
            self.action = -1
        return self.action

    def updateQTable(self, playerPos):
        self.prevPos = self.currentState
        self.gridPos = []
        self.gridPos.append(playerPos%12)
        self.gridPos.append(playerPos//12)
        self.currentState = self.gridPos[0]-1 + (self.gridPos[1]-1) * 10
        if self.tileArray[playerPos].cellType == "G":
            self.reward = 1000
            self.nextEpisode()
        elif self.tileArray[playerPos].cellType == " ":
            self.reward = -0.5
        elif self.tileArray[playerPos].cellType == "O":
            self.reward = -1000
            self.nextEpisode()
        else:
            self.reward = 0
            print("whoops")
        self.QTable[self.prevPos][self.action-1] = self.QTable[self.prevPos][self.action-1] + \
            self.learnRate * (self.reward + self.discount * np.max(self.QTable[self.currentState]) - self.QTable[self.prevPos][self.action-1])
        self.tileArray[self.prevPlayerPos].weight = np.average(self.QTable[self.prevPos])