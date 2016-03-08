import random


f = open ('points.txt','w')
for i in range (1000):
    a = random.uniform(-100,100)
    b = random.uniform (-100,100)
    f.write (str(a)+" "+str(b))
    f.write ("\n")

f.close()
