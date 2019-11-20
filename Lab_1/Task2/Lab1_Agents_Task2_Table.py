from Lab1_Agents_Task2_Deck import Deck
from Lab1_Agents_Task2_PokerPlayer_random import RandomPlayer

class Table:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = None 
        self.player2 = None
        self.player1Bet = 0
        self.player2Bet = 0
        self.pot = 0
    
    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.set_table(self)
        self.player2.set_table(self)
        

    def get_new_deck(self):
        self.deck = Deck()
        self.deck.shuffle()

    def reset_pot(self):
        self.player1Bet = 0
        self.player2Bet = 0
        self.pot = 0

    def get_bets(self, betP1, betP2):
        self.player1Bet = self.player1Bet + betP1
        self.player2Bet = self.player2Bet + betP2
        self.pot = self.player1Bet + self.player2Bet
        print("Player 1 bet: {}$, Player 2 bet: {}$ and the pot is {}$".format(betP1, betP2, self.pot))  

    def check_winner(self):
        winner = None
        player1Hand = self.player1.identifyHand()
        player2Hand = self.player2.identifyHand()
        
        if "three of kind" in player1Hand["pair"] and "three of a kind" in player2Hand["pair"]: 
            if player1Hand["value"] > player2Hand["value"]:
                winner = self.player1
            else:
                winner = self.player2
        elif "three of kind" in player1Hand["pair"]:
            winner = self.player1
        elif "three of a kind" in player2Hand["pair"]:
            winner = self.player2
        if "two pair" in player1Hand["pair"] and "two pair" in player2Hand["pair"]: 
            if player1Hand["value"] > player2Hand["value"]:
                winner = self.player1
            else:
                winner = self.player2
        elif "two pair" in player1Hand["pair"]:
            winner = self.player1
        elif "two pair" in player2Hand["pair"]:
            winner = self.player2
        elif player1Hand["value"] > player2Hand["value"]:
            winner = self.player1
        else:
            winner = self.player2
        
        return winner
        