import random

class Card:
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        
    def cardrank(self):
        return int(self.number)
    
    def cardsuit(self):
        return str(self.suit)
        
class Deck:
    
    def __init__(self, name=""):
        self.stack = []
        self.name = name
        
    def shuffle(self):
        suit = ["heart", "clover", "spade", "diamond"]
        for n in suit:
            for j in range(1, 14):
                self.stack.append(Card(j,n))
                random.shuffle(self.stack)
    
    def dealcard(self,player,computer):
        for j in range(len(self.stack)):
            if j % 2 != 1:
                player.stack.append(self.stack[j])
            else:
                computer.stack.append(self.stack[j])

    

def playgame(deck):
    player_card = deck[len(deck)-2]    
    computer_card = deck[len(deck)-1]
    if player_card.cardrank() > computer_card.cardrank():
        return 1
    elif computer_card.cardrank() > player_card.cardrank():
        return 2
    else:
        return 3
    
    
def Main():
    deck= Deck()
    me = Deck()
    comp = Deck()
    deck.shuffle()
    deck.dealcard(me,comp)
    deck = []
    round = 0
    print("new game started!")
    while True: 
        round += 1
        print(str(len(me.stack)) + " cards remaining" + " on round " + str(round))
        input("Press Enter to continue...")
        deck.append(me.stack.pop())
        deck.append(comp.stack.pop())
        
        if len(me.stack) == 0:
            print("Unfortunately you lost")
            break
        elif len(comp.stack) == 0:
            print( "You win! Congratulations")
            break

        result = playgame(deck)
        
        if result == 1:
            print("player won this round")
            while len(deck) != 0:
                me.stack.append(deck.pop())
            deck = []
            random.shuffle(me.stack)
            random.shuffle(comp.stack)
            
        if result == 2:
            print("comp won")
            while len(deck) != 0:
                comp.stack.append(deck.pop())
            deck = []
            random.shuffle(me.stack)
            random.shuffle(comp.stack)    
                
        if result == 3:
            print("there was a tie")
            deck.append(me.stack.pop())
            deck.append(comp.stack.pop())
            deck.append(me.stack.pop())
            deck.append(comp.stack.pop())            
            result = 0
            random.shuffle(me.stack)
            random.shuffle(comp.stack)

    
Main()
        
        