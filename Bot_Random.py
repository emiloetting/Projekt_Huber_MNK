from Player import Player
from Board import Board
import numpy as np
from random import randint
from random import shuffle


class Bot_Random(Player):
    '''Bot, der nur random Züge spielen kann'''
    def __init__(self, number):
        self.number = number 
        self.name = "RandomBot"       

    def make_move(self, board = Board):  
        '''Ermöglicht dem Bot das Setzen seiner Markierung auf dem Spielfeld-Array.
        2 Pseudo-Zufallszahlen werden erstellt, die für die Indexierung eines Feldes
        verwendet werden. Ist Feld frei, setzt Bot an dieser Stelle. Andernfalls werden
        neue Zufallszahlen generiert, bis der Bot ein leeres Feld trifft
        '''                        
        x_coordinate = randint(0,4)                                         
        y_coordinate = randint(0,4)                                         
        while board.array[y_coordinate][x_coordinate] != 0:                 #wenn Feld belegt
            x_coordinate = randint(0,4)                                    
            y_coordinate = randint(0,4)                                     

        board.set_field_value(y_coordinate, x_coordinate, self.number)      #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array                                                  
