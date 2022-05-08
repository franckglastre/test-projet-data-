#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:57:01 2022

@author: franckglastre
"""

class Case():
    def __init__(self):
        self.occupe=' '
    
    def jouer1(self):
        if ((self.occupe=='O')|(self.occupe==' ')):
            self.occupe='X'
            
    def jouer2(self):
        if (self.occupe!='X'):
            self.occupe='O'
            
class Terrain():
    def __init__(self):
        self.grill=[]
        for i in range(9):
            self.grill.append(Case())
        self.tour=1
    
    def __str__(self):
        liste=""
        for i,obj in enumerate(self.grill):
            if i in [2,5,8]:
                liste+=self.grill[i].occupe + '\n'
            else:
                liste+=self.grill[i].occupe + "|" 
        return liste
          
         
    def jouer(self,n):
       if self.tour==1:
           self.tour=0
           self.grill[n].jouer1()
       else:
           self.grill[n].jouer2()
           self.tour=1
                  
       
        
ter=Terrain()

ter.jouer(2)
ter.jouer(3)
ter.jouer(4)
print(ter)

