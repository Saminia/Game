import random
import numpy as np
list1=["A","Q","K","J"]+ list(range(2,11))
list2=["Peak", "Heart", "Cross", "Diamond"]
card_set = [(a,b) for a in list1 for b in list2]
bet=input(" What amount would you like to bet? ")
money=input("How much money you start with?")

class player(object):
    def __init__(self,decision,card_batch):
        self.decision=decision
        self.card_batch=card_batch


    def cards(self,card_batch):
        played = random.choice(card_batch)
        card_batch.remove(played)
        return card_batch, played

    def move(self,l):
        p1 = input("Player, do you hit or stand?")
        while p1 != 'hit' and p1 != 'stand':
            p1 = input("Your input is not acceptable. Input either "'hit'" or "'stand'"")
        if p1=='stand':
            t=self.card_batch
            r=(0, 'Heart')
            return t,r
        elif p1=='hit':
            t,r=self.cards(self.card_batch)
            l = [l, r]
            print("Your cards are", str(l))
            return t,r

    def count(self,played_cards):
        li = [x[0] for x in played_cards]
        h=[10 if x == 'Q' or x== 'J' or x=='K' else x for x in li]
        r=h
        v=[11 if x == 'A' else x for x in h]
        w=[1 if x == 'A' else x for x in r]
        return sum(np.array(v)), sum(np.array(w))


    def result(self,hand_sum1,hand_sum2,dealer_sum,bet,money):
        if hand_sum1 > 21 and hand_sum2 > 21:
            print("You Busted!")
            return money - bet
        elif (hand_sum1 > dealer_sum and hand_sum1 <21) or (hand_sum2 > dealer_sum and hand_sum2 <21):
            print("You won!")
            return money + bet
        elif hand_sum1 < dealer_sum or hand_sum2 < dealer_sum:
            print("You lost!")
            return money - bet
        else:
            print("No winner!")
            return(money)


f=player("hit",card_set)
i=card_set

while len(i) > 5:
    #print(i)
    bet=input(" What amount would you like to bet? ")
    a, card1 = f.cards(card_set)
    c, dealer_card1 = f.cards(a)
    b, card2 = f.cards(c)
    d, dealer_card2 = f.cards(b)
    print("Your hand is", str(card1),"and", str(card2))
    print("Dealer's is", str(dealer_card1))
    l=[card1,card2]
    i,y=f.move(l)
    l=[card1,card2,y]
    dealer_cards=[dealer_card1,dealer_card2]
    m,n=f.count(dealer_cards)
    j,k=f.count(l)
    money=f.result(j,k,m,bet,money)
    print(money)

if money >1000:
    print("you won " , money-1000 , "dollars")

else:
    print("you lost ", 1000-money, "dollars")











