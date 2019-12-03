from Poker import Poker
from poker_game_example import PokerPlayer, get_next_states
import random

class RandomPlayer(PokerPlayer):
    def __init__(self, stack):
        self.name = "Random Agent"
        self.init_stack = stack
        self.agent = PokerPlayer(None, stack_=stack, action_=None, action_value_=None)
        super().__init__(self.agent)
        self.node_count = 0

    def end_of_game(self, state, max_hands):
        
        #if state.phase == 'SHOWDOWN' and ((state.agent.stack >= self.init_stack + 100) or state.nn_current_hand <= max_hands or self.node_count > 10000):
        
        if state.phase == 'SHOWDOWN' and (state.agent.stack >= self.init_stack + 100 and state.nn_current_hand <= max_hands or self.node_count > 10000):
            return True
        else:
            return False

    def search_next_state(self, state_queue):
        if(len(state_queue) > 0):
            return get_next_states(state_queue.pop(random.randint(0, len(state_queue) - 1)))
        else:
            return get_next_states(state_queue.pop())


