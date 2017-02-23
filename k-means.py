# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:10:54 2015

@author: janczakp
"""

from math import sqrt
from random import randrange, random
import matplotlib.pyplot as plt

class point:

    def __init__(self, x, y, classification):
        self.x = x
        self.y = y
        self.classification = classification

def affichageBicolore(liste, CentroidR, CentroidB):
    listeXR = []
    listeYR = []
    listeXB = []
    listeYB = []
    for elem in listeP:
        if elem.classification == 'R':
            listeXR.append(elem.x)
            listeYR.append(elem.y)
            plt.plot(listeXR, listeYR, 'ro')
        elif elem.classification == 'B':
                listeXB.append(elem.x)
                listeYB.append(elem.y)
                plt.plot(listeXB, listeYB, 'wo')
    plt.plot(CentroidB.x, CentroidB.y, 'co')
    plt.plot(CentroidR.x, CentroidR.y, 'mo')
    plt.show()
    plt.close

def calculerCentroid(centroid, liste):
    xMoy = 0
    yMoy = 0
    n = 0
    for element in liste:
        if centroid.classification == element.classification:
            xMoy = xMoy + element.x
            yMoy = yMoy + element.y
            n += 1
    xMoy = xMoy / n
    yMoy = yMoy / n
    centroid.x = xMoy
    centroid.y = yMoy
    return centroid

def prepareDonnees():
       listeP = []
       i = 0
       
       while i < 59:
           nbX = randrange(0, 10)+random()
           nbY = randrange(0, 10)+random()
           P = point(nbX, nbY, '')
           listeP.append(P)
           i += 1
       return listeP
        
def calculerCluster(listeP, CentroidR, CentroidB):
    #calcul des distances par rapport à CentroidR et B
    listePointsAppris = []
    for indice, element in enumerate (listeP):
        distanceR = sqrt((CentroidR.x - element.x)**2 +(CentroidR.y - element.y)**2)
        distanceB = sqrt((CentroidB.x - element.x)**2 +(CentroidB.y - element.y)**2)
        if distanceR <= distanceB:
            element.classification = 'R'
        elif distanceB < distanceR:
            element.classification = 'B'     
        listePointsAppris.append(element)
    listeP = []
    listeP = listePointsAppris
    return listeP
    
def compterPoints(listeP):
    compteur = 0
    for elem in listeP:
        if elem.classification == 'R':
            compteur +=1
        else:
            continue
    return compteur

CentroidR = point(randrange(0, 10)+random(), randrange(0, 10)+random(), 'R')
CentroidB = point(randrange(0, 10)+random(), randrange(0, 10)+random(), 'B')


#etape preliminaire
listeP = prepareDonnees()
for elem in listeP:
    print"elem: ",elem, " X = ",elem.x, " Y = ",elem.y
    #affiche la liste des coordonnées
listeX = []
listeY = []
for elem in listeP:
    listeX.append(elem.x)
    listeY.append(elem.y)
    plt.plot(listeX, listeY, 'bo')
plt.plot(CentroidB.x, CentroidB.y, 'co')
plt.plot(CentroidR.x, CentroidR.y, 'mo')
plt.show()
plt.close#affiche les points avant d'être classés et les 2 centroids

j = 0
refXR = CentroidR.x
listeP = calculerCluster(listeP, CentroidR, CentroidB)
CentroidR = calculerCentroid(CentroidR, listeP)

while refXR != CentroidR.x:
    refXR = CentroidR.x
    listeP = calculerCluster(listeP, CentroidR, CentroidB)# attribution couleurs
    
    affichageBicolore(listeP, CentroidR, CentroidB)
    
    CentroidR = calculerCentroid(CentroidR, listeP)
    CentroidB = calculerCentroid(CentroidB, listeP)
    
    affichageBicolore(listeP, CentroidR, CentroidB)
    print "R: ",compterPoints(listeP), "   B: ",59- compterPoints(listeP)
    print"R",CentroidR.x, CentroidR.y, " et B ", CentroidB.x, CentroidB.y  
    j += 1
    
