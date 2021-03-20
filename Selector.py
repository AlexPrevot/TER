# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:23:27 2021

@author: User
"""
from math import *
import random


def pointDist(cX1,cY1,cX2,cY2):
    return sqrt((cX2-cX1)**2 + ((cY2-cY1)**2 ))





def bestPath(nbrPath,Map):
    cityTab = Map.cities
    distMini = float(inf)
    smallestPath = [[]]
    
    #-----
    
    for i in range(nbrPath):
        cityTab = Map.randomPath()
        distanceChemin = 0
        for j in range(len(cityTab)):
            if (j+1)<len(cityTab):
                distanceChemin += pointDist(cityTab[j][0],
                                            cityTab[j][1],
                                            cityTab[j+1][0],
                                            cityTab[j+1][1])
        if (distanceChemin < distMini):
            distMini = distanceChemin
            smallestPath = cityTab
    print(distMini)
    return smallestPath    
         
def selectionPath(nbrPath, Map):
    cityTab = Map.cities
    tabPath =[]
    tabBestPath =[]
    
    for i in range(nbrPath):
        cityTab = Map.randomPath()
        distanceChemin = 0
        for j in range(len(cityTab)):
            if (j+1)<len(cityTab):
                distanceChemin += pointDist(cityTab[j][0],
                                            cityTab[j][1],
                                            cityTab[j+1][0],
                                            cityTab[j+1][1])
        
        tabPath.append([cityTab,distanceChemin])
    
    tabPath.sort(key=lambda x:x[1])
    print(tabPath)
    
    #print("tabPath trié : " + tabPath)
    
    tabBestPath = tabPath[0:3]
    
    print(tabBestPath)
    
    return tabBestPath
 

#croisement entre 2 chemins   
def crossOverPath(nbrElementTab1,tabPath1, tabPath2):
    newTabPathCO=[]
    for i in range(nbrElementTab1):
        newTabPath= newTabPath.append(tabPath1[i])
        
    for i in range(np.size(tabPath2)):
        if tabPath2[i] not in newTabPath():
            newTabPath=newTabPath.append(tabPath2[i])
    
    return newTabPathCO


#mutation d'un chemin
def mutationPath(tabPath):
    newTabPathMutation=tabPath
    element1 = random.sample(range(0 , np.size(tabPath)),1)
    element2 = random.sample(range(0 , np.size(tabPath)),1)
    
    swapPositions(tabPath, element1, element2)
    
    return newTabPathMutation
   
    
# Swap function 
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
    

   
    
    
    
        
    
    