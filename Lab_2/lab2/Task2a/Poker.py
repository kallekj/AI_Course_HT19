from poker_game_example import PokerPlayer, GameState, get_next_states
import copy


"""
Game flow:
Two agents will keep playing until one of them lose 100 coins or more.
"""

class Poker():


    def __init__(self, theAgent, max_hands, theStack):
        self.game_agent = theAgent
        self.game_agent.stack = theStack
        self.opponent = PokerPlayer(current_hand_=None, stack_=theStack, action_=None, action_value_=None)
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
        self.end_state = None
        self.max_hands = max_hands
        self.dealed_hands = 0
        

    def play_poker(self):

        while self.running:

            if self.round_init:
                self.round_init = False
                states_ = get_next_states(self.init_state)
                self.state_queue.extend(states_[:])
            else:

                # Find next possible states
                states = self.game_agent.search_next_state(self.state_queue.pop(0))
                self.state_queue.extend(states_)

                for _state_ in states_:
                    if _state_.phase == 'SHOWDOWN' and (_state_.opponent.stack <= 300 or _state_.agent.stack <= 300): #or _state_.MAX_HANDS >= 4):
                            self.end_state_ = _state_
                            self.running = False

    
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

