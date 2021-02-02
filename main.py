import math
import random
HISMAX = 40257
HISMIN = 391
GIVE = 20

class tempSeq:
    def __init__(self, seq = [], day='0000-00-00'):
        self.day = day
        self.seq = seq

    def add(self, toAdd = (0,0)):
        self.seq.append(toAdd)

    def toString(self):
        for i in range(len(self.seq)):
            print("t"+str(i)+"---")
            print(self.seq[i][0])
            print(self.seq[i][1])

class tokens:
    def __init__(self, ta = 0, tb = 0)

myseq = tempSeq()
        
for i in range(20000):
    n = random.randint(HISMIN,HISMAX)
    pa = random.randint(n-GIVE, n+GIVE)
    pb = random.randint(n-GIVE, n+GIVE)
    myseq.add(tuple((pa,pb)))

 
