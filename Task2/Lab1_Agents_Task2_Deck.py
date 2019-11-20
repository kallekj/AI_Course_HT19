from Lab1_Agents_Task2_Cards import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.deck = []
        self.generate()

    def generate(self):
        suits = ["H","D","S","C"]
        values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for suit in suits:
            for value in values:
                self.deck.append(Card(value, suit))

    def shuffle(self):
        shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()
    
    def print_deck(self):
        for card in self.deck:
            print(card)

    def get_hand(self):
        return [self.get_card(), self.get_card(), self.get_card()]

    def cards_left(self):
        return len(self.deck)