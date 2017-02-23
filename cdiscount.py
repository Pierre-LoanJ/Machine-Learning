# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 17:55:07 2015

@author: janczakp
"""
/*
* Description du programme et de l'algorithme
*
* nettoyage des données (transformer en minuscules, sans accent français, ponctuation qui peuvent toucher les mots: 
* parenthèses virgules etc...) suppression des mots non significatifs (le la les du des etc...)
* transformation des mots en singulier (suppresion du s final sauf certains mots comme VHS ou coloris, 
* suppression du x final s'il ne s'agit d'une exception type cheval travail, 
* les exceptions sont gérées dans des cas à part entière)
* comparaison de chaque mot (description + libellé) avec chaque mot des catégories 1, 2 et 3 réunies), 
* un compteur est incrémenté à chaque foi que la comparaison renvoie vrai (sans pondération entre les catégories.
* la classifcation est choisie pour le couple produit-catégorie dont le compteur est le plus élévé. 
* ne gère pas les ex-aequo pour l'instant
*/
                                                                           
import csv
import time


def enleverPluriel(listeDeListeDeMots):
    listeDeListeMotsSingulier = []
    listeSing = []
    for listeDeMots in listeDeListeDeMots:
        listeSing = []
        for mot in listeDeMots:
            if mot == '':
                continue
            elif mot == "vhs":
                continue
            elif mot == "coloris":
                continue
            elif mot == "3ds":
                continue
            elif mot == "chevaux":
                listeSing.append("cheval")
            elif mot == "travaux":
                listeSing.append("travail")
            elif mot == "animaux":
                listeSing.append("animal")
            elif mot == "bocaux":
                listeSing.append("bocal")
            elif mot == "maux":
                listeSing.append("mal")
            elif mot == "mineraux":
                listeSing.append("mineral")
            elif mot == "martiaux":
                continue
            elif mot == "medicaux":
                listeSing.append("medical")
            elif mot == "beaux":
                continue
            elif mot == "postaux":
                listeSing.append("postal")
            else:
                if mot[len(mot) - 1] == 's':
                    mot2 = mot[0:len(mot)-1]
                    listeSing.append(mot2)
                elif mot[len(mot) - 1] == 'x':
                    mot2 = mot[0:len(mot)-1]
                    listeSing.append(mot2)
                else:
                    listeSing.append(mot)
        
        listeDeListeMotsSingulier.append(listeSing)
        
    return listeDeListeMotsSingulier   
    
def raccourcir(listeDeListe):
    listeDeListeLight = []
    listeLight = []
    for liste in listeDeListe:
        listeLight = []
        for word in liste:
            
            if word == '':# ok garder
                continue
            elif word == '&':#ok ne degrade pas
                continue
            elif word == ':':#ok ne degrade pas
                continue
            elif word == '-':# OK ne pas supprimer
                continue
            elif word == '/':#ok ne degrade pas
                continue
            elif word == "...":#ok ne degrade pas
                continue
            elif word == '+':#ok ne degrade pas
                continue
            elif word == 'l':#ok ne degrade pas
                continue
            elif word == 'a':#ne pas supprimer apporte 1%
                continue
            elif word == 'd':#ne pas supprimer, apporte 0.1%
                continue
            elif word == "de":#ne pas supprimer apporte 1.1% et diminue le temps d'execution du coeur par 2
                continue
            elif word == "le":
                continue
            elif word == "la":
                continue
            elif word == "les":
                continue
            elif word == "du":
                continue
            elif word == "des":
                continue
            elif word == "au":
                continue
            elif word == "aux":
                continue
            elif word == "et":
                continue
            elif word == "en":
                continue
            elif word == "avec":
                continue
            elif word == "pour":
                continue
            elif word == "vendu":
                continue
            elif word == "new":#ne degrade pas
                continue
            else:
                listeLight.append(word)
                
        listeDeListeLight.append(listeLight)
    return listeDeListeLight

def nettoyerCategorie(liste):
    
    listeDescription2 = []
    for texte in liste:
        listeDescription2.append(texte.lower())

    listeDescription3 = []
    for des in listeDescription2:
        listeDescription3.append(des.replace('[', ' '))
    del listeDescription2

    listeDescription4 = []
    for des in listeDescription3:
        listeDescription4.append(des.replace(']', ' '))
    del listeDescription3

    listeDescription5 = []
    for des in listeDescription4:
        listeDescription5.append(des.replace('(', ' '))
    del listeDescription4
    
    listeDescription6 = []
    for des in listeDescription5:
        listeDescription6.append(des.replace(')', ' '))
    del listeDescription5
    
    listeDescription7 = []
    for des in listeDescription6:
        listeDescription7.append(des.replace('\'', ' '))
    del listeDescription6
    
    listeDescription8 = []
    for des in listeDescription7:
        listeDescription8.append(des.replace('/', ' '))
    del listeDescription7
    
    
    listeDescription9 = []
    for des in listeDescription8:
        if des[len(des) - 1] == 's':
            des2 = des[0:len(des)-1]
            listeDescription9.append(des2)
        else:
            listeDescription9.append(des)
    
    return listeDescription9

def nettoyerProduit(liste):#prend une liste de string
    
    listeDescription2 = []
    for texte in liste:
        listeDescription2.append(texte.lower())

    listeDescription3 = []
    for des in listeDescription2:
        listeDescription3.append(des.replace('é', 'e'))
    del listeDescription2

    listeDescription4 = []
    for des in listeDescription3:
        listeDescription4.append(des.replace('à', 'a'))
    del listeDescription3

    listeDescription5 = []
    for des in listeDescription4:
        listeDescription5.append(des.replace('è', 'e'))
    del listeDescription4
    
    listeDescription6 = []
    for des in listeDescription5:
        listeDescription6.append(des.replace('ê', 'e'))
    del listeDescription5
    
    listeDescription7 = []
    for des in listeDescription6:
        listeDescription7.append(des.replace('ç', 'c'))
    del listeDescription6
    
    listeDescription8 = []
    for des in listeDescription7:
        listeDescription8.append(des.replace('ù', 'u'))
    del listeDescription7
    
    listeDescription9 = []
    for des in listeDescription8:
        listeDescription9.append(des.replace('ï', 'i'))
    del listeDescription8
    
    listeDescription10 = []
    for des in listeDescription9:
        listeDescription10.append(des.replace('ë', 'e'))
    del listeDescription9
    
    listeDescription11 = []
    for des in listeDescription10:
        listeDescription11.append(des.replace('\'', ' '))
    del listeDescription10
    
    listeDescription12 = []
    for des in listeDescription11:
        listeDescription12.append(des.replace('[', ' '))
    del listeDescription11

    listeDescription13 = []
    for des in listeDescription12:
        listeDescription13.append(des.replace(']', ' '))
    del listeDescription12

    listeDescription14 = []
    for des in listeDescription13:
        listeDescription14.append(des.replace('(', ' '))
    del listeDescription13
    
    listeDescription15 = []
    for des in listeDescription14:
        listeDescription15.append(des.replace(')', ' '))
    del listeDescription14
    
    listeDescription16 = []
    for des in listeDescription15:
        listeDescription16.append(des.replace(',', ' '))
    del listeDescription15
    
    listeDescription17 = []
    for des in listeDescription16:
        listeDescription17.append(des.replace('.', ' '))
    del listeDescription16
    
    listeDescription18 = []
    for des in listeDescription17:
        listeDescription18.append(des.replace('/', ' '))
    del listeDescription17
    
    
    
    return listeDescription18
    
    

def clearList(liste):
    if len(liste) > 0:
        p = len(liste) -1
        while p >= 0:
            liste.remove(liste[p])
            p-=1
    
    return liste

def chercherOcc(listeTextes, mot):#donne le nombre d'occurences du mot
    
    compteur = 0

    for liste in listeTextes:
        if str(liste).lower().find(mot) > 0:
            print str(liste).lower().find(mot)
            compteur +=1
    return compteur
    

""" +++++++++++++++++++++ DEBUT ++++++++++++++++++++++++ """


"""------------ extraction des produits ---------------- """
tps_lecture1 = time.clock()

fichierEntree = "melange_training_1.csv"
file = open(fichierEntree, "r")
reader = csv.reader(file, lineterminator = "\n", delimiter=';')


listeIdProduits = [] # id des produits
listeDescription = []# description
listeLibelle = [] #libelle
listeCat3Confusion = [] # categorie 3 issu des produits pour vérification

for row in reader:
    
    listeIdProduits.append(row[0])# id produit
    listeCat3Confusion.append(int(row[3]))# categorie pour verification
    listeDescription.append(row[4]) # champ description
    listeLibelle.append(row[5]) # champ libellé
del row

file.close()

del fichierEntree, reader, file


""" ------------- extraction des categories de rayons ---------------------"""

fichierEntree2 = "rayon.csv"
file2 = open(fichierEntree2, "r")
reader2 = csv.reader(file2, lineterminator = "\n", delimiter=';')


listeCategorie3 = [] #texte de la categorie 3
listeCategorie2 = [] # texte de la categorie 2
listeCategorie1 = [] #texte de la categorie 1
listeIdCat3 = [] # ID de la categorie 3

for ligne in reader2:
    if ligne[0] == 'Categorie1':
        continue
    else:
        listeCategorie3.append(ligne[5])
        listeCategorie2.append(ligne[3])
        listeCategorie1.append(ligne[1])
        listeIdCat3.append(int(ligne[4]))
del ligne
    
file2.close()

del fichierEntree2, reader2, file2

tps_lecture2 = time.clock()


""" --------------  nettoyage des données produits -------------------- """

tps_clean1 = time.clock()

listeDescriptionPropre = []#en minuscule, sans accent français
listeDescriptionPropre = nettoyerProduit(listeDescription)

listeLibellePropre = []
listeLibellePropre = nettoyerProduit(listeLibelle)


#creer une liste où chaque élément est une liste contenant tous les mots de la 
#description de chaque produit
listeMotsDescription = []#splitté
listeMotsLibelle = []

for descr in listeDescriptionPropre:
    listeMotsDescription.append(descr.split(' '))
del descr

for lib in listeLibellePropre:
    listeMotsLibelle.append(lib.split(' '))
del listeLibellePropre
del lib


listeMotsDescriptionSing = enleverPluriel(listeMotsDescription)

listeMotsLibelleSing = enleverPluriel(listeMotsLibelle)



listeMotsDescriptionLight = []#sans les mots inutiles du genre et le la du des...
listeMotsDescriptionLight = raccourcir(listeMotsDescriptionSing)

listeMotsLibelleLight = []#sans les mots inutiles du genre et le la du des...
listeMotsLibelleLight = raccourcir(listeMotsLibelleSing)



lConcPduit = [] #liste Concatenee des mots Description et Libelle des Produit

for indice, valeur in enumerate(listeMotsDescriptionLight):
    lConcPduit.append(listeMotsDescriptionLight[indice] + listeMotsLibelleLight[indice])



""" --------------  nettoyage des données  catégories -------------------- """




listeCategorie3Propre = []
#convertie les chaines en minuscule
#enlève les caractères qui peuvent toucher les mots
# comme ( ou [ ou / ou '   
listeCategorie3Propre = nettoyerCategorie(listeCategorie3)

listeCategorie2Propre = []
listeCategorie2Propre = nettoyerCategorie(listeCategorie2)

listeCategorie1Propre = []
listeCategorie1Propre = nettoyerCategorie(listeCategorie1)


listeMotsCat1 = []# coupe les chaines en mots
for listeCat1 in listeCategorie1Propre:
    listeMotsCat1.append(listeCat1.split(' '))


listeMotsCat2 = []
for listeCat2 in listeCategorie2Propre:
    listeMotsCat2.append(listeCat2.split(' '))


listeMotsCat3 = []
for listeCat3 in listeCategorie3Propre:
    listeMotsCat3.append(listeCat3.split(' '))

    
del  listeCat3, listeCat2, listeCat1

listeMotsCatSing1 = enleverPluriel(listeMotsCat1)

listeMotsCatSing2 = enleverPluriel(listeMotsCat2)

listeMotsCatSing3 = enleverPluriel(listeMotsCat3)

listeMotsCategorieLight1 = []#enlève les mots non significatifs: avec, et, le, la...
                            # et les caractères pris comme des mots: -, /
listeMotsCategorieLight1 = raccourcir(listeMotsCatSing1)

listeMotsCategorieLight2 = []
listeMotsCategorieLight2 = raccourcir(listeMotsCatSing2)

listeMotsCategorieLight3 = []
listeMotsCategorieLight3 = raccourcir(listeMotsCatSing3)

lConcCat3et2 = [] #liste Concatenee des mots Description et Libelle des Produit
lConcCat123 = []


for indice, valeur in enumerate(listeMotsCategorieLight1):
    lConcCat123.append(listeMotsCategorieLight1[indice] + listeMotsCategorieLight2[indice] + listeMotsCategorieLight3[indice])


tps_clean2 = time.clock()

"""  ---------------  coeur de l'alo avec des dictionnaires --------------- """



dicoProduits = {"IdProduit": listeIdProduits, "listeConcatenee": lConcPduit, "description": listeMotsDescription, "libelle": listeMotsLibelle, "cat3Confusion": listeCat3Confusion}
#id produit, listes de mots description concatenee avec libelle (pour chaque produit), 2 listes servant à construire la concatenation, et la categorie 3 pour verification
dicoCategorie = {"IdCategorie3": listeIdCat3, "texteCategorie": lConcCat123}
# id categorie3, listes de mots de chaque catégorie

del listeIdProduits, listeLibelle
del listeIdCat3, listeMotsCat3


dicoResultat = {"categorie": [], "produit": [], "max": [], "cat3Conf": listeCat3Confusion}
#            categorie predite, id produit, combien de mots ont matché, catégorie 3 pour vérification

del listeCat3Confusion


tps_coeur1 = time.clock()

listeMatchs = [] #contient les nb de matchs pour chaque couple
lcat = []
for ind, prod in enumerate(dicoProduits["listeConcatenee"]):
#prod = liste de mots, dicoProduits["listeConcatenee"] = liste de listes

    nbMatchMeilleurCouple = 0
    clearList(listeMatchs)# RAZ pour chaque nouveau couple
    
    for ray in dicoCategorie["texteCategorie"]:
# ray = liste de mots, dicoCategorie["texteCategorie"] = liste de listes
    
        compteurMatch = 0 #compteur incrémenté quand on retrouve le même mot
                          #dans le texte produit et dans le texte categorie.
                          # compteur remis à zéro pour toute nouvelle catégorie.
                          #compare donc les couples produit-catégorie.
        
        for mot in prod:#pour chaque mot du texte produit
            for mot2 in ray:#pour chaque mot pareil mais du texte catégorie
                if (mot == mot2):
                    compteurMatch +=1
                       
        lcat.append(ray)#retient la position des couples en les sauvegardant dans lcat
        listeMatchs.append(compteurMatch)#liste du nbre de match pour chaque couple
     
    nbMatchMeilleurCouple = max(listeMatchs)#nb matchs du meilleur couple
    indexMeilleurCouple = listeMatchs.index(max(listeMatchs))#position du meilleur couple
    
    dicoResultat["max"].append(nbMatchMeilleurCouple)#inutile
    dicoResultat["produit"].append(dicoProduits["IdProduit"][ind])#inutile, doit garder l'id
    dicoResultat["categorie"].append(dicoCategorie["IdCategorie3"][indexMeilleurCouple])
    
del prod, ray, mot, mot2, lcat

tps_coeur2 = time.clock()

""" - ecriture du fichier de sortie  et calcul de la matrice de confusion - """

tps_ecriture1 = time.clock()

res = "fichierResultat7.csv"
file = open(res, "w")
writer = csv.writer(file, lineterminator = "\n", delimiter=';')
writer.writerow(("Id_Produit",';',"Id_Categorie"))

confusion = 0
i =0
for ligne in dicoResultat["produit"]:

    writer.writerow((dicoResultat["produit"][i],';', dicoResultat["categorie"][i]))
    #  id_produit,   categorie predite 
    
    if dicoResultat["categorie"][i] == dicoResultat["cat3Conf"][i]:
        confusion +=1

    print "\r"
    print "Le produit ", dicoResultat["produit"][i], "est classé par l'algorithme dans la catégorie: ", dicoResultat["categorie"][i]," , "
    print "sa vraie catégorie est ", dicoResultat["cat3Conf"][i]
    print "\r"
   
    i+=1

file.close()

""" ----------------  matrice de confusion    -----------------------  """

nbProd = 52

print "score de confusion = " , confusion, ", soit ", float(confusion)/nbProd*100, " % de bonnes prédictions."

tps_ecriture2 = time.clock()

print "lecture: ", tps_lecture2 - tps_lecture1
print "cleaning : ", tps_clean2 - tps_clean1
print "coeur : ", tps_coeur2 - tps_coeur1
print "ecriture: ", tps_ecriture2 - tps_ecriture1

