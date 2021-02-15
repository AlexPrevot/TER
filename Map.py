# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:52:13 2021

@author: User
"""

from Error import error
from random import seed
from random import randint


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
        if(Map.count >= 2):
            error("Map creation call : You can't create more than one map")
    
    
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
    
    
    #------------------------------------------Map redefinition
    
    def refresh(self):
        self.cities = self.createMap()
        return self.cities
    
    
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
        