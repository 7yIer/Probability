import time
from firebase_admin import db


import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate('./serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
'databaseURL': 'https://XXX.firebaseio.com/'
})

class GlobalHistory:
    def __init__(self):
        self.startingState = db.reference().get()
    def logMove(self, cords, index):

        r = db.reference("History")
        s = r.get()
        if s is None:
            s = [{ cords : 1}]
        else:
            while index >= len(s):
                s.append({ cords : 0 })
            s[index][cords] = s[index][cords] + 1

        r.set(s)
        time.sleep(2)
    def getMove(self, cords, index):
        r = db.reference("History")
        s = r.get()
        return s[index][cords]
    def reset(self):
        db.reference("History").set(self.startingState)
