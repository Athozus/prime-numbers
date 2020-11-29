from math import sqrt, ceil
from time import time

def primesNb(maxI, minI=2, show=False):
    if show:
        time1 = time()
        n = 0
        for i in range(minI, maxI):
            premier = True
            for j in range(2, ceil(sqrt(i))):
                if i%j==0:
                    premier = False
                    break
            if premier:
                n +=1
                print(i)
    else:
        time1 = time()
        n = 0
        for i in range(minI, maxI):
            premier = True
            for j in range(2, ceil(sqrt(i))):
                if i%j==0:
                    premier = False
                    break
            if premier:
                n +=1

    timeExe = time()-time1
    print("Fin des calculs")
    print("Nombres testés : " + str(maxI) + " (" + str(ceil(maxI/timeExe*1000)/1000) + "/s)")
    print("Nombres premiers : " + str(n))
    print("Pourcentage : " + str(ceil(n/maxI*100000)/1000) + " %")
    print("Temps d'exécution : " + str(ceil(timeExe*1000)/1000) + " s")
