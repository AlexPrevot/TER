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


#note : changer le deuxième for car complexité de n², on peut transformer en n
def crossOverPath(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPathCO.append(tabPath1[i])

    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPathCO:
            newTabPathCO.append(tabPath2[i])

    return newTabPathCO



#note : sous forme n et non n^2
def crossOverPath2(nbr,path1, path2):

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
    newTabPathMutation=tabPath
    element1 = randint(0 , len(tabPath)-1)
    element2 = randint(0 , len(tabPath)-1)
    
    t = tabPath.copy()
    newTabPathMutation = swapPositions(t, element1, element2)
    
    return newTabPathMutation


def mutationLoop(tab):
    mutant = []
    for i in tab:
        mutant.append(mutationPath(i))
    return mutant

# Swap function 
def swapPositions(tab, pos1, pos2):
    tab[pos1], tab[pos2] = tab[pos2], tab[pos1] 
    return tab





def selectionPath(nbrPath, Map, bestElementsSize):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    print("NOUVELLE SELECTION")
    import time
    start = time.process_time()
    # your code here    
    
    
    for i in range(nbrPath):
            cityTab = Map.randomPath()
            tabPath.append([cityTab,Map.pathLength(cityTab)])
            
    m = 0
    for j in tabPath:
        m += j[1]
    
    m = m/len(tabPath)
    print("moyenne de : " + str(m))
            
    for k in range(800):
                        
        tabPath.sort(key=lambda x:x[1])
        
        tabBestPath = []
        
        for i in range(len(tabPath)):
            tabBestPath.append(tabPath[i][0])
        
        
        
        tabBestPath = tabBestPath[0:bestElementsSize]
        
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
        
        
        
        


def selectionPath2(nbrPath, Map, bestElementsSize):
    if (bestElementsSize > nbrPath):
        error("bestElementsSize supperior to nbrPath")
        
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
        
    
    for i in range(nbrPath):
        cityTab = Map.randomPath()
        distanceChemin = 0
        tabPath.append([cityTab,Map.pathLength(cityTab)])
    
    
    tabPath.sort(key=lambda x:x[1])
    
    
    tabBestPath = []
    
    for i in tabPath:
        tabBestPath.append(i[0])
        
    
    tabBestPath = tabBestPath[0:bestElementsSize]
    
    newGenerationCO = []
    newGenerationM  = []
    
    print(tabBestPath)
    
    
    newGenerationCO.append(crossOverPath(2, tabBestPath[0], tabBestPath[2]))
    newGenerationM.append(mutationPath(tabBestPath[0]))
    
    print("tabBestPath")
    print(tabBestPath)
    print("newnewGenerationCO")
    print(newGenerationCO)
    print("newGenerationM")
    print(newGenerationM)
    return tabBestPath
    
        
    
    