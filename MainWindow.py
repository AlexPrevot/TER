# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:39:59 2021

@author: User
"""

from tkinter import *
from functools import partial

class window:        
    def placePoint(self,coX,coY):
        self.canvas.create_rectangle(coX + 0, coY + 0, coX + 5, coY + 5, fill='black')

    def bindPoint(self,coX1,coY1,coX2,coY2):
        self.canvas.create_line(coX1,coY1,coX2,coY2)
        
    def appear(self):
        self.root.mainloop()
    
    def buttonAction(self,function):
        tab = function()
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        for i in range(len(tab)):
            self.placePoint(tab[i][0],tab[i][1])
        
    def __init__(self,function):
        self.root = Tk(className='Voyageur de Commerce - Bourmaud Paul, Prevot Alexandre')
        self.root.geometry("700x600")
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 500, 500, fill='white')
        self.butt = Button(self.root, text = "Generation", command = partial(self.buttonAction,function), bg = 'red')
        self.butt.pack()
        



