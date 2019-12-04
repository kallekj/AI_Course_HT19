from Poker import Poker
from task2_random import RandomPlayer
from task2_BFS import BFSPlayer
from task2_Greedy import GreedyPlayer
import copy
import pandas as pd

def main():
    # BFSAgent = BFSPlayer(300)
    # RandomAgent = RandomPlayer(300)
    # GreedyAgent = GreedyPlayer(300)

    # BFS = Poker(BFSAgent,4)
    # Random = Poker(RandomAgent,4)
    # Greedy = Poker(GreedyAgent, 4)    

    BFS_Data=[]
    Random_Data=[]
    Greedy_Data=[]

    for i in range(100):
        print(i)
        BFSAgent = BFSPlayer(300)
        RandomAgent = RandomPlayer(300)
        GreedyAgent = GreedyPlayer(300)
        BFS = Poker(BFSAgent,4)
        Random = Poker(RandomAgent,4)
        Greedy = Poker(GreedyAgent, 4)

        BFS.play_poker()
        BFS_Data.append(BFS.get_game_info())

        Random.play_poker()
        Random_Data.append(Random.get_game_info())

        Greedy.play_poker()
        Greedy_Data.append(Greedy.get_game_info())

    BFS_DF = pd.DataFrame(BFS_Data)
    BFS_Mean = BFS_DF.mean(axis=0)
    Random_DF = pd.DataFrame(Random_Data)
    Random_Mean = Random_DF.mean(axis=0)
    Greedy_DF = pd.DataFrame(Greedy_Data)
    Greedy_Mean = Greedy_DF.mean(axis=0)

    print("\n       BFS Mean")
    print(BFS_Mean)
    print("\n       Random Mean")
    print(Random_Mean)
    print("\n       Greedy Mean")
    print(Greedy_Mean)
    


    print("")
    print(BFS_Mean.to_latex())
    print("")
    print(Random_Mean.to_latex())
    print("")
    print(Greedy_Mean.to_latex())

if __name__ == "__main__":
    main()
