from math import sqrt, ceil
from time import time

input("Le programme va calculer les nombres premiers. Appuyez sur Entrée pour démarrer.")
print("Début des calculs")

time1 = time()

maxI = 10**18+1000
n = 0
last = 2

for i in range(10**18-1,maxI+1,2):
    premier = True
    for j in range(2,ceil(sqrt(maxI))):
        if i%j == 0:
            premier = False
            break
    if premier:
        n += 1
        last = i
        print(i)

time = time()-time1
print("Fin des calculs")
print("Nombres testés : " + str(maxI) + " (" + str(ceil(maxI/time*1000)/1000) + "/s)")
print("Nombres premiers : " + str(n))
print("Pourcentage : " + str(ceil(n/maxI*100000)/1000) + " %")
print("Temps d'exécution : " + str(ceil(time*1000)/1000) + " s")
