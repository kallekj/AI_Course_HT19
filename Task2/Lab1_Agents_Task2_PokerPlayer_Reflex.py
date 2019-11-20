from Lab1_Agents_Task2_PokerPlayer import PokerPlayer

class ReflexPlayer(PokerPlayer):

    def analyzeHand(self):
        bet = 0
        if "three of kind" in self.handValue["pair"]:
            bet = 50
        elif "two pair" in self.handValue["pair"]:
            if self.handValue["value"] < 5:
                bet = 20
            elif self.handValue["value"] < 8:
                bet = 30
            else:
                bet = 40
        elif self.handValue["value"] < 8:
            bet = 5
        elif self.handValue["value"] < 16:
            bet = 10
        elif self.handValue["value"] < 24:
            bet = 15
        elif self.handValue["value"] < 32:
            bet = 20
        else:
            bet = 25
        return bet
    
    def bet(self):
        return self.analyzeHand()
