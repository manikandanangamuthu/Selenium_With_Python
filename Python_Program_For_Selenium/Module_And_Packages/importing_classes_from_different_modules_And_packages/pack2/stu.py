class Student:

    def __init__(self, sid, sname, ssal):
        self.sid = sid
        self.sname = sname
        self.ssal = ssal

    def displayemp(self):
        print(self.sid, self.sname, self.ssal)