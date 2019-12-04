from Poker import Poker
from poker_game_example import PokerPlayer, get_next_states
import random

class GreedyPlayer(PokerPlayer):
    def __init__(self, stack):
        self.name = "Greedy Agent"
        self.init_stack = stack
        self.agent = PokerPlayer(None, stack_=stack, action_=None, action_value_=None)
        super().__init__(self.agent)
        self.node_count = 0

    def end_of_game(self, state, max_hands):
        
        #if (state.phase == 'SHOWDOWN' and state.agent.stack >= self.init_stack + 100):
        
        if state.phase == 'SHOWDOWN' and (state.agent.stack >= self.init_stack + 100 and state.nn_current_hand <= max_hands):
            return True
        else:
            return False

    def search_next_state(self, state_queue):
        state_queue.sort(key= lambda state: state.nn_current_hand)
        theItem = state_queue[0]
        state_queue.remove(theItem)
        return get_next_states(theItem)
