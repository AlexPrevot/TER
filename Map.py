# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:52:13 2021

@author: User
"""

from Error import error
from random import seed
from random import randint
import random
import math

from math import *


class Map:
    count = 0
    #------------------------------------------Error Check
    
    def errorCheck(self,size,MAX,MIN):
        if(type(size) is not int):
            error("Map creation : size is a " + str(type(size)) + ": To create a map you need an int")
        if(type(MAX) is not int):
            error("Map creation : MAX is a " + str(type(MAX)) + ": To create a map you need an int")
        if(type(MIN) is not int):
            error("Map creation : MIN is a " + str(type(MIN)) + ": To create a map you need an int")
        if(MIN > MAX):
            error("Map creation : MIN is a greater than MAX")
        #if(Map.count >= 2):
            #error("Map creation call : You can't create more than one map")
    
    
    #------------------------------------------Map Creation
    
    def createMap(self):
        size = self.size
        MAX = self.MAX
        MIN = self.MIN
        cityTab = []
        #--randomly made
        for i in range(size):
            coX = randint(MIN,MAX)
            coY = randint(MIN,MAX)
            cityTab.append([coX,coY])
        return cityTab
    
    def creatMapCircle(self):
        size = self.size
        MAX = self.MAX
        MIN = self.MIN
        r=2*size
        cityTab = []
        #--creation ville en forme de cercle
        for i in range(size):
            coX=250+r*math.cos((i*2*math.pi)/size)
            coY=250+r*math.sin((i*2*math.pi)/size)
            cityTab.append([coX,coY]) 
            
        self.cities = cityTab    
        return cityTab
    
    #------------------------------------------Map redefinition
    
    def refresh(self):
        self.cities = self.createMap()
        return self.cities
    
    #------------------------------------------find a random path
    
    #note : CHANGER CA AVEC LA CREATION DU TABLEAU PAR NUMPY SINON CA SERA LENT
    def randomPath(self):
        newPath = []
        for i in range(self.size):
            newPath.append(i)
        random.shuffle(newPath)
        return newPath
    
    #------------------------------------------get the score of a path
    
    def pointDist(self,cX1,cY1,cX2,cY2):
        return sqrt((cX2-cX1)**2 + ((cY2-cY1)**2 ))
    

    def pathLength(self, intTab):
        distanceChemin = 0
        cities = self.cities
        for i in range(len(intTab)):
            if (i+1)<len(cities):
                distanceChemin += self.pointDist(cities[intTab[i]][0],
                                            cities[intTab[i]][1],
                                            cities[intTab[i+1]][0],
                                            cities[intTab[i+1]][1])
        
        distanceChemin += self.pointDist(cities[intTab[0]][0],
                                            cities[intTab[0]][1],
                                            cities[intTab[-1]][0],
                                            cities[intTab[-1]][1])
        return distanceChemin
        
    
    #------------------------------------------ (!) OBJECT INSTANCIATION (!)
    #--We check any irregularities before continue with 'errorCheck' fct
    #--We can create only a single map, it is a singleton
    
    def __init__(self,size,MAX,MIN):
        Map.count += 1
        self.errorCheck(size,MAX,MIN)
        self.size = size
        self.MAX = MAX
        self.MIN = MIN
        self.cities = self.createMap()
        