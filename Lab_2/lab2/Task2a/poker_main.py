from Poker import Poker
from task2_random import RandomPlayer
from task2_BFS import BFSPlayer
from task2_Greedy import GreedyPlayer

def main():
    BFSAgent = RandomPlayer(300)
    game = Poker(BFSAgent, 4)
    
    game.play_poker()
    game.print_game_info()
    #BFSAgent.print_agent_performance()



if __name__ == "__main__":
    main()
