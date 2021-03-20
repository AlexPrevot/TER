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


def pointDist(cX1,cY1,cX2,cY2):
    return sqrt((cX2-cX1)**2 + ((cY2-cY1)**2 ))


def crossOverPath(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPathCO.append(tabPath1[i])

    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPathCO:
            newTabPathCO.append(tabPath2[i])

    return newTabPathCO


#mutation d'un chemin
def mutationPath(tabPath):
    newTabPathMutation=tabPath
    element1 = randint(0 , len(tabPath)-1)
    element2 = randint(0 , len(tabPath)-1)
    
    t = tabPath.copy()
    newTabPathMutation = swapPositions(t, element1, element2)
    
    return newTabPathMutation


# Swap function 
def swapPositions(tab, pos1, pos2):
    tab[pos1], tab[pos2] = tab[pos2], tab[pos1] 
    return tab


def selectionPath(nbrPath, Map, bestElementsSize):
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
    
        
    
    