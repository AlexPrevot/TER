# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:39:59 2021

@author: User
"""

from tkinter import *
from functools import partial
from Map import Map


import Selector as slt

class window:
    #----------------------function to place points
    def placePoint(self,coX,coY):
        self.canvas.create_rectangle(coX + 0, coY + 0, coX + 5, coY + 5, fill='black')






    #----------------------function to bind points with their coordon
    def bindPoint(self,coX1,coY1,coX2,coY2):
        self.canvas.create_line(coX1,coY1,coX2,coY2)
    
    
    
    
    
    
    
    #----------------------function to bind points with their coordononate
    def appear(self):
        self.root.mainloop()
    
 
    
    #----------------------action of the buttons
    
    
    def buttonGenerate(self):
        tab = self.actualMap.refresh()
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        
        for i in range(len(tab)):
            self.placePoint(tab[i][0],tab[i][1])
            
        
    #--------
        
    def buttonPath(self):
        tab = self.actualMap.randomPath()
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        
        for i in range(len(tab)):
            self.placePoint(tab[i][0],tab[i][1])
        
        tab = slt.selectionPath(10,self.actualMap)
        
        for j in range(len(tab)):
            if (j+1)<len(tab):
                self.bindPoint(tab[j][0],tab[j][1],tab[j+1][0],tab[j+1][1])
        
        
    #-------------------------------------------(!) OBJECT INSTANCIATION (!)
        
        
        
    def __init__(self):
        #window creation
        self.root = Tk(className='Voyageur de Commerce - Bourmaud Paul, Prevot Alexandre')
        self.root.geometry("700x600")
        
        #we set a canvas where we'll put useful things
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        
        #the button of the window
        self.buttGeneration = Button(self.root, text = "Generation", command = self.buttonGenerate, bg = 'red')
        self.buttGeneration.pack()
        self.buttPath = Button(self.root, text = "trouver un chemin", command = self.buttonPath, bg = 'red')
        self.buttPath.pack()
        
        #Map creation
        self.actualMap = Map(4,500,0) 



