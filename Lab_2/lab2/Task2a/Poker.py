from poker_game_example import PokerPlayer, GameState, get_next_states
import copy


"""
Game flow:
Two agents will keep playing until one of them lose 100 coins or more.
"""

class Poker():


    def __init__(self, theAgent, max_hands):
        self.game_agent = theAgent
        # Init opponent with the same amount of money in the stack as the agent 
        self.opponent = PokerPlayer(current_hand_=None, stack_=self.game_agent.stack, action_=None, action_value_=None)
        self.init_state = GameState(nn_current_hand_=0,
                                    nn_current_bidding_=0,
                                    phase_ = 'INIT_DEALING',
                                    pot_=0,
                                    acting_agent_=None,
                                    agent_=self.game_agent,
                                    opponent_=self.opponent
                                    )
        self.running = True
        self.state_queue = []
        self.round_init = True
        self.max_hands = max_hands
        self.end_state = None 

    def play_poker(self):

        while self.running:

            if self.round_init:
                self.round_init = False
                states_ = get_next_states(self.init_state)
                self.state_queue.extend(states_[:])
                
            else:

                # Find next possible states
                states_ = self.game_agent.search_next_state(self.state_queue)
                self.state_queue.extend(states_)

                for _state_ in states_:
                    
                    if self.game_agent.end_of_game(_state_, self.max_hands):
                        self.end_state = _state_
                        self.running = False
                    
                    self.game_agent.node_count += 1

        """
        Printing game flow & info
        """

        nn_level = 0
        current_state = self.end_state
        print('------------ print game info ---------------')
        print('nn_states_total', len(self.state_queue))

        while current_state.parent_state != None:
            nn_level += 1
            print(nn_level)
            current_state.print_state_info()
            current_state = current_state.parent_state

        print(nn_level)

