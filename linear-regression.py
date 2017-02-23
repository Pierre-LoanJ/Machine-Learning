# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:35:04 2015

@author: janczakp
"""

/*
* This program is an application of linear regression model using the least squares method
*/

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def Tracer(listeX, listeY, a, b):
    #print(listeTemp)
    absX = np.linspace(0,10,100)
    ordY = a*absX + b
    plt.plot(listeX, listeY, 'bo')
    plt.plot(absX,ordY,'b')
    plt.axis(-10,10,-10,10)
    plt.show()

def Moyenne(liste):
    moy = np.mean(liste)
    return moy

    
P1 = point(1, 2)
P2 = point(2, 3.5)
P3 = point(3, 4)
P4 = point(4, 4)
P5 = point(5, 5)
P6 = point(6, 12)
P7 = point(7, 11)

listeP = [P1, P2, P3, P4, P5, P6, P7]
listeX = []
listeY = []
for elem in listeP:
        listeX.append(elem.x)
        listeY.append(elem.y)


"""a partir du fichier"""
listeXfile = []
listeYfile = []
fichier = open("C:/python/liste de points.csv","r")
for indice,ligne in enumerate(fichier):
    if indice == 0:
        print " 1ere ligne"
    elif indice > 0:    
        print(ligne)
        l = ligne.rstrip('\n')
        s = l.split(';')
        listeXfile.append(s[1])
        listeYfile.append(s[2])
        
for indice, element in enumerate(listeXfile):
    listeXfile[indice] = int(element)
for indice, element in enumerate(listeYfile):
    listeYfile[indice] = int(element)


"""calcul de la regression et representation du graphique"""
Xmoy = Moyenne(listeXfile)
Ymoy = Moyenne(listeYfile)
covariance = np.cov(listeXfile, listeYfile)[0][1]
variance = np.var(listeXfile)
varY = np.var(listeYfile)
coefCorrLin = covariance / (sqrt(variance)*sqrt(varY))
a = covariance/variance
b = Ymoy -a*Xmoy
print "correlation lineaire: ",coefCorrLin
Tracer(listeXfile, listeYfile, a, b)


#print Xmoy
#print Ymoy
#print "cov: %f" %covariance
#print "variance %f" %variance
