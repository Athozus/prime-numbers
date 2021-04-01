from math import ceil
from time import time

def primesNb(max, show=True):
    if show:
        time1 = time()
        n = 0
        nbs = [True] * max + [True]
        for i in range(2, max):
            if nbs[i]:
                print(i)
                n +=1
                for j in range(i*2, max, i):
                    nbs[j] = False
    else:
        time1 = time()
        n = 0
        nbs = [True] * max + [True]
        for i in range(2, max):
            if nbs[i]:
                n +=1
                for j in range(i*2, max, i):
                    nbs[j] = False
    print("Examinated: " + str(max))
    print("Primes: " + str(n))
    print("Percentage : " + str(ceil(n/max*1000)/1000) + " %")
    print("Exec time : " + str(time()-time1) + "(" + str(((max/(time()-time1)*1000)/1000)) + " / s)")
