from tkinter import *
from functools import partial
from Map import Map


import Selector as slt

class window:
    #----------------------function to place points
    def placePoint(self,coX,coY):
        self.canvas.create_rectangle(coX + 0, coY + 0, coX + 5, coY + 5, fill='black')


    #----------------------function to bind points with their coordon
    #note : le truc ne marche pas pour l'instant
    def bindPoint(self,coX1,coY1,coX2,coY2):
        self.canvas.create_line(coX1,coY1,coX2,coY2)
     
  
    #----------------------function to bind points with their coordononate
    def appear(self):
        self.root.mainloop()
    

    
    #----------------------action of the buttons
    
    #bouton positionnement des points de maniere aleatoire
    def buttonGenerate(self):
        tab = self.actualMap.refresh()
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        
        for i in range(len(tab)):
            self.placePoint(tab[i][0],tab[i][1])
            
    #bouton positionnement des points de manière aléatoire
    def buttonGenerateCircle(self):
        tab = self.actualMap.creatMapCircle()
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        
        for i in range(len(tab)):
            self.placePoint(tab[i][0],tab[i][1])
            
        
    #--------
    #lance lalgo de recherche
    def buttonPath(self):
        tab = self.actualMap.randomPath()
        cities = self.actualMap.cities
        self.canvas.delete("all")
        #self.canvasText.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        for i in range(len(tab)):
            self.placePoint(cities[tab[i]][0],cities[tab[i]][1])
        
        tab = slt.selectionPath(400,self.actualMap,200)

        
        #self.textBestPath = Label(self.root, text = str(self.actualMap.pathLength(tab)))
        self.stringVariable.set(str(self.actualMap.pathLength(tab)))
        cities = self.actualMap.cities
        for j in range(len(tab)):
            if (j+1)<len(tab):
                self.bindPoint(cities[tab[j]][0],
                               cities[tab[j]][1],
                               cities[tab[j+1]][0],
                               cities[tab[j+1]][1])
                
        self.bindPoint(cities[tab[0]][0],
                               cities[tab[0]][1],
                               cities[tab[len(tab)-1]][0],
                               cities[tab[len(tab)-1]][1])
        
    
            
        
        
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
        self.buttGenerationR = Button(self.root, text = "Generation Random", command = self.buttonGenerate, bg = 'red')
        self.buttGenerationR.pack()
        self.buttGenerationC = Button(self.root, text = "Generation Circle", command = self.buttonGenerateCircle, bg = 'red')
        self.buttGenerationC.pack()
        self.buttPath = Button(self.root, text = "Trouver un chemin", command = self.buttonPath, bg = 'red')
        self.buttPath.pack()
        #self.canvasText = Canvas(self.root, width=500, height=500)
        #self.canvasText.pack()
        self.stringVariable= StringVar()
        self.textBestPath = Label(self.root, textvariable = self.stringVariable) 
        self.textBestPath.pack()
        
        
        #Map creation
        self.actualMap = Map(100,500,0) 