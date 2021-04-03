from math import ceil, sqrt
from time import time

def primesNb(max, show=True):
    time1 = time()
    n = 0
    try:
        if max < 1024:
            print(1/0)
        nbs = [True] * max + [True]
        if show:
             for i in range(2, max):
                if nbs[i]:
                    print(i)
                    n +=1
                    for j in range(i*2, max, i):
                        nbs[j] = False
        else:
            for i in range(2, max):
                if nbs[i]:
                    n +=1
                    for j in range(i*2, max, i):
                        nbs[j] = False
    except:
        if show:
            for i in range(1, max):
                prime = True
                if i == 2:
                    pass
                elif i%2 == 0:
                    prime = False
                else:
                    for j in range(1, ceil(sqrt(max)), 2):
                        if i%j == 0:
                            prime = False
                            break
                if prime:
                    n += 1
                    print(i)
        else:
            for i in range(1, max):
                prime = True
                if i == 2:
                    pas
                elif i%2 == 0:
                    prime = False
                else:
                    for j in range(1, ceil(sqrt(max)), 2):
                        if i%j == 0:
                            prime = False
                            break
                if prime:
                    n += 1
    print("Examinated: " + str(max))
    print("Primes: " + str(n))
    print("Percentage : " + str(ceil(n/max*1000)/1000) + " %")
    print("Exec time : " + str(time()-time1) + "(" + str(((max/(time()-time1)*1000)/1000)) + " / s)")
