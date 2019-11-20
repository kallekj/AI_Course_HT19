import random
from Lab1_Agents_Task2_PokerPlayer import PokerPlayer

class RandomPlayer(PokerPlayer):

    def bet(self):
        return random.randint(0,50)
        

