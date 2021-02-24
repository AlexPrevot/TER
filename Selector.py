# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:23:27 2021

@author: User
"""
from math import *
from Error import error

def pointDist(cX1,cY1,cX2,cY2):
    return sqrt((cX2-cX1)**2 + ((cY2-cY1)**2 ))





"""def bestPath(nbrPath,Map):
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
    return smallestPath    """

         
def selectionPath(nbrPath, Map, bestElementsSize):
    if (bestElementsSize > nbrPath):
        error("bestElementsSize supperior to nbrPath")
        
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
    
    tabBestPath = tabPath[0:bestElementsSize]
    
    return tabBestPath
    
        
    
    