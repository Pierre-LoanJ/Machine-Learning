# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:41:40 2015

@author: janczakp
"""

from math import sqrt
import matplotlib.pyplot as plt

class point:

    def __init__(self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification

def calculerDistance(listeP, I):
    listeD = []
    for indice, element in enumerate (listeP):
        distance = sqrt((I.x-element.x)**2 +(I.y-element.y)**2)
        #print("point:",listeP[indice]," distance:",distance )
        listeD.append([distance, element.classification])
    return listeD
    
def trierListe(listeD):
    temp =  0
    j = 0
    while j < len(listeD)-1:
        i = 0
        while i < len(listeD)-1:
            if listeD[i] > listeD[i+1]:
                temp = listeD[i+1]
                listeD[i+1] = listeD[i]
                listeD[i] = temp
                i+=1
            else:
                i+=1
        j+=1
    return listeD

def compterOccurrence(listeDtriee):
    k = 3
    compteurA = 0
    compteurB = 0
    for dist, classe in enumerate(listeDTriee):
        if k <3:
            if classe == 'A':
                compteurA +=1
                k+=1
            elif classe == 'B':
                compteurB +=1
                k+=1
        else:
            break
    if compteurA > compteurB:
        return 'A'
    else:
        return 'B'
    
P1 = point(1, 5, 'A')
P2 = point(2, 7, 'A')
P3 = point(3, 6, 'A')
P4 = point(4, 1, 'B')
P5 = point(5, 4, 'B')
P6 = point(6, 3, 'B')
P7 = point(7, 2, 'B')
I = point (3.5, 3.5, '')

#print("description de x", I.x, I.y, I.classification )

listeP = [P1, P2, P3, P4, P5, P6, P7]
listeD = []
listeDTriee = []
listeD = calculerDistance(listeP,I)
print ("liste avant tri",listeD)
listeDTriee = trierListe(listeD)
print ("liste apres tri",listeDTriee)
I.classification = compterOccurrence(listeDTriee)
print("I est de classification",I.classification)

listeX = []
listeY = []
for elem in listeP:
        listeX.append(elem.x)
        listeY.append(elem.y)

plt.plot(listeX, listeY, 'ro')
plt.plot(I.x, I.y, 'ro')
plt.axis(-10,10,-10,10)
plt.show()
