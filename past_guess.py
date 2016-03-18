# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:16:56 2016

@author: David
"""

class PastGuess:
    def __init__(self, positions = [], results = [0,0] ):
        self.positions = positions
        self.correctPositions = results[0]
        self.jumbledPositions = results[1]
        
    def __str__(self):
        return str(self.positions) + ' : [' + str(self.correctPositions) + ',' + str(self.jumbledPositions) + ']'
        
        