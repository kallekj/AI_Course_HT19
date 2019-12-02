from Poker import Poker
from task2_random import RandomPlayer

def main():
    randomAgent = RandomPlayer(300)
    game = Poker(randomAgent, 4)
    
    game.play_poker()



if __name__ == "__main__":
    main()
