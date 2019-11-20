# theDeck = Deck()
# theDeck.shuffle()

# theDeck.print()

class Hand:

    def __init__(self, hand=[]):
        self.hand = hand
        self.handValue = []

    def __str__(self):
        return "".join(self.hand)

    def new_hand(self, deck):
        self.hand = [deck.get_card(), deck.get_card(), deck.get_card()]

    def identifyHand(self):
        possibleHands = ["high cards", "two pair", "three of cards"]
        nMax = 0
        n = 0
        theValue = None
        for value in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
            for card in self.hand:
                if card.rank == value:
                    n += 1
            if n > nMax:
                nMax = n
                n = 0
                theValue = value
            n = 0

        print(nMax, theValue)
        return [possibleHands[nMax-1], theValue]

        

