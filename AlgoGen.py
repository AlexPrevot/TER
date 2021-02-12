# -*- coding: utf-8 -*-
from Map import Map
from MainWindow import window
#import Error



lala = Map(10,8,1)

b = window(lala.refresh)

for i in range(6):
    b.placePoint(lala.cities[i][0],lala.cities[i][1])



b.appear()

"""
Created on Sat Feb  6 17:19:26 2021

@author: User
"""


        



