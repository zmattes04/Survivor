import pygame
import player

class inventory(player):
    def __init__(self, size):
        self.size = 20
        self.items = [None] * self.size #array of 20 empty items

    def add_item(self, item):
        

