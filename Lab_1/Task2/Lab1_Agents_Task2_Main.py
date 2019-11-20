from Lab1_Agents_Task2_Deck import Deck
from Lab1_Agents_Task2_PokerPlayer_random import RandomPlayer
from Lab1_Agents_Task2_PokerPlayer_Fixed import FixedPlayer
from Lab1_Agents_Task2_PokerPlayer_Reflex import ReflexPlayer
from Lab1_Agents_Task2_Table import Table



theTable = Table()
player1 = ReflexPlayer()
player2 = RandomPlayer()
theTable.add_players(player1, player2)



for i in range(50):

    print("\nNew game!")

    if theTable.deck.cards_left() < 6:
        theTable.get_new_deck()
    
    player1.new_hand(theTable.deck)
    player2.new_hand(theTable.deck)

    for j in range(3):
        theTable.get_bets(player1.bet(), player2.bet())

    print("Player 1 hand is: {}".format(player1))
    print("Player 2 hand is: {}".format(player2))

    if theTable.check_winner() == player1:
        print("Player 1 won: {}$".format(theTable.pot))
        player1.collect_pot(theTable.pot)
        theTable.reset_pot()
    else:
        print("Player 2 won: {}$".format(theTable.pot))
        player2.collect_pot(theTable.pot)
        theTable.reset_pot()
        
print("\n============ Game over! ============")
print("Player 1 won {} times and cashed in a total of {}$! $/win = {}$".format(player1.wins, player1.cash, player1.cash/player1.wins))
print("Player 2 won {} times and cashed in a total of {}$! $/win = {}$".format(player2.wins, player2.cash, player2.cash/player2.wins))
