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
        self.depth = 0

    def play_poker(self):
        
        while self.running:
            if self.round_init:
                self.round_init = False
                states_ = get_next_states(self.init_state)
                self.state_queue.extend(states_[:]) # Extend queue with a copy of states_
                self.game_agent.node_count += len(self.state_queue)
                
            else:

                # Find next possible states
                states_ = self.game_agent.search_next_state(self.state_queue)
                self.state_queue.extend(states_[:]) # Extend queue with a copy of states_

                for _state_ in states_:
                    
                    if self.game_agent.end_of_game(_state_, self.max_hands):
                        self.end_state = _state_
                        self.game_agent.end_state = _state_
                        self.running = False
                    
                    self.game_agent.node_count += 1



    def print_game_info(self):
        """
        Printing game flow & info
        """

        if self.depth != 0:
            self.depth = 0

        current_state = self.end_state
        print('------------ print game info ---------------')
        print('State queue length', len(self.state_queue))

        while current_state.parent_state != None:
            self.depth += 1
            current_state = current_state.parent_state

        print("****** {} Performance *******".format(self.game_agent.name))
        print("Current stack: {}   Node Count: {}   Depth: {}   Number of hands: {}".format(self.end_state.agent.stack, self.game_agent.node_count, self.depth, self.end_state.nn_current_hand))
        print("")
        print("****** Opponent ******")
        print("Current stack: {}".format(self.end_state.opponent.stack))

    
    def get_game_info(self):
        
        
        if self.depth != 0:
            self.depth = 0

        current_state = self.end_state
        
        while current_state.parent_state != None:
            self.depth += 1
            current_state = current_state.parent_state
            

        return {"stack":self.end_state.agent.stack, 
                "nNodes":self.game_agent.node_count, 
                "depth":self.depth, 
                "nHands":self.end_state.nn_current_hand, 
                "opponentStack":self.end_state.opponent.stack}

