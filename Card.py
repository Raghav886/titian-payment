from os import name
from tkinter import N
from tokenize import Double
from unicodedata import decimal


class Card:
    def __init__(self, n) -> None:
        self.name = n
    
    def fee(self) -> decimal:
        if(self.name == "Amex"):
            return 1
        elif (self.name == "Visa"):
            return 1.2
        else:
            return 0.7

