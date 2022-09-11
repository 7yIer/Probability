from GlobalHistory import GlobalHistory 
from GlobalCounter import GlobalCounter


class Probability:
    def __init__(self):
        self.GlobalHistory = GlobalHistory()
        self.GlobalCounter = GlobalCounter()
    def calculateProbability(self, cords, moveNumber):
        moveWinCount = self.GlobalHistory.getMove(cords, moveNumber)
        totalCount = self.GlobalCounter.getCount(cords, moveNumber)

        return moveWinCount / totalCount
    def reset(self):
        self.GlobalHistory.reset()
        self.GlobalCounter.reset()
    def log(self, cords, index):
        self.GlobalHistory.logMove(cords, index)
        self.GlobalCounter.logCount(cords, index)

p = Probability()
p.log("00", 0)