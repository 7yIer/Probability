from firebase_admin import db


import firebase_admin
from firebase_admin import credentials

class GlobalCounter:
    def __init__(self):
        self.startingState = db.reference("Counter").get()
    def getCount(self, cords, moveNumber):
        r = db.reference("Counter")
        s = r.get()
        index = moveNumber - 1
        return s[index][cords]
    def logCount(self, cords, index):
        r = db.reference("Counter")
        s = r.get()

        if s is None:
            s = {}
            s[index] = 1
        else:
            while index >= len(s):
                s.append(0)
            

            s[index] = s[index] + 1

        
        r.set(s)
    def decrementCount():
        r = db.reference("Counter")
        s = r.get()

        if s is None:
            return
        else:
            r.set(s - 1)
    def reset(self):
        db.reference("Counter").set(self.startingState)

