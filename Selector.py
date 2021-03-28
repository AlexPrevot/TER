# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:23:27 2021

@author: User
"""
from math import *
from Error import error

from random import seed
from random import randint

import random

import numpy as np



import myModule


#note : changer le deuxième for car complexité de n², on peut transformer en n
def crossOverPath3(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPathCO.append(tabPath1[i])

    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPathCO:
            newTabPathCO.append(tabPath2[i])

    return newTabPathCO


def crossOverPath3(nbr,path1, path2):
    child = []
    seen = []
    temp = [-1]*len(path1)
    miss = []
    
    l = len(path1)
    for i in range(0,l,2):
        if i < l:
            child.append(path1[i])
        if i+1 < l:
            child.append(path2[i+1])
    
    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child


#note : sous forme n et non n^2
def crossOverPath(nbr,path1, path2):
    #child from the cross_over
    child=path2.copy()
    #tab of already present values (but only their coordinates)
    seen=[]
    temp = [-1]*len(path1)
    #tab of missing value in the order of path2
    miss = []
    
    #copy piece of path1 in path2
    for i in range(nbr):
        child[i] = path1[i]

    #find already seen value
    for i in range(len(temp)):
        if temp[child[i]] == -1:
            temp[child[i]] = i
        else:
            seen.append(i)
    
    for i in range(len(temp)):
        if temp[path2[i]] == -1:
            miss.append(path2[i])
    
    for i in range(len(seen)):
        child[seen[i]] = miss[i]
    
    return child	


#crossover ERO 
def matriceConversion(path1,path2):
    mat1 = [-1]*len(path1)
    mat2 = [-1]*len(path2)
    matFinal = []
  
    #mat1[path1[0]] = [path1[len(path1)-2],path1[1]]
    #mat2[path2[0]] = [path2[len(path2)-2],path2[1]]
    
    #mat1.append([path1[len(path1)-1],path1[1]])
    #mat2.append([path2[len(path2)-1],path2[1]])
    
    for i in range(len(path1)):
        if i== (len(path1))-1:
            #mat1.append([path1[len(path1)-1],path1[0]])
            #mat2.append([path2[len(path2)-1],path2[0]])
            mat1[path1[i]] = [path1[len(path1)-2],path1[0]]
            mat2[path2[i]] = [path2[len(path2)-2],path2[0]]
            
        else :
            #mat1.append([path1[i],path1[i+1]])
            #mat2.append([path2[i],path2[i+1]])
            mat1[path1[i]] = [path1[i-1],path1[i+1]]
            mat2[path2[i]] = [path2[i-1],path2[i+1]]
  
    for i in range(len(path1)):
        matFinal.append(matriceUnion(mat1[i], mat2[i]))
    
    
    
    print("matrice 1")
    print (mat1)
    
    print("matrice 2")
    print (mat2)
    
    print("matrice Final")
    print (matFinal)
    
            
            
def matriceUnion(mat1,mat2):
    final_mat = list(set(mat1) | set(mat2))
    return final_mat




def crossOverLoop(nbrPath, tab):
    crossedTabs = []
    iteration = 0
    for i in range(nbrPath - len(tab)):
        for j in range(i,len(tab)):
            if(iteration + len(tab) < nbrPath):                
                iteration += 1
                crossedTabs.append(
                                    crossOverPath(floor(len(tab[0])/2),tab[i],tab[j]))
            else:
                if crossedTabs:
                    return crossedTabs
                else:
                    error("Le cross_over ne s'est fait pas fait")
    return crossedTabs
        

#mutation d'un chemin
def mutationPath(tabPath):
    element1 = randint(0 , len(tabPath)-1)
    element2 = randint(0 , len(tabPath)-1)
    swapPositions(tabPath, element1, element2)
    return tabPath



def mutationLoop(tab):
    for i in range(len(tab)):
        if randint(0,4) > 3:
            tab[i] = mutationPath(tab[i])
    return tab

# Swap function 
def swapPositions(tab, pos1, pos2):
    tab[pos1], tab[pos2] = tab[pos2], tab[pos1] 





def selectionPath(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    
    
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    generation = 0
    bestScore = float('inf')
    iteration = 0
    
    print("Chemin initial")
    print (tabPath[0][0])
    print (tabPath[1][0])
    matriceConversion(tabPath[0][0] , tabPath[1][0])
    
    
    while (iteration < 30):
        generation += 1
        tabPath.sort(key=lambda x:x[1])
        
        tabBestPath = []
        
        for i in range(bestElementsSize):
            tabBestPath.append(tabPath[i][0])

        
        genCrossed = crossOverLoop(nbrPath, tabBestPath)
        genMutated = mutationLoop(tabBestPath[1:])
        
        tabBestPath = genMutated + genCrossed
        
        tabPath = []
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
        
        if tabPath[0][1] < bestScore:
            iteration = 0
            bestScore = tabPath[0][1]
        else:
            iteration +=1
    
    
    tabPath.sort(key=lambda x:x[1])
    print("RESULTAT FINAL")
    print(tabPath[0][0])
    print(tabPath[0][1])
    print("TEMPS")
    print(time.process_time() - start)
    print("Nombre de Generation : ")
    print(generation)
    
    """
    print("RESULTAT FINAL")
    resultat = myModule.genalgo(Map.cities, nbrPath)
    print(resultat)
    print(Map.pathLength(resultat))
    print("TEMPS")
    print(time.process_time() - start)
    """
    return tabPath[0][0]
    #return resultat





















def selectionPath2(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    
    
    
    import time
    start = time.process_time()
    
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
    
    
    
    
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
    
    
    for k in range(30):
                        
        tabPath.sort(key=lambda x:x[1])
        
        tabBestPath = []
        
        for i in range(bestElementsSize):
            tabBestPath.append(tabPath[i][0])

        
        genCrossed = crossOverLoop(nbrPath, tabBestPath)
        genMutated = mutationLoop(tabBestPath[1:])
        
        tabBestPath = genMutated + genCrossed
        
        tabPath = []
        
        for i in tabBestPath:
            tabPath.append([i,Map.pathLength(i)])
        
    
    
    
    
    tabPath.sort(key=lambda x:x[1])
    print("RESULTAT FINAL")
    print(tabPath[0][0])
    print(tabPath[0][1])
    print("TEMPS")
    print(time.process_time() - start)
    
   
    
    return tabPath[0][0]
        
        
    
    
    