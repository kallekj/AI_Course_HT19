class PokerPlayer:

    def __init__(self):
        self.hand = []
        self.handValue = None
        self.table = None
        self.wins = 0
        self.cash = 0

    def __str__(self):
        retStr = ""
        for card in self.hand:
            retStr = "".join([retStr, str(card)])
        return retStr

    def new_hand(self, deck):
        self.hand = [deck.get_card(), deck.get_card(), deck.get_card()]
        self.handValue = self.identifyHand()
    
    def draw_card(self, deck):
        self.hand.append(deck.get_card())

    def set_table(self, table):
        self.table = table
    
    def collect_pot(self, pot):
        self.cash = self.cash + pot
        self.wins += 1

    def identifyHand(self):
        possibleHands = ["high cards", "two pair", "three of cards"]
        lookup = dict(J=11, Q=12, K=13, A=14)
        nMax = 0
        n = 0
        theRank = None # The rank of the paired cards or the total value of the hand if only "high cards"
        matchedCards = []
        totalValue = None
        # To calculate if there is "two pair", "Three of cards" or just "high cards" 
        for rank in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
            for card in self.hand:
                if card.rank == rank:
                    n += 1 # Increase counter if there is a match
                    matchedCards.append(rank) # Add the matched card to a list, this is used to calculate the hand total value if high cards
            if n > nMax: # If the number of matched cards is higher than the old max(matched cards)
                nMax = n
                n = 0
                theRank = rank # the rank of the paired cards
                if rank in ["2","3","4","5","6","7","8","9","10"]:
                    totalValue = int(rank)
                else:
                    totalValue = lookup[rank]
            n = 0

        if nMax == 1:
            temp = 0
            for value in matchedCards:
                if value in ["2","3","4","5","6","7","8","9","10"]:
                    temp = temp + int(value)
                else:
                    temp = temp + lookup[value]
            totalValue = temp
            theRank = None

        
        return dict(pair=possibleHands[nMax-1], rank=theRank, value=totalValue)
            

